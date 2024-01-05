from application import db, app

app.app_context().push()

class Trainer(db.Model):
    __tablename__ = "Trainers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Trainer(id: {self.id}, name: {self.name})"
    
    @property
    def json(self):
        return {
            "id": self.id,
            "name": self.name,
        }