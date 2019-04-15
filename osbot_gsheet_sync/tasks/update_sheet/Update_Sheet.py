import os

from pbx_gs_python_utils.utils.Lambdas_Helpers import slack_message
from pbx_gs_python_utils.utils.Misc import Misc


class Update_Sheet:

    def log_message(self):
        print('******* In Update_Sheet **** [Start]')
        message = os.environ['message']
        channel = 'DDKUZTK6X'
        team_id = 'T7F3AUXGV'
        slack_message(message, [], channel, team_id)

        print('******* In Update_Sheet **** [End]')
if __name__ == '__main__':
    Update_Sheet().log_message()