import requests
import pandas as pd
import sqlite3
#Fetch details from Fakestore
prod_res= requests.get('https://fakestoreapi.com/products')
df_products= pd.DataFrame(prod_res.json())
print(df_products.head())
#
#
#unnest 'rating' column
ratings = pd.json_normalize(df_products['rating'])
print(ratings.head())
df_products['rating_score']= ratings['rate']
df_products['rating_count']= ratings['count']
df_products = df_products.drop(columns=['rating'])

#2 Fetch orders/carts Data
cart_res= requests.get('https://fakestoreapi.com/carts')
df_carts= pd.DataFrame(cart_res.json())

#Fact Table Creation
order_list=[]
for order in cart_res.json():
    for items in order['products']:
        order_list.append({
            'order_id':order['id'],
            'user_id':order['userId'],
            'order_date':order['date'],
            'product_id':items['productId'],
            'quantity':items['quantity'],
        })
df_orders= pd.DataFrame(order_list)
#3 Local Sqlite Database connection and Save
conn= sqlite3.connect('ecommercepipeline.db')
df_products.to_sql('dim_products', conn, index=False, if_exists= 'replace')
df_orders.to_sql('fact_orders', conn, index=False, if_exists= 'replace')

print("SUCCESS: DATABASE 'e-commerce_pipeline.db' created with 'dim_products' and 'fact_orders' tables ")
