DATABASE_SCHEMA = """
Database Name: CompanyDB

----------------------------------------------------

Table: employees

Columns:
- employee_id INTEGER PRIMARY KEY
- first_name TEXT
- last_name TEXT
- email TEXT
- phone TEXT
- salary INTEGER
- department_id INTEGER
- hire_date DATE

----------------------------------------------------

Table: departments

Columns:
- department_id INTEGER PRIMARY KEY
- department_name TEXT
- location TEXT

----------------------------------------------------

Table: customers

Columns:
- customer_id INTEGER PRIMARY KEY
- customer_name TEXT
- email TEXT
- city TEXT
- country TEXT

----------------------------------------------------

Table: products

Columns:
- product_id INTEGER PRIMARY KEY
- product_name TEXT
- category TEXT
- purchase_price REAL
- selling_price REAL
- discount_percentage REAL
- stock_quantity INTEGER

----------------------------------------------------

Table: orders

Columns:
- order_id INTEGER PRIMARY KEY
- customer_id INTEGER
- order_date DATE
- total_amount REAL

----------------------------------------------------

Table: order_items

Columns:
- order_item_id INTEGER PRIMARY KEY
- order_id INTEGER
- product_id INTEGER
- quantity INTEGER
- unit_price REAL

----------------------------------------------------

Relationships

employees.department_id -> departments.department_id

orders.customer_id -> customers.customer_id

order_items.order_id -> orders.order_id

order_items.product_id -> products.product_id
"""