from unittest import TestCase
from pbx_gs_python_utils.utils.Dev import Dev
from osbot_gsheet_sync.Trigger_Build import Trigger_Build
import osbot_gsheet_sync._utils.Str_Extension_Methods

class test_Trigger_Build(TestCase):

    def setUp(self):
        self.trigger_build = Trigger_Build()

    def test_trigger_task__ping(self):
        str(self.trigger_build.trigger_task({'task_name':'ping'})).print()

    def test_trigger_load_sheet(self):
        file_id = '1_Bwz6z34wALFGb1ILUXG8CtF1-Km6F9_sGXnAu4gewY'
        command = 'load_sheet'
        build_id = self.trigger_build.trigger_task('update_sheet',file_id, command)
        Dev.pprint(build_id)
        #self.api.code_build.build_wait_for_completion(build_id)

    def test_trigger_sync_sheet(self):
        file_id = '1_Bwz6z34wALFGb1ILUXG8CtF1-Km6F9_sGXnAu4gewY'
        command = 'sync_sheet'
        build_id = self.trigger_build.trigger_task('update_sheet',file_id, command)
        Dev.pprint(build_id)

    # def test_jira_load(self):
    #     file_id = '1_Bwz6z34wALFGb1ILUXG8CtF1-Km6F9_sGXnAu4gewY'
    #     gsuite_secret_id ='gsuite_gsbot_user'
    #     sheets_sync = API_Jira_Sheets_Sync(file_id=file_id, gsuite_secret_id=gsuite_secret_id)
    #     result = sheets_sync.load_data_from_jira()
    #     Dev.pprint(result)

