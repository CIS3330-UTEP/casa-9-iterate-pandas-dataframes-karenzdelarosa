import pandas as pd
data = "big-mac-full-index.csv"
df = pd.read_csv(data)

# Method 4: Using iterrows()
print("Using iterrows() to iterate through rows:")
for index, row in df.iterrows():
    print(f"Row {index}: {row['name']} - {row['dollar_price']}")

#method 6
print("\nUsing apply() method:")
df.apply(lambda row: print(f"Row {row.name}: {row['name']} - {row['dollar_price']}"), axis=1)

