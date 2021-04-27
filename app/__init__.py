from flask import Flask
from app.config import Config

app = Flask(__name__)

app.config.from_object(Config)
app.config ['UPLOAD_FOLDER'] = './app/static/uploads'

from app import views
