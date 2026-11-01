import pandas as pd 

# Loading the Dataset

def load_items_data(items_file_path):
    df=pd.read_csv(items_file_path)
    print("Items Data Loaded Successfully")
    return df

# Items Data Inspection

def items_data_inspection(df):
    print(df.head(5))
    print(df.shape)
    print(f"Number of Rows in Data Frame: \n{len(df)}")
    print(f"Number of columns in Data Frame: \n{len(df.columns)}")
    print(f"Columns in Data Frame: \n{(df.columns)}")
    df.info()
    print(f"Number of Missing Values in Order_Items_data: \n{df.isnull().sum()}")
    print(f"Number of Duplicated Values in Order_Items_data: {df.duplicated().sum()}")
    print(f"Number Order-item's combinations: {df.duplicated(['order_id','order_item_id']).sum()}")
    print(df[['price','freight_value']].describe())
    print(df.describe(include='all'))
    for col in df.columns:
        print(f"{col} : {df[col].nunique()} \nValue_Counts : {df[col].value_counts()}")

# Cleaning Items Dataset

def clean_items_data(df):
    copy_df=df.copy()
    copy_df['shipping_limit_date']=pd.to_datetime(copy_df['shipping_limit_date'],errors='coerce')
    print(f"Total Number of Negative Prices: {(copy_df['price']<0).sum()}")
    print(f"Total Number of Negative freight_value: {(copy_df['freight_value']<0).sum()}")
    print(f"Number Order-item's combinations: {copy_df.duplicated(['order_id','order_item_id']).sum()}")
    print("Missing shipping dates after conversion:",copy_df['shipping_limit_date'].isna().sum())
    
    return copy_df

# Saving The Cleaned Dataset

def save_cleaned_items(df):
    output_path = r"Data_sets\cleaned_order_items.csv"
    df.to_csv(output_path, index=False)
    print("Cleaned order items dataset saved.")
    print("Rows saved:", len(df))
    print("Columns saved:", len(df.columns))


def items_main():
    items_file_path=r"Data_sets\Olist_Dataset\olist_order_items_dataset.csv"
    items_data=load_items_data(items_file_path)
    items_data_inspection(items_data)
    cleaned_items_data=clean_items_data(items_data)
    save_cleaned_items(cleaned_items_data)

    return cleaned_items_data

if __name__=="__main__":
    (cleaned_items_data)= items_main()