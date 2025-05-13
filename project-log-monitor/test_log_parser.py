
import unittest
import os
from log_parser import count_errors_in_log

class TestLogParser(unittest.TestCase):

    def setUp(self):
        # Create a temporary log file for testing
        self.test_log_file = "test_demo.log"
        with open(self.test_log_file, 'w') as f:
            f.write("[INFO] Startup complete\n")
            f.write("[ERROR] Database connection failed\n")
            f.write("[WARNING] Low memory\n")
            f.write("[ERROR] Timeout occurred\n")
            f.write("[INFO] Shutdown\n")

    def test_error_count(self):
        # Expecting 2 error lines
        result = count_errors_in_log(self.test_log_file)
        self.assertEqual(result, 2)

    def test_file_not_found(self):
        # Should return -1 when file does not exist
        result = count_errors_in_log("non_existing_file.log")
        self.assertEqual(result, -1)

    def tearDown(self):
        # Clean up the temporary test file
        if os.path.exists(self.test_log_file):
            os.remove(self.test_log_file)

if __name__ == '__main__':
    unittest.main()
