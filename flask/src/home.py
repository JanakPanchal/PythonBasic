from flask import render_template
class Home:
    def displayHomepage(self):
		return render_template("home.html")
	