from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify, json, flash
import requests
from flask_login import current_user
myworkouts_views = Blueprint('myworkouts_views', __name__, template_folder='../templates')
#from App.controllers import ()
from App.controllers import (
    get_workouts_by_day,
    edit_workout,
    delete_workout,
    user_required,
    get_all_workouts
)

#returns multiple workouts in each attribute so use a for loop to list
@myworkouts_views.route('/myworkouts', methods=['GET'])
@user_required
def myworkouts_page():
    mon = get_workouts_by_day(current_user.id,"mon")
    tue = get_workouts_by_day(current_user.id,"tue")
    wed = get_workouts_by_day(current_user.id,"wed")
    thu = get_workouts_by_day(current_user.id,"thu")
    fri = get_workouts_by_day(current_user.id,"fri")
    sat = get_workouts_by_day(current_user.id,"sat")
    sun = get_workouts_by_day(current_user.id,"sun")
    workouts = get_all_workouts();
    return render_template('myworkouts.html', monday = mon , tuesday=tue, wednesday = wed, thursday = thu, friday= fri, saturday=sat, sunday = sun, workouts = workouts)

#just does a flash and reloads the page to show the updated info
@myworkouts_views.route('/myworkouts', methods=['POST'])
@user_required
def editWorkout():
    data = request.form
    new_workout = edit_workout(data["workoutId"],current_user.id, data["sets"], data["reps"], data["weight"], data["day"])
    if(new_workout):
        flash("Successfully Edited")
        # workout = get_workout_by_id(new_workout.workoutId)
        return redirect(request.referrer)

#just does a flash and reloads the page to show the updated info
@myworkouts_views.route('/myworkouts/<int:uwid>', methods=['GET'])
@user_required
def deleteWorkout(uwid):
    if delete_workout(uwid,current_user.id):
        flash("Successfully Deleted")
        # workout = get_workout_by_id(new_workout.workoutId)
        return redirect(request.referrer)