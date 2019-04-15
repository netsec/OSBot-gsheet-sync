from unittest import TestCase

from osbot_aws.apis.IAM import IAM
from osbot_aws.helpers.Create_Code_Build import Create_Code_Build
from pbx_gs_python_utils.utils.Dev import Dev


class test_Trigger_Builds(TestCase):

    def setUp(self):
        self.project_name = 'OSBot-gsheet-sync'
        self.account_id = IAM().account_id()
        self.api = Create_Code_Build(account_id=self.account_id, project_name=self.project_name)

    def test_trigger_Update_Sheet(self):
        kvargs = {
                    'projectName'       : self.project_name,
                    'buildspecOverride' : 'osbot_gsheet_sync/update_sheet/buildspec.yml'
                  }
        result = self.api.code_build.codebuild.start_build(**kvargs)#.get('build').get('arn')

        Dev.pprint(result)


