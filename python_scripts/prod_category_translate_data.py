
import pandas as pd

# Loading Category Translation Dataset

def load_category_data(category_file_path):
    df = pd.read_csv(category_file_path)
    print("Category Translation Dataset Loaded Successfully")
    return df

# Inspecting Category Translation Dataset

def inspect_category_data(df):
    print(df.head(10))
    print(f"Number of Rows: {len(df)}")
    print(f"Number of Columns: {len(df.columns)}")
    print(f"Shape of DataFrame: {df.shape}")

    df.info()

    print(f"Missing Values:\n{df.isnull().sum()}")

# Duplicate Inspection

def inspect_category_duplicates(df):
    print("Exact Duplicate Rows:", df.duplicated().sum())

    print("Duplicate Portuguese Category Names:",df.duplicated(subset='product_category_name').sum())

    print("Duplicate English Category Names:",df.duplicated(subset='product_category_name_english').sum())

    print("Unique Portuguese Categories:",df['product_category_name'].nunique())

    print("Unique English Categories:",df['product_category_name_english'].nunique())


# Cleaning Category Translation Dataset

def clean_category_data(df):
    copied_df = df.copy()
    print("Rows Before Cleaning:", len(copied_df))
    copied_df = copied_df.drop_duplicates()
    text_columns = ['product_category_name','product_category_name_english']
    for col in text_columns:
        copied_df[col] = copied_df[col].str.strip().str.lower()
    print("Rows After Cleaning:", len(copied_df))
    return copied_df

# Validating Cleaned Dataset

def validate_cleaned_category(df):

    print("Number of Rows:", len(df))
    print("Number of Columns:", len(df.columns))
    print("Exact Duplicate Rows:", df.duplicated().sum())
    print("Duplicate Portuguese Category Names:",df.duplicated(subset='product_category_name').sum())
    print("Missing Values:")
    print(df.isnull().sum())
    print("Unique Portuguese Categories:",df['product_category_name'].nunique())
    print("Unique English Categories:",df['product_category_name_english'].nunique())


# Saving Cleaned Dataset

def save_cleaned_category_data(df):
    output_path = r"Data_sets\Cleaned_Dataset\cleaned_category_translation.csv"
    df.to_csv(output_path, index=False)
    print("Cleaned Category Translation Dataset Saved Successfully")

# Category Translation Main Function

def category_main():

    category_file_path = r"Data_sets\Cleaned_Dataset\Olist_Dataset\product_category_name_translation.csv"
    category_data = load_category_data(category_file_path)
    inspect_category_data(category_data)
    inspect_category_duplicates(category_data)
    cleaned_category_data = clean_category_data(category_data)
    validate_cleaned_category(cleaned_category_data)
    save_cleaned_category_data(cleaned_category_data)
    return cleaned_category_data


if __name__ == "__main__":
    cleaned_category_data = category_main()
