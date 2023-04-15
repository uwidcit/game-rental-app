from .auth import auth_views
from .allworkouts import allworkouts_views
from .myworkouts import myworkouts_views
from .workout import workout_views

views = [
    workout_views,
    myworkouts_views,
    allworkouts_views,
    auth_views
]