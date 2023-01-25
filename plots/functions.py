import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


def plot_data_hist(dataframe: pd.DataFrame):
    for i in dataframe.columns:
        if dataframe[i].dtype != 'object':
            plt.subplots()
            sns.histplot(x=dataframe[i], data=dataframe, kde=True)
            plt.show()


def plot_data_box(dataframe: pd.DataFrame):
    for i in dataframe.columns:
        if dataframe[i].dtype != 'object':
            plt.subplots()
            sns.boxplot(x=dataframe[i], data=dataframe)
            plt.show()


def plot_count_box(dataframe: pd.DataFrame):
    for i in dataframe.columns:
        if dataframe[i].dtype != 'object':
            plt.subplots()
            sns.countplot(x=dataframe[i], data=dataframe)
            plt.show()
