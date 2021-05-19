import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate("D:\Iot-Domain-Analyst\iot-domain-analyst-156c3-firebase-adminsdk-7nqm7-c221471c89.json")
firebase_admin.initialize_app(cred, {
	'databaseURL':'https://iot-domain-analyst-156c3-default-rtdb.asia-southeast1.firebasedatabase.app/'
	})
ref = db.reference("/")
x = ref.get()
location = x['regid']['location']
print(location)

