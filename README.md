# Excel Data Appender

This Python script appends user input data to an existing Excel file. The file path is stored in an environment file (.env) for easy configuration.

## Prerequisites

Ensure you have the following Python packages installed:

```bash
pip install pandas openpyxl python-dotenv
```

## Setup

1. Create a `.env` file in the root of your project directory with the following content:

```plaintext
EXCEL_FILE_PATH="your_excel_file_path"
```

2. Make sure the Excel file specified in `EXCEL_FILE_PATH` exists and has the following columns in a sheet named `Sheet1`:

| Car name | Color | Age | Speed | Autopass |
|----------|-------|-----|-------|----------|
| ...      | ...   | ... | ...   | ...      |

## Usage

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

## Example Excel Table

Before running the script:

| Car name | Color | Age | Speed | Autopass |
|----------|-------|-----|-------|----------|
| Ford     | Blue  | 5   | 120   | No       |
| Honda    | Black | 3   | 130   | Yes      |

After running the script with the provided input:

| Car name | Color | Age | Speed | Autopass |
|----------|-------|-----|-------|----------|
| Ford     | Blue  | 5   | 120   | No       |
| Honda    | Black | 3   | 130   | Yes      |
| Tesla    | Red   | 2   | 150   | Yes      |

## Troubleshooting

- Ensure the Excel file is not open in another program while running the script.
- Verify the `.env` file contains the correct path to your Excel file.
- Make sure the columns in the Excel file match the columns specified in the script.

---
This README provides comprehensive instructions for setting up and using the script, ensuring users can easily append data to their Excel files.
