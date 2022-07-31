"""
Test custom Django management commands
"""

from unittest.mock import patch

from psycopg2 import OperationalError as Psycopg2Error

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """ Test Commands """

    # Tests waiting for DB when DB is ready
    def test_wait_for_db_ready(self, patched_check):
        # Return True when DB is ready
        patched_check.return_value = True

        # calling command
        call_command('wait_for_db')

        # command should call only once as connection is ready
        patched_check.assert_called_once_with(databases=['default'])

    # Test waiting when database is getting operational error
    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        # returning 2 Pycopg2Errors and
        # 3 OperationalErrors and True at last when DB is ready
        patched_check.side_effect = [Psycopg2Error] * 2 + \
                                    [OperationalError] * 3 + [True]

        call_command('wait_for_db')

        # command should call 6 times as DB is ready in 6th check
        self.assertGreater(patched_check.call_count, 0)

        patched_check.assert_called_with(databases=['default'])
