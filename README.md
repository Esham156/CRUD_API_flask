# Flask Pokemon CRUD API

This Flask CRUD API manages Pokémon information, allowing users to perform CRUD operations on Pokémon data, including their name, type, and attack.

## Features
Create: Add new Pokémon data to the database.
Read: Retrieve existing Pokémon data from the database.
Update: Modify existing Pokémon data in the database.
Delete: Remove Pokémon data from the database.

## Setup

### Prerequisites

- python3 installed
- pipenv

### Installation

run the following command to install and navigate to the api directory

```bash 
git clone "" && cd $_
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
| POST   | `/api/pokemon`                       | Create a new Pokémon entry.             |
| GET    | `/api/pokemon`                       | Retrieve all Pokémon entries.           |
| GET    | `/api/pokemon/<pokemon_id>`          | Retrieve a specific Pokémon entry by its index. |
| PUT    | `/api/pokemon/<pokemon_id>`          | Update a specific Pokémon entry.        |
| DELETE | `/api/pokemon/<pokemon_id>`          | Delete a specific Pokémon entry.        |


## Payload Format
When sending POST or PUT requests to create or update Pokémon entries, use the following JSON format :
```json
{
  "name": "Pikachu",
  "type": "Electric",
  "attack": "Thunderbolt"
}

```