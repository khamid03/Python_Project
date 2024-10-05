import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def read_head(filename):
    data = pd.read_csv(filename)
    return str(data.head())
