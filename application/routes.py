from application import app
from flask import jsonify

@app.route('/')
def hello():
    return jsonify({
        "message": "Welcome",
        "description": "Pokemons API",
        "endpoints": [
            "GET /",
            "GET /pokemons",
            "GET /pokemons/<int:id>",
            "POST /pokemons",
            "PATCH /pokemons/<int:id>",
            "DELETE /pokemons/<int:id>"
        ]
    }), 200