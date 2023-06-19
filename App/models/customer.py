from .user import User
from App.database import db

class Customer(User):
    __tablename__ = 'customer'
    status = db.Column(db.String(120), nullable=False, default='active')
    listings = db.relationship('Listing', backref=db.backref('owner', lazy='joined'))
    rentals = db.relationship('Rental', backref=db.backref('renter', lazy='joined'))
    payments = db.relationship('Payment', backref=db.backref('customer', lazy='joined'))

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)
        self.user_type = "customer"

    def __repr__(self):
        return f'<Customer {self.id} {self.username}>'

    def get_rentals(self):
        oustanding_rentals = []
        rental_history = []
        for rental in self.rentals:
            if rental.return_date is None:
                oustanding_rentals.append(rental)
            else:
                rental_history.append(rental)
        return oustanding_rentals, rental_history

    def toJSON(self):
        return{
            'id': self.id,
            'username': self.username,
            'type': 'customer',
            'status': self.status
        }