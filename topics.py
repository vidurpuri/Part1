'''
Problem starement : 

Before any manipulation we need to have two questions related to any datastet 
1. How many rows and column ? ( we can get same from info() but cannot be used )
2. What are Column names in Dataset ?

Shape - Return tuple with no. of rows and column (4,5)
Column - Return List of All Names of columns

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

print('Number of Rows and COlumns')
print(f'Shape: {df.shape}')

print('All Columns names')
print(f'Column: {df.columns}')

# Output 

# Number of Rows and COlumns
# Shape: (9, 4)
# All Columns names
# Column: Index(['Name', 'Age', 'Salary', 'Score'], dtype='str')