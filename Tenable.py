import pandas as pd 
# imports the path


def read_csv_file(file_path):
    # Reads a CSV file and returns a DataFrame.

    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
           # Includes error handling for file reading issues.

file_path = r'vulnerabilities-verified.csv'  
# Path to the CSV file

data = read_csv_file(file_path)
# Reads the CSV file


# 100K plus
# exported as Excel

# Separate each column into a variable if data is available
if data is not None:
    display_ipv4_address = data['asset.display_ipv4_address']
    #asset_id = data['asset.id']
    asset_name = data['asset.name']
    asset_tags = data['asset.tags']
    #definition_id = data['definition.id']
    definition_name = data['definition.name']
    #definition_vpr_score = data['definition.vpr.score']
    vulnerability_id = data['id']
    #port = data['port']
    #protocol = data['protocol']
    severity = data['severity']
    #state = data['state']
else:
    print("No data available to separate columns.")
# Separate which data you want in each column 

print(asset_tags.head()) #column maybe?
#print(asset_id.head())
print(asset_name.head())
print(vulnerability_id.head())
print(severity.head())
# You can now print which one you want 