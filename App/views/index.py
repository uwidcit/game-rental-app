from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from flask_login import current_user

index_views = Blueprint('index_views', __name__, template_folder='../templates')
from App.controllers import (
    get_listing,
    get_all_listings,
    initialize,
)

@index_views.route('/', methods=['GET'])
def index_page(listing_id=None):
    listings = get_all_listings()
    return render_template('index.html', listings=listings)

@index_views.route('/<int:listing_id>', methods=['GET'])
def get_listing_page(listing_id):
    listing = get_listing(listing_id)
    return render_template('detail.html', listing=listing)

@index_views.route('/init', methods=['GET'])
def init():
    initialize()
    return jsonify(message='db initialized!')

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})

@index_views.route('/about', methods=['GET'])
def about_page():
    return render_template('about.html')

# profile page
@index_views.route('/profile', methods=['GET'])
def profile_page():
    return render_template('profile.html', current_user=current_user)