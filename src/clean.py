import pandas
import math
import numpy as np


def get_cleaned_data(filename):
    data_raw = pandas.read_csv(filename)
    outliers = set()

    for column in data_raw:
        if column == 'Date':
            continue
        daily_data = data_raw[column].diff()
        sorted_column_data = np.array(daily_data.sort_values())

        Q3_index = math.ceil(75/100 * len(sorted_column_data))
        Q1_index = math.ceil(25/100 * len(sorted_column_data))
        alpha = 1.5
        IQR = sorted_column_data[Q3_index] - sorted_column_data[Q1_index]
        upper_threshold = sorted_column_data[Q3_index] + alpha * IQR
        lower_threshold = sorted_column_data[Q1_index] - alpha * IQR

        column_outliers = daily_data[(daily_data != 0) & ((daily_data < lower_threshold) | (daily_data > upper_threshold))].index
        outliers = outliers.union(column_outliers)
        print ("\nColumn: %s \nDropped %s outlier rows \nIQR = %s \nlower thresold = %s \nupper thresold = %s" % (
        column, len(column_outliers), IQR, lower_threshold, upper_threshold))

    data_raw.drop(outliers, inplace=True)

    return data_raw


def get_daily_data(cumulative_data):
    for column in cumulative_data:
        if column == 'Date':
            continue
        cumulative_data[column] = cumulative_data[column].diff().fillna(0)

    return cumulative_data
