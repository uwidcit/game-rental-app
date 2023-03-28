from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify

index_views = Blueprint('index_views', __name__, template_folder='../templates')
from App.controllers import (
    get_all_listings,
    initialize,
)

@index_views.route('/', methods=['GET'])
def index_page():
    listings = get_all_listings()
    return render_template('index.html', listings=listings)

@index_views.route('/init', methods=['GET'])
def init():
    initialize()
    return jsonify(message='db initialized!')

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})