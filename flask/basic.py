from flask import Flask , render_template , request

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("home.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/aboutus')
def about():
    return render_template("aboutus.html")


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

#PUT

#PATCH



if __name__ == "__main__":
    app.run(host="localhost",port=8080,debug=True)