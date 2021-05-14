import clean
import auto_regression
import pandas as pd
import numpy as np
import ewma

import exploratory

# A) Mandatory tasks to be performed on assigned COVID-19 dataset (4.csv)
# 1) Clean dataset and detect outliers using Tukey’s rule. Also split given cumulative data into daily #cases/#deaths
data, daily_data = clean.get_cleaned_data("../data/States Data/4.csv", drop_outliers=True)
data['Date'] = pd.to_datetime(data['Date'])
#print(data)

# 2a) Time Series analysis
auto_regression.perform_auto_regression(data, 3)
auto_regression.perform_auto_regression(data, 5)
ewma.run_ewma_analysis(data)

# B) Exploratory tasks to be performed using US-all and X datasets. We have chosen our X dataset to be US domestic Flights cancellation data from Jan-Jun 2020.
# Full dataset can be found at https://www.kaggle.com/akulbahl/covid19-airline-flight-delays-and-cancellations?select=jantojun2020.csv
_, us_all_daily_data = clean.get_cleaned_data("../data/US-all/US_confirmed.csv", us_all=True, drop_outliers=False)

# Since our X dataset has flight data only from Jan-Jun 2020, and the US-all dataset has sparse data for Jan 2020 (just 9 entries),
# we will restrict our tests to only use Feb-June subset of US-all covid data.
monthly_cases_mean = exploratory.monthly_mean_daily_cases(us_all_daily_data, '2020-02-01', '2020-06-30')

# Find months with min and max monthly cases in New York, which we will use later in the hypostheses for our inferences.
# Both will be of the form '<month_number> <year>'. Eg: min='3 2020' denotes the month with least average cases is March 2020.
min_month_NY, max_month_NY = monthly_cases_mean['NY'].idxmin(), monthly_cases_mean['NY'].idxmax()
