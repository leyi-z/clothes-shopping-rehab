from flask import Flask, jsonify, request, abort

from models import db_drop, db_create, setup_db, Location, Clothes



app = Flask(__name__)
setup_db(app)



# Drop and create tables
# db_drop()
# db_create()



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
    locations = Location.query.order_by(Location.id).all()
    locations = [location.format() for location in locations]
    return jsonify({
        "success": True,
        "locaions": locations
    })
# returns the user's locations; psych and recorder
# curl --request GET http://localhost:5000/locations


@app.route('/locations', methods=['POST'])
def locations_add():
    return jsonify("To add locations to user's table.")
# add entries to the user's locations; recorder only
# curl -X POST http://127.0.0.1:5000/locations


@app.route('/locations/<int:location_id>', methods=['GET'])
def locations_one(location_id):
    location = Location.query.filter(Location.id == location_id).one_or_none()
    location = location.format()
    return jsonify({
        "success": True,
        "location": location
    })
# returns the user's locations; psych and recorder
# curl --request GET http://localhost:5000/locations/1


@app.route('/locations/<int:location_id>', methods=['PATCH'])
def locations_edit(location_id):
    return jsonify("To edit user's locations.")
# edit entries of the user's locations; recorder only
# curl -X PATCH http://127.0.0.1:5000/locations/1


@app.route('/locations/<int:location_id>', methods=['DELETE'])
def locations_delete(location_id):
    return jsonify("To delete user's locations.")
# delete entries of the user's locations; recorder only
# curl -X DELETE http://127.0.0.1:5000/locations/1




########
# Clothes
########
@app.route('/clothes', methods=['GET'])
def clothes_list():
    clothes = Clothes.query.order_by(Clothes.id).all()
    clothes = [piece.format() for piece in clothes]
    return jsonify({
        "success": True,
        "clothes": clothes
    })
# show all clothes; psych and recorder
# curl --request GET http://localhost:5000/clothes


@app.route('/clothes', methods=['POST'])
def clothes_add():
    return jsonify("To add clothes to user's table.")
# add entries to the user's locations; recorder only
# curl -X POST http://127.0.0.1:5000/clothes


@app.route('/clothes/<int:clothes_id>', methods=['PATCH'])
def clothes_edit(clothes_id):
    return jsonify("To edit user's clothes.")
# edit entries of the user's locations; recorder only
# curl -X PATCH http://127.0.0.1:5000/clothes/1


@app.route('/clothes/<int:clothes_id>', methods=['DELETE'])
def clothes_delete(clothes_id):
    return jsonify("To delete user's clothes.")
# delete entries of the user's locations; recorder only
# curl -X DELETE http://127.0.0.1:5000/clothes/1




