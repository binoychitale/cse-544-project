import pandas
import math

def get_cleaned_data(filename):
    data_raw = pandas.read_csv(filename)
    deleted_rows = {}
    CT_confirmed = data_raw.sort_values(by="CT confirmed", ascending=False)["CT confirmed"]
    Q3_index = math.ceil(75/100 * len(CT_confirmed))
    Q1_index = math.ceil(25/100 * len(CT_confirmed))
    alpha = 1.5
    IQR = CT_confirmed[Q3_index] - CT_confirmed[Q1_index]

    upper_threshold = CT_confirmed[Q3_index] + alpha * IQR
    lower_threshold = CT_confirmed[Q1_index] - alpha * IQR

    outliers = data_raw[(data_raw['CT confirmed'] != 0) & ((data_raw['CT confirmed'] > upper_threshold) | (data_raw['CT confirmed'] < lower_threshold))].index

    data_raw.drop(outliers, inplace=True)

    print ("Dropped %s outlier rows \nIQR = %s \nlower thresold = %s \nupper thresold = %s" % (len(outliers), IQR, lower_threshold, upper_threshold))

    return data_raw