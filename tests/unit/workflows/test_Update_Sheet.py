import os
import sys ; sys.path.append('..')

from unittest import TestCase

from osbot_gsheet_sync.tasks.update_sheet.Update_Sheet import Update_Sheet


class test_Update_Sheet(TestCase):

    def setUp(self):
        self.api = Update_Sheet()

    def test_exec_command(self):
        os.environ['file_id'] = '1_Bwz6z34wALFGb1ILUXG8CtF1-Km6F9_sGXnAu4gewY'
        os.environ['command'] = 'load_sheet'
        self.api.exec_command()