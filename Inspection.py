import pandas as pd 
df=pd.read_csv(r"Data_sets/Olist_Dataset/olist_geolocation_dataset.csv")

# Data Frame Inspection

print(df.head(10))
print(df.shape)
print(f" The Number of Rows are {len(df)}")
print(f" The Number of Columns are {len(df.columns)}")

print(f" The datatype of Columns are")
df.info()
print(f"The Total Number of Missing Values is \n{df.isnull().sum()} ")

# Dupicate Rows and Data Inspection

df_identical=df.duplicated().sum()
if df_identical>=1:
    print(f" The Identical row count is {df_identical}")
    print(df[df.duplicated()])
else:
    print(" There are No duplicates")
print(f" The Total Number of Postal Code prefix count is: {df.duplicated("geolocation_zip_code_prefix").sum()}" )
print(df[df.duplicated("geolocation_zip_code_prefix")])
print(f" The Total Repeated Count of Geographical Coordinates: {df.duplicated(subset=["geolocation_lng","geolocation_lat"]).sum()}")
print(df[df.duplicated(subset=["geolocation_lng","geolocation_lat"])])


prefix_count=df["geolocation_zip_code_prefix"].value_counts()

print(f"The Unique Citys count is: {df["geolocation_city"].nunique()} ")
print("The frequency of each values :")
print(prefix_count)
print(f""" The post code with Highest number of rows is {prefix_count.idxmax()} 
 and the number of rows are { prefix_count.max()} """)

prefix_more_than_once=prefix_count[prefix_count>1]
print("The Post code prefix's witch appears more than once :")
print(prefix_more_than_once)