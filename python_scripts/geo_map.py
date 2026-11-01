import pandas as pd 

# Loading Geolocation Dataset

def load_path(file_path):
    
    df=pd.read_csv(file_path)
    print("Dataset Loaded Successfully")
    return df

# Data Frame Inspection
def inspect_data(df):
    print(df.head(10))
    print(df.shape)
    print(f" The Number of Rows are {len(df)}")
    print(f" The Number of Columns are {len(df.columns)}")

    print(f" The datatype of Columns are")
    df.info()
    print(f"The Total Number of Missing Values is \n{df.isnull().sum()} ")

# Dupicate Rows and Data Inspection

def inspect_duplicates(df):
    df_identical=df.duplicated().sum()
    if df_identical>=1:
        print(f" The Identical row count is {(df_identical)}")
        print(df[df.duplicated()])
    else:
        print(" There are No duplicates")
    print(f" The Total Number of Postal Code prefix count is: {df.duplicated("geolocation_zip_code_prefix").sum()}" )
    print(df[df.duplicated("geolocation_zip_code_prefix")])
    print(f" The Total Repeated Count of Geographical Coordinates: {df.duplicated(subset=["geolocation_lng","geolocation_lat"]).sum()}")
    print(df[df.duplicated(subset=["geolocation_lng","geolocation_lat"])])

# Inspect postal-prefix frequencies

def inspect_postal_prefixes(df):

    prefix_count=df["geolocation_zip_code_prefix"].value_counts()

    print(f"The Unique Citys count is: {df['geolocation_city'].nunique()} ")
    print("The frequency of each values :")
    print(prefix_count)
    print(f""" The post code with Highest number of rows is {prefix_count.idxmax()} 
    and the number of rows are { prefix_count.max()} """)

    prefix_more_than_once=prefix_count[prefix_count>1]
    print(f"The Number Post code prefix's which appears more than once are {prefix_more_than_once.count()}")
    print("The Post code prefix's which appears more than once :")
    print(prefix_more_than_once)
    prefix_once=prefix_count[prefix_count==1]
    print(f"The Nmber of  Post code prefix's Appearances: \n{prefix_once.count()}")
    print("The Post code prefix's which appear once are :")
    print(prefix_once)

# Valid Location Values Inspection

def inspect_coordinates(df):

    print(f"Longitude — Min: {df['geolocation_lng'].min()} Max: {df['geolocation_lng'].max()} ")
    print(f"Latitude  — Min: {df['geolocation_lat'].min()} Max: {df['geolocation_lat'].max()} ")

    lat_out=0
    for i in df['geolocation_lat']:
        if i < -34 or i>6:
            lat_out+=1
    lng_out=0

    for i in df['geolocation_lng']:
        if i <-74 or i>-34:
            lng_out+=1

    invalid_coordinates=((df['geolocation_lat']<-34)|(df['geolocation_lat']>6)| (df['geolocation_lng']<-74)| (df['geolocation_lng']>-34))
    invalid_rows=df[invalid_coordinates]
    print(f"There are  {len(invalid_rows)} invalid Coordinates Rows and They are: ")
    print((invalid_rows))

    percentage_of_coordinates_outbound=(len(invalid_rows)/len(df))*100
    print(f"The Percenatge of Invalid Coordinate Outbound is {percentage_of_coordinates_outbound:.4f}%")

    print(f"The Number of postal prefixes, cities, and states appear in those rows are: \n{invalid_rows.nunique()}")
    print(f" Unique postal prefixes: \n{invalid_rows['geolocation_zip_code_prefix'].unique()}")
    print(f" Unique Cities: \n{invalid_rows['geolocation_city'].unique()}")
    print(f" Unique States: \n{invalid_rows['geolocation_state'].unique()}")

    unusual_coordinates=(invalid_rows.groupby(['geolocation_lat','geolocation_lng']).size().sort_values(ascending=False))
    print(f"Number Rows that shares Unusual Coordinates: {len(unusual_coordinates)}")
    print(unusual_coordinates.nsmallest(5))
    print(unusual_coordinates.nlargest(5))
    return invalid_rows
# Creating a Copy of Dataset and Dropping Duplicate

def clean_geolocation_data(df):

    cleaned_df=df.copy()
    cleaned_df.info()
    original_rows=len(cleaned_df)
    cleaned_df=cleaned_df.drop_duplicates()

    print(f"Original Data Frame: /n {df.shape}")
    print(f"Copied Data Frame: /n {cleaned_df.shape}")
    print(f"Diplicates in Copied Data Frame: {cleaned_df.duplicated().sum()}")

    # Standardize Text Column

    cleaned_df['geolocation_city']=(cleaned_df['geolocation_city'].str.strip().str.lower())
    cleaned_df['geolocation_state']=(cleaned_df['geolocation_state'].str.strip().str.upper())
    print("Original row count:", original_rows)
    print("Rows after duplicate removal:", len(cleaned_df))
    print("Duplicate rows removed:", original_rows - len(cleaned_df))

    return cleaned_df

# Validate the Cleaned Dataset

def validate_cleaned_data(cleaned_df):
    print("Cleaned dataset shape:", cleaned_df.shape)
    print("Remaining exact duplicates:", cleaned_df.duplicated().sum())

    print("\nMissing values:")
    print(cleaned_df.isnull().sum())
    invalid_coordinates = ((cleaned_df["geolocation_lat"] < -34) | (cleaned_df["geolocation_lat"] > 6) | (cleaned_df["geolocation_lng"] < -74) | (cleaned_df["geolocation_lng"] > -28))
    Candidate_outliers=cleaned_df[invalid_coordinates]
    print(f"Candidate coordinate Outliers after Cleaning: {len(Candidate_outliers)}  ")
    return Candidate_outliers

# Storing the Data

def save_cleaned_items(df):
    output_path = r"Data_sets\cleaned_geolocation_data.csv"
    df.to_csv(output_path, index=False)
    print("Cleaned order items dataset saved.")
    print("Rows saved:", len(df))
    print("Columns saved:", len(df.columns))

def main():
    file_path = r"Data_sets/Olist_Dataset/olist_geolocation_dataset.csv"
    geolocation_df=load_path(file_path)
    inspect_data(geolocation_df)
    inspect_duplicates(geolocation_df)
    inspect_postal_prefixes(geolocation_df)
    original_outliers = inspect_coordinates(geolocation_df)
    cleaned_df = clean_geolocation_data(geolocation_df)
    cleaned_outliers = validate_cleaned_data(cleaned_df)
    save_cleaned_items(cleaned_df)

    return geolocation_df,cleaned_df,original_outliers,cleaned_outliers

if __name__=="__main__":
    (geolocation_df,cleaned_df,original_outliers,cleaned_outliers)=main()