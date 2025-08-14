import pandas as pd
import numpy as np


# Load the dataset
df = pd.read_csv("Data Set/indian_employees_data.csv")
print(df.head(n=5), end="\n\n============\n\n")

# Checking the missing value
print("Missing values in each column\n-------------------")
print(df.isnull().sum())

# replacing the nan values
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Salary"].fillna(df["Salary"].mean(), inplace=True)
# df["ExperienceYears"].fillna(df["ExperienceYears"].mean(), inplace=True)

# replacing the inf/-inf values to nan

df.replace([np.inf, -np.inf], np.nan, inplace=True)

# filling the nan values
df.fillna(21, inplace=True)

# remove duplicates
df.drop_duplicates(inplace=True)

# df.to_csv("Data Set/final.csv", index=False)
# print(df.head())

# remove negative salaries
df["Salary"] = np.where(df["Salary"] < 0, df["Salary"].mean(), df["Salary"])

print(df.head())