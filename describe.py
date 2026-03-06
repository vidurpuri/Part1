# Describe Method 

# It provides us the aggregate/Statistical info with respect to data 

import pandas as pd

data = {
    "Name": ['Ram','Ajay','Sundar','Rajesh','Atul','Rahul','Reshma','Aditi','Mukesh'],
    "Age": [22,45,34,23,52,28,43,45,36],
    "Salary": [18000,28000,38000,48000,58000,68000,78000,88000,8000],
    "Score": [87,89,76,78,96,79,97,86,92]
}

df = pd.DataFrame(data)
print(df)

print('Statistical Represenattion of DataFrame')
print(df.describe())

# Output

# Statistical Represenattion of DataFrame
#              Age        Salary      Score
# count   9.000000      9.000000   9.000000  --- It give count of non-null values
# mean   36.444444  48000.000000  86.666667  --- It gives Average of columns
# std    10.596121  27386.127875   7.713624
# min    22.000000   8000.000000  76.000000  --- It gives min value of column
# 25%    28.000000  28000.000000  79.000000
# 50%    36.000000  48000.000000  87.000000
# 75%    45.000000  68000.000000  92.000000
# max    52.000000  88000.000000  97.000000 --- It gives max value of column 