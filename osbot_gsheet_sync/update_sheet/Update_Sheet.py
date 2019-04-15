from pbx_gs_python_utils.utils.Lambdas_Helpers import slack_message
from pbx_gs_python_utils.utils.Misc import Misc


class Update_Sheet:

    def log_message(self):
        message = Misc.random_string_and_numbers(prefix='this is a message from code build - ')
        channel = 'DDKUZTK6X'
        team_id = 'T7F3AUXGV'
        slack_message(message, [], channel, team_id)


if __name__ == '__main__':
    Update_Sheet().log_message()