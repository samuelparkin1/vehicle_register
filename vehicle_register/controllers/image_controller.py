from flask import Blueprint, request, redirect, abort, url_for, current_app
from pathlib import Path
from models.vehicles import Vehicle
import boto3


vehicle_images = Blueprint('vehicle_images', __name__)

@vehicle_images.route("/vehicles/<int:id>/image/", methods=["POST"])
def update_image(id):
    vehicle=Vehicle.query.get_or_404(id)
    if "image" in request.files:
        image = request.files["image"]
        if Path(image.filename).suffix != ".png":
            return abort(400, description="Invalid file type")
 
        bucket = boto3.resource("s3").Bucket(current_app.config["AWS_S3_BUCKET"])
        bucket.upload_fileobj(image, vehicle.image_filename)

        # note that we have removed this line:
        # image.save(f"static/{vehicle.image_filename}")


        return redirect(url_for("vehicles.get_vehicle", id=id))
    return abort(400, description="No image")