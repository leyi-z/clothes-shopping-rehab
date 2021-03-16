from flask import Flask, jsonify, request, abort




app = Flask(__name__)




########
# Homepage
########
@app.route('/', methods=['GET'])
def homepage():
    return jsonify("This is the homepage!")
# curl --request GET http://localhost:5000/




########
# Login 
########
@app.route('/login', methods=['GET'])
def login():
    return jsonify("This is the login page!")
# curl --request GET http://localhost:5000/login




########
# Locations
########
@app.route('/locations', methods=['GET'])
def locations_list():
    return jsonify("User's locations.")
# returns the user's locations; psych and recorder
# curl --request GET http://localhost:5000/locations


@app.route('/locations/<int:location_id>', methods=['GET'])
def locations_one(location_id):
    return jsonify("List of clothes at one location.")
# returns the user's locations; psych and recorder
# curl --request GET http://localhost:5000/locations/1


@app.route('/locations', methods=['POST'])
def locations_add():
    return jsonify("To add locations to user's table.")
# add entries to the user's locations; recorder only
# curl -X POST http://127.0.0.1:5000/locations


@app.route('/locations', methods=['PATCH'])
def locations_edit():
    return jsonify("To edit user's locations.")
# edit entries of the user's locations; recorder only
# curl -X PATCH http://127.0.0.1:5000/locations


@app.route('/locations', methods=['DELETE'])
def locations_delete():
    return jsonify("To delete user's locations.")
# delete entries of the user's locations; recorder only
# curl -X DELETE http://127.0.0.1:5000/locations




########
# Clothes
########
@app.route('/clothes', methods=['GET'])
def clothes_list():
    return jsonify("This is user's clothes!")
# show all clothes; psych and recorder
# curl --request GET http://localhost:5000/clothes


@app.route('/clothes', methods=['POST'])
def clothes_add():
    return jsonify("To add clothes to user's table.")
# add entries to the user's locations; recorder only
# curl -X POST http://127.0.0.1:5000/clothes


@app.route('/clothes', methods=['PATCH'])
def clothes_edit():
    return jsonify("To edit user's clothes.")
# edit entries of the user's locations; recorder only
# curl -X PATCH http://127.0.0.1:5000/clothes


@app.route('/clothes', methods=['DELETE'])
def clothes_delete():
    return jsonify("To delete user's clothes.")
# delete entries of the user's locations; recorder only
# curl -X DELETE http://127.0.0.1:5000/clothes




