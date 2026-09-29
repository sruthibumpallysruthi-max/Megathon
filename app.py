from flask import Flask, jsonify,request
from flask_cors import CORS

app = Flask(__name__)
CORS (app)
@app.route("/")
def home():
    return "Hello from Flask!"
@app.route("/user")
def user():
    data={
        "name":"shruthi",
        "age":19,
        "branch":"cse"
    }
    return jsonify(data)

@app.route("/greet", methods=["POST"])
def greet():
    data = request.json

    name = data["name"]

    return jsonify({
        "message": "Hello " + name
    })
@app.route("/issue",methods=["POST"])
def issue():
    data=request.json
    problem=data["problem"]
    return jsonify({"message": "Issue reported: " + problem})

app.run(debug=True)