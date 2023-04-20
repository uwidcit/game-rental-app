from App.models import Workout, ExtraWorkout
from App.database import db
from App.config import config

import requests
import json


def create_workout(name, type, muscle, equipment, difficulty , instructions):
    newworkout = Workout(name=name, type=type, muscle=muscle, equipment=equipment, difficulty=difficulty, instructions=instructions)
    db.session.add(newworkout)
    db.session.commit()
    return newworkout


def get_workout(name):
    workout = Workout.query.filter(Workout.name.like(f'%{name}%')).all()
    if workout :
        return workout
    else:
        try:
            workout = fetch_api_workout(name)
            workouts = []
            if workout:
                for w in workout:
                    new_workout = Workout(name=w['name'].title(), type=w['type'], muscle=w['muscle'], equipment=w['equipment'], difficulty=w['difficulty'], instructions=w['instructions'])
                    workouts.append(new_workout)
                    db.session.add(new_workout)
                db.session.commit()
                return workouts
        except Exception as e:
            raise Exception(f"Error fetching workout from API: {e}")
    return None

def get_all_workouts():
    return Workout.query.all()

def get_all_workouts2():
    return ExtraWorkout.query.all()

def fetch_api_workout(query):    
    api_url = f'https://api.api-ninjas.com/v1/exercises?name={query}'
    try:
        response = requests.get(api_url, headers={'X-Api-Key':f'{config["NINJA_TOKEN"]}'})
        if response.status_code != requests.codes.ok:  
           response.raise_for_status()
        return json.loads(response.text)
    except Exception as e:
        raise Exception(f"Error fetching workouts from API: {e}")
    return None

def fetch_api_workouts(query_type, query):
    api_url = f'https://api.api-ninjas.com/v1/exercises?{query_type}={query}'
    try:
        response = requests.get(api_url, headers={'X-Api-Key':f'{config["NINJA_TOKEN"]}'})
        if response.status_code != requests.codes.ok:  
           response.raise_for_status()
        return json.loads(response.text)
    except Exception as e:
        raise Exception(f"Error fetching workouts from API: {e}")
    return []

def fetch_api_extra_workouts():
    api_url = 'https://exercisedb.p.rapidapi.com/exercises'
    headers = {
        "X-RapidAPI-Key": "e6c22e8e13mshf7acf532fb1d00cp148c62jsn39fb0852a2ae",
        "X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
    }
    try:
        response = requests.request("GET", api_url, headers=headers)
        if response.status_code != requests.codes.ok:  
           response.raise_for_status()
        return json.loads(response.text)
    except Exception as e:
        raise Exception(f"Error fetching workouts from API: {e}")
    return []

def cache_api_extra_workouts():
    
    workouts = fetch_api_extra_workouts()
    works =[]
    for workout in workouts:
        name = workout['name'].title()                                    
        new_workout = ExtraWorkout(name=name, bodyPart=workout['bodyPart'], gifUrl=workout['gifUrl'], equipment=workout['equipment'], target=workout['target'])
        works.append(new_workout)
        db.session.add(new_workout)
    db.session.commit()
    return works
    
# def cache_api_workouts():
    
#     query_type = ["type", "muscle", "difficulty"]
#     query_by_type = ["cardio", "plyometrics", "strength","stretching","strongman","powerlifting"]
#     query_by_muscle = ["abdominals" ,"chest","glutes","quadriceps","lower_back","abductors","calves", "hamstrings"]
#     query_by_difficulty = ["beginner", "intermediate", "expert"]
#     workouts = []
#     for x in query_by_type:
#         workouts_by_type = fetch_api_workouts(query_type="type", query=x)
#         for workout in  workouts_by_type:
#             new_workout = Workout(name=workout['name'].title(), type=workout['type'], muscle=workout['muscle'], equipment=workout['equipment'], difficulty=workout['difficulty'], instructions=workout['instructions'])
#             workouts.append(new_workout)
#             db.session.add(new_workout)
#     for x in query_by_muscle:
#         workouts_by_type= fetch_api_workouts(query_type="muscle", query=x)
#         for workout in  workouts_by_type:
#             new_workout = Workout(name=workout['name'].title(), type=workout['type'], muscle=workout['muscle'], equipment=workout['equipment'], difficulty=workout['difficulty'], instructions=workout['instructions'])
#             workouts.append(new_workout)
#             db.session.add(new_workout)
#     for x in query_by_difficulty:
#         workouts_by_type= fetch_api_workouts(query_type="difficulty", query=x)
#         for workout in  workouts_by_type:
#             new_workout = Workout(name=workout['name'].title(), type=workout['type'], muscle=workout['muscle'], equipment=workout['equipment'], difficulty=workout['difficulty'], instructions=workout['instructions'])
#             workouts.append(new_workout)
#             db.session.add(new_workout)
#     db.session.commit()
#     return workouts


def cache_api_workouts():
    query_type = ["type", "muscle", "difficulty"]
    query_by_type = ["cardio", "plyometrics", "strength","stretching","strongman","powerlifting"]
    query_by_muscle = ["abdominals", "biceps", "chest","glutes","quadriceps","lower_back","abductors","calves", "hamstrings"]
    query_by_difficulty = ["beginner", "intermediate", "expert"]
    workouts = set()
    for x in query_by_type:
        workouts_by_type = fetch_api_workouts(query_type="type", query=x)
        for workout in workouts_by_type:
            name = workout['name'].title()
            if name not in workouts:
                new_workout = Workout(name=name, type=workout['type'], muscle=workout['muscle'], equipment=workout['equipment'], difficulty=workout['difficulty'], instructions=workout['instructions'])
                workouts.add(name)
                db.session.add(new_workout)
    for x in query_by_muscle:
        workouts_by_type= fetch_api_workouts(query_type="muscle", query=x)
        for workout in workouts_by_type:
            name = workout['name'].title()
            if name not in workouts:
                new_workout = Workout(name=name, type=workout['type'], muscle=workout['muscle'], equipment=workout['equipment'], difficulty=workout['difficulty'], instructions=workout['instructions'])
                workouts.add(name)
                db.session.add(new_workout)
    for x in query_by_difficulty:
        workouts_by_type= fetch_api_workouts(query_type="difficulty", query=x)
        for workout in workouts_by_type:
            name = workout['name'].title()
            if name not in workouts:
                new_workout = Workout(name=name, type=workout['type'], muscle=workout['muscle'], equipment=workout['equipment'], difficulty=workout['difficulty'], instructions=workout['instructions'])
                workouts.add(name)
                db.session.add(new_workout)
    db.session.commit()
    return workouts

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

def get_all_workouts1(muscle=None, workout_type=None, difficulty=None, page=1):
    query = Workout.query

    # Filter by muscle group if provided
    if muscle:
        query = query.filter_by(muscle=muscle)

    # Filter by workout type if provided
    if workout_type:
        query = query.filter_by(type=workout_type)

    # Filter by difficulty level if provided
    if difficulty:
        query = query.filter_by(difficulty=difficulty)

    # Paginate the results
    workouts = query.paginate(page=page, per_page=10)

    return workouts

def get_workout_by_id(workoutId):
    return Workout.query.get(workoutId)