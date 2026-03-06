import pandas as pd

# craete data with row, column values 
data = {
    "Name": ['Ram','Ajay','Sundar'],
    "Age": [20,22,23],
    "City": ['Mumbai','Delhi','Banglore']
}

# create dataframe with above data 
df = pd.DataFrame(data)
print(df)

#save the dataframe in excel xlsx format
# df.to_excel("output.xlsx", index=False)

#save dataframe in csv
df.to_csv("output.csv", index=False)

#save data in json 
# df.to_json("output.json", index=False)