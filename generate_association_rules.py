import pandas as pd
from apyori import apriori

def generate_rules(transactions_file, min_support=0.01, min_confidence=0.2, min_lift=3, min_length=2):
    # Load transactions from pickle file
    transactions = pd.read_pickle(transactions_file)
    
    # Apply Apriori algorithm
    association_rules = apriori(transactions, 
                                min_support=min_support, 
                                min_confidence=min_confidence, 
                                min_lift=min_lift, 
                                min_length=min_length)
    
    # Convert association rules to a list
    rules = list(association_rules)
    
    return rules

def print_rules(rules, output_file):
    # Open a file to write the results
    with open(output_file, 'w') as result_file:
        number = 1
        for rule in rules:
            pair = rule[0] 
            items = [x for x in pair]
            
            result_file.write(f"Rule #{number}\n")
            result_file.write(f"Antecedent: {items[0]} => Consequent: {items[1]}\n")
            result_file.write(f"Support: {rule[1]}\n")
            result_file.write(f"Confidence: {rule[2][0][2]}\n")
            result_file.write(f"Lift: {rule[2][0][3]}\n")
            result_file.write("="*50 + "\n")
            
            print(f"Rule #{number}")
            print(f"Antecedent: {items[0]} => Consequent: {items[1]}")
            print(f"Support: {rule[1]}")
            print(f"Confidence: {rule[2][0][2]}")
            print(f"Lift: {rule[2][0][3]}")
            print("="*50)
            
            number += 1

if __name__ == '__main__':
    # Input and output file paths
    transactions_file = 'data/transactions.pkl'
    output_file = 'Rules.txt'
    
    # Step 1: Generate association rules
    rules = generate_rules(transactions_file)
    
    # Step 2: Print and save the rules
    print_rules(rules, output_file)
    print(f"Rules saved to {output_file}")


transactions = pd.read_pickle('data/transactions.pkl')  # Load transaction data from the pickle file

# Step 2: Apply Apriori algorithm to generate association rules
association_rules = apriori(transactions, 
                            min_support=0.01, 
                            min_confidence=0.2, 
                            min_lift=3, 
                            min_length=2)

# Convert the association rules to a list
rules = list(association_rules)

# Step 3: Save the generated rules to a Pickle file
pd.to_pickle(rules, 'data/association_rules.pkl')  # Save rules to a Pickle file
print("Association rules saved to 'data/association_rules.pkl'")
