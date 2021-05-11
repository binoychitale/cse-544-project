import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class Bayesian:
    lambda_power = 0
    e_exponent = 0
    denominator = 1

    def __init__(self, beta):
        self.e_exponent = 1 / beta
        self.denominator = beta

    def get_posterior(self, observations):
        sum_obs = 0
        prod_fact = 1
        for obs in observations:
            sum_obs += obs
            prod_fact *= math.factorial(obs)

        self.lambda_power += sum_obs
        self.denominator *= prod_fact
        self.e_exponent += len(observations)

    def get_pdf(self, x):
        result = []
        for point in x:
            result.append((pow(point, self.lambda_power) * pow(math.e, -1 * point * self.e_exponent)) / 1)

        return result


def combine_deaths(row):
    return row['CT deaths'] + row['DC deaths']


def plot_pdf(estimator, trial):
    x_axis = np.arange(0, 100, 0.001)
    plt.plot(x_axis, estimator.get_pdf(x_axis), label=("row " + str(trial)))


def perform_bayesian_inference(daily_data):
    daily_data['Date'] = pd.to_datetime(daily_data['Date'])
    daily_data['combined_deaths'] = daily_data.apply(lambda row: combine_deaths(row), axis=1)

    mme_start_date = pd.to_datetime('2020-06-01')
    mme_end_date = mme_start_date + pd.DateOffset(days=28)

    MME_data = daily_data[(daily_data['Date'] >= mme_start_date) & (daily_data['Date'] < mme_end_date)]
    lambda_mme = MME_data.mean(axis=0)['combined_deaths']

    bayesian_estimator = Bayesian(lambda_mme)

    for i in range(0, 4):
        mme_start_date = mme_end_date
        mme_end_date = mme_start_date + pd.DateOffset(days=7)

        observations = np.array(daily_data[(daily_data['Date'] >= mme_start_date) & (daily_data['Date'] < mme_end_date)]['combined_deaths'])
        bayesian_estimator.get_posterior(observations)
        plot_pdf(bayesian_estimator, i + 1)
    plt.legend()
    plt.show()
