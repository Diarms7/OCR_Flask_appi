import json
import pymysql
import pickle
from firebase_admin import credentials, firestore
import firebase_admin
import google.cloud


# initialize Firestore Database
#cred = credentials.Certificate("./etatfinancierkey.json")
#db = firebase_admin.initialize_app(cred)
#db = firestore.client()


#doc_ref = db.collection(u'users').document()


    
#for i in data_dict:
  #print(i)
  
#mydb = pymysql.connect(host= '35.223.240.47',
#    user='root',
#    passwd='1234',
#   db='etatfinancier')
#cursor = mydb.cursor()
with open('Test.json') as json_data:
    data_dict = json.load(json_data)
    
#data_str = json.dumps(data_dict)
#serial_grades = pickle.dumps( data_dict )
print(data_dict)

#doc_ref.set({u'text': data_dict})
#users_ref = db.collection(u'users')
#for i in data_dict():
    #print(i)

#dic = {'office': {'component_office': ['Word2010SP0', 'PowerPoint2010SP0']}}
#sql = "INSERT INTO finance({data_dict})"


#cursor.execute(sql, ("35.223.240.47", json.dumps(data_dict)))
#cursor.commit()
  

    