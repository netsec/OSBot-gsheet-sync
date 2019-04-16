from unittest import TestCase

from pbx_gs_python_utils.utils.Dev import Dev

from osbot_gsheet_sync.api.Run_Command import Run_Command


class test_Run_Command(TestCase):
    def setUp(self):
        file_id          = '1_Bwz6z34wALFGb1ILUXG8CtF1-Km6F9_sGXnAu4gewY'
        self.run_command = Run_Command(file_id=file_id)
        assert type(self.run_command.sync_class).__name__ is 'API_Jira_Sheets_Sync'

    def test_resolve_method(self):
        assert type(self.run_command.resolve_method('sync_sheet')).__name__== 'method'
        assert self.run_command.resolve_method('abc') is None

    def test_run(self):
        self.run_command.sync_class.jira_rest = lambda: 'jira rest command'                             # hook method
        assert self.run_command.run('jira_rest') == {'data': 'jira rest command', 'status': 'ok'}       # confirm method call
        assert self.run_command.run('abc')       == { 'data': 'class `API_Jira_Sheets_Sync` did not contain the method `abc`','status': 'not-found'}

    def test_run_load_sheet(self):
        result = self.run_command.run('load_sheet')
        Dev.pprint(result)

    def test_run_load_sheet_mock(self):
        assert self.run_command.resolve_method('load_data_from_jira') is not None
        assert self.run_command.resolve_method('load_sheet'         ) == self.run_command.resolve_method('load_data_from_jira')

        self.run_command.sync_class.load_sheet = lambda : 'in load_sheet'
        assert self.run_command.run('load_sheet') == {'data': 'in load_sheet', 'status': 'ok'}





