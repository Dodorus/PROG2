from datetime import datetime
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