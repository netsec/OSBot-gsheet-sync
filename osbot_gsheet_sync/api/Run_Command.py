from osbot_gsuite.apis.sheets.API_Jira_Sheets_Sync import API_Jira_Sheets_Sync
from pbx_gs_python_utils.utils.Misc import Misc


class Run_Command():
    def __init__(self,file_id):
        self.sync_class = API_Jira_Sheets_Sync(file_id=file_id)
        self.sync_class.load_sheet = self.sync_class.load_data_from_jira    # until this happens in the main method, fix it here

    def resolve_method(self, method_name):
        try:
            return getattr(self.sync_class, method_name)
        except:
            return None

    def run(self,command_name, **kwargs):
        method = self.resolve_method(command_name)
        if method:
            try:
                result = method(**kwargs)
                return { 'status': 'ok', 'data':result}
            except Exception as error:
                return {'status': 'error', 'data': '{0}'.format(error)}
        return {'status': 'not-found', 'data': 'class `{0}` did not contain the method `{1}`'.format(type(self.sync_class).__name__, command_name)}



