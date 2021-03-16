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
# User homepage and table creation
########
@app.route('/<user_id>', methods=['GET'])
def user_main(user_id):
    return jsonify("This is the main page of " + user_id + "!")
# curl --request GET http://localhost:5000/user123


@app.route('/<user_id>/create', methods=['POST'])
def user_create(user_id):
    return jsonify("This is where user creates tables")
# curl -X POST http://localhost:5000/user123/create




########
# Locations
########
@app.route('/<user_id>/locations', methods=['GET'])
def locations_show(user_id):
    return jsonify("This is " + user_id + "'s locations!")
# returns the user's locations; user only
# curl --request GET http://localhost:5000/user123/locations


@app.route('/<user_id>/locations', methods=['POST'])
def locations_add(user_id):
    return jsonify("To add locations to " + user_id + "'s table.")
# add entries to the user's locations; user only
# curl -X POST http://127.0.0.1:5000/user123/locations


@app.route('/<user_id>/locations', methods=['PATCH'])
def locations_edit(user_id):
    return jsonify("To edit " + user_id + "'s locations.")
# edit entries of the user's locations; user only
# curl -X PATCH http://127.0.0.1:5000/user123/locations


@app.route('/<user_id>/locations', methods=['DELETE'])
def locations_delete(user_id):
    return jsonify("To delete " + user_id + "'s locations.")
# delete entries of the user's locations; user only
# curl -X DELETE http://127.0.0.1:5000/user123/locations




########
# Clothes
########
@app.route('/<user_id>/clothes', methods=['GET'])
def clothes_show(user_id):
    return jsonify("This is " + user_id + "'s clothes!")
# curl --request GET http://localhost:5000/user123/clothes


@app.route('/<user_id>/clothes', methods=['POST'])
def clothes_add(user_id):
    return jsonify("To add clothes to " + user_id + "'s table.")
# add entries to the user's locations
# curl -X POST http://127.0.0.1:5000/user123/clothes


@app.route('/<user_id>/clothes', methods=['PATCH'])
def clothes_edit(user_id):
    return jsonify("To edit " + user_id + "'s clothes.")
# edit entries of the user's locations
# curl -X PATCH http://127.0.0.1:5000/user123/clothes


@app.route('/<user_id>/clothes', methods=['DELETE'])
def clothes_delete(user_id):
    return jsonify("To delete " + user_id + "'s clothes.")
# delete entries of the user's locations
# curl -X DELETE http://127.0.0.1:5000/user123/clothes




########
# Categories (Optional)
########
# @app.route('/categories', methods=['GET'])
# def categories_show():
#     return jsonify("All categories.")
# # return all clothes categories; public
# # curl --request GET http://localhost:5000/categories
#
# @app.route('/categories', methods=['POST'])
# def categories_add():
#     return jsonify("To add categories.")
# # add entries to categories; manager only
# # curl -X POST http://127.0.0.1:5000/categories
#
# @app.route('/categories', methods=['PATCH'])
# def categories_edit():
#     return jsonify("To edit categories.")
# # edit entries of categories; manager only
# # curl -X PATCH http://127.0.0.1:5000/categories
#
# @app.route('/categories', methods=['DELETE'])
# def categories_delete():
#     return jsonify("To delete categories.")
# # delete entries of categories; manager only
# # curl -X DELETE http://127.0.0.1:5000/categories