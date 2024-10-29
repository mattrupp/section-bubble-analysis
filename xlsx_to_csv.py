import os
import pandas as pd
from pathlib import Path


# combine all sheets from an excel file
def read_and_concat_sheets(file_path, selected_columns):

    # Read the Excel file into an ExcelFile object
    excel_file = pd.ExcelFile(file_path)
    # Read the header row to get the existing column names
    df_header = pd.read_excel(file_path, nrows=0)
    existing_cols = df_header.columns.tolist()
    
    if selected_columns:
        selected_columns = [col for col in selected_columns if col in existing_cols]

    # Create an empty list to store the DataFrames
    dfs = []

    # Iterate through each sheet in the Excel file
    for sheet_name in excel_file.sheet_names:
        # Read the sheet into a DataFrame
        df = excel_file.parse(sheet_name, usecols=selected_columns)        
        # Append the DataFrame to the list
        dfs.append(df)
    # Concatenate all the DataFrames into one
    concatenated_df = pd.concat(dfs, ignore_index=True)

    return concatenated_df


def xls_to_csv(file_path, selected_columns=[], overwrite=False, multiple_sheets=False):
    try:
        file_path = Path(file_path)
        # make sure the file exists
        if file_path.is_file():
            base_name, ext = os.path.splitext(file_path)
            csv_file_path = Path(base_name + '.csv')

            if csv_file_path.is_file() and not overwrite:
                print(str(csv_file_path) + ' already exists!')
            else:
                if multiple_sheets:
                    df = read_and_concat_sheets(file_path, selected_columns)
                else:
                    excel_file = pd.ExcelFile(file_path)
                    # Read the header row to get the existing column names
                    df_header = pd.read_excel(file_path, nrows=0)
                    existing_cols = df_header.columns.tolist()
                    
                    if selected_columns:
                        selected_columns = [col for col in selected_columns if col in existing_cols]

                    df = excel_file.parse(usecols=selected_columns)
                # Write the DataFrame to a CSV file
                df.to_csv(csv_file_path, index=False)
                print(f'{csv_file_path} has been created.')
        return(csv_file_path)
    except Exception as error:
        print("An exception occurred:", error)
        print(f'File "{file_path}" not found!')


# xls_to_csv('bubble_orders.xlsx',
#                ['Line', 'Blend','EndOfPourTimeStamp', 'SmartPartNumber', 'Order Number'],
#                overwrite=False
#                )