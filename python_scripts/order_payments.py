import pandas as pd 

# Loading Geolocation Dataset

def load_payment_data_path(file_path):
    
    df=pd.read_csv(file_path)
    print("Dataset Loaded Successfully")
    return df

# payment Data Frame Inspection
def inspect_payment_data(df):
    print(df.head(10))
    print(df.shape)
    print(f" The Number of Rows are {len(df)}")
    print(f" The Number of Columns are {len(df.columns)}")

    print(f" The datatype of Columns are")
    df.info()
    print(f"The Total Number of Missing Values is \n{df.isnull().sum()} ")

# Payment Duplicates_Inspection

def payment_duplicate_check(df):
    print(f"Total Number of Duplicates: {df.duplicated().sum()}")
    print("Duplicate order-payment combinations:",df.duplicated(subset=['order_id', 'payment_sequential']).sum())
    print(f"Unique Order ID's: {df['order_id'].nunique()}")
    print(f"Unique Payment Type's: {df['payment_type'].nunique()}")
    print(df['payment_type'].unique())
    print(f"Value Counts for Payment Types: \n{df['payment_type'].value_counts()}")
    print(df[['payment_value','payment_installments']].describe())
    print("Negative Payments:", negative_payment:=(df['payment_value']<0).sum())
    if negative_payment >0:
        print(df[df['payment_value']<0])
    print("Negative Installment Counts:", negative_installments:=(df['payment_installments']<=0).sum())
    if negative_installments>0:
        print(df[df['payment_installments']<=0])

# Payment Data Cleaning

def clean_payment_data(df):
    cleaned_df = df.copy()

    zero_installments = cleaned_df[cleaned_df['payment_installments'] <= 0]

    print("Records with zero or negative installments:")
    print(zero_installments)
    cleaned_df['payment_type'] = (cleaned_df['payment_type'].str.strip().str.lower())
    print(df['payment_value'].sum())

    return cleaned_df

# Cleaned Payment Data Stored

def save_cleaned_payments(df):
    output_path = r"Data_sets/cleaned_order_payments.csv"
    df.to_csv(output_path, index=False)

    print("Cleaned payment data saved successfully!")
    print(f"Rows saved: {len(df)}")

def payment_main():
    file_path=r"Data_sets/Cleaned_Dataset\Olist_Dataset/olist_order_payments_dataset.csv"
    payment_data=load_payment_data_path(file_path)
    inspect_payment_data(payment_data)
    payment_duplicate_check(payment_data)
    cleaned_payment_data=clean_payment_data(payment_data)
    save_cleaned_payments(cleaned_payment_data)

    return cleaned_payment_data

if __name__=="__main__":
    (cleaned_payment_data)=payment_main()