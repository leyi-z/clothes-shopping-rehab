from flask import Flask, jsonify, request, abort

from models import db_drop, db_create, setup_db, Location, Clothes
from auth import AuthError, requires_auth, auth_url



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
    url = auth_url()
    return jsonify({
        "url": url
    })

    



########
# Locations
########
@app.route('/locations', methods=['GET'])
@requires_auth('get:inventory')
def locations_list(jwt):
    locations = Location.query.order_by(Location.id).all()
    locations = [location.format() for location in locations]
    return jsonify({
        "success": True,
        "locaions": locations
    })
# returns the user's locations; psych and recorder


@app.route('/locations', methods=['POST'])
@requires_auth('add:inventory')
def locations_add(jwt):
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
@requires_auth('get:inventory')
def locations_one(jwt,location_id):
    clothes = Clothes.query.filter(Clothes.location == location_id).all()
    clothes = [piece.format() for piece in clothes]
    return jsonify({
        "success": True,
        "clothes": clothes
    })
# returns clothes stored at specified location; psych and recorder


@app.route('/locations/<int:location_id>', methods=['PATCH'])
@requires_auth('update:inventory')
def locations_edit(jwt,location_id):
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
@requires_auth('delete:inventory')
def locations_delete(jwt,location_id):
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
@requires_auth('get:inventory')
def clothes_list(jwt):
    clothes = Clothes.query.order_by(Clothes.id).all()
    clothes = [piece.format() for piece in clothes]
    return jsonify({
        "success": True,
        "clothes": clothes
    })
# show all clothes; psych and recorder


@app.route('/clothes', methods=['POST'])
@requires_auth('add:inventory')
def clothes_add(jwt):
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
@requires_auth('update:inventory')
def clothes_edit(jwt,clothes_id):
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
@requires_auth('delete:inventory')
def clothes_delete(jwt,clothes_id):
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



########
# Error Handlers
########
@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "Bad request"
    }), 400


@app.errorhandler(401)
def unauthorized(error):
    return jsonify({
        "success": False,
        "error": 401,
        "message": "unauthorized"
    }), 401


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "not found"
    }), 404


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({
        "success": False,
        "error": 405,
        "message": "method not allowed"
    }), 405


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@app.errorhandler(500)
def server_error(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": "internal server error"
    }), 500


@app.errorhandler(AuthError)
def auth_error(error):
    return jsonify({
        "success": False,
        "error": 401,
        "message": "unauthorized"
    }), 401

