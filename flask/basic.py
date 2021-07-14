from flask import Flask , render_template , request
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='student_db',
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

import  json
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("home.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/aboutus')
def about():
    return json.dumps(dict( uid = 1 , name = "janak" , roll = "admin" , location = "mumbai" ))

@app.route("/process_user_data",methods=['POST',"GET"])
def process_user_data():
    fname = request.args.get("fname")
    lname = request.args.get("lname")
    return json.dumps(dict(Full_Name = "{} {}".format(fname ,lname)))



#web application book car from one place to other place
#frontend
#html , angular , bootstrap , react


#json #xml

#endapoint
#login
# user detalis



#Backend
#java python php nodejs



# Sr.No.	Methods & Description
# 1
# GET
#
# Sends data in unencrypted form to the server. Most common method.
#
# 2
# HEAD
#
# Same as GET, but without response body
#
# 3
# POST
#
# Used to send HTML form data to server. Data received by POST method is not cached by server.
#
# 4
# PUT
#
# Replaces all current representations of the target resource with the uploaded content.
#
# 5
# DELETE
#
# Removes all current representations of the target resource given by a URL


#POST

@app.route('/login',methods = ['POST'])
def login():
    user = request.form['username']
    password = request.form['password']
    location = request.form['location']
    if user == "janak" and password == "123456":
        return "user is valid {}".format(location)
    else:
        return "user is invalid"

#GET
@app.route('/userdetalis',methods = ['GET'])
def userdetalis():
    return dict( uid = 1 , name = "janak" , roll = "admin" , location = "mumbai" )


#DELETE
@app.route('/deleteuser',methods = ["POST"])
def deleteuser():
    userdata  = [ {"name" : "janak" , "location":"mumbai"} , {"name":"rohan" , "location":"US"} , {"name":"amit" , "location":"canada"}]
    user = request.form['username']
    for ud in userdata:
        if ud["name"] == user:
            userdata.remove(ud)
    return json.dumps(userdata)

#PUT
@app.route('/updateuser',methods = ["PUT"])
def updateuser():
    userdata  = [ {"name" : "janak" , "location":"mumbai"} , {"name":"rohan" , "location":"US"} , {"name":"amit" , "location":"canada"}]
    phoneno = request.form['phone']
    user = request.form['username']
    for ud in userdata:
        if ud["name"] == user:
            ud["phone"] = phoneno
            userdata.append(ud)
            break
    return json.dumps(userdata)

#PATCH



if __name__ == "__main__":
    app.run(host="localhost",port=8080,debug=True)