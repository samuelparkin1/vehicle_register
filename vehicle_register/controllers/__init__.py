# Imports the controllers as a Blueprint.
from controllers.vehicle_controller import vehicles
from controllers.staff_controller import staff
from controllers.user_controller import users


# The registerable_controllers list are imported into the create_app function within main.py.
# Adding all controller to registerable_controllers list will ensure they're included.
registerable_controllers = [vehicles, staff, users]