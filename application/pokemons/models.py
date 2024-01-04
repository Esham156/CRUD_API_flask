from application import db, app

app.app_context().push()

class Pokemon(db.Model):
    __tablename__ = "Pokemons"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    attack = db.Column(db.String(100), nullable=False)

    def __init__(self, name, type, attack):
        self.name = name
        self.type = type
        self.attack = attack

    def __repr__(self):
        return f"Pokemon(id: {self.id}, name: {self.name})"
    
    @property
    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "attack": self.attack
        }