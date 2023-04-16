from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify, flash

workout_views = Blueprint('workout_views', __name__, template_folder='../templates')
from App.controllers import (
    get_all_workouts_by_muscle,
    get_all_workouts_by_type,
    get_all_workouts_by_diffculty,
    user_required
)

@workout_views.route('/musclegroup/<query>', methods=['GET'])
def workout_page_muscle(query):
    workouts = get_all_workouts_by_muscle(query)
    return render_template('workout.html', workouts=workouts)

@workout_views.route('/type/<query>', methods=['GET'])
def workout_page_type(query):
    workouts = get_all_workouts_by_type(query)
    return render_template('workout.html', workouts=workouts)

@workout_views.route('/diffuculty/<query>', methods=['GET'])
def workout_page_diffuculty(query):
    workouts = get_all_workouts_by_diffuculty(query)
    return render_template('workout.html', workouts=workouts)

@workout_views.route('/workout/<int:workoutId>', methods=['POST'])
@user_required
def saveWorkout(workoutId):
  data = request.form
  new_workout = save_workout(current_user.id, workoutId, data["sets"], data["reps"], data["weight"], data["day"])
  workout = get_workout_by_id(new_workout.workoutId)
  flash('Successfully Saved' + " " + workout.name)
  return redirect(request.referrer)