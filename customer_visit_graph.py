import mysql.connector
import datetime
import plotly.graph_objects as go

# Define function to get month from date
def get_month(date):
    return date.month

# Connect to MySQL database
cnx = mysql.connector.connect(
    host="3.35.138.95",
    user="myname",
    password="1234",
    database="mydb",
    port='53686'
)

# Retrieve customer and order history data from the database
cursor = cnx.cursor()
query = """
    SELECT customers.customer_id, customers.visit_count, order_his.order_date 
    FROM customers 
    INNER JOIN order_his 
    ON customers.customer_id = order_his.customer_id 
    WHERE order_his.order_date BETWEEN '2022-01-01' AND '2022-12-31'
"""
cursor.execute(query)
data = cursor.fetchall()

# Close the database connection
cursor.close()
cnx.close()

# Get the customer ID from the user
customer_id = input("Enter customer ID: ")

# Count the number of visits for the customer by month
visits_by_month = {}
for row in data:
    if row[0] == customer_id:
        order_date = row[2]
        month = order_date.month
        visit_count = row[1]
        if month not in visits_by_month:
            visits_by_month[month] = visit_count
        else:
            visits_by_month[month] += visit_count

# Create a bar chart of the results using Plotly
x = []
y = []
for month in range(1, 13):
    x.append(datetime.date(2022, month, 1).strftime('%B'))
    y.append(visits_by_month.get(month, 0))

fig = go.Figure(go.Bar(x=x, y=y))
fig.update_layout(title=f'Customer Visits by Month for {customer_id} in 2022', yaxis_title='Visit Count')
fig.show()
