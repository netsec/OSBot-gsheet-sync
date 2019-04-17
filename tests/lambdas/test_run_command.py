from unittest                           import TestCase
from pbx_gs_python_utils.utils.Dev      import Dev
from osbot_aws.helpers.Lambda_Package   import Lambda_Package

class test_run_command(TestCase):
    def setUp(self):
        self.task_name  = 'update_sheet'
        self.command    = 'load_sheet'
        self.file_id    = '1_Bwz6z34wALFGb1ILUXG8CtF1-Km6F9_sGXnAu4gewY'
        self.aws_lambda = Lambda_Package('osbot_gsheet_sync.lambdas.run_command')
        self.result     = None

        self.aws_lambda.update_code()       # use when wanting to update lambda function

    def tearDown(self):
        if self.result:
            Dev.pprint(self.result)

    def test_invoke_lambda(self):
        payload     = { 'task_name': self.task_name, 'command': self.command,'file_id': self.file_id }
        self.result = self.aws_lambda.invoke(payload)


    def test_ping(self):
        payload     = { 'task_name': 'ping'}
        self.result = self.aws_lambda.invoke(payload)


