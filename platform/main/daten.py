from datetime import datetime
from main import app
import secrets
import os
from PIL import Image
import wtforms_json
import json

def load_values():
    datei_json = "rezepte_data.json"

    try:
        with open(datei_json) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt

def save_pictures(from_picture):
	random = secrets.token_hex(8)
	_, b_ext = os.path.splitext(from_picture.filename)
	picture_fn = random + b_ext
	picture_path = os.path.join(app.root_path, 'static/img/rzp_images', picture_fn)
	
	#resize someting goes wrong here
	output_size = (500, 500)
	i = Image.open(from_picture)
	i.thumbnail(output_size)
	i.save(picture_path)

	return picture_fn
