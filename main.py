import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
file_path = os.getenv('EXCEL_FILE_PATH')
existing_data = pd.read_excel(file_path, sheet_name='Sheet1')
car = input("Enter car: ")
color = input("Enter color: ")
age = int(input("Enter Age: "))
speed = int(input("Enter speed: "))
autopass = input("Enter Autopass: ")
new_data = pd.DataFrame({'Car name': [car],
                         'Color': [color],
                         'Age': [age],
                         'Speed': [speed],
                         'Autopass': [autopass]
                         })
appended_data = pd.concat([existing_data, new_data], ignore_index=True)
appended_data.to_excel(file_path, index=False, sheet_name='Sheet1')
