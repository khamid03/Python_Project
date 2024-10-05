import sys
import unittest
import pandas as pd
import task

# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_read(self):
        self.assertEqual(task.read_head("dataset.csv"), str(pd.read_csv("dataset.csv").head()))

class TestImport(unittest.TestCase):
    def test_pandas(self):
        self.assertIn('pandas', sys.modules)
    def test_seaborn(self):
        self.assertIn('seaborn' , sys.modules)
    def test_matplotlib(self):
        self.assertIn('matplotlib.pyplot' , sys.modules)
if __name__ == '__main__':
    unittest.main()