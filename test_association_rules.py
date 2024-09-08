import pandas as pd
#from apyori import apriori

# Function to load the rules from the previous generation
def load_rules(file_path):
    # Load association rules from a pickle or regenerate them if needed
    rules = pd.read_pickle(file_path)
    return rules

# Example: Load association rules (already generated)
rules = pd.read_pickle('data/association_rules.pkl')  # Use your saved rules file


def predict_products(product, rules, top_n=3):
    # List to store matching rules
    matching_rules = []
    
    # Iterate through the rules and find ones where the product is in the antecedent
    for rule in rules:
        antecedent = list(rule[0])
        if product in antecedent:
            consequent = list(rule[2][0][1])  # Consequent from the rule
            confidence = rule[2][0][2]        # Confidence of the rule
            lift = rule[2][0][3]              # Lift of the rule
            support = rule[1]                 # Support of the rule
            
            # Append relevant details for each matching rule
            matching_rules.append({
                'antecedent': antecedent,
                'consequent': consequent,
                'confidence': confidence,
                'lift': lift,
                'support': support
            })
    
    # Sort the rules by [confidence] or lift (higher is better)
    matching_rules = sorted(matching_rules, key=lambda x: x['confidence'], reverse=True)
    
    # Return the top N rules
    return matching_rules[:top_n]


# Example: Test the model by predicting products likely to be bought with 'Product_1'
product = '60 CAKE CASES VINTAGE CHRISTMAS'
predicted_rules = predict_products(product, rules)

# Display the predictions
for i, rule in enumerate(predicted_rules):
    print(f"Prediction {i+1}:")
    print(f"  Antecedent: {rule['antecedent']}")
    print(f"  Consequent: {rule['consequent']}")
    print(f"  Confidence: {rule['confidence']}")
    print(f"  Lift: {rule['lift']}")
    print(f"  Support: {rule['support']}")
    print("="*50)
