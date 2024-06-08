import os
import sys
import psycopg2
from flask import Flask, jsonify, request, Request
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from flask_cors import CORS
import urllib



project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)
("Project Root: ", project_root)
from src.setup import api as setup_api
from src.operations import api as operations_api

app = Flask(__name__)

api = Api(
    version="1.0",
    title="Church Management Softwarre",
    description="An API for managing users of a particular church",
    license="MIT",
    contact="Baggieboy.",
)
# api.add_namespace(setup_api, "/setup")
# api.add_namespace(operations_api, "/operations")
#api.init_app(app)


params = urllib.parse.quote_plus('DRIVER={SQL Server};SERVER=ALTCLAN\SQLEXPRESS;DATABASE=Church;Trusted_Connection=yes;')
app.config["SQLALCHEMY_DATABASE_URI"] = "mssql+pyodbc:///?odbc_connect=%s" % params
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
CORS(app)  # 

@app.route('/setup/rank')
def get_setup_rank():
    try:
       
        print('\n\n----------- Connection successful !')
        rank_query = text('SELECT * from rank_tab')
        
        with db.engine.begin() as conn:
            result = conn.execute(rank_query).fetchall()
            
            for record in result:
                print(record)
            data = [
                {"rank_name": record[0], "rank_type": record[1], "rank_level": record[2], "id": record[3] }
                for record in result
            ]
            
            print(jsonify(data))
            print(data)
        return jsonify(data)
                   
  
    except Exception as e:
        print('\n\n----------- Connection failed ! ERROR : ', e)
  
@app.route('/setup/group')
def get_setup_group():
    try:
       
        print('\n\n----------- Connection successful !')
        group_query = text('SELECT * from group_tab')
        
        with db.engine.begin() as conn:
            result = conn.execute(group_query).fetchall()
            
            for record in result:
                print(record)
            data = [
                {"group_name": record[0], "group_level": record[1], "id": record[2] }
                for record in result
            ]
            
            print(jsonify(data))
            print(data)
        return jsonify(data)
                   
  
    except Exception as e:
        print('\n\n----------- Connection failed ! ERROR : ', e)
  

@app.route('/setup/marital_status')
def get_setup_marital_status():
    try:
       
        print('\n\n----------- Connection successful !')
        marital_status_query = text('SELECT * from marital_status_tab')
        
        with db.engine.begin() as conn:
            result = conn.execute(marital_status_query).fetchall()
            
            for record in result:
                print(record)
            data = [
                {"marital_status": record[0], "id": record[1] }
                for record in result
            ]
            
            print(jsonify(data))
            print(data)
        return jsonify(data)
                   
  
    except Exception as e:
        print('\n\n----------- Connection failed ! ERROR : ', e)
  
@app.route('/setup/occupation')
def get_setup_occupation():
    try:
       
        print('\n\n----------- Connection successful !')
        occupation_query = text('SELECT * from occupation_tab')
        
        with db.engine.begin() as conn:
            result = conn.execute(occupation_query).fetchall()
            
            for record in result:
                print(record)
            data = [
                {"occupation_type": record[0], "occupation_level": record[1], "id": record[2] }
                for record in result
            ]
            
            print(jsonify(data))
            print(data)
        return jsonify(data)
                   
  
    except Exception as e:
        print('\n\n----------- Connection failed ! ERROR : ', e)
  


@app.route('/setup/service_church')
def get_setup_service_church():
    try:
       
        print('\n\n----------- Connection successful !')
        service_church_query = text('SELECT * from church_tab')
        
        with db.engine.begin() as conn:
            result = conn.execute(service_church_query).fetchall()
            
            for record in result:
                print(record)
            data = [
                {"church_name": record[0], "church_level": record[1], "id": record[2] }
                for record in result
            ]
            
            print(jsonify(data))
            print(data)
        return jsonify(data)
                   
  
    except Exception as e:
        print('\n\n----------- Connection failed ! ERROR : ', e)
  

@app.route('/financials/setup/fund_channel')
def get_setup_fund_channel():
    try:
       
        print('\n\n----------- Connection successful !')
        service_fund_channel_query = text('SELECT * from fund_channel_tab')
        
        with db.engine.begin() as conn:
            result = conn.execute(service_fund_channel_query).fetchall()
            
            for record in result:
                print(record)
            data = [
                {"fund_channel_name": record[0], "id": record[1] }
                for record in result
            ]
            
            print(jsonify(data))
            print(data)
        return jsonify(data)
                   
  
    except Exception as e:
        print('\n\n----------- Connection failed ! ERROR : ', e)
  



@app.route('/financials/setup/loan_account')
def get_setup_loan_account():
    try:
       
        print('\n\n----------- Connection successful !')
        loan_account_query = text('SELECT * from loan_account_tab')
        
        with db.engine.begin() as conn:
            result = conn.execute(loan_account_query).fetchall()
            
            for record in result:
                print(record)
            data = [
                {"borrower": record[0], "id": record[1] }
                for record in result
            ]
            
            print(jsonify(data))
            print(data)
        return jsonify(data)
                   
  
    except Exception as e:
        print('\n\n----------- Connection failed ! ERROR : ', e)
  
@app.route('/financials/setup/account_type')
def get_setup_account_type():
    try:
       
        print('\n\n----------- Connection successful !')
        account_type_query = text('SELECT * from account_type_tab')
        
        with db.engine.begin() as conn:
            result = conn.execute(account_type_query).fetchall()
            
            for record in result:
                print(record)
            data = [
                {"acc_type_name": record[0], "id": record[1] }
                for record in result
            ]
            
            print(jsonify(data))
            print(data)
        return jsonify(data)
                   
  
    except Exception as e:
        print('\n\n----------- Connection failed ! ERROR : ', e)
  

@app.route('/financials/setup/income')
def get_setup_income():
    try:
       
        print('\n\n----------- Connection successful !')
        income_query = text('SELECT * from income_tab')
        
        with db.engine.begin() as conn:
            result = conn.execute(income_query).fetchall()
            
            for record in result:
                print(record)
            data = [
                {"collection_id": record[0], "collection_date": record[1] }
                for record in result
            ]
            
            print(jsonify(data))
            print(data)
        return jsonify(data)
                   
  
    except Exception as e:
        print('\n\n----------- Connection failed ! ERROR : ', e)
  

@app.route('/financials/setup/expenditure')
def get_setup_expenditure():
    try:
       
        print('\n\n----------- Connection successful !')
        expenditure_query = text('SELECT * from expense_tab')
        
        with db.engine.begin() as conn:
            result = conn.execute(expenditure_query).fetchall()
            
            for record in result:
                print(record)
            data = [
                {"expense_name": record[0], "funds_type": record[1] }
                for record in result
            ]
            
            print(jsonify(data))
            print(data)
        return jsonify(data)
                   
  
    except Exception as e:
        print('\n\n----------- Connection failed ! ERROR : ', e)
  




@app.route('/setup/service')
def get_setup_service():
    try:
       
        print('\n\n----------- Connection successful !')
        service_query = text('SELECT * from service_tab')
        
        with db.engine.begin() as conn:
            result = conn.execute(service_query).fetchall()
            
            for record in result:
                print(record)
            data = [
                {"id": record[0], "service_level": record[1], "service_name": record[2] }
                for record in result
            ]
            
            print(jsonify(data))
            print(data)
        return jsonify(data)
                   
  
    except Exception as e:
        print('\n\n----------- Connection failed ! ERROR : ', e)
  

@app.route('/user/roles')
def get_user_role():
    try:
       
        print('\n\n----------- Connection successful !')
        role_query = text('SELECT * from user_role_tab')
        
        with db.engine.begin() as conn:
            result = conn.execute(role_query).fetchall()
            
            for record in result:
                print(record)
            data = [
                {"username": record[0], "adminread": record[1], "adminedit": record[2], "admindelete": record[3] }
                for record in result
            ]
            
            print(jsonify(data))
            print(data)
        return jsonify(data)
                   
  
    except Exception as e:
        print('\n\n----------- Connection failed ! ERROR : ', e)
  

@app.route('/operations/membership/personal')
def get_operations_personal():
    try:
       
        print('\n\n----------- Connection successful !')
        personal_query = text('SELECT * from personal_tab')
        
        with db.engine.begin() as conn:
            result = conn.execute(personal_query).fetchall()
            
            for record in result:
                print(record)
            data = [
                { 'id': record[0], "membership_no": record[1], "surname": record[2], "other_names": record[3], "current_rank": record[4], "marital_status": record[5], "sex": record[6],}
                for record in result
            ]
            
            print(jsonify(data))
            print(data)
        return jsonify(data)
                   
  
    except Exception as e:
        print('\n\n----------- Connection failed ! ERROR : ', e)
  
@app.route('/operations/membership/birth')
def get_operations_births():
    try:
       
        print('\n\n----------- Connection successful !')
        births_query = text('SELECT * from births_tab')
        
        with db.engine.begin() as conn:
            result = conn.execute(births_query).fetchall()
            
            for record in result:
                print(record)
            data = [
                { 'given_names': record[0], "sex": record[1], "prophet": record[2], "mother_name": record[3], "dob": record[4], "christening_date": record[5], "membership_no": record[6],}
                for record in result
            ]
            
            print(jsonify(data))
            print(data)
        return jsonify(data)
                   
  
    except Exception as e:
        print('\n\n----------- Connection failed ! ERROR : ', e)
  


@app.route('/users')
def get_users():
    

    try:
       
        print('\n\n----------- Connection successful !')
        user_query = text('SELECT * from user_tab')
        role_query = text('SELECT * from user_role_tab')
        
        with db.engine.begin() as conn:
            result = conn.execute(user_query).fetchall()
            
            for record in result:
                print(record)
            data = [
                {"username": record[0], "membership_no": record[1], "non_member_name": record[2], "password": record[3], "date_created": record[4] }
                for record in result
            ]
            
            print(jsonify(data))
            print(data)
        return jsonify(data)
                   
  
    except Exception as e:
        print('\n\n----------- Connection failed ! ERROR : ', e)
  




@app.route('/events/setup/committee')
def get_setup_committee():
    try:
       
        print('\n\n----------- Connection successful !')
        committee_query = text('SELECT * from committee_name_tab')
        
        with db.engine.begin() as conn:
            result = conn.execute(committee_query).fetchall()
            
            for record in result:
                print(record)
            data = [
                {"event_id": record[0], "committee_id": record[1], "committee_name": record[2] }
                for record in result
            ]
            
            print(jsonify(data))
            print(data)
        return jsonify(data)
                   
  
    except Exception as e:
        print('\n\n----------- Connection failed ! ERROR : ', e)
  
@app.route('/events/setup/event_name')
def get_setup_event_name():
    try:
       
        print('\n\n----------- Connection successful !')
        event_query = text('SELECT * from events_name_tab')
        
        with db.engine.begin() as conn:
            result = conn.execute(event_query).fetchall()
            
            for record in result:
                print(record)
            data = [
                {"id": record[0],"event_name": record[1] }
                for record in result
            ]
            
            print(jsonify(data))
            print(data)
        return jsonify(data)
                   
  
    except Exception as e:
        print('\n\n----------- Connection failed ! ERROR : ', e)
  
"""@app.route('/events/setup/formation')
def get_setup_formation():
    try:
       
        print('\n\n----------- Connection successful !')
        formation_query = text('SELECT * from formation_name_tab')
        
        with db.engine.begin() as conn:
            result = conn.execute(formation_query).fetchall()
            
            for record in result:
                print(record)
            data = [
                {"id": record[0],"formation_name": record[1] }
                for record in result
            ]
            
            print(jsonify(data))
            print(data)
        return jsonify(data)
                   
  
    except Exception as e:
        print('\n\n----------- Connection failed ! ERROR : ', e)
  

"""
     
with app.app_context():
    try:
       
        print('\n\n----------- Connection successful !')
        db.create_all()
        user_query = text('SELECT * from user_tab')
        role_query = text('SELECT * from user_role_tab')
        
        with db.engine.begin() as conn:
            result = conn.execute(user_query).fetchall()
            
            for record in result:
                print(record)
            data = [
                {"username": record[0], "membership_no": record[1], "non_member_name": record[2], "password": record[3], "date_created": record[4] }
                for record in result
            ]
            
          
                   
  
    except Exception as e:
        print('\n\n----------- Connection failed ! ERROR : ', e)
  


if __name__ == "__main__":
    app.run(debug=True)
