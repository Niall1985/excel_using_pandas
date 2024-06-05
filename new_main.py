#if the user wishes to make entries into a blank excel workbook, then this is the code

import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()
new_file_path = os.getenv('NEW_EXCEL_FILE_PATH')
num_columns = int(input("Enter the number of columns: "))
columns = []
for i in range(num_columns):
    column_name = input(f"Enter the name for column {i+1}: ")
    columns.append(column_name)
num_rows = int(input("Enter the number of rows: "))
data = {column: [] for column in columns}
for i in range(num_rows):
    print(f"Enter data for row {i+1}:")
    for column in columns:
        value = input(f"Enter value for {column}: ")
        data[column].append(value)
new_data = pd.DataFrame(data)
new_data.to_excel(new_file_path, index=False)
print(f"Data has been saved to {new_file_path}")
