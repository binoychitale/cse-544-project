import clean
import one_sample_ks_perm

data, daily_data = clean.get_cleaned_data("../data/States Data/4.csv")
#print(data)

# 2c) Perform 1-Sample KS and Permutations tests on the #cases/#deaths data of the 2 states
one_sample_ks_perm.KS_1_sample_main(daily_data)
one_sample_ks_perm.Permutation_main(daily_data)