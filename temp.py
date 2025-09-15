import numpy as np
import pandas as pd


 # URL to the CSV file on the UCI Machine Learning Repository
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# Column names for the Iris dataset (you can adjust them as needed)
column_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]

# Read the CSV file into a DataFrame
df = pd.read_csv(url, names=column_names)

# Display the first few rows of the DataFrame
print(df.head())
print(df.info())