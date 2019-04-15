from unittest import TestCase

from osbot_aws.apis.IAM import IAM
from osbot_aws.helpers.Create_Code_Build import Create_Code_Build
from pbx_gs_python_utils.utils.Dev import Dev


class test_Trigger_Builds(TestCase):

    def setUp(self):
        self.project_name = 'OSBot-gsheet-sync'
        self.account_id = IAM().account_id()
        self.api = Create_Code_Build(account_id=self.account_id, project_name=self.project_name)

    def trigger_task(self,task_name,message):
        kvargs = {
            'projectName'      : self.project_name,
            'buildspecOverride': 'osbot_gsheet_sync/tasks/{0}/buildspec.yml'.format(task_name),
            'environmentVariablesOverride': [{ 'name' : 'message',
                                               'value': message,
                                               'type' : 'PLAINTEXT'}]
            #'sourceVersion'    : task_name
        }
        return self.api.code_build.codebuild.start_build(**kvargs).get('build')

    def test_trigger_Update_Sheet(self):
        self.trigger_task('update_sheet','this is a message from CodeBuild')
        self.api.code_build.build_wait_for_completion()


