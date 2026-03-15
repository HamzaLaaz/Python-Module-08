import pandas as pd

# Create a DataFrame (table of data)
df = pd.DataFrame({
    'name': ['Neo', 'Trinity', 'Morpheus'],
    'power': [95, 88, 92],
    'redpill': [True, True, True]
})

print(df.head())        # show first rows
print(df.describe())    # statistics summary
print(df['power'].mean())  # average of a column
