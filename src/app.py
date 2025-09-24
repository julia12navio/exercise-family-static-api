"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
# from models import Person


app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Create the jackson family object
jackson_family = FamilyStructure("Jackson")


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


# Generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


# 1) GET /members
@app.route('/members', methods=['GET'])
def get_members():
    try:
        members = jackson_family.get_all_members()
        return jsonify(members), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 2) GET /members/<int:member_id> 
@app.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    try:
        member = jackson_family.get_member(member_id)
        if not member:
            return jsonify({"msg": "Member not found"}), 404
        return jsonify(member), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 3) POST /members -> add
@app.route('/members', methods=['POST'])
def add_member():
    try:
        if not request.is_json:
            return jsonify({"msg": "Content-Type must be application/json"}), 400
        payload = request.get_json()

        # Campos mínimos: first_name, age, lucky_numbers 
        required = ["first_name", "age", "lucky_numbers"]
        if not all(k in payload for k in required):
            return jsonify({"msg": "Missing required fields"}), 400

        new_member = jackson_family.add_member(payload)
        return jsonify(new_member), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# 4) DELETE /members/<int:member_id> -> delete
@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    try:
        deleted = jackson_family.delete_member(member_id)
        if not deleted:
            return jsonify({"msg": "Member not found"}), 404
        return jsonify({"done": True}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500   

# This only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
