import pandas as pd

# Create a simple dictionary of data
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [24, 27, 22, 32],
    "Occupation": ["Engineer", "Doctor", "Artist", "Data Scientist"],
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)

# Basic DataFrame operations
# print("\nDataFrame Info:")
# print(df.info())

# print("\nSummary Statistics:")
# print(df.describe())

# print("\nAccessing a specific column (Age):")
# print(df['Age'])

# print("\nFiltering rows where Age > 25:")
# print(df[df['Age'] > 25])
