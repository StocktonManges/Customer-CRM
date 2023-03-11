from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM customers')
    customers = cursor.fetchall()
    cursor.execute('SELECT * FROM orders')
    orders = cursor.fetchall()
    conn.close()
    return render_template('./GUI/dashboard.html', customers=customers, orders=orders)

@app.route('/add-customer', methods=['POST'])
def add_customer():
    owner_name = request.form['owner_name']
    company = request.form['company']
    address = request.form['address']
    phone = request.form['phone']
    email = request.form['email']
    instagram_handle = request.form['instagram_handle']
    contact_creator = request.form['contact_creator']
    notes = request.form['notes']
    
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO customers (owner_name, company, address, phone, email, instagram_handle, contact_creator, notes) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (owner_name, company, address, phone, email, instagram_handle, contact_creator, notes))
    conn.commit()
    conn.close()
    return "<script>alert('New customer was saved.');</script>"

@app.route('/add-order', methods=['POST'])
def add_order():
    customer_id = request.form['customer_id']
    order_date = request.form['order_date']
    order_revenue = request.form['order_revenue']
    last_contact_date = request.form['last_contact_date']
    follow_up_date = request.form['follow_up_date']
    key_details = request.form['key_details']
    next_steps = request.form['next_steps']
    order_status = request.form['order_status']
    order_owner = request.form['order_owner']
    
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO orders (customer_id, order_date, order_revenue, last_contact_date, follow_up_date, key_details, next_steps, order_status, order_owner) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (customer_id, order_date, order_revenue, last_contact_date, follow_up_date, key_details, next_steps, order_status, order_owner))
    conn.commit()
    conn.close()
    return "<script>alert('New order was saved.');</script>"

if __name__ == '__main__':
    app.run(debug=True)