from unittest import TestCase

from osbot_aws.apis.IAM import IAM
from osbot_aws.helpers.Create_Code_Build import Create_Code_Build
from osbot_gsuite.apis.sheets.API_Jira_Sheets_Sync import API_Jira_Sheets_Sync
from pbx_gs_python_utils.utils.Dev import Dev


class test_Trigger_Builds(TestCase):

    def setUp(self):
        self.project_name = 'OSBot-gsheet-sync'
        self.account_id = IAM().account_id()
        self.api = Create_Code_Build(account_id=self.account_id, project_name=self.project_name)

    def trigger_task(self,task_name,file_id, command):
        kvargs = {
            'projectName'      : self.project_name,
            'buildspecOverride': 'osbot_gsheet_sync/tasks/{0}/buildspec.yml'.format(task_name),
            'environmentVariablesOverride': [{ 'name': 'file_id', 'value': file_id, 'type': 'PLAINTEXT'},
                                             { 'name': 'command', 'value': command, 'type': 'PLAINTEXT'}]
            #'sourceVersion'    : task_name
        }
        return self.api.code_build.codebuild.start_build(**kvargs).get('build').get('arn')

    def test_trigger_load_sheet(self):
        file_id = '1_Bwz6z34wALFGb1ILUXG8CtF1-Km6F9_sGXnAu4gewY'
        command = 'load_sheet'
        build_id = self.trigger_task('update_sheet',file_id, command)
        Dev.pprint(build_id)
        #self.api.code_build.build_wait_for_completion(build_id)

    def test_trigger_sync_sheet(self):
        file_id = '1_Bwz6z34wALFGb1ILUXG8CtF1-Km6F9_sGXnAu4gewY'
        command = 'sync_sheet'
        build_id = self.trigger_task('update_sheet',file_id, command)
        Dev.pprint(build_id)

    def test_jira_load(self):
        file_id = '1_Bwz6z34wALFGb1ILUXG8CtF1-Km6F9_sGXnAu4gewY'
        gsuite_secret_id ='gsuite_gsbot_user'
        sheets_sync = API_Jira_Sheets_Sync(file_id=file_id, gsuite_secret_id=gsuite_secret_id)
        result = sheets_sync.load_data_from_jira()
        Dev.pprint(result)

