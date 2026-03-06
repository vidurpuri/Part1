#Info() Usuage 

#Problem statement 
# 1. How many Rows and Columns
# 2. How many entries 
# 3. data Type ?
# 4. Any Null entries ?

import pandas as pd

df = pd.read_json('sample_Data.json')

print('Dispalying info about Sample Data Json file')
print(df.info())

# Output 

# Dispalying info about Sample Data Json file
# <class 'pandas.DataFrame'>
# RangeIndex: 20 entries, 0 to 19
# Data columns (total 6 columns):
#  #   Column       Non-Null Count  Dtype
# ---  ------       --------------  -----
#  0   id           20 non-null     int64
#  1   name         20 non-null     str
#  2   description  20 non-null     str
#  3   price        20 non-null     float64
#  4   category     20 non-null     str
#  5   image        20 non-null     str
# dtypes: float64(1), int64(1), str(4)
# memory usage: 1.1 KB