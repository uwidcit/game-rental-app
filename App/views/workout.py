from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify

workout_views = Blueprint('workout_views', __name__, template_folder='../templates')
from App.controllers import (
    get_all_workouts_by_muscle,
    get_all_workouts_by_type,
    get_all_workouts_by_diffculty
)