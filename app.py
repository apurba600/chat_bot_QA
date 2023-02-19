from flask import Flask, render_template, url_for, request
import openai

API_KEY = "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"
openai.api_key = API_KEY

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/go")
def go():
	query = request.args.get("query", "")

	response = openai.Completion.create(
  	model="text-davinci-003",
  	prompt= query,
  	temperature=0,
  	max_tokens=100,
  	top_p=1,
  	frequency_penalty=0,
  	presence_penalty=0,
	)
	result = response.choices[0].text
	return render_template("go.html", query = query, result = result)

if __name__ == "__main__":
	app.run(debug = True)