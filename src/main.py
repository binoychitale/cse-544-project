import clean
import auto_regression
import pandas as pd
import numpy as np
import ewma

data, daily_data = clean.get_cleaned_data("../data/States Data/4.csv")
data['Date'] = pd.to_datetime(data['Date'])

auto_regression.perform_auto_regression(data, 3)
auto_regression.perform_auto_regression(data, 5)

ewma.run_ewma_analysis(data)

#print(data)