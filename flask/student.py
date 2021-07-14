from flask import Flask , render_template , request
import mysql.connector
from mysql.connector import Error
import  json

app = Flask(__name__)
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='fired',
                                         user='root',
                                         password='')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
	
def addnew_student(fname,lname,location):
	with connection.cursor() as cursor:
		query = "INSERT INTO `student` (`fname`, `lname`, `location`) VALUES (%s, %s, %s)"
		cursor.execute(query, (fname, lname, location))
		
		
def get_all_student():
	with connection.cursor() as cursor:
		sql = "SELECT * FROM `student`"
		cols = ['id', 'fname', 'lname','location']
		cursor.execute(sql)
		result = cursor.fetchall()
	return list(result)

def deleteuserfromdb(id):
	with connection.cursor() as cursor:
		sql = "DELETE FROM `student` WHERE `id`=4"
		cursor.execute(sql,id)
	return "true"
		
	
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
	return  json.dumps(result)

@app.route('/deletestudent',methods = ["POST"])
def deleteuser():
	data = request.get_json()
	result = deleteuserfromdb(data['id'])
	return json.dumps({"message": result})
	

if __name__ == "__main__":
    app.run(host="localhost",port=8080,debug=True)