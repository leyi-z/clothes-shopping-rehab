from flask import Flask, jsonify, request, abort

from models import db_drop, db_create, setup_db, Location, Clothes



app = Flask(__name__)
setup_db(app)


# Drop and create tables to initialize database
# db_drop()
# db_create()

# @app.after_request
# def after_request(response):
#     response.headers.add(
#         'Access-Control-Allow-Headers',
#         'Content-Type, Authorization'
#     )
#     response.headers.add(
#         'Access-Control-Allow-Methods',
#         'GET, POST, PATCH, DELETE, OPTIONS'
#     )
#     return response



########
# Homepage
########
@app.route('/', methods=['GET'])
def homepage():
    return jsonify("This is the homepage!")




########
# Login 
########
@app.route('/login', methods=['GET'])
def login():
    return jsonify("This is the login page!")




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


@app.route('/locations', methods=['POST'])
def locations_add():
    body = request.get_json()
    new_name = body.get('name', None)
    try:
        new_location = Location(
            name=new_name
        )
        new_location.insert()
        return jsonify({
            "success": True,
            "new_id": new_location.id
        })
    except Exception as e:
        print(e)
        abort(422)
# add entries to the user's locations; recorder only


@app.route('/locations/<int:location_id>', methods=['GET'])
def locations_one(location_id):
    clothes = Clothes.query.filter(Clothes.location == location_id).all()
    clothes = [piece.format() for piece in clothes]
    return jsonify({
        "success": True,
        "clothes": clothes
    })
# returns clothes stored at specified location; psych and recorder


@app.route('/locations/<int:location_id>', methods=['PATCH'])
def locations_edit(location_id):
    body = request.get_json()
    new_name = body.get('name', None)
    location = Location.query.filter(Location.id == location_id).one_or_none()
    try:
        location.name = new_name
        location.update()
        return jsonify({
            "success": True,
            "updated_id": location.id
        })
    except Exception as e:
        print(e)
        abort(422)
# edit entries of the user's locations; recorder only


@app.route('/locations/<int:location_id>', methods=['DELETE'])
def locations_delete(location_id):
    location = Location.query.filter(Location.id == location_id).one_or_none()
    try:
        location.delete()
        return jsonify({
            "success": True,
            "deleted id": location_id
        })
    except Exception as e:
        print(e)
        abort(422)
# delete entries of the user's locations; recorder only




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


@app.route('/clothes', methods=['POST'])
def clothes_add():
    body = request.get_json()
    new_location = body.get('location', None)
    new_category = body.get('category', None)
    new_description = body.get('description', None)
    try:
        new_piece = Clothes(
            location=new_location,
            category=new_category,
            description=new_description
        )
        new_piece.insert()
        return jsonify({
            "success": True,
            "new_id": new_piece.id
        })
    except Exception as e:
        print(e)
        abort(422)
# add entries to the user's locations; recorder only


@app.route('/clothes/<int:clothes_id>', methods=['PATCH'])
def clothes_edit(clothes_id):
    body = request.get_json()
    new_location = body.get('location', None)
    new_category = body.get('category', None)
    new_description = body.get('description', None)
    piece = Clothes.query.filter(Clothes.id == clothes_id).one_or_none()
    try:
        piece.location = new_location
        piece.category = new_category
        piece.description = new_description
        piece.update()
        return jsonify({
            "success": True,
            "updated_id": piece.id
        })
    except Exception as e:
        print(e)
        abort(422)
# edit entries of the user's locations; recorder only


@app.route('/clothes/<int:clothes_id>', methods=['DELETE'])
def clothes_delete(clothes_id):
    piece = Clothes.query.filter(Clothes.id == clothes_id).one_or_none()
    try:
        piece.delete()
        return jsonify({
            "success": True,
            "deleted id": clothes_id
        })
    except Exception as e:
        print(e)
        abort(422)
# delete entries of the user's locations; recorder only




