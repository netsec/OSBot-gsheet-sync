import sys; sys.path.append('.')
import os
from pbx_gs_python_utils.utils.Dev      import Dev
from osbot_gsheet_sync.api.Run_Command  import Run_Command

class Update_Sheet:

    def exec_command(self):
        print('******* In Update_Sheet **** [Start]')
        file_id = os.environ.get('file_id')
        command = os.environ.get('command')

        if file_id is None or command is None:
            Dev.pprint('**** missing file_id or command environment variables****')
        else:
            result = Run_Command(file_id).run(command)
            Dev.pprint('****** result*****', result)

        return "loaded data from jira completed...."

if __name__ == '__main__':
    Update_Sheet().exec_command()