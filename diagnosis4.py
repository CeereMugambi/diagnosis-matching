#This code outputs a list of the tuples....eureka
import pandas as pd

# Load data into a Pandas DataFrame
data = pd.read_excel('META_DATA_DIAGNOSIS.xlsx', engine='openpyxl', names=['code', 'diagnosis', 'smart common name'], keep_default_na=False)

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

#example testing
results = lookup('pid', data)
if results is None:
    print("No diagnoses found.")
else:
    # Create a DataFrame from the list of tuples
    df = pd.DataFrame(results, columns=['Diagnosis', 'Diagnosis Code'])
    print(df)
