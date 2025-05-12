#eda_lib.py

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def outlier_detecterminator(df, col : str):

  Q1 = df[col].quantile(0.25)
  Q3 = df[col].quantile(0.75)
  IQR = Q3 - Q1
  lower_bound = round(Q1 - 1.5*IQR,3)
  upper_bound = round(Q3 + 1.5*IQR,3)
  print(f"Lower Bound of {col}  =  {lower_bound}")
  print(f"Upper Bound of {col}  =  {upper_bound}")

  df_lower_0 = df[df[col] <= lower_bound]
  df_upper_0 = df[df[col] >= upper_bound]

  print(f"Lower bound count of {col}..: {df_lower_0.shape[0]}")
  print(f"Upper bound count of {col}..: {df_upper_0.shape[0]}")
  print('')

  sns.boxplot(df[col])
  plt.title(f"Boxplot of {col} before repressed")
  plt.show()

  print("")


  if not df_lower_0.empty:
    df.drop(df_lower_0.index, inplace=True)

  if not df_upper_0.empty:
    df.drop(df_upper_0.index, inplace=True)


  df_lower_1 = df[df[col] <= lower_bound]
  df_upper_1 = df[df[col] >= upper_bound]

  print(f"Lower bound count of {col}..: {df_lower_1.shape[0]}")
  print(f"Upper bound count of {col}..: {df_upper_1.shape[0]}")
  print('')


  sns.boxplot(df[col])
  plt.title(f"Boxplot of {col} after repressed")
  plt.show()

  print("")