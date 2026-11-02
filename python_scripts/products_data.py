import pandas as pd 

# Loading Products Dataset

def load_products_data(products_file_path):
    
    df=pd.read_csv(products_file_path)
    print("Product Dataset Loaded Successfully")
    return df

# products_Data Frame Inspection
def inspect_product_data(df):
    print(df.head(10))
    print(df.shape)
    print(f" The Number of Rows are {len(df)}")
    print(f" The Number of Columns are {len(df.columns)}")

    print(f" The datatype of Columns are")
    df.info()
    print(f"The Total Number of Missing Values is \n{df.isnull().sum()} ")

# Dupicate Rows and Data Inspection

def inspect_products_duplicates(df):
    df_identical=df.duplicated().sum()
    if df_identical>=1:
        print(f" The Identical row count is {(df_identical)}")
        print(df[df.duplicated()])
    else:
        print(" There are No duplicates")
    df_row_identical=df.duplicated(subset='product_id').sum()
    if df_row_identical>=1:
        print(f" The Identical Order_ID row count is {(df_row_identical)}")
        print(df[df.duplicated('product_id')])
    else:
        print(" There are No Product_ID duplicates")
    print(f"Unique Product ID's: {df['product_id'].nunique()}")

def products_main():
    products_file_path=r"Data_sets\Olist_Dataset\olist_products_dataset.csv"
    products_data=load_products_data(products_file_path)
    inspect_product_data(products_data)
    inspect_products_duplicates(products_data)

products_main()