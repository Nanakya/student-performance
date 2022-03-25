import pandas as pd
import statistics
import csv
df = pd.read_csv("sp.csv")
rs_list = df["reading score"].to_list()

#Mean for rs and Weight
rs_mean = statistics.mean(rs_list)

#Median for rs and weight
rs_median = statistics.median(rs_list)

#Mode for rs and weight
rs_mode = statistics.mode(rs_list)

#Printing mean, median and mode to validate
print("Mean, Median and Mode of rs is {}, {} and {} respectively".format(rs_mean, rs_median, rs_mode))

#Standard deviation for rs and weight
rs_std_deviation = statistics.stdev(rs_list)
print("standard deviation",rs_std_deviation)
#1, 2 and 3 Standard Deviations for rs
rs_first_std_deviation_start, rs_first_std_deviation_end = rs_mean-rs_std_deviation, rs_mean+rs_std_deviation
rs_second_std_deviation_start, rs_second_std_deviation_end = rs_mean-(2*rs_std_deviation), rs_mean+(2*rs_std_deviation)
rs_third_std_deviation_start, rs_third_std_deviation_end = rs_mean-(3*rs_std_deviation), rs_mean+(3*rs_std_deviation)
#1, 2 and 3 Standard Deviations for weight

#Percentage of data within 1, 2 and 3 Standard Deviations for rs
rs_list_of_data_within_1_std_deviation = [result for result in rs_list if result > rs_first_std_deviation_start and result < rs_first_std_deviation_end]
rs_list_of_data_within_2_std_deviation = [result for result in rs_list if result > rs_second_std_deviation_start and result < rs_second_std_deviation_end]
rs_list_of_data_within_3_std_deviation = [result for result in rs_list if result > rs_third_std_deviation_start and result < rs_third_std_deviation_end]
#Percentage of data within 1, 2 and 3 Standard Deviations for Weight

#Printing data for rs and weight (Standard Deviation)
print("{}% of data for rs lies within 1 standard deviation".format(len(rs_list_of_data_within_1_std_deviation)*100.0/len(rs_list)))
print("{}% of data for rs lies within 2 standard deviations".format(len(rs_list_of_data_within_2_std_deviation)*100.0/len(rs_list)))
print("{}% of data for rs lies within 3 standard deviations".format(len(rs_list_of_data_within_3_std_deviation)*100.0/len(rs_list)))
