from App.models import UserWorkout, Workout, User
from App.database import db
from App.config import config

import requests
import json


def save_workout(userId, workoutId,sets, reps, weight, day):  
    workout = UserWorkout(userId = userId,workoutId = workoutId ,sets = sets, reps=reps,weight = weight,day = day)
    user = User.query.filter_by(id=userId).first()
    db.session.add(workout)   
    user.workouts.append(workout)   
    db.session.commit()
    return workout

def edit_workout(uwId,userId,sets,reps,weight,day):
    workout = UserWorkout.query.filter_by(uwId = uwId, userId=userId).first()
    if workout:
      workout.sets = sets
      workout.reps = reps
      workout.weight = weight
      workout.day = day
      db.session.add(workout)
      db.session.commit()
      return workout
    return None

def delete_workout(uwId,userId):
    workout = UserWorkout.query.filter_by(uwId = uwId, userId=userId).first()
    if workout:
      db.session.delete(workout)
      db.session.commit()
      return True
    return None

def get_workouts_by_day(userId,day):
   user = User.query.filter_by(id=userId).first()
   if user: 
        workout = UserWorkout.query.filter_by(day = day, userId=userId).all()
        return workout
   else:
      return None

def get_all_user_workouts():
  return UserWorkout.query.all()

def get_user_workouts(userId):
  return UserWorkout.query.filter_by(userId=userId).all() 
  
 
    