from ..extensions import db
from datetime import datetime

class User(db.Model):
    userId = db.Column(db.String(8), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    phoneNumber = db.Column(db.Integer, nullable=False)
    role = db.Column(db.String(10), default='USER')
    isBlocked = db.Column(db.Boolean, default=False)
    # auto generator date
    date = db.Column(db.DateTime, default=datetime.utcnow)


    def to_dict(self):
        return{
            'userId': self.userId,
            'name': self.name,
            'email': self.email,
            'address': self.address,
            'phoneNumber': self.phoneNumber,
            'role': self.role,
            'isBlocked': self.isBlocked,
            'date': self.date
        }