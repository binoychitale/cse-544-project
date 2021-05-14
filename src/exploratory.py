import pandas as pd

us_all_date_col = 'Date'

# Returns datadrame containing mean daily cases for every month, for each state
def monthly_mean_daily_cases(daily_data, l_date_range, u_date_range):
    state_data = daily_data[(daily_data[us_all_date_col] >= l_date_range) & (daily_data[us_all_date_col] <= u_date_range)].copy()
    
    # Use aggregation to find mean monthly cases for every state
    state_data[us_all_date_col] = pd.to_datetime(state_data[us_all_date_col])
    monthly_cases_mean = state_data.groupby(pd.Grouper(key=us_all_date_col, freq='1M')).mean()
    monthly_cases_mean.index = monthly_cases_mean.index.strftime('%-m %Y')
    
    return monthly_cases_mean