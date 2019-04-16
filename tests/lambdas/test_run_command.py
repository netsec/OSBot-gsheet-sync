from unittest import TestCase

from osbot_aws.helpers.Lambda_Package import Lambda_Package
from pbx_gs_python_utils.utils.Dev import Dev


import osbot_gsheet_sync._utils.Str_Extension_Methods
from pbx_gs_python_utils.utils.Files import Files

from osbot_gsheet_sync.lambdas.run_command import run


class test_run_command(TestCase):

    def test_invoke_lambda(self):
        package = Lambda_Package('osbot_gsheet_sync.lambdas.run_command')
        type(run)
        #code_folder = Files.path_combine(__file__, '..')
        code_folder = run.__code__.co_filename.path_combine('../..')#.file_exists().print()

        package.add_folder(code_folder).add_root_folder().add_pbx_gs_python_utils()
        package.get_files().print()
        #Dev.pprint(_.invoke())
            #.toString().print()
