import numpy as np


def predict_ewma(alpha, data):
    ewma = 0

    for i in range(len(data)):
        weight = pow(1 - alpha, i)
        ewma += weight * data[len(data) - 1 - i]
    return alpha * ewma

alpha_values = [0.5, 0.8]


def run_ewma_analysis(data):
    for column in data:
        if column == 'Date':
            continue
        print()
        for alpha in alpha_values:
            MSE = 0
            MAPE = 0
            mape_count = 0
            for end in range(22, 29):
                end_date = '2020-08-%s' % end

                training_data = data[(data['Date'] >= '2020-08-01') & (data['Date'] < end_date)]

                prediction = predict_ewma(alpha, np.float_(np.array(training_data[column])))
                print("Predicted %s on %s for alpha=%s: %s" % (column, end_date, alpha, prediction))

                actual_value = data[data['Date'] == end_date][column].values[0]
                MSE += pow(prediction - actual_value, 2)
                if actual_value != 0:
                    MAPE += abs(prediction - actual_value) / actual_value * 100
                    mape_count += 1

            MSE /= len(range(22, 29))
            MAPE /= mape_count
            print ("MSE for alpha = %s: %s" % (alpha, MSE))
            print ("MAPE for alpha = %s: %s" % (alpha, MAPE))