from App.models import Rental, Listing, Customer
from .payment import create_rental_payment
from App.database import db

from datetime import datetime

def create_rental(userId, listingId):
    listing = Listing.query.filter_by(listingId=listingId, status='available').first()
    if listing:
        listing.status = 'rented'
        rental = Rental(userId, listingId)
        db.session.add(rental)
        db.session.add(listing)
        db.session.commit()
        return rental
    return False

def return_rental(rentalId):
    rental = Rental.query.get(rentalId)
    if rental:
        fees = rental.return_rental()
        create_rental_payment(rentalId, rental.userId, fees)
        return fees
    return False

def get_rentals_json():
    rentals = Rental.query.all()
    return [rental.toJSON() for rental in rentals]

def get_outstanding_customer_rentals(customerId):
    customer = Customer.query.get(customerId)
    if customer :
        return Rental.query.filter_by(renterId=customerId, return_date=None).all()
    return []
        
def get_outstanding_rentals():
    return Rental.query.filter_by(return_date=None).all()

def get_rental(rentalId):
    return Rental.query.get(rentalId)

