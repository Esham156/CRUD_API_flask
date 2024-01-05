from application import db, app
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

app.app_context().push()

class Pokemon(db.Model):
    __tablename__ = "Pokemons"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    pokemon_type = db.Column(db.String(100), nullable=False)
    attack = db.Column(db.String(100), nullable=False)
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainers.id'), nullable=False)

    trainer = relationship("Trainer", back_populates="pokemons")

    def __init__(self, name, pokemon_type, attack):
        self.name = name
        self.pokemon_type = pokemon_type
        self.attack = attack

    def __repr__(self):
        return f"Pokemon(id: {self.id}, name: {self.name})"
    
    @property
    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "pokemon_type": self.pokemon_type,
            "attack": self.attack
        }