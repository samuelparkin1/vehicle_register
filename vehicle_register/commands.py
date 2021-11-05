from main import db
from flask import Blueprint

db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables created!")

@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables deleted")

@db_commands.cli.command("seed")
def seed_db():
    from models.vehicles import Vehicle
    from faker import Faker
    faker = Faker()

    for i in range(10):
        vehicle = Vehicle (faker.catch_phrase())
        db.session.add(vehicle)
    
    db.session.commit()
    print("Tables seeded")

@db_commands.cli.command("reset")
def reset_db():
    """ DROPS CREATES AND SEEDS TABLE"""
    db.drop_all()
    print("Tables deleted")

    db.create_all()
    print("Tables created!")

    from models.vehicles import Vehicle
    from faker import Faker
    faker = Faker()

    for i in range(20):
        vehicle = Vehicle (faker.catch_phrase())
        db.session.add(vehicle)
    
    db.session.commit()
    print("Tables seeded")

