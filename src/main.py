import clean
import bayesian_inference

data, daily_data = clean.get_cleaned_data("../data/States Data/4.csv")
bayesian_inference.perform_bayesian_inference(daily_data)
#print(data)