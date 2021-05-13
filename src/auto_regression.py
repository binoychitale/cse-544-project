import numpy as np
import pandas as pd


class AR:
    model = []
    order = 0

    def __init__(self, order):
        self.order = order


    def train(self, data):
        X_matrix = []
        Y_values = []
        start_index = self.order
        for i in range(start_index, len(data)):
            x_row = [1]
            Y_values.append([data[i]])
            for j in range(1, self.order + 1):
                x_row.append(data[i - (self.order - j)])
            X_matrix.append(x_row)

        X_matrix = np.float_(np.array(X_matrix))
        Y_values = np.float_(np.array(Y_values))
        b_matrix = np.matmul(np.linalg.inv(np.matmul(X_matrix.transpose(), X_matrix)), np.matmul(X_matrix.transpose(), Y_values))
        self.model = b_matrix

    def predict(self, input):
        return np.matmul(input, self.model)


def perform_auto_regression(data, order):
    ar = AR(order)

    for column in data:
        if column == 'Date':
            continue
        print()
        MSE = 0
        MAPE = 0
        for end in range(22, 29):
            end_date = '2020-08-%s' % end

            training_data = data[(data['Date'] >= '2020-08-01') & (data['Date'] < end_date)]

            ar.train(np.float_(np.array(training_data[column])))

            input_values = [0]
            date_val = pd.to_datetime(end_date)
            for i in range(order):
                input_values.append(data[data['Date'] == date_val - pd.DateOffset(days=(order - i))][column].values[0])

            prediction = ar.predict(input_values)
            actual_value = data[data['Date'] == end_date][column].values[0]
            MSE += pow(prediction - actual_value, 2)
            MAPE += abs(prediction - actual_value) / actual_value * 100

            print("Predicted %s on %s: %s" % (column, end_date, prediction))
        MSE /= len(range(22,29))
        MAPE /= len(range(22, 29))

        print ("MSE for %s: %s" % (column, MSE))
        print ("MAPE for %s: %s" % (column, MAPE))