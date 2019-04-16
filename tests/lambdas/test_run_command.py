from unittest import TestCase

from osbot_aws.helpers.Lambda_Package import Lambda_Package


class test_run_command(TestCase):

    def invoke_lambda(self):
        _ = Lambda_Package('osbot_gsheet_sync.lambdas.run_command')

        _._lambda
