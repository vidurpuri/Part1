import pandas as pd

    # Our main focus is to preview and check if data is loaded fine in Dataframe 

#read json file 
df = pd.read_json("sample_Data.json")

# if no integer given to head() or tail() , be default it will display first 5 and last rows 

print('Uisng Head to First display 10 rows')
print(df.head(10)) 

print('Uisng Tail to Last display 10 rows')
print(df.tail(10))