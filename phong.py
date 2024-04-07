import pandas as pd

# A: Delete blank data
# B: Delete duplicate data
# C: Delete data containing negative numbers
# D: Delete data containing special characters

action = "D"
ProductData_csv = "ProductData.csv"

data = pd.read_csv(ProductData_csv)

if action == "A":
    done = data.dropna()
elif action == "B":
    done = data.drop_duplicates()
elif action == "C":
    column = "Price"  # Column name that needs to handle negative data
    if column in data.columns:
        done = data[data[column] >= 0]
    else:
        print(f"Error: Column '{column}' does not exist in the data")
        done = None
elif action == "D":
    column_name = "ProductName"  # Column names that need to process data contain special 
    if column_name in data.columns:
        data[column_name] = data[column_name].str.replace(r'[^a-zA-Z0-9\s]', '', regex=True)
        done = data
    else:
        print(f"Error: Column '{column_name}' does not exist in the data")
        done = None
else:
    print("Error: Invalid action")

if done is not None:
    done.to_csv(f"processed{ProductDatacsv}", index=False)
    print(f"The file {ProductData_csv} has been processed and saved as processed{ProductData_csv}")

