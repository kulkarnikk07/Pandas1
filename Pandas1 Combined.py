# Pandas1

# 1 Problem 1 : Make a Pandas DataFrame with two-dimensional list	(	https://www.geeksforgeeks.org/make-a-pandas-dataframe-with-two-dimensional-list-python/)

import pandas as pd  
    
lst = [['Geek', 25], ['is', 30], 
       ['for', 26], ['Geeksforgeeks', 22]] 
df = pd.DataFrame(lst, columns =['Tag', 'number']) 
print(df )

# 2 Problem 2 :Big Countries	(	https://leetcode.com/problems/big-countries/ )

import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    df = world[(world['area']>= 3000000) | (world['population'] >= 25000000)]
    return df[['name','population','area']]

# 3 Problem 3 :Recyclable and Low Fat Products	(	https://leetcode.com/problems/recyclable-and-low-fat-products/ )

import pandas as pd

# using the boolean comparison with & operator
def find_products(products: pd.DataFrame) -> pd.DataFrame:
    df =products[(products['low_fats']=='Y') & (products['recyclable']== 'Y')]
    return df[['product_id']]

# 4 Problem 4 :Customer Who Never Order	(	https://leetcode.com/problems/customers-who-never-order/  )

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    
    df = customers.merge(orders, left_on = 'id', right_on = 'customerId' , how = 'left')
    df = df[df['customerId'].isna()]
    return df[['name']].rename(columns={'name':'Customers'})