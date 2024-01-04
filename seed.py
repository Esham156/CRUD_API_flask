from application import db
from application.pokemons.models import Pokemon

db.drop_all()
print("Dropping Database")

db.create_all()
print("Creating Database")

print("Seeding Database")
entry1 = Pokemon(name="Pikachu", type="Electric", attack="Thunderbolt")

entry2 = Pokemon(name="Charizard", type="Fire/Flying", attack="Flamethrower")

entry3 = Pokemon(name="Bulbasaur", type="Grass/Poison", attack="Vine Whip")

entry4 = Pokemon(name="Squirtle", type="Water", attack="Water Gun")


db.session.add_all([entry1, entry2, entry3, entry4])

db.session.commit()