from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    role = db.Colum (db.String(20),nullable = False,default = 'resident')
    contact = db.Column(db.String(50), nullable = True)

    street_id = db.Column(db.Integer, db.ForeignKey('streets.id'), nullable = True)

    stop_requests - db.relationship('StopRequest', back_populates = 'resident', cascade = "all, delete-orphan")
    notifications = db.relationship('Notification', back_populates = 'resident', cascade = "all, delete-orphan")

    def __init__(self, username, password role= 'resident', contact = None, street_id = None):
        self.username = username
        self.set_password(password)
        self.role = role
        self.contact = contact
        self.street_id = street_id

    def get_json(self):
        return{
            'id': self.id,
            'username': self.username,
            'role': self.role,
            'street_id' : self.street_id,
            'contact' : self.contact
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def_repr_(self):
        return f"<User id= {self.id} username = {slef.username} role= {self.role}>"

