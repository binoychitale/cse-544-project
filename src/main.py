import clean
from ks_test import KS_2_Sample_Test

data = clean.get_cleaned_data("../data/States Data/4.csv")
#print(data)

# 2c) Perform 2-Sample KS Test on the #cases/#deaths data of the 2 states
KS_2_Sample_Test(data, 'confirmed')
KS_2_Sample_Test(data, 'deaths')