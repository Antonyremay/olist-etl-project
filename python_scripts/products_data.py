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

# Handling Missing Values

def missing_prod_categories(df):
    print(f"Missing Values: \n{df.isnull().sum()}")
    missing_val=(df['product_category_name'].isnull().sum())
    if missing_val>=1:
        print(df[df['product_category_name'].isnull()])
    else:
        print("No Missing Product Categories")

# Identifying missing_product_measurements

def inspect_missing_product_measurements(df):
    columns=['product_weight_g' ,'product_length_cm' ,'product_height_cm','product_width_cm']
    missing_rows=df[df[columns].isnull().any(axis=1)].copy()
    print(f"Total affected products: {len(missing_rows)}")
    print(missing_rows)
    missing_rows['missing_values_count'] = missing_rows[columns].isnull().sum(axis=1)
    print(missing_rows)
    invalid_measurement=df[(df[columns]<=0).any(axis=1)].copy()
    print(f"Total Invalid_Measurement products: {len(invalid_measurement)}")
    invalid_measurement['Invalid_values_count']=((invalid_measurement[columns]<=0).sum(axis=1))
    print(f"Invalid Measurement Counts: \n{invalid_measurement['Invalid_values_count'].value_counts()}")
    print(invalid_measurement)

# Standardizing the DataFrame

def clean_products_data(df):
    copied_df=df.copy()
    print(f"Before Cleaning Number of Rows are: {len(copied_df)}")
    copied_df['product_category_name']=copied_df['product_category_name'].str.strip().str.lower()
    print(f"After Cleaning Number of Rows are: {len(copied_df)}")
    return copied_df

# Validating Cleaned Dataframe

def validating_cleaned_df(df):
    columns=['product_weight_g' ,'product_length_cm' ,'product_height_cm','product_width_cm']
    print(f"Number of Rows after cleaning: {len(df)}")
    print(f"Number of Columns after cleaning {len(df.columns)}")
    print(f"Duplicate Product ID count {df.duplicated(subset='product_id').sum()}")
    print(f"Missing Values:\n{df.isnull().sum()}")
    missin_row=df[df[columns].isnull().any(axis=1)].copy()
    print(f"Total affected products: {len(missin_row)}")
    missin_row['Missing_valCount']=missin_row[columns].isnull().sum(axis=1)
    print(missin_row)
    Invalid_measurement=df[(df[columns]<=0).any(axis=1)].copy()
    Invalid_measurement['Negative_counts']=(Invalid_measurement[columns]<=0).sum(axis=1)
    print(Invalid_measurement)

# Storing Data

def save_cleaned_products_data(df):
        output_path = r"Data_sets\Cleaned_Dataset\cleaned_products.csv"
        df.to_csv(output_path,index=False)
        print("Cleaned Products Dataset Saved Successfully")
    
def products_main():
    products_file_path=r"Data_sets\Olist_Dataset\olist_products_dataset.csv"
    products_data=load_products_data(products_file_path)
    inspect_product_data(products_data)
    inspect_products_duplicates(products_data)
    missing_prod_categories(products_data)
    inspect_missing_product_measurements(products_data)
    cleaned_products_data=clean_products_data(products_data)
    validating_cleaned_df(cleaned_products_data)
    save_cleaned_products_data(cleaned_products_data)

    return cleaned_products_data

if __name__=="__main__":
     cleaned_products_data=products_main()