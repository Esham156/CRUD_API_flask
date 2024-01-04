from application import app ## app from __init__.py
from application.pokemons import routes
from application import routes

if __name__ == "__main__":
    app.run(port=4000, debug=True)