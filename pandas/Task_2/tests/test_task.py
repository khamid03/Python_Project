import unittest
import pandas as pd
from task import read_and_return_specific_column,read_and_set_index,read_and_rename_column,read_and_valuecount,read_and_sortvalues,read_and_return_specific_info,read_and_return_concatenation
from pandas.util.testing import assert_frame_equal
data = pd.read_csv('dataset.csv')
data1 = data.set_index('genre')
data2 = data.rename({'platform':'device'},axis='columns')
data3 = pd.DataFrame(data['platform'].value_counts())
data4 = data.sort_values(by='genre')

check = data['platform'] == 'PS4'
data5 = data[check]

check_1 = data['platform'] == 'PS4'
check_2 = data['platform'] == 'XOne'
data6 = pd.concat([data[check_1], data[check_2]])
# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_return_specific(self):
        assert_frame_equal(read_and_return_specific_column('dataset.csv'), pd.DataFrame(data['platform']))

    def test_return_set_index(self):
        assert_frame_equal(read_and_set_index('dataset.csv'), data1)

    def test_return_renamed(self):
        assert_frame_equal(read_and_rename_column('dataset.csv'), data2)

    def test_return_valuecount(self):
        assert_frame_equal(read_and_valuecount('dataset.csv'), data3)

    def test_return_sortvalues(self):
        assert_frame_equal(read_and_sortvalues('dataset.csv'), data4)

    def test_return_specific_info(self):
        assert_frame_equal(read_and_return_specific_info('dataset.csv'), data5)

    def test_return_concatenation(self):
        assert_frame_equal(read_and_return_concatenation('dataset.csv'), data6)
if __name__ == "__main__":
    unittest.main()