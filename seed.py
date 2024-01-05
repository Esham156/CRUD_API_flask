from application import db
from application.pokemons.model import Pokemon
from application.trainers.model import Trainer

db.drop_all()

db.create_all()

entry1 = Trainer(name= "Ash Ketchum")

entry2 = Trainer(name= "Brock")

entry3 = Trainer(name= "Misty")

entry4 = Pokemon(name = "Pikachu", pokemon_type= "Electric", attack = "Thunderbolt", trainer_id = 1)
entry5 = Pokemon(name = "Charizard", pokemon_type= "Fire/Flying", attack = "Flamethrower", trainer_id = 1)
entry6 = Pokemon(name = "Bulbasaur", pokemon_type= "Grass/Poison", attack = "Vine Whip", trainer_id = 3 )
entry7 = Pokemon(name = "Squirtle", pokemon_type = "Water", attack = "Water Gun", trainer_id = 3)

    
    
    
    


db.session.add_all([entry1, entry2, entry3, entry4, entry5, entry6, entry7])

db.session.commit()