from flask import Flask
from flask_restful import Resource, Api
from flask import jsonify
import datetime
import json
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="api"
)

app = Flask(__name__)
api = Api(app)

@app.route('/', methods=['GET'])
def getUsers():
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM users")

    row_headers=[x[0] for x in mycursor.description]
   
    myresult = mycursor.fetchall()
    
    json_data=[]

    for result in myresult:
        json_data.append(dict(zip(row_headers,result)))

    data = json.dumps(json_data, indent=4, sort_keys=True, default=str)

    return  data

app.run()

