from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/contactus")
def contacts():
	return render_template("contactus.html")

@app.route("/team")
def team():
	return render_template("team.html")

@app.route("/chinafocus")
def china():
	return render_template("china_focus.html")

@app.route("/techfocus")
def tech():
	return render_template("technology_focus.html")

@app.route("/investment")
def investment():
	return render_template("investment_philosophy.html")


if __name__ == "__main__":
	app.run(debug=True, use_debugger=False, use_reloader=False)