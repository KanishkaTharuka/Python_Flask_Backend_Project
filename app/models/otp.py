from ..extensions import db
from datetime import datetime, timedelta

class OTP(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email=db.Column(db.String(120), primary_key=True)
    otp=db.Column(db.Integer, nullable=False)
    createdAt=db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return{
            'email': self.email,
            'otp': self.otp,
            'date': self.date
        }
    def is_expired(self):
        return datetime.utcnow() > self.createdAt + timedelta(minutes=10)