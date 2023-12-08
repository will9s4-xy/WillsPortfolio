import unittest
from io import StringIO
from unittest.mock import patch
from source.service import add_user, remove_user, read_database, database

class TestUserManagement(unittest.TestCase):

    @patch('builtins.input', side_effect=['Doug'])
    def test_add_user(self, mock_input):
        initial_count = len(database)
        add_user()
        updated_count = len(database)
        self.assertEqual(updated_count, initial_count + 1)

    @patch('builtins.input', side_effect=['Bob'])
    def test_remove_user_existing_user(self, mock_input):
        initial_count = len(database)
        remove_user()
        updated_count = len(database)
        self.assertEqual(updated_count, initial_count - 1)

    @patch('builtins.input', side_effect=['Dave'])
    def test_remove_user_non_existing_user(self, mock_input):
        initial_count = len(database)
        remove_user()
        updated_count = len(database)
        self.assertEqual(updated_count, initial_count)

    @patch('builtins.input')
    def test_read_database(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            read_database()
            output = mock_stdout.getvalue().strip()
            self.assertIn('User ID:', output)
            self.assertIn('Username:', output)

if __name__ == '__main__':
    unittest.main()
