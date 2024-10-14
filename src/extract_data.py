import pandas as pd

def extract_data(file_path):
    # Load the customer Churn CSV data into DataFrame
    ds = pd.read_csv(filepath)
    return df

if __name__ == "__main__":
    file_path = "../data/customer_churn.csv"
    data = extract_data(filepath)
    print(data.head())
