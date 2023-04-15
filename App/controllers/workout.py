from App.models import Workout
from App.database import db
from App.config import config

import requests
import json


def create_workout(name, type, muscle, equipment, difficulty , instructions):
    newworkout = Workout(name=name, type=type, muscle=muscle, equipment=equipment, difficulty=difficulty, instructions=instructions)
    db.session.add(newworkout)
    db.session.commit()
    return newworkout

def get_workout(rawgId):
    workout = Workout.query.filter_by(rawgId=rawgId).first()
    if workout :
        return workout
    else:
        workout = fetch_api_workout(rawgId)
        if workout:
            new_workout = create_workout(title=['name'], rawgId=game['id'], rating=rating, boxart=game['background_image'], genre=game['genres'][0]['slug'])
            return game
    return None

def get_all_workouts():
    return Workout.query.all()

def fetch_api_workout(query):
    query = "incline hammer curls"
    api_url = 'https://api.api-ninjas.com/v1/exercises?name={}'.format(query)
    response = requests.get(api_url, headers={'X-Api-Key': 'QY76AwkXk/VatIhcdT7isA==IMr5kwbqBVr2Bl3J'})
    if response.status_code == requests.codes.ok:  
        return response.json()        
    return jsonify("Error:", response.status_code, response.text)
    

def search_api_game(query):    
    api_url = 'https://api.api-ninjas.com/v1/exercises?name={}'.format(query)
    response = requests.get(api_url, headers={'X-Api-Key': 'QY76AwkXk/VatIhcdT7isA==IMr5kwbqBVr2Bl3J'})
    if response.status_code == requests.codes.ok:  
        return response.json()        
    return jsonify("Error:", response.status_code, response.text)

def fetch_api_workouts(query_type, query):
    api_url = f'https://api.api-ninjas.com/v1/exercises?{query_type}={query}'
    try:
        response = requests.get(api_url, headers={'X-Api-Key':f'{config["NINJA_TOKEN"]}'})
        if response.status_code != requests.codes.ok:  
           response.raise_for_status()
        return json.loads(response.text)
    except Exception as e:
        print(f"error: {e}")
    return []
    
def cache_api_workouts():
    
    query_type = ["type", "muscle", "difficulty"]
    query_by_type = ["cardio", "plyometrics", "strength","stretching","strongman","powerlifting"]
    query_by_muscle = ["abdominals", "biceps", "chest","glutes","quadriceps","lower_back","abductors","calves", "hamstrings"]

    query_by_difficulty = ["beginner", "intermediate", "expert"]
    for x in query_by_type:
        workouts_by_type= fetch_api_workouts(query_type="type", query=x)
        for workout in  workouts_by_type:
            newworkout = Workout(name=workout['name'], type=workout['type'], muscle=workout['muscle'], equipment=workout['equipment'], difficulty=workout['difficulty'], instructions=workout['instructions'])
            db.session.add(newworkout)
    for x in query_by_muscle:
        workouts_by_type= fetch_api_workouts(query_type="mucle", query=x)
        for workout in  workouts_by_type:
            newworkout = Workout(name=workout['name'], type=workout['type'], muscle=workout['muscle'], equipment=workout['equipment'], difficulty=workout['difficulty'], instructions=workout['instructions'])
            db.session.add(newworkout)
    for x in query_by_difficulty:
        workouts_by_type= fetch_api_workouts(query_type="difficulty", query=x)
        for workout in  workouts_by_type:
            newworkout = Workout(name=workout['name'], type=workout['type'], muscle=workout['muscle'], equipment=workout['equipment'], difficulty=workout['difficulty'], instructions=workout['instructions'])
            db.session.add(newworkout)
    db.session.commit()

def get_all_workouts_json():
    workouts = Workout.query.all()
    if not workouts:
        return []
    return [workout.toJSON() for workout in workouts]


def get_all_workouts_by_muscle(query):
    workouts =  Workout.query.filter_by(muscle=query).all()
    if not workouts:
        return []
    return workouts
def get_all_workouts_by_type(query):
    workouts =  Workout.query.filter_by(type=query).all()
    if not workouts:
        return []
    return workouts

def get_all_workouts_by_diffculty(query):
    workouts =  Workout.query.filter_by(difficulty=query).all()
    if not workouts:
        return []
    return workouts