#This is interactive and enables the user to select an excel file and also to add the keyword to lookup
import pandas as pd
import tkinter as tk
import time
from tkinter import filedialog

# Define a function to browse for the Excel file
print('Welcome to Smart Diagnostics')
time.sleep(3)
print('Proceed to select your excel file')

def browse_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[('Excel files', '*.xlsx')])
    return file_path

# Ask the user to select the Excel file
file_path = browse_file()

# Load data into a Pandas DataFrame
data = pd.read_excel(file_path, engine='openpyxl', names=['code', 'diagnosis', 'smart common name'], keep_default_na=False)

def lookup(keyword, data):
    # Fill any NaN or NA values in the 'diagnosis' column with 'NA'
    data['diagnosis'] = data['diagnosis'].fillna('NA').astype(str)
    
    # Find all rows that contain the keyword in the 'diagnosis' column
    matches = data.loc[data['diagnosis'].str.contains(keyword, case=False)]
    
    # Check if any rows were found
    if len(matches) == 0:
        return None
    
    # Get all matching rows and return the diagnoses and codes as a list of tuples
    rows = [(row['smart common name'], row['code']) for _, row in matches.iterrows()]
    return rows

# Prompt the user to enter the keyword
keyword = input("Enter a keyword: ")

#example testing
results = lookup(keyword, data)
if results is None:
    print("No diagnoses found.")
else:
    # Create a DataFrame from the list of tuples
    df = pd.DataFrame(results, columns=['Diagnosis', 'Diagnosis Code'])
    print(df)
