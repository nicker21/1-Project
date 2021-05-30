from flask import Flask
from db import execute_query
from html_formatters import format_records

app = Flask(__name__)


# def get_unique() -> /unique
@app.route("/unique")
def get_unique():
    query = f"select * from customers group by FirstName"
    records = execute_query(query)
    print(records)
    return format_records(records)


# def get_count() -> /count
@app.route("/count")
def get_count():
    query = f"select * from tracks"
    records = execute_query(query)
    print(records)
    return f'Записи = {len(records)}'


# def get_sales() -> /sales
@app.route("/sales")
def get_sales():
    query = f"select * from invoice_items"
    records = execute_query(query)
    total = 0
    for elem in records:
        total += (elem[3] * elem[4])
    print(total)
    return f'Сумма продаж = {total}'


app.run(debug=True)
