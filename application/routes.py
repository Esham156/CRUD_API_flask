from application import app
from flask import jsonify

@app.route('/')
def hello():
    return jsonify({
        "message": "Welcome",
        "description": "Pokemons API",
        "endpoints": {
            "trainers" : [
            "GET /",
            "GET /trainers",
            "GET /trainers/<int:id>",
            "POST /trainers",
            "PATCH /trainers/<int:id>",
            "DELETE /trainers/<int:id>"],
            
            
            "pokemons" : 
            [
            "GET /pokemons",
            "GET /pokemons/<int:id>",
            "POST /pokemons",
            "PATCH /pokemons/<int:id>",
            "DELETE /pokemons/<int:id>"
                ]
            }
        
    }), 200