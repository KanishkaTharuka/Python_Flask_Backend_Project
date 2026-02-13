from flask import Flask, Blueprint, request, jsonify
from ..models.user import User
from ..extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt

user_bp = Blueprint('user_bp', __name__, url_prefix='/api/user')


@user_bp.route('/register', methods=['POST'])
def create_user():
    data = request.json


    # generate user_id (UID36001)
    lastUser = User.query.order_by(User.userId.desc()).first()
    uId = "UID36001"
    if(lastUser) :
        lastUserInString = lastUser.userId
        lastUserWithoutPrefix = lastUserInString.replace("UID", "")
        lastUserInteger = int(lastUserWithoutPrefix)
        newUserInteger = lastUserInteger + 1

        newUserIntegerString = str(newUserInteger)
        uId = "UID" + newUserIntegerString



    if User.query.filter_by(email=data["email"]).first():
        return jsonify(
            {
                "message": "User with this email already exists."
            }
        ), 400
    
    hashed_password = generate_password_hash(data['password'])

    new_user = User(
        userId=uId,
        name=data['name'],
        email=data['email'],
        password=hashed_password,
        role=data['role'],
        address=data['address'],
        phoneNumber=data['phoneNumber'],
    )

    db.session.add(new_user)
    db.session.commit() 

    return jsonify(
        new_user.to_dict()
    ), 201

@user_bp.route('/login', methods=['POST'])
def login_user():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()

    if user and check_password_hash(user.password, data['password']):

        token = create_access_token(
            identity=user.userId,
            additional_claims={
                "name": user.name,
                "email": user.email,
                "role": user.role
            }
        )

        return jsonify(
            {
                "message": "Login successful",
                "token": token,
                "user": user.to_dict()
            }
        ), 200
    else:
        return jsonify(
            {
                "message": "Invalid email or password"
            }
        ), 401
    



@user_bp.route('/<string:user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    user=User.query.get(user_id)
    if user:
        return jsonify(user.to_dict())
    else:
        return jsonify({"message": "User not found"}), 404
    

@user_bp.route('/', methods=['GET'])
@jwt_required()
def get_all_users():

    current_user = get_jwt_identity()
    claims = get_jwt()
    role = claims.get('role')

    if(role != 'ADMIN'):
        return jsonify({"message": "You are not authorized to access this resource"}), 403



    users = User.query.all()
    users_list = [user.to_dict() for user in users]
    return jsonify({
        "message": "Users fetched successfully",
        "current_user": current_user,
        "role": role,
        "users": users_list
    }), 200 


@user_bp.route('/<string:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    user = User.query.get(user_id)

    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted successfully"})
    else:
        return jsonify({"message": "User not found"}), 404
    

@user_bp.route('/<string:user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    user=User.query.get(user_id)
    data=request.json

    if user:
        user.name=data.get('name', user.name)
        user.email=data.get('email', user.email)
        user.address=data.get('address', user.address)
        user.phoneNumber=data.get('phoneNumber', user.phoneNumber)

        if 'password' in data:
            user.password=generate_password_hash(data['password'])

        db.session.commit()

        return jsonify(user.to_dict())
    else:
        return jsonify({"message": "User not found"}), 404
    


    
