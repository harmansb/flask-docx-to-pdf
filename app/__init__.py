from flask import Flask

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "app/uploads/"
app.config["SECRET_KEY"] = "your_secret_key"

# Ensure the uploads directory exists
import os
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

from app import routes
