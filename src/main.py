import clean
from hypothesis_tests import run_hypothesis_tests

data, daily_data = clean.get_cleaned_data("../data/States Data/4.csv")
#print(data)

# 2b) Wald's, Z and T Tests on the #cases/#deaths data of the 2 states in the given time range
run_hypothesis_tests(daily_data)