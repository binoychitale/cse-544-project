import clean
from posterior import calculate_posterior

data, daily_data = clean.get_cleaned_data("../data/States Data/4.csv")
#print(data)

# 2d) Apply Bayesian Inference to calculate the posterior for combined deaths data
calculate_posterior(daily_data)