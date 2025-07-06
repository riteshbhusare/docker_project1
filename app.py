from flask import flask
app = Flask(_name_)
@app.route(*/info*)
def lwinfo():
	return "I am Ritesh Bhusare from India"
@app.route("/phone")
def lwphone():
	return"14549500"
app.run(host="0.0.0.0")