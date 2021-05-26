# -*- coding: utf-8 -*-
"""
Created on Sun May 23 19:20:45 2021

@author: gupta
"""

import sqlite3
from flask import g
from flask import Flask
from flask import request
from flask import jsonify
import json

db = 'C:/Users/gupta/Desktop/Purdue/Subjects/Production/database.db'

print ("Opened database successfully")

conn = sqlite3.connect('database.db')

conn.execute('CREATE TABLE models (name TEXT, tokenizer TEXT, model TEXT)')
print ("Table created successfully")
conn.close()

# Create my flask app
app = Flask(__name__)

@app.route('/models', methods=['GET','POST'])
def models():
    if request.method == 'POST':
            add = json.loads(request.data)
            print(add)
            name = add ['name']
            tokenizer = add['tokenizer']
            model = add['model']
            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO models (name,tokenizer,model) VALUES (?,?,?)",(name,tokenizer,model))
                con.commit()
                msg = "Record successfully added"
                print(msg)
                return (add)
    if request.method == 'GET':
            modelname = request.args.get('name')
            model = request.args.get('model')
            tokenizer = request.args.get('tokenizer')
            if model and tokenizer:
                new_model = User(
                    modelname=name,
                    model=model,
                    tokenizer = tokenizer,
                    created=dt.now(),
                    admin=False
                    )
                db.session.add(new_model)  # Adds new User record to database
                db.session.commit()  # Commits all changes
                return (f"{new_model} successfully created!")




#@app.route("/addmodels", methods=['POST'])
#def models():
 #   if request.method == 'POST':
 #           data = request.data
 #           print(data)
 #           #name = request.data['name']
            #tokenizer = request.data['tokenizer']
            #model = request.data['model']
            
  #          with sql.connect("database.db") as con:
   #             cur = con.cursor()
    #            cur.execute("INSERT INTO addmodels (name,tokenizer,model) VALUES (?,?,?)",(name,tokenizer,model))
     #       
      #          con.commit()
       ##return data
      
         
#@app.route('/list')
#def list():
 #  con = sql.connect("database.db")
  # con.row_factory = sql.Row
   
   #cur = con.cursor()
  # cur.execute("select * from models")
   
   #rows = cur.fetchall();
   #return render_template("list.html",rows = rows)
      
# Run if running "python answer.py"
if __name__ == '__main__':

    # Run our Flask app and start listening for requests!
    app.run(host='0.0.0.0', port=8000, threaded=True)
