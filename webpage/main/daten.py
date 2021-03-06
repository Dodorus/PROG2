#import aller pakete
from datetime import datetime
from main import app
import os
from PIL import Image
import wtforms_json
import json
from os import urandom
#import fertig

#funktion um daten aus dem json zu laden, wird ab Version 2 des Apps nicht mehr genutzt, da Mongo DB verwendet wird
def load_values():
    datei_json = "rezepte_data.json"

    try:
        with open(datei_json) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}


    return datei_inhalt


def load_json(json_path):
    try:
        with open(json_path) as open_file:
            user_data = json.load(open_file)
    except FileNotFoundError:
        user_data = {}

    return user_data

def update_json(json_path_up, user_data_up):
    with open(json_path_up, "w") as jsonFile:
        json.dump(user_data_up, jsonFile)

def save_json(json_path, user_data):
    with open(json_path, "w", encoding="utf-8") as open_file:
        json.dump(user_data, open_file, indent=4)

#funktion im bilder beim upload zu speichern
def save_pictures(from_picture):
	random = urandom(8).hex()
	_, b_ext = os.path.splitext(from_picture.filename)
	picture_fn = random + b_ext
	picture_path = os.path.join(app.root_path, 'static/img/rzp_images', picture_fn)

	#print("da gehts nicht weiter")
	output_size = (500, 500)
	i = Image.open(from_picture)
	i.thumbnail(output_size)
	i.save(picture_path)

	return picture_fn
