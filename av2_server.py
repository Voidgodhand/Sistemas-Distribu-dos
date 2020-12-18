import mysql.connector
from flask import Flask
import json
from flask_jsonpify import jsonify

app = Flask(__name__)

@app.route("/lista_clientes/<pais>")
def lista_clientes(pais=None):
    conn = mysql.connector.connect (host='argama.c0so6ajbhjaj.us-east-1.rds.amazonaws.com', user='admin', passwd='sanduba1', port='3306', database='chinook')
    cursor = conn.cursor()
    qstr="select * from customers WHERE Country = \'"+pais+"\'"
    print (qstr)
    query = cursor.execute(qstr)
    row_headers=[x[0] for x in cursor.description]
    records = cursor.fetchall()
    print (records)
    result = [dict(zip(tuple (row_headers) ,i)) for i in records]
    print (result)
    jret = jsonify(result)
    print (jret)
    conn.close()
    return jret
    
@app.route("/lista_pedidos/<id>")
def lista_pedidos(id=None):
    conn = mysql.connector.connect (host='argama.c0so6ajbhjaj.us-east-1.rds.amazonaws.com', user='admin', passwd='sanduba1', port='3306', database='chinook')
    cursor = conn.cursor()
    qstr="select InvoiceId from invoices WHERE CustomerId = \'"+id+"\'"
    print (qstr)
    query = cursor.execute(qstr)
    row_headers=[x[0] for x in cursor.description]
    records = cursor.fetchall()
    print (records)
    result = [dict(zip(tuple (row_headers) ,i)) for i in records]
    print (result)
    jret = jsonify(result)
    print (jret)
    conn.close()
    return jret
    
@app.route("/get_valor/<id>")
def get_valor(id=None):
    conn = mysql.connector.connect (host='argama.c0so6ajbhjaj.us-east-1.rds.amazonaws.com', user='admin', passwd='sanduba1', port='3306', database='chinook')
    cursor = conn.cursor()
    qstr="select UnitPrice * Quantity AS Valor from invoice_items WHERE InvoiceId = \'"+id+"\'"
    print (qstr)
    query = cursor.execute(qstr)
    row_headers=[x[0] for x in cursor.description]
    records = cursor.fetchall()
    print (records)
    result = [dict(zip(tuple (row_headers) ,i)) for i in records]
    print (result)
    jret = jsonify(result)
    print (jret)
    conn.close()
    return jret
    
app.run(host='0.0.0.0', port='8080')