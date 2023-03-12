import sqlite3
import tkinter as tk

# Create a connection to the SQLite3 database
conn = sqlite3.connect('mydatabase.db')

# Create a cursor object
cursor = conn.cursor()

# Retrieve all customers and orders from the database
cursor.execute('SELECT * FROM customers')
customers = cursor.fetchall()
cursor.execute('SELECT * FROM orders')
orders = cursor.fetchall()

# Create a tkinter window
root = tk.Tk()
root.title('CRM Dashboard')

# Create a frame for customers
customer_frame = tk.Frame(root, padx=10, pady=10)
customer_frame.pack(side=tk.LEFT)

# Create a label for customers
customer_label = tk.Label(customer_frame, text='Customers', font=('Arial', 16, 'bold'))
customer_label.pack()

# Create a table for customers
customer_table = tk.Frame(customer_frame)
customer_table.pack()
tk.Label(customer_table, text='ID').grid(row=0, column=0)
tk.Label(customer_table, text='Owner Name').grid(row=0, column=1)
tk.Label(customer_table, text='Company').grid(row=0, column=2)
tk.Label(customer_table, text='Address').grid(row=0, column=3)
tk.Label(customer_table, text='Phone').grid(row=0, column=4)
tk.Label(customer_table, text='Email').grid(row=0, column=5)
tk.Label(customer_table, text='Instagram Handle').grid(row=0, column=6)
tk.Label(customer_table, text='Contact Creator').grid(row=0, column=7)
tk.Label(customer_table, text='Notes').grid(row=0, column=8)

# Insert customer data into the table
for i, customer in enumerate(customers):
    for j, value in enumerate(customer):
        tk.Label(customer_table, text=value).grid(row=i+1, column=j)

# Create a frame for orders
order_frame = tk.Frame(root, padx=10, pady=10)
order_frame.pack(side=tk.RIGHT)

# Create a label for orders
order_label = tk.Label(order_frame, text='Orders', font=('Arial', 16, 'bold'))
order_label.pack()

# Create a table for orders
order_table = tk.Frame(order_frame)
order_table.pack()
tk.Label(order_table, text='ID').grid(row=0, column=0)
tk.Label(order_table, text='Customer ID').grid(row=0, column=1)
tk.Label(order_table, text='Order Date').grid(row=0, column=2)
tk.Label(order_table, text='Order Revenue').grid(row=0, column=3)
tk.Label(order_table, text='Last Contact Date').grid(row=0, column=4)
tk.Label(order_table, text='Follow-up Date').grid(row=0, column=5)
tk.Label(order_table, text='Key Details').grid(row=0, column=6)
tk.Label(order_table, text='Next Steps').grid(row=0, column=7)
tk.Label(order_table, text='Order Status').grid(row=0, column=8)
tk.Label(order_table, text='Order Owner').grid(row=0, column=9)

# Insert order data into the table
for i, order in enumerate(orders):
    for j, value in enumerate(order):
        tk.Label(order_table, text=value).grid(row=i+1, column=j)

# Run the tkinter event loop
root.mainloop()
