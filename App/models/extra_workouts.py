from App.database import db

class ExtraWorkout(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    bodyPart = db.Column(db.String(20), nullable=False)
    equipment =db.Column(db.String(20), nullable=False)
    gifUrl = db.Column(db.String(50), nullable=False)        
    target = db.Column(db.String(20), nullable=False)

    def __init__(self, name, bodyPart, equipment, gifUrl, target):
        self.name = name
        self.bodyPart = bodyPart
        self.equipment = equipment
        self.gifUrl = gifUrl
        self.target = target
      

    def __repr__(self):
        return f'<Workout {self.id} - {self.name} - {self.target}>' 

    def toJSON(self):
        return {
            'id': self.id,            
            'name': self.name,
            'bodyPart' : self.bodyPart,
            'equipment': self.equipment,
            'gifUrl': self.gifUrl,
            'target': self.target  
        }

