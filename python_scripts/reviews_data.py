import pandas as pd

# Loading the dataset

def load_reviews_data(review_file_path):
    df=pd.read_csv(review_file_path)
    print("Data Loaded Successfuly")
    return df

# Inspecting Reviews DataFrame

def inspect_review_data(df):
    print(df.head(10))
    print(f"The number of Rows: {len(df)}")
    print(f"The number of columns: {len(df.columns)}")
    print(f"The Shape of DataFrame: {df.shape}")
    df.info()
    print(df.describe())
    print(f"Mssing Values in DataFrame: \n{df.isnull().sum()}" )
    print(f" Data Types of review_creation_date and review_answer_timestamp: \n{df[['review_creation_date','review_answer_timestamp']].dtypes}")

# Duplicate Inspection

def duplicate_inspection(df):
    print(f"Duplicate Values in DataFrame: {df.duplicated().sum()}" )
    print(f"Duplicate Review_id Values in DataFrame: {df.duplicated(subset='review_id').sum()}" )
    print(df[df['review_id'].duplicated(keep=False)])
    print(f"Unique Review_ID : {df['review_id'].nunique()}")
    print(f"Unique Order_Id Values: {df['order_id'].nunique()}")
    print(f"Review Score Disctribution: \n{df['review_score'].value_counts().sort_index()}")
    print("Missing Review Scores:", df['review_score'].isnull().sum())
    out_bound=df[(df['review_score']<1 )| (df['review_score']>5)].copy()
    print(f"Number of Invalid Reviews: {len(out_bound)}")
    if len(out_bound)>0:
        print(out_bound)

# Date Checking and Correction

def time_stamp_checking(df):
    print("Date Columns Missing Values")
    copied_df=df.copy()
    date_columns=['review_creation_date','review_answer_timestamp']
    for col in date_columns:
        copied_df[col]=pd.to_datetime(copied_df[col],errors="coerce")
    Missing_date=copied_df[date_columns].isnull().sum()
    print(Missing_date)
    if Missing_date.sum() >=1:
        print(copied_df[copied_df[date_columns].isnull().any(axis=1)])
    for col in date_columns:
        print(f"Invalid or missing {col}: {copied_df[col].isnull().sum()}")
    invalid_dates=copied_df[copied_df[date_columns].isnull().any(axis=1)].copy()
    print(f"Total affected records: {len(invalid_dates)}")
    print(invalid_dates)
    invalid_chronology=copied_df[copied_df['review_answer_timestamp']<copied_df['review_creation_date']].copy()
    print(f"Number of Invalid Chronological Dates: {len(invalid_chronology)}")
    if len(invalid_chronology)>=1:
        print(invalid_chronology)
    return copied_df

#  Cleaning Reviews Dataset

def clean_reviews_data(df):
    copied_df = df.copy()

    print("Rows Before Cleaning:", len(copied_df))
    copied_df = copied_df.drop_duplicates()
    text_columns = ['review_comment_title','review_comment_message']
    for col in text_columns:
        copied_df[col] = copied_df[col].str.strip()
    date_columns = ['review_creation_date','review_answer_timestamp']
    for col in date_columns:
        copied_df[col] = pd.to_datetime(copied_df[col], errors='coerce')

    print("Rows After Cleaning:", len(copied_df))
    print("Duplicate Review IDs:", copied_df.duplicated(subset='review_id').sum())

    invalid_scores = copied_df[~copied_df['review_score'].between(1, 5)]
    print("Invalid Review Scores:", len(invalid_scores))

    return copied_df

# Saving Cleaned Dataset

def save_cleaned_reviews_data(df):
    output_path = r"Data_sets\Cleaned_Dataset\cleaned_reviews.csv"
    df.to_csv(output_path, index=False)
    print("Cleaned Reviews Dataset Saved Successfully")

def reviews_main():
    review_file_path=r"Data_sets/Olist_Dataset/olist_order_reviews_dataset.csv"
    review_data=load_reviews_data(review_file_path)
    inspect_review_data(review_data)
    duplicate_inspection(review_data)
    time_inspected_data=time_stamp_checking(review_data)
    cleaned_review_data=clean_reviews_data(time_inspected_data)
    save_cleaned_reviews_data(cleaned_review_data)
    return cleaned_review_data


# Reviews Main

if __name__=="__main__":
    cleaned_review_data=reviews_main()