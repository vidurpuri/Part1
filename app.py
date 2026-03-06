import pandas as pd

#read csv file from pandas and store in dataframe
#df = pd.read_csv("sales_data_sample.csv", encoding="latin1")

#read excel file from pandas and store in dataframe
# We installed xlrd for reading .xls files 
# we installed openpyxl to read .xlsx files
#df = pd.read_excel("SampleSuperstore.xlsx",engine="xlrd")

#read json file from pandas and store in dataframe
df = pd.read_json("sample_Data.json")

print(df)