
import os
import psycopg2
import json
#
# 
# using flask_restful 
from flask import Flask, jsonify, request 
from flask_restx import Api, Resource, Namespace

  
# creating the flask app 
app = Flask(__name__) 
# creating an API object 
api = Namespace("OPERATIONS", description="Castle Church Management Software Internal API Operations route")

  
# making a class for a particular resource A
# the get, post methods correspond to get and post requests 
# they are automatically mapped by flask_restful. 
# other methods include put, delete, etc. 
@app.route("/")
class Operations(Resource): 
    def get(self): 
  
        return jsonify({'message': 'hello world'}) 
  
    # Corresponds to POST request 
    def post(self): 
          
        data = request.get_json()     # status code 
        return jsonify({'data': data}), 201
  
  