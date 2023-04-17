import pandas as pd
import sqlalchemy 
from sqlalchemy import create_engine
import plotly.express as px

# db연결
db_host = "3.35.138.95"
db_name = "mydb"
db_user = "myname"
db_password = "1234"
db_port = "53686"

db_url = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

engine = sqlalchemy.create_engine(db_url)

# 유저에게 product_id받기
product_id = input("Enter a product ID: ")

# order_his테이블에서 유저가 입력한 product_id를 조회해서 데이터 받아오기
query = f"SELECT * FROM order_his WHERE product_id = {product_id};"

# order_his테이블 판다스 데이터프레임형식으로 로드하기
order_history = pd.read_sql(query, engine)

# order_date칼럼 datetime형식으로 변환
order_history['order_date'] = pd.to_datetime(order_history['order_date'])

# 시즌을 월별로 정의
seasons = {
    'Winter': [12, 1, 2],
    'Spring': [3, 4, 5],
    'Summer': [6, 7, 8],
    'Fall': [9, 10, 11]
}

# 오더별로 시즌정리(뭐하는 코드인지 사실 잘 모름... 해석가능한사람은 주석달아주세요.)
edges = [0, 3, 6, 9, 12]
order_history['season'] = pd.cut(
    order_history['order_date'].dt.month,
    bins=edges,
    labels=list(seasons.keys()),
    include_lowest=True
)

# 필터된 테이블을 시즌별 주문량으로 엮기
quantity_by_season = order_history.groupby('season')['quantity'].sum()

# 시즌별 총 금액 계산
total_amount_by_season = order_history.groupby('season')['total_amount'].sum()

# x좌표 순서대로 정의하기
season_categories = ['Spring', 'Summer', 'Fall', 'Winter']

# 시즌순서대로 칼럼 나열하기
order_history['season'] = pd.Categorical(order_history['season'], categories=season_categories, ordered=True)

# 시즌별 총주문금액 그래프 만들기
fig = px.bar(
    x=quantity_by_season.index, 
    y=quantity_by_season.values, 
    color=quantity_by_season.index,
    text=[f"Total Amount: ₩{total:,}" for total in total_amount_by_season.values],
    labels={'x': 'Season', 'y': 'Total Quantity'},
    title=f"Total Quantity and Amount by Season for Product ID {product_id}",
)

# 콤마와 원화기호 설정
fig.update_traces(texttemplate='%{text}', textposition='outside')

# y축 포맷 설정
fig.update_yaxes(
    tickprefix='',
    tickformat=',',
)

# 그래프 출력
fig.show()