'''
1. Select specific Column
2. Filter Rows on certain condition
3. Combine multiple conditions
'''
import pandas as pd

data = {
    "Name": ['Ram','Ajay','Sundar','Rajesh','Atul','Rahul','Reshma','Aditi','Mukesh'],
    "Age": [22,45,34,23,52,28,43,45,36],
    "Salary": [18000,28000,38000,48000,58000,68000,78000,88000,8000],
    "Score": [87,89,76,78,96,79,97,86,92]
}

df = pd.DataFrame(data)
print(df)

#Select Single Column 
column = df["Name"]
print(column)

#Select Multiple Column 
multi_column = df[['Name','Age']]
print(multi_column)

#Single Condition Filter Rows salary > 50k
filterSingle = df[df['Salary'] > 50000]
print(filterSingle)


#Filtering rows salary ? 50k and Age > 30
multiple_filter = df[(df['Salary'] > 50000) & (df['Age'] > 30)]
print(multiple_filter)

#Filtering Using OR multiple rows
filter_or = df[(df['Age'] > 30) | (df['Score'] > 90)]
print(filter_or)