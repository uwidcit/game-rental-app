from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify, json, flash
import requests
from flask_login import current_user
myworkouts_views = Blueprint('myworkouts_views', __name__, template_folder='../templates')
#from App.controllers import ()
from App.controllers import (
    get_workouts_by_day,
    edit_workout,
    edit_workout2,
    delete_workout,
    delete_workout2,
    user_required,
    get_all_workouts
)

#returns multiple workouts in each attribute so use a for loop to list
@myworkouts_views.route('/myworkouts', methods=['GET'])
@user_required
def myworkouts_page():
    mon,mon1 = get_workouts_by_day(current_user.id,"mon")
    tue,mon2 = get_workouts_by_day(current_user.id,"tue")
    wed,wed2 = get_workouts_by_day(current_user.id,"wed")
    thu,thu2 = get_workouts_by_day(current_user.id,"thu")
    fri,fri2 = get_workouts_by_day(current_user.id,"fri")
    sat,sat2 = get_workouts_by_day(current_user.id,"sat")
    sun,sun2 = get_workouts_by_day(current_user.id,"sun")
    workouts = get_all_workouts()
    

    week_workouts = {
    'Monday': (mon, mon2),
    'Tuesday': (tue, tue2),
    'Wednesday': (wed, wed2),
    'Thursday': (thu, thu2),
    'Friday': (fri, fri2),
    'Saturday': (sat, sat2),
    'Sunday': (sun, sun2)
}

    w_days = {"Monday": "mon", "Tuesday": "tue", 
    "Wednesday": "wed", "Thursday": 
    "thu", "Friday": "fri", 
    "Saturday": "sat", "Sunday": "sun"}
    return render_template('myworkouts.html', days = week_workouts, workouts = workouts, w_days=w_days)

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

@myworkouts_views.route('/myworkouts', methods=['POST'])
@user_required
def editPersonalWorkout():
    data = request.form
    new_workout = edit_workout2(data["pwid"],current_user.id, data["name"],data["sets"], data["reps"], data["weight"], data["day"])
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

@myworkouts_views.route('/personalworkouts/<int:pwid>', methods=['GET'])
@user_required
def deletePersonalWorkout(pwid):
    if delete_workout2(pwid,current_user.id):
        flash("Successfully Deleted")
        # workout = get_workout_by_id(new_workout.workoutId)
        return redirect(request.referrer)

@myworkouts_views.route('/createworkout' )
@user_required
def createWorkout_page():
    w_days = {"Monday": "mon", "Tuesday": "tue", 
    "Wednesday": "wed", "Thursday": 
    "thu", "Friday": "fri", 
    "Saturday": "sat", "Sunday": "sun"}
    return render_template('createworkout.html',w_days=w_days)