# -*- coding: utf-8 -*-
"""DS5110_HW4

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IHD_C8fbe-hre2yyCjAqIpROIyRITHBA
"""

import pandas as pd
import matplotlib.pyplot as plt

# load data
df = pd.read_csv('/content/Iris.csv')

# get numerical features
numerical_features = df.select_dtypes(include=['number']).columns

# zero-shift all values by the min and scale to the ratio of min/max
df_normalized = (df[numerical_features] - df[numerical_features].min()) / (df[numerical_features].max() - df[numerical_features].min())

# zero-shift all values by mean and divide by standard deviation
df_standardized = (df[numerical_features] - df[numerical_features].mean()) / df[numerical_features].std()

# concat original labels
df_normalized = pd.concat([df_normalized, df.drop(columns=numerical_features)], axis=1)
df_standardized = pd.concat([df_standardized, df.drop(columns=numerical_features)], axis=1)

# export
df_normalized.to_csv('normalized_iris.csv', index=False)
df_standardized.to_csv('standardized_iris.csv', index=False)

# histograms of standardized data columns with mean and median lines to examine distributions
plt.figure
plt.hist(df_standardized['SepalLengthCm'])
plt.axvline(df_standardized['SepalLengthCm'].mean(), color='r', linestyle='dashed', linewidth=1)
plt.axvline(df_standardized['SepalLengthCm'].median(), color='g', linestyle='dashed', linewidth=1)
plt.show()

plt.figure
plt.hist(df_standardized['SepalWidthCm'])
plt.axvline(df_standardized['SepalWidthCm'].mean(), color='r', linestyle='dashed', linewidth=1)
plt.axvline(df_standardized['SepalWidthCm'].median(), color='g', linestyle='dashed', linewidth=1)
plt.show()

plt.figure
plt.hist(df_standardized['PetalLengthCm'])
plt.axvline(df_standardized['PetalLengthCm'].mean(), color='r', linestyle='dashed', linewidth=1)
plt.axvline(df_standardized['PetalLengthCm'].median(), color='g', linestyle='dashed', linewidth=1)
plt.show()

plt.figure
plt.hist(df_standardized['PetalWidthCm'])
plt.axvline(df_standardized['PetalWidthCm'].mean(), color='r', linestyle='dashed', linewidth=1)
plt.axvline(df_standardized['PetalWidthCm'].median(), color='g', linestyle='dashed', linewidth=1)
plt.show()