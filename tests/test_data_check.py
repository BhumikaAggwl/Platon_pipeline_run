import os
import unittest

class TestDataPath(unittest.TestCase):
    def test_data_path_exists(self):
        path = "/Users/Lenovo/projects/isro/data"
        self.assertTrue(os.path.exists(path), f"Data path not found: {path}")

if __name__ == '__main__':
    unittest.main()
