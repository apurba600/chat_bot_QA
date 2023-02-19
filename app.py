from flask import Flask, render_template, url_for, request
from model import searchup

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/go")
def go():
	query = request.args.get("query", "")
	result = searchup(query)
	return render_template("go.html", query = query, result = result)

if __name__ == "__main__":
	app.run(debug = True)