# Flask Pokemon CRUD API

This Flask CRUD API manages Pokémon information, allowing users to perform CRUD operations on Pokémon data, including their name, type, and attack.

## Features
Create: Add new Pokémon/new Trainer data to the database.
Read: Retrieve existing Pokémon/Trainer data from the database.
Update: Modify existing Pokémon/Trainer data in the database.
Delete: Remove Pokémon/Trainer data from the database.

## Setup

### Prerequisites

- python3 installed
- pipenv

### Installation

run the following command to install and navigate to the api directory

```bash 
git clone git@github.com:Esham156/CRUD_API_flask.git && cd $_
```

start the virtual environment:
```bash
pipenv shell
```
install dependencies:
```bash
pipenv install
```
you can exit the virtual environment by typing:
```bash
exit
```
create a dotenv file:
```bash
echo -e "FLASK_DEBUG=1\nSQLALCHEMY_DATABASE_URI='\connection_string\'" > .env
```
replace 'connection_string' with the one from your database.

to run the API, run the following command:
```bash
flask run
```
## API Endpoints
| Method | Endpoint                             |Description                            |
| ------ | ------------------------------------ | -------------------------------------- |
| POST   | `/pokemons`                       | Create a new Pokémon entry.             |
| GET    | `/pokemons`                       | Retrieve all Pokémon entries.           |
| GET    | `/pokemons/<pokemon_id>`          | Retrieve a specific Pokémon entry by its index. |
| PUT    | `/pokemons/<pokemon_id>`          | Update a specific Pokémon entry.        |
| DELETE | `/pokemons/<pokemon_id>`          | Delete a specific Pokémon entry.        |
| POST   | `/trainers`                       | Create a new Trainer entry.             |
| GET    | `/trainers`                       | Retrieve all Trainer entries.           |
| GET    | `/trainers/<trainer_id>`          | Retrieve a specific Trainer entry by its index. |
| PUT    | `/trainers/<trainer_id>`          | Update a specific Trainer entry.        |
| DELETE | `/trainers/<trainer_id>`          | Delete a specific Trainer entry.        |


## Payload Format
When sending POST or PUT requests to create or update Pokémon entries, use the following JSON format :
pokemon:
```json
{
  "name": "Pikachu",
  "type": "Electric",
  "attack": "Thunderbolt",
  "trainer" : 1
}
```
trainer:
```json
{
  "name":
}
```