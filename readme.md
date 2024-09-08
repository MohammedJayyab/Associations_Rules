## Market Basket Analysis Using Apriori Algorithm

### Table of Contents

1. [Project Motivation](#motivation)
2. [Installation](#installation)
3. [File Descriptions](#descriptions)
4. [Steps to Run](#steps)
5. [Results](#results)
6. [License](#license)

## 1. Project Motivation <a name="motivation"></a>

The goal of this project is to perform market basket analysis using the Apriori algorithm to identify product associations from transactional data. This technique allows us to generate association rules that can help in making product recommendations, such as "Customers who bought X also bought Y." These insights can be applied in retail environments for cross-selling and recommendation systems to improve customer experience and increase sales.

This project uses:

The Apriori algorithm to find frequent itemsets and generate association rules.
Real-world retail data to identify patterns of frequently bought products.

## Installation <a name="installation"></a>

### Step 1: Create a Virtual Environment

We recommend creating a virtual environment to manage dependencies for the project:

`python -m venv venv`

Activate the virtual environment:

- On Windows:
  `venv\Scripts\activate`

- On Mac/Linux:
  `source venv/bin/activate`

### Step 2: Install Dependencies

Once the virtual environment is activated, install the necessary libraries using the `requirements.txt` file:

`pip install -r requirements.txt`

The required dependencies include:

- pandas
- scikit-learn
- numpy
- mlxtend
- apyori
- openpyxl

## 3. File Descriptions <a name="descriptions"></a>

The project includes the following key files:

- `data_preprocessing_xls.py`: This script loads, cleans, and processes the raw retail data from an Excel file containing multiple sheets. It filters out canceled transactions and prepares a list of unique product descriptions. Additionally, it generates a transaction matrix for market basket analysis and saves it to a pickle file (`transactions.pkl`).

- `generate_association_rules.py`: This script loads the transaction data from the pickle file, applies the Apriori algorithm to generate association rules, and saves the rules to a file (`association_rules.pkl`). It also prints and saves the generated rules for later use.

- `test_association_rules.py`: This script loads the previously generated association rules and tests them by predicting products likely to be bought together with a given product. It ranks the rules by confidence and lift and prints the top predicted product combinations.

- `requirements.txt`: A list of required libraries for the project.

## 4. Steps to Run <a name="steps"></a>

### Step 1: Preprocess the Data

Run the `data_preprocessing_xls.py` script to load and clean the raw Excel data, and generate a transaction dataset:

`python data_preprocessing_xls.py`

This script will:

- Combine data from all sheets in the Excel file.
- Clean and filter out invalid or canceled transactions.
- Save the processed transaction data as `transactions.pkl`.

### Step 2: Generate Association Rules

Run the `generate_association_rules.py` script to apply the Apriori algorithm and generate association rules:

`python generate_association_rules.py`

This script will:

- Load the transaction dataset (`transactions.pkl`).
- Apply the Apriori algorithm to identify frequent itemsets and - - generate association rules.
- Save the rules to `association_rules.pkl`.

### Step 3: Test Association Rules

Run the `test_association_rules.py` script to test and predict product combinations:

`python test_association_rules.py`

This script will:

- Load the generated association rules from `association_rules.pkl`.
- Predict products that are likely to be bought together with a specified product.
- Print the top rules based on confidence and lift.

## 5. Results <a name="results"></a>

### Association Rules:

The project successfully identifies associations between products from the dataset. Some examples of rules include:

**Rule #1**: If a customer buys `"60 CAKE CASES VINTAGE CHRISTMAS"`, they are likely to also buy `"PAPER CHAIN KIT VINTAGE CHRISTMAS"`.

- **Confidence**: 46.18%
- **Lift**: 14.28

  **Rule #2**: If a customer buys `"PAPER CHAIN KIT 50'S CHRISTMAS"`, they are also likely to buy `"PAPER CHAIN KIT VINTAGE CHRISTMAS"`.

- **Confidence**: 35.63%
- **Lift**: 11.01
  These rules can be used in retail systems to provide recommendations for frequently bought together products, which can drive cross-selling and improve the customer experience.

## 6. License <a name="License"></a>
