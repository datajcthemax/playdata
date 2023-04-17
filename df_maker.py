import pandas as pd
from sqlalchemy import create_engine


HOST = '3.35.138.95'
USER = 'myname'
PW = '1234'
DATABASE = 'mydb'
PORT = '52505'

# 기존에 sql-connect말고 sqlalchemy로 db연결. 데이터프레임 읽을때 마다 에러 떠서 신경쓰여서 사용해봄
engine = create_engine(f'mysql+pymysql://{USER}:{PW}@{HOST}:{PORT}/{DATABASE}')

# order_his 테이블을 데이터프레임으로 전환
df = pd.read_sql_table('Amazon_Fashion', engine)

# market_list ['id', 'category_id', 'product_name', 'product_price', 'product_details', 'product_count']

# change the name of the 'Row ID' column to 'id'

df = df.rename(columns={'sub_category': 'category_id'})
df = df.rename(columns={'name': 'product_name'})
df = df.rename(columns={'actual_price': 'product_price'})
df = df.rename(columns={'main_category': 'product_details'})
df = df.rename(columns={'no_of_ratings': 'product_count'})

# remove the 'Salary' column from the dataframe
df = df.drop(columns=['image'])
df = df.drop(columns=['link'])
df = df.drop(columns=['discount_price'])
df = df.drop(columns=['ratings'])

# send the dataframe to a table in the database
table_name = 'market_list_1'
df.to_sql(name=table_name, con=engine, if_exists='append', index=False)

# commit the changes to the database
engine.dispose()

# print the updated dataframe
print(df)