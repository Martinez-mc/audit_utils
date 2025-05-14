# MDB to Excel Converter

import os
import subprocess
import pandas as pd

def export_table_to_csv(mdb_file, table_name, output_csv):
    try:
        command = ['mdb-export', mdb_file, table_name]
        with open(output_csv, 'w') as csv_file:
            subprocess.run(command, stdout=csv_file, check=True)
        print(f"Exported {table_name} to {output_csv}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while exporting {table_name}: {e}")

def merge_dataframes(df1, df2):
    # Merge the two DataFrames on the 'strMapAcctNo' column
    merged_df = pd.merge(df1, df2, on='strMapAcctNo', how='inner')
    
    # Select the required columns
    selected_columns = [
        'strMapAcctNo', 'strMapAcctName', 'strAccountNo', 'strAccountName', 'strClass',
        'curCYPrelim', 'curPYFinal1', 'curPYFinal2', 'curPYFinal3',
        'curPYFinal4', 'curPYFinal5', 'curPYFinal6', 'strType', 'strSign'
    ]
    
    # Return the DataFrame with only the selected columns
    return merged_df[selected_columns]

def get_mdb_file(directory):
    # List all files in the specified directory
    files = os.listdir(directory)
    
    # Filter for MDB files
    mdb_files = [f for f in files if f.endswith('.mdb')]
    
    # Check the number of MDB files found
    if len(mdb_files) == 0:
        raise FileNotFoundError("No MDB files found in the directory.")
    elif len(mdb_files) > 1:
        raise ValueError("More than one MDB file found in the directory.")
    
    # Return the full path of the found MDB file
    return os.path.join(directory, mdb_files[0])

if __name__ == "__main__":
    # Directory containing the MDB file
    mdb_directory = 'mdb/'
    
    try:
        # Get the MDB file from the directory
        mdb_file = get_mdb_file(mdb_directory)
        
        # Define CSV file names
        csv_gl_account = 'tblGLAccount.csv'
        csv_gl_map_account = 'tblGLMapAccount.csv'
        
        # Export the tables to CSV
        export_table_to_csv(mdb_file, 'tblGLAccount', csv_gl_account)
        export_table_to_csv(mdb_file, 'tblGLMapAccount', csv_gl_map_account)
        
        # Read the CSV files into DataFrames
        df_gl_account = pd.read_csv(csv_gl_account)
        df_gl_map_account = pd.read_csv(csv_gl_map_account)
        
        # Merge the DataFrames
        merged_df = merge_dataframes(df_gl_account, df_gl_map_account)
        
        # Export the merged DataFrame to Excel without the index
        merged_df.to_excel('cw_tb.xlsx', index=False)
        
        # Clean up: delete the CSV files
        os.remove(csv_gl_account)
        os.remove(csv_gl_map_account)
        print(f"Deleted temporary files: {csv_gl_account} and {csv_gl_map_account}")
        
        print(merged_df)
        
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
