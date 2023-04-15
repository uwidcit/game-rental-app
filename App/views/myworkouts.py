from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify, json
import requests
myworkouts_views = Blueprint('myworkouts_views', __name__, template_folder='../templates')
#from App.controllers import ()
from App.controllers import (
    get_all_workouts_by_muscle,
    get_all_workouts_by_type,
    get_all_workouts_by_diffculty
)
@myworkouts_views.route('/myworkouts', methods=['GET'])
def myworkouts_page():
    return render_template('allworkouts.html')

@myworkouts_views.route('/musclegroup/<query>', methods=['GET'])
def workout_page_muscle(query):
    workouts = get_all_workouts_bymuscle(query)
    return render_template('workout.html', workouts=workouts)

@myworkouts_views.route('/type/<query>', methods=['GET'])
def workout_page_type(query):
    workouts = get_all_workouts_bytype(query)
    return render_template('workout.html', workouts=workouts)

@myworkouts_views.route('/diffuculty/<query>', methods=['GET'])
def workout_page_diffuculty(query):
    workouts = get_all_workouts_bydiffuculty(query)
    return render_template('workout.html', workouts=workouts)