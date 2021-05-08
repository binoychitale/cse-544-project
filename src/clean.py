import pandas
import math

def get_cleaned_data(filename):
    data_raw = pandas.read_csv(filename)

    for column in data_raw:
        if column == 'Date':
            continue
        column_data = data_raw.sort_values(by=column)[column]
        Q3_index = math.ceil(75/100 * len(column_data))
        Q1_index = math.ceil(25/100 * len(column_data))
        alpha = 1.5
        IQR = column_data[Q3_index] - column_data[Q1_index]
        upper_threshold = column_data[Q3_index] + alpha * IQR
        lower_threshold = column_data[Q1_index] - alpha * IQR

        outliers = data_raw[(data_raw[column] != 0) & ((data_raw[column] > upper_threshold) | (data_raw[column] < lower_threshold))].index

        data_raw.drop(outliers, inplace=True)
        print ("\nColumn: %s \nDropped %s outlier rows \nIQR = %s \nlower thresold = %s \nupper thresold = %s" % (column, len(outliers), IQR, lower_threshold, upper_threshold))

    return data_raw