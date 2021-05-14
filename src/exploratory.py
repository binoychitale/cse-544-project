import pandas as pd

date_col_us_all = 'Date'
month_col_flights = 'MONTH'
year_col_flights = 'YEAR'

# Returns datadrame containing mean daily cases for every month, for each state
def monthly_mean_daily_cases(daily_data, l_date_range, u_date_range):
    state_data = daily_data[(daily_data[date_col_us_all] >= l_date_range) & (daily_data[date_col_us_all] <= u_date_range)].copy()
    
    # Use aggregation to find mean monthly cases for every state
    state_data[date_col_us_all] = pd.to_datetime(state_data[date_col_us_all])
    monthly_cases_mean = state_data.groupby(pd.Grouper(key=date_col_us_all, freq='1M')).mean()
    monthly_cases_mean.index = monthly_cases_mean.index.strftime('%-m %Y')
    
    return monthly_cases_mean

# Perform One-Tailed Unpaired T-Test to accept or reject the null hypothesis H0, such that 
# H0: mean(daily cancellations in month with no/least covid cases) >= mean(daily cancellations in month with highest covid cases)
# H1: mean(daily cancellations in month with no/least covid cases) < mean(daily cancellations in month with highest covid cases)
def one_tailed_unpaired_t_test(flights_data_NY, min_month_NY, max_month_NY):
    # X - Data for month with least average daily covid cases
    min_month, min_year = int(min_month_NY.split(' ')[0]), int(min_month_NY.split(' ')[1])
    X = flights_data_NY[(flights_data_NY[month_col_flights] == min_month) & (flights_data_NY[year_col_flights] == min_year)]

    # Y - Data for month with highest average daily covid cases
    max_month, max_year = int(max_month_NY.split(' ')[0]), int(max_month_NY.split(' ')[1])
    Y = flights_data_NY[(flights_data_NY[month_col_flights] == max_month) & (flights_data_NY[year_col_flights] == max_year)]