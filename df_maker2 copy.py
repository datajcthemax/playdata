import pandas as pd
from sqlalchemy import create_engine


HOST = '3.35.138.95'
USER = 'myname'
PW = '1234'
DATABASE = 'mydb'
PORT = '52505'

# 기존에 sql-connect말고 sqlalchemy로 db연결. 데이터프레임 읽을때 마다 에러 떠서 신경쓰여서 사용해봄
engine = create_engine(f'mysql+pymysql://{USER}:{PW}@{HOST}:{PORT}/{DATABASE}')

# 해당 테이블 df로 전환
df = pd.read_sql_table('market_list_1', engine)

# drop rows with null values
df.dropna(inplace=True)

# check the updated dataframe
print(df)

# send the dataframe to a table in the database
table_name = 'market_list_1'
df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)

# commit the changes to the database
engine.dispose()

# print the updated dataframe
print(df)









