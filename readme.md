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

`test_association_rules.py`: This script loads the previously generated association rules and tests them by predicting products likely to be bought together with a given product. It ranks the rules by confidence and lift and prints the top predicted product combinations.

`requirements.txt`: A list of required libraries for the project.

## 4. Steps to Run <a name="steps"></a>

## 5. Results <a name="results"></a>

## 6. License <a name="License"></a>
