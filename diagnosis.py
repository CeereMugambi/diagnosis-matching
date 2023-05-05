#this code simply looksup the diagnosis given and outputs the corresponding code and smart common name as a tuple
#the tuple outputed comprises of only the first row found
import pandas as pd

# Load data into a Pandas DataFrame
data = pd.read_excel('META_DATA_DIAGNOSIS.xlsx', engine='openpyxl', names=['code', 'diagnosis', 'smart common name'], keep_default_na=False)

# Define a function to lookup the diagnosis code based on symptoms
def lookup(symptoms):
    # Find the first row that matches the symptoms
    row = data.loc[(data['diagnosis'] == symptoms)].iloc[0]
    
    # Return the diagnosis and code as a tuple
    return (row['smart common name'], row['code'])

# Example usage
diagnosis, code = lookup('ABDOMINAL AND PELVIC PAIN/PID')
print("Diagnosis:", diagnosis)
print("Diagnosis Code:", code)
