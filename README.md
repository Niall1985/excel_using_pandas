# Excel Data Appender

This Python script appends user input data to an existing Excel file or allows the user to create a new Excel workbook and enter data into it. The file paths are stored in an environment file (.env) for easy configuration.

## Prerequisites

Ensure you have the following Python packages installed:

```bash
pip install pandas openpyxl python-dotenv
```

## Setup

1. Create a `.env` file in

the root of your project directory with the following content:

```plaintext
EXCEL_FILE_PATH="path_to_your_file"
NEW_EXCEL_FILE_PATH="path_to_your_file"
```

## Usage

### Appending Data to an Existing Excel File

1. Run the script:

```bash
python your_script_name.py
```

2. Enter the required details when prompted:

```plaintext
Enter car: Tesla
Enter color: Red
Enter Age: 2
Enter speed: 150
Enter Autopass: Yes
```

3. The script will append the entered data to the existing Excel file in the specified sheet.

### Creating and Adding Data to a New Excel Workbook

1. Run the script:

```bash
python your_script_name.py
```

2. Enter the number of columns and their names:

```plaintext
Enter the number of columns: 5
Enter the name for column 1: Car name
Enter the name for column 2: Color
Enter the name for column 3: Age
Enter the name for column 4: Speed
Enter the name for column 5: Autopass
```

3. Enter the number of rows and data for each row:

```plaintext
Enter the number of rows: 1
Enter data for row 1:
Enter value for Car name: Tesla
Enter value for Color: Red
Enter value for Age: 2
Enter value for Speed: 150
Enter value for Autopass: Yes
```

4. The script will save the data to a new Excel file at the specified path.

## Example Excel Table

### Before Running the Script (Existing Excel File)

| Car name | Color | Age | Speed | Autopass |
|----------|-------|-----|-------|----------|
| Ford     | Blue  | 5   | 120   | No       |
| Honda    | Black | 3   | 130   | Yes      |

### After Running the Script with Provided Input (Existing Excel File)

| Car name | Color | Age | Speed | Autopass |
|----------|-------|-----|-------|----------|
| Ford     | Blue  | 5   | 120   | No       |
| Honda    | Black | 3   | 130   | Yes      |
| Tesla    | Red   | 2   | 150   | Yes      |

## Script

### Appending Data to an Existing Excel File

```python
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the path to the Excel file from the environment variable
file_path = os.getenv('EXCEL_FILE_PATH')

# Read the existing Excel file
existing_data = pd.read_excel(file_path, sheet_name='Sheet1')

# Prompt the user for input for each column
car = input("Enter car: ")
color = input("Enter color: ")
age = int(input("Enter Age: "))
speed = int(input("Enter speed: "))
autopass = input("Enter Autopass: ")

# Create a DataFrame with the user input
new_data = pd.DataFrame({'Car name': [car],
                         'Color': [color],
                         'Age': [age],
                         'Speed': [speed],
                         'Autopass': [autopass]
                         })

# Append new data to existing data using pd.concat
appended_data = pd.concat([existing_data, new_data], ignore_index=True)

# Write the appended data back to the Excel file with specified sheet name
appended_data.to_excel(file_path, index=False, sheet_name='Sheet1')
```

### Creating and Adding Data to a New Excel Workbook

```python
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the path to the new Excel file from the environment variable
new_file_path = os.getenv('NEW_EXCEL_FILE_PATH')

# Prompt the user for column names
num_columns = int(input("Enter the number of columns: "))
columns = []
for i in range(num_columns):
    column_name = input(f"Enter the name for column {i+1}: ")
    columns.append(column_name)

# Prompt the user for data for each column
num_rows = int(input("Enter the number of rows: "))
data = {column: [] for column in columns}

for i in range(num_rows):
    print(f"Enter data for row {i+1}:")
    for column in columns:
        value = input(f"Enter value for {column}: ")
        data[column].append(value)

# Create a DataFrame with the user input
new_data = pd.DataFrame(data)

# Save the DataFrame to a new Excel workbook
new_data.to_excel(new_file_path, index=False)

print(f"Data has been saved to {new_file_path}")
```

## Troubleshooting

- Ensure the Excel file is not open in another program while running the script.
- Verify the `.env` file contains the correct paths to your Excel files.
- Make sure the columns in the existing Excel file match the columns specified in the script when appending data.
