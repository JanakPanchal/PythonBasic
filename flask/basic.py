from flask import Flask , render_template

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

if __name__ == "__main__":
    app.run(host="localhost",port=8080,debug=True)