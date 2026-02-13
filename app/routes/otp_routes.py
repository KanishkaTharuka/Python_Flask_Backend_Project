from ..models.otp import OTP
from ..models.user import User  
from ..extensions import db, mail
from flask import Flask, request, jsonify, Blueprint
from datetime import datetime
import secrets
from werkzeug.security import generate_password_hash
from flask_mail import Message

otp_bp = Blueprint('otp_bp', __name__, url_prefix='/api/otp')

@otp_bp.route('/send', methods=['POST'])
def send_otp():
    email = request.json['email']

    if not email:
        return jsonify({"message": "Email is required"}), 400
    
    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({"message": "User not found"}), 404

    # generate 6digit random number
    otp = secrets.randbelow(900000) + 100000

    OTP.query.filter_by(email=email).delete()

    new_otp = OTP(
        email=email,
        otp=otp
    )

    db.session.add(new_otp)
    db.session.commit()

    msg = Message(
        "OTP",
        recipients=[email],
    )

    msg.body = f"Your OTP is: {otp}"

    mail.send(msg)

    return jsonify({"message": "OTP sent successfully"}), 200



@otp_bp.route('/verify', methods=['POST'])
def verify_otp():
    email=request.json['email']
    otp=request.json['otp']
    newPassword = request.json['password']

    otpRecord=OTP.query.filter_by(email=email).first()

    if not otpRecord:
        return jsonify({"message": "OTP not found"}), 404
    
    if otpRecord.is_expired():
        return jsonify({"message": "OTP has expired"}), 401

    if otpRecord.otp != int(otp):
        return jsonify({"message": "Invalid OTP"}), 401

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({"message": "User not found"}), 404

    user.password = generate_password_hash(newPassword)

    OTP.query.filter_by(email=email).delete()
    db.session.commit()

    return jsonify({"message": "Password changed successfully"}), 200