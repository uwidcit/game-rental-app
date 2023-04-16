from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify, json, flash
import requests
myworkouts_views = Blueprint('myworkouts_views', __name__, template_folder='../templates')
#from App.controllers import ()
from App.controllers import (
    get_workouts_by_day,
    edit_workout,
    delete_workout,
    user_required
)

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
    return render_template('myworkouts.html', mon = mon , tue=tue, wed = wed, thu = thu, fri= fri, sat=sat, sun = sun)

@myworkouts_views.route('/myworkouts/<int:uwid>', methods=['POST'])
@user_required
def editWorkout(uwid):
    data = request.form
    new_workout = edit_workout(uwid,current_user.id, data["sets"], data["reps"], data["weight"], data["day"])
    if(new_workout):
        flash("Successfully Edited")
        # workout = get_workout_by_id(new_workout.workoutId)
        return redirect(request.referrer)

@myworkouts_views.route('/myworkouts/<int:uwid>', methods=['POST'])
@user_required
def deleteWorkout(uwid):
    data = request.form
    if delete_workout(uwid,current_user.id):
        flash("Successfully Deleted")
        # workout = get_workout_by_id(new_workout.workoutId)
        return redirect(request.referrer)