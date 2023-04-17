import random
from datetime import datetime, timedelta
import mysql.connector
from random import randrange




#아이템 100개 채워넣기
for i in range(223):
  # db 연결
  conn = mysql.connector.connect(
    host="3.35.138.95",
    port="53686",
    user="myname",
    password="1234",
    database="mydb"
  )

  # customers 테이블에서 랜덤 고객 추출
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM customers ORDER BY RAND() LIMIT 1")
  random_customer = cursor.fetchone()
  random_customer_id = random_customer[0]
  print(random_customer)

  # market_list에서 재고가 1개라도 있는 랜덤 제품 추출
  cursor.execute("SELECT * FROM market_list WHERE product_count > 0 ORDER BY RAND() LIMIT 1")
  random_product = cursor.fetchone()
  random_product_id = random_product[0]
  random_product_category_id = random_product[1]
  random_product_price = random_product[3]
  print(random_product)

  # 랜덤 날짜 생성
  start_date = datetime(2022, 1, 1)
  end_date = datetime(2023, 4, 11)
  random_days = random.randrange((end_date - start_date).days)
  random_date = start_date + timedelta(days=random_days)
  print(random_date.strftime('%Y-%m-%d'))

  # 랜덤 주문 수량 생성 (최대값 10)
  random_quantity = randrange(1, 10)
  print(random_quantity)

  # 총주문액
  total_amount = int(random_product_price) * int(random_quantity)
  print(total_amount)

  # order_his table [order_id, customer_id, category_id, product_id, order_date, quantity, total_amount]

  # 주문내역에 삽입할 것들
  sql = "INSERT INTO order_his (customer_id, category_id, product_id, order_date, quantity, total_amount) VALUES (%s, %s, %s, %s, %s, %s)"
  val = (random_customer_id, random_product_category_id, random_product_id, random_date, random_quantity, total_amount)
  cursor.execute(sql, val)

  # market_list에서 해당 제품의 재고(product_count) 차감
  new_product_count = random_product[5] - random_quantity
  if new_product_count < 0:
      print("Out of stock. Generating a new random order.")
      conn.rollback()
  else:
      sql = "UPDATE market_list SET product_count = %s WHERE id = %s"
      val = (new_product_count, random_product_id)
      cursor.execute(sql, val)

      # 고객테이블 visit_count와 total_amount 갱신
      visit_count = random_customer[9] + 1  # increment visit_count by 1
      total_amount_sum = random_customer[10] + total_amount  # add total_amount to the current sum

      sql = "UPDATE customers SET visit_count = %s, total_spend = %s WHERE customer_id = %s"
      val = (visit_count, total_amount_sum, random_customer_id)
      cursor.execute(sql, val)

      conn.commit()

