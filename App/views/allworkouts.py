from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify, json, flash
import requests
allworkouts_views = Blueprint('allworkouts_views', __name__, template_folder='../templates')
#from App.controllers import ()

@allworkouts_views.route('/allworkouts', methods=['GET'])
def allworkouts_page():
    return render_template('allworkouts.html')

#returns multiple workouts
@allworkouts_views.route('/search', methods=['POST'])
def searchworkouts_page():
    data = request.form
    workouts = get_workout(data["name"])
    return render_template('search.html', workouts=workouts) 