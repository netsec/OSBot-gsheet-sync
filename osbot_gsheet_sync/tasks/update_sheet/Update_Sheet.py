import os

from osbot_gsuite.apis.sheets.API_Jira_Sheets_Sync import API_Jira_Sheets_Sync
from pbx_gs_python_utils.utils.Dev import Dev
from pbx_gs_python_utils.utils.Lambdas_Helpers import slack_message
from pbx_gs_python_utils.utils.Misc import Misc


class Update_Sheet:

    def log_message(self):
        graph_name = 'graph_BEY'
        folder     = '1o-kpQ9sLzo0_wE13XcmnUuH7GNsHpdbp'
        domain     = 'photobox.com'

        print('******* In Update_Sheet **** [Start]')
        message = os.environ['message']
        channel = 'DDKUZTK6X'
        team_id = 'T7F3AUXGV'
        slack_message(message, [], channel, team_id)

        file_id = '1_Bwz6z34wALFGb1ILUXG8CtF1-Km6F9_sGXnAu4gewY'
        gsuite_secret_id = 'gsuite_gsbot_user'
        sheets_sync = API_Jira_Sheets_Sync(file_id=file_id, gsuite_secret_id=gsuite_secret_id)
        sheet_name = sheets_sync.sheet_name()
        Dev.pprint('sheet name', sheet_name)
        sheet_data = sheets_sync.get_sheet_data(sheet_name)
        Dev.pprint(sheet_data)

        sheets_sync.update_sheet_data_with_jira_data(sheet_data)
        raw_data = sheets_sync.convert_sheet_data_to_raw_data(sheet_data)
        sheets_sync.update_file_with_raw_data(raw_data, sheets_sync.sheet_name())
        sheets_sync.update_file_with_raw_data(raw_data,sheets_sync.sheet_name_backup())
        return "loaded data from jira completed...."
        #result = sheets_sync.load_data_from_jira()
        #Dev.pprint(result)


        print('******* In Update_Sheet **** [End]')

    def exec_command(self):
        file_id = os.environ.get('file_id')
        command = os.environ.get('command')
        if file_id is None or command is None:
            Dev.pprint('**** missing file_id or command environment variables****')
        else:
            gsuite_secret_id = 'gsuite_gsbot_user'
            sheets_sync = API_Jira_Sheets_Sync(file_id=file_id, gsuite_secret_id=gsuite_secret_id)
            if command is 'load_sheet': result = sheets_sync.load_data_from_jira()
            if command is 'sync_sheet': result = sheets_sync.sync_sheet()

            Dev.pprint('****** result*****', result)

if __name__ == '__main__':
    Update_Sheet().exec_command()