import os
import pandas as pd

# Define the paths for the source files and the output file
source_directory = r'C:\Users\carro\Downloads\Lead Procurement Analyst Business Case Solved\Business_B - Ayser'
destination_file = r'C:\Users\carro\Downloads\Lead Procurement Analyst Business Case Solved\Consolidated Data\Business B Consolidated.xlsx'

# Initialize an empty DataFrame to store the consolidated data
consolidated_data = pd.DataFrame()

# Loop through all the files in the source directory
for filename in os.listdir(source_directory):
    if filename.endswith('.xlsx'):
        # Construct the full file path
        file_path = os.path.join(source_directory, filename)
        
        # Read the "Data" sheet from the current Excel file
        try:
            df = pd.read_excel(file_path, sheet_name='Data')
            if not df.empty:
                # Combine 'Day', 'Month', 'Year' columns into a single 'Date' column
                if {'Day', 'Month', 'Year'}.issubset(df.columns):
                    df['Date'] = pd.to_datetime(df[['Year', 'Month', 'Day']])
                    df.drop(columns=['Day', 'Month', 'Year'], inplace=True)
                # Append the data to the consolidated DataFrame
                consolidated_data = pd.concat([consolidated_data, df], ignore_index=True)
        except Exception as e:
            print(f"Error reading {filename}: {e}")

# Check if the consolidated DataFrame is not empty before saving
if not consolidated_data.empty:
    # Aggregate data by Month and Printer, calculating average Availability and sum of Volume
    consolidated_data['Month'] = consolidated_data['Date'].dt.to_period('M')
    aggregated_data = consolidated_data.groupby(['Printer', 'Month']).agg({
        'Availability': 'mean',  # Calculate average availability
        'Volume': 'sum'
    }).reset_index()
    
    # Convert the 'Month' period back to a datetime format for easier handling
    aggregated_data['Month'] = aggregated_data['Month'].dt.to_timestamp()
    
    # Save the aggregated DataFrame to an Excel file
    os.makedirs(os.path.dirname(destination_file), exist_ok=True)
    aggregated_data.to_excel(destination_file, index=False)
    print(f"Aggregation and consolidation complete. Data saved to {destination_file}")
else:
    print("No data to consolidate. The output file was not created.")
