from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify, json
import requests
allworkouts_views = Blueprint('allworkouts_views', __name__, template_folder='../templates')
#from App.controllers import ()
from App.controllers import (
    get_all_workouts_by_muscle,
    get_all_workouts_by_type,
    get_all_workouts_by_diffculty
)
@allworkouts_views.route('/allworkouts', methods=['GET'])
def allworkouts_page():
    return render_template('allworkouts.html')

@allworkouts_views.route('/musclegroup/<query>', methods=['GET'])
def workout_page_muscle(query):
    workouts = get_all_workouts_bymuscle(query)
    return render_template('workout.html', workouts=workouts)

@allworkouts_views.route('/type/<query>', methods=['GET'])
def workout_page_type(query):
    workouts = get_all_workouts_bytype(query)
    return render_template('workout.html', workouts=workouts)

@allworkouts_views.route('/diffuculty/<query>', methods=['GET'])
def workout_page_diffuculty(query):
    workouts = get_all_workouts_bydiffuculty(query)
    return render_template('workout.html', workouts=workouts)