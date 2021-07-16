from flask import Flask , render_template , request
import  json
from model import addnew_student, get_all_student , deleteuserfromdb , updatestudent

app = Flask(__name__)
	
@app.route('/add_student',methods = ['POST'])
def add_new_student():
	data = request.get_json()
	try :
		addnew_student(data["fname"],data["lname"],data["location"])
		return json.dumps({"message":"user is added "})
	except Exception as e :
		return json.dumps({"message": e})

@app.route('/getallstudent',methods = ["get"])
def getallstudnet():
	result = get_all_student()
	return json.dumps(result)

@app.route('/deletestudent',methods = ["POST"])
def deleteuser():
	data = request.get_json()
	result = deleteuserfromdb(data['id'])
	return json.dumps({"message": result})

@app.route('/updatestudentdata',methods = ["PUT"])
def updatestudentdata():
	data = request.get_json()
	result = updatestudent(data['id'] ,data['fname'])
	return json.dumps({"message" : result})
	

if __name__ == "__main__":
    app.run(host="localhost",port=8080,debug=True)