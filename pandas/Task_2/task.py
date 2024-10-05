# todo: replace this with an actual task
import pandas as pd

def read_and_return_specific_column(filename):
    data = pd.read_csv(filename)
    return pd.DataFrame(data['platform'])
def read_and_set_index(filename):
    data = pd.read_csv(filename)
    data.set_index('genre', inplace=True)
    return data
def read_and_rename_column(filename):
    data = pd.read_csv(filename)
    data.rename({'platform':'device'},axis='columns', inplace=True)
    return data
def read_and_valuecount(filename):
    data = pd.read_csv(filename)
    data_new = pd.DataFrame(data['platform'].value_counts())
    return data_new
def read_and_sortvalues(filename):
    data = pd.read_csv(filename)
    data_new = data.sort_values(by='genre')
    return data_new
def read_and_return_specific_info(filename):
    data = pd.read_csv(filename)
    check = data['platform'] == 'PS4'
    return data[check]
def read_and_return_concatenation(filename):
    data = pd.read_csv(filename)
    check_1 = data['platform'] == 'PS4'
    check_2 = data['platform'] == 'XOne'
    answer = pd.concat([data[check_1], data[check_2]])
    return answer