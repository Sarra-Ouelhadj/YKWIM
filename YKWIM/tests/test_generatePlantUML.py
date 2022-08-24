from YKWIM import app, generatePlantUML as pl
import json

def test_generatePlantUML():
    with open(app.config["UPLOAD_FOLDER"]+"parsing_result_original.json") as json_file:
        d=json.load(json_file)
    assert pl.generatePlantUML(d)
