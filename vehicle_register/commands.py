from main import db
from flask import Blueprint

db_commands = Blueprint("db-custom", __name__)

@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables created!")

@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    db.engine.execute("DROP TABLE IF EXISTS alembic_version;")
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
    db.engine.execute("DROP TABLE IF EXISTS alembic_version;")
    db.create_all()
    print("Tables created!")

    from models.vehicles import Vehicle
    from models.staff import Staff
    from faker import Faker
    faker = Faker(['en_AU'])

    for i in range(20):
        vehicle = Vehicle (faker.license_plate())
        db.session.add(vehicle)
        
    for i in range(20):
        staff = Staff (faker.name())
        db.session.add (staff)
    
    
    db.session.commit()
    print("Tables seeded")

