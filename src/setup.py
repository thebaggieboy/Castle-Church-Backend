
# using flask_restful 
from flask import Flask, jsonify, request 
from flask_restx import Api, Resource, Namespace

  
# creating the flask app 
app = Flask(__name__) 
# creating an API object 
api = Namespace("SETUP", description="Castle Church Management Software Internal API")

  
@app.route("/")
class Setup(Resource): 
    def get(self): 
  
        return jsonify({'message': 'hello world'}) 
  
    # Corresponds to POST request 
    def post(self): 
          
        data = request.get_json()     # status code 
        return jsonify({'data': data}), 201
  
  