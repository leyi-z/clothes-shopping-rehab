from flask import Flask, jsonify, request, abort

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    return jsonify("This is the homepage!")
# curl --request GET http://localhost:5000/