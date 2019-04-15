import sys ; sys.path.append('..')

from unittest import TestCase

from osbot_gsheet_sync.workflows.Update_Sheet import Update_Sheet


class test_Update_Sheet(TestCase):

    def setUp(self):
        self.api = Update_Sheet()

    def test_log_message(self):
        self.api.log_message()