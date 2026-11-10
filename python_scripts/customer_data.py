import pandas as pd 

# Loading the Dataset

def load_customer_data(customer_file_path):
    df=pd.read_csv(customer_file_path)
    print("Customers Data Loaded Successfully")
    return df

# Items Data Inspection

def customer_data_inspection(df):
    print(df.head(5))
    print(df.shape)
    print(f"Number of Rows in Data Frame: \n{len(df)}")
    print(f"Number of columns in Data Frame: \n{len(df.columns)}")
    print(f"Columns in Data Frame: \n{(df.columns)}")
    df.info()
    print(f"Number of Missing Values in Customers_data: \n{df.isnull().sum()}")
    print(f"Number of Duplicated Values in Customer_data: {df.duplicated().sum()}")
    for col in df.columns:
        print(f"{col} : {df[col].nunique()}")

# Cleaning the Customer Data

def clean_customer_data(df):
    cleaned_df = df.copy()

    text_columns = ['customer_city', 'customer_state']

    for col in text_columns:
        cleaned_df[col] = cleaned_df[col].str.strip().str.upper()
    print("Duplicate customer IDs:",Duplicate_customer:=(cleaned_df['customer_id'].duplicated().sum()))
    if Duplicate_customer>0:
        print(cleaned_df[cleaned_df['customer_id'].duplicated()])
    return cleaned_df

# Storing the Cleaned Dataset 

def save_cleaned_customers(df):
    output_path = r"Data_sets\Cleaned_Dataset\cleaned_customers.csv"
    df.to_csv(output_path, index=False)

    print("Cleaned customer data saved successfully!")
    print(f"Rows saved: {len(df)}")

def customer_main():
    customer_file_path=r"Data_sets\Cleaned_Dataset\Olist_Dataset\olist_customers_dataset.csv"
    customer_data=load_customer_data(customer_file_path)
    customer_data_inspection(customer_data)
    cleaned_customer_data=clean_customer_data(customer_data)
    save_cleaned_customers(cleaned_customer_data)
    return cleaned_customer_data

if __name__=="__main__":
    (cleaned_customer_data)=customer_main()