import pandas as pd

# Loading Order Dataset

def load_data(file_path):
    df=pd.read_csv(file_path)
    print(" Orders Dataset Loaded Successfully")
    return df

# Inspecting the Dataset

def data_inspection(df):
    print(df.head(5))
    print(df.shape)
    print(f"The Number of Rows are: {len(df)}")
    print(f"The Number of Columns are: {len(df.columns)}")
    print(f"Data Frame Columns: \n{df.columns} ")
    print("The Datatypes of columns are: ")
    df.info()
    print(df.dtypes)
    print(f"The Number of missing values in order dataset is: \n{df.isnull().sum()}")

# Duplicate Data Inspection

def duplicate_check(df):
    print(f"The Duplicated Rows: \n{df.duplicated().sum()}")
    print(f"The Duplicated Order_id's: \n{df.duplicated(subset=['order_id']).sum()}")
    print(f"The Number of Order belong to each Statuses: \n {df['order_status'].value_counts()}")

# Date Column Correction

def date_validating(df):
    date_columns=[]
    for col in df.columns:
        sample=df[col].dropna().head(20)
        if len(sample)>0:
            try:
                pd.to_datetime(sample,errors="raise")
                date_columns.append(col)
            except(ValueError,TypeError):
                pass
    print(f"Possible Columns: {date_columns}")
    missing_before = df[date_columns].isna().sum()
    print(f" Mssing Values: \n{missing_before}")

    for col in date_columns:
        df[col]=pd.to_datetime(df[col],errors="coerce")
    missing_after = df[date_columns].isna().sum()
    print(f"\nMissing values after conversion:\n{missing_after}")
    print(f"\nAdditional missing values:\n{missing_after - missing_before}")    

    print("Date Columns are Converted to Date Format")
    print("\n--- DATE COLUMN VALIDATION ---")
    print(df[date_columns].dtypes)
    
    return df,date_columns

# Standardizing Date Formats and Data Types

def cleaning_process (df):
    copied_df=df.copy()
    print(f"Columns in Copied Dataframe and its Datatypes: \n{copied_df.dtypes}")
    print(copied_df['order_status'].unique())
    copied_df['order_status']=copied_df['order_status'].str.strip().str.lower()
    print(copied_df['order_status'].unique())
    original_status = df['order_status']
    cleaned_status = copied_df['order_status']
    print("Rows changed:", (original_status != cleaned_status).sum())
    print(f"Duplicated Order_id's: {copied_df.duplicated(subset=['order_id']).sum()}")
    return copied_df

# Chronological_Wise Data Cleaning

def chronological_cleaning(df):

    date_pairs = [
            ('order_purchase_timestamp', 'order_approved_at'),
            ('order_purchase_timestamp', 'order_delivered_carrier_date'),
            ('order_purchase_timestamp', 'order_delivered_customer_date'),
            ('order_approved_at', 'order_delivered_carrier_date'),
            ('order_approved_at', 'order_delivered_customer_date'),
            ('order_delivered_carrier_date', 'order_delivered_customer_date')
        ]

    for earlier, later in date_pairs:
            invalid = df[earlier].notna() & df[later].notna() & (df[earlier]>df[later])

            print(f"\n{earlier} occurs after {later}: {invalid.sum()}")

            print(df.loc[invalid, ['order_id', earlier, later]].head())

    late_delivery = (df['order_delivered_customer_date'].dt.normalize()> df['order_estimated_delivery_date'].dt.normalize())

    print("Orders delivered after estimated date:", late_delivery.sum())

    print(df.loc[late_delivery, ['order_id','order_delivered_customer_date','order_estimated_delivery_date']].head())

def save_cleaned_orders(df):
    output_path=r"Data_sets/cleaned_orders.csv"
    df.to_csv(output_path,index=False)
    print("Cleaned orders dataset saved.")
    print("Saved rows:", len(df))
    print("Saved columns:", len(df.columns))
    print("Duplicate order IDs:", df["order_id"].duplicated().sum())

def Order_main():
    file_path=r"Data_sets\Cleaned_Dataset\Olist_Dataset\olist_orders_dataset.csv"
    order_data_df=load_data(file_path)
    data_inspection(order_data_df)
    duplicate_check(order_data_df)
    order_data_df,date_checked=date_validating(order_data_df)
    cleaned_order_data_df=cleaning_process(order_data_df)
    chronological_cleaning(cleaned_order_data_df)
    save_cleaned_orders(cleaned_order_data_df)


    return cleaned_order_data_df
if __name__=="__main__":
    Order_main()