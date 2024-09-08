import pandas as pd

def load_and_clean_data(input_file):
    # Read all sheets from the Excel file into a dictionary of DataFrames
    all_sheets = pd.read_excel(input_file, sheet_name=None)

    # Combine all sheets into a single DataFrame
    combined_data = pd.concat(all_sheets.values(), ignore_index=True)
    
    # Filter out canceled transactions (those starting with 'C')
    not_canceled_retail_data = combined_data[~combined_data['Invoice'].astype(str).str.startswith('C', na=False)]
    
    # Drop rows with missing descriptions and convert descriptions to string
    not_canceled_retail_data = not_canceled_retail_data[~not_canceled_retail_data['Description'].isna()]
    not_canceled_retail_data['Description'] = not_canceled_retail_data['Description'].astype(str)
    
    return not_canceled_retail_data

def export_unique_descriptions_to_txt(data, output_file):
    # Get unique descriptions from the 'Description' column
    unique_descriptions = data['Description'].unique()
    
    # Write the unique descriptions to a text file
    with open(output_file, 'w') as f:
        for description in unique_descriptions:
            f.write(description + '\n')

    print(f"Unique descriptions saved to '{output_file}'")

def process_transaction_matrix(data):
    # Group data by invoice and get a list of items for each invoice
    gb_retail_data = data.groupby(['Invoice'])['Description'].apply(list).to_frame().reset_index()    
    
    # Extract transactions as a list of lists
    transactions = gb_retail_data['Description'].to_list()
    
    return transactions

if __name__ == '__main__':
    # Input Excel file with multiple sheets
    input_file = 'data/online_retail_II.xlsx'
    
    # Step 1: Load and clean the data (from all sheets)
    cleaned_data = load_and_clean_data(input_file)
    export_unique_descriptions_to_txt(cleaned_data, 'data/unique_products.txt')
    
    # Step 2: Process transaction matrix 
    transactions = process_transaction_matrix(cleaned_data)
    
    # Step 3: Optionally, save the transactions to a pickle file for future use
    pd.to_pickle(transactions, 'data/transactions.pkl')
    print("Transactions saved to 'data/transactions.pkl'")
