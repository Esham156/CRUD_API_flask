from flask import jsonify, request
from werkzeug import exceptions
from .models import Pokemon
from .. import db


def index():
    pokemons = Pokemon.query.all()
    try:
        return jsonify({ "data": [c.json for c in pokemons] }), 200
    except:
        raise exceptions.InternalServerError(f"We are working on it")

def show(id):
    print("id", type(id))
    pokemon = Pokemon.query.filter_by(id=id).first()
    try:
        return jsonify({ "data": pokemon.json }), 200
    except:
        raise exceptions.NotFound(f"You get it")


def create():
    try:
        name, type, attack = request.json.values()

        new_pokemon = Pokemon(name, type, attack)

        db.session.add(new_pokemon)
        db.session.commit()

        return jsonify({ "data": new_pokemon.json }), 201
    except:
        raise exceptions.BadRequest(f"We cannot process your request")

def update(id):
    data = request.json
    pokemon = Pokemon.query.filter_by(id=id).first()

    for (attribute, value) in data.items():
        if hasattr(pokemon, attribute):
            setattr(pokemon, attribute, value)

    db.session.commit()
    return jsonify({ "data": pokemon.json })

def destroy(id):
    pokemon = Pokemon.query.filter_by(id=id).first()
    db.session.delete(pokemon)
    db.session.commit()
    return "Pokemon Deleted", 204