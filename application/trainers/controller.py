from flask import jsonify, request
from werkzeug import exceptions
from .model import Trainer
from .. import db


def index():
    trainers = Trainer.query.all()
    try:
        return jsonify({ "data": [c.json for c in trainers] }), 200
    except:
        raise exceptions.InternalServerError(f"We are working on it")

def show(id):
    trainer = Trainer.query.filter_by(id=id).first()
    try:
        return jsonify({ "data": trainer.json }), 200
    except:
        raise exceptions.NotFound(f"You get it")


def create():
    try:
        name = request.json.values()

        new_trainer = Trainer(name)

        db.session.add(new_trainer)
        db.session.commit()

        return jsonify({ "data": new_trainer.json }), 201
    except:
        raise exceptions.BadRequest(f"We cannot process your request")

def update(id):
    data = request.json
    trainer = Trainer.query.filter_by(id=id).first()

    for (attribute, value) in data.items():
        if hasattr(trainer, attribute):
            setattr(trainer, attribute, value)

    db.session.commit()
    return jsonify({ "data": trainer.json })

def destroy(id):
    trainer = Trainer.query.filter_by(id=id).first()
    db.session.delete(trainer)
    db.session.commit()
    return "Trainer Deleted", 204