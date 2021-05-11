import pandas
import math
import numpy as np


def get_cleaned_data(filename):
    data_raw = pandas.read_csv(filename)

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

        outliers = daily_data[(daily_data != 0) & ((daily_data < lower_threshold) | (daily_data > upper_threshold))].index

        data_raw.drop(outliers, inplace=True)
        print ("\nColumn: %s \nDropped %s outlier rows \nIQR = %s \nlower thresold = %s \nupper thresold = %s" % (column, len(outliers), IQR, lower_threshold, upper_threshold))
    return data_raw
