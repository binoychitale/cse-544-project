import pandas
import math
import numpy as np

def get_cleaned_data(filename):
    data_raw = pandas.read_csv(filename)
    outliers = set()
    daily_data = pandas.DataFrame()

    for column in data_raw:
        if column == 'Date':
            daily_data[column] = data_raw[column]
            continue
        
        daily_column = data_raw[column].diff().fillna(data_raw.iloc[0][column])
        daily_data[column] = daily_column
        sorted_column_data = np.array(daily_column.sort_values())

        Q3_index = math.ceil(75/100 * len(sorted_column_data))
        Q1_index = math.ceil(25/100 * len(sorted_column_data))
        alpha = 1.5
        IQR = sorted_column_data[Q3_index] - sorted_column_data[Q1_index]
        upper_threshold = sorted_column_data[Q3_index] + alpha * IQR
        lower_threshold = sorted_column_data[Q1_index] - alpha * IQR

        column_outliers = daily_column[(daily_column != 0) & ((daily_column < lower_threshold) | (daily_column > upper_threshold))].index
        outliers = outliers.union(column_outliers)
        print ("\nColumn: %s \nDropped %s outlier rows \nIQR = %s \nlower thresold = %s \nupper thresold = %s" % (
        column, len(column_outliers), IQR, lower_threshold, upper_threshold))

    data_raw.drop(outliers, inplace=True)
    daily_data.drop(outliers, inplace=True)

    return data_raw, daily_data
