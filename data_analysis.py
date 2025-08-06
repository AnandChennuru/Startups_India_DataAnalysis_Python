import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom


df = pd.read_csv(r"data_sets/Startup_Success_India_Historical_2019_2023.csv")


## DESCRIPTIVE STATISTICS

# # Data Info.
# print(df.head())
# print(df.info())
# print(df.dtypes)
# print(df.describe())
#
# num_df = df.select_dtypes(include='number')
# cat_df = df.select_dtypes(include='object')
#
# # Totals
# print("Totals: ")
# print("Startups(2019-23): ", num_df["Startups"].sum())
# print("Jobs: ", num_df["Jobs"].sum())
# print("Funds: ", num_df["Avg_Funding_Received_Lakhs"].sum())
# print("Women-Led: ", num_df["Women_Led_Startups"].sum())
#
# # Simple Statistical Measures
# print(num_df.mean())
# print(num_df.median())
# print(num_df.std())
# print(num_df.describe())
# print(cat_df.describe())
#
# # Unique values
# print("Sectors: ", set(df["Focus_Sectors"]))
# print("Notable Programs: ", set(df["Notable_Programs"]))
#
# # State-wise - groupby
# print(df.groupby("State/UT")["Startups"].sum())
# print(df.groupby("State/UT")["Jobs"].sum())
# print(df.groupby("State/UT")["Support_Institutions_Count"].sum())


# Correlation
print("Startup_Survival_Rate vs. Avg_Funding_Received_Lakhs: ", df["Startup_Survival_Rate"].corr(df[
                                                                                                    "Avg_Funding_Received_Lakhs"]))
print("Startup_Survival_Rate vs. Education_Index: ", df["Startup_Survival_Rate"].corr(df["Education_Index"]))
print("Startup_Survival_Rate vs. Scaleup_Rate: ", df["Startup_Survival_Rate"].corr(df["Scaleup_Rate"]))
print("Startup_Survival_Rate vs. Urbanization_Level: ", df["Startup_Survival_Rate"].corr(df["Urbanization_Level (%)"]))
print("Avg_Funding_Received_Lakhs vs. Jobs: ", df["Avg_Funding_Received_Lakhs"].corr(df["Jobs"]))


## BINOMIAL PROBABILITY

# n = df["Startups"]
# p = df["Startup_Survival_Rate"]
# k = n*p
#
# # pmf
# pmf_values = np.array(binom.pmf(k,n,p))
# x_values_pmf = np.arange(len(pmf_values))
#
# plt.figure(figsize=(10, 4))
# plt.stem(x_values_pmf, pmf_values)
# plt.title('Binomial Probability Mass Function')
# plt.xlabel('Number of Successful Startups (k)')
# plt.ylabel('P(X = k)')
# plt.grid(True)
# plt.tight_layout()
# plt.show()
#
# # cf - fewer
# cdf_values = binom.cdf(k,n,p)
# x_values_cdf = np.arange(len(cdf_values))
#
# plt.plot(x_values_cdf, cdf_values, marker='o', linestyle='-', markersize=3)
# plt.title('Cumulative Distribution of Startup Success Probability')
# plt.xlabel('Startups (Index)')
# plt.ylabel('Cumulative Probability')
# plt.grid(True)
# plt.show()
#
# # cf - higher
# cdf2_values = 1- binom.cdf(k,n,p)
# x2_values_cdf = np.arange(len(cdf_values))
#
# plt.plot(x2_values_cdf, cdf2_values, marker='o', linestyle='-', markersize=3)
# plt.title('Cumulative Distribution of Startup Success Probability')
# plt.xlabel('Startups (Index)')
# plt.ylabel('Cumulative Probability')
# plt.grid(True)
# plt.show()
