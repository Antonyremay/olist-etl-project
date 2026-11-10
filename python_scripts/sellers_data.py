
import pandas as pd

# Loading Sellers Dataset

def load_sellers_data(seller_file_path):
    df = pd.read_csv(seller_file_path)
    print("Sellers Dataset Loaded Successfully")
    return df


# Inspecting Sellers Dataset

def inspect_sellers_data(df):
    print(df.head(10))
    print(f"Number of Rows: {len(df)}")
    print(f"Number of Columns: {len(df.columns)}")
    print(f"Shape of DataFrame: {df.shape}")

    df.info()

    print(f"Missing Values:\n{df.isnull().sum()}")


# Duplicate Inspection

def inspect_seller_duplicates(df):
    print("Exact Duplicate Rows:", df.duplicated().sum())
    print("Duplicate Seller IDs:",df.duplicated(subset='seller_id').sum())
    print("Unique Seller IDs:", df['seller_id'].nunique())


    duplicate_sellers = df[df['seller_id'].duplicated(keep=False)]
    if len(duplicate_sellers) > 0:
        print("Duplicate Seller Records:")
        print(duplicate_sellers)

# Location Inspection

def inspect_seller_locations(df):

    print("Unique Seller Cities:", df['seller_city'].nunique())

    print("Unique Seller States:", df['seller_state'].nunique())

    print("\nSeller Distribution by State:")
    print(df['seller_state'].value_counts(dropna=False))

    print("\nSeller Cities:")
    print(df['seller_city'].value_counts().head(20))

#  Cleaning Sellers Dataset

def clean_sellers_data(df):
    copied_df = df.copy()

    print("Rows Before Cleaning:", len(copied_df))

    # Remove exact duplicate rows
    copied_df = copied_df.drop_duplicates()

    # Standardize city and state names
    text_columns = ['seller_city', 'seller_state']

    for col in text_columns:
        copied_df[col] = copied_df[col].str.strip().str.upper()

    print("Rows After Cleaning:", len(copied_df))

    return copied_df

# Validating Cleaned Dataset

def validate_cleaned_sellers(df):

    print("Number of Rows:", len(df))
    print("Number of Columns:", len(df.columns))

    print("Exact Duplicate Rows:", df.duplicated().sum())

    print("Duplicate Seller IDs:",df.duplicated(subset='seller_id').sum())
    print("Missing Values:")
    print(df.isnull().sum())
    print("Unique Seller IDs:", df['seller_id'].nunique())

# Saving Cleaned Dataset

def save_cleaned_sellers_data(df):

    output_path = r"Data_sets\Cleaned_Dataset\cleaned_sellers.csv"

    df.to_csv(output_path, index=False)

    print("Cleaned Sellers Dataset Saved Successfully")


# sellers Main Function

def sellers_main():

    seller_file_path = r"Data_sets\Cleaned_Dataset\Olist_Dataset\olist_sellers_dataset.csv"
    seller_data = load_sellers_data(seller_file_path)
    inspect_sellers_data(seller_data)
    inspect_seller_duplicates(seller_data)
    inspect_seller_locations(seller_data)
    cleaned_sellers_data = clean_sellers_data(seller_data)
    validate_cleaned_sellers(cleaned_sellers_data)
    save_cleaned_sellers_data(cleaned_sellers_data)

    return cleaned_sellers_data


if __name__ == "__main__":
    cleaned_sellers_data = sellers_main()

