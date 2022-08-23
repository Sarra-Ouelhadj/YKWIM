from YKWIM import app, generateJSON as g
from YKWIM import generatePlantUML as pl
import subprocess
import uuid
import os

def plantUML2Image(file, image_type="png", path=app.config["UPLOAD_FOLDER"]):
    """generate UML diagram image (.png or .svg) from template"""

    d= pl.generatePlantUML(g.generateJSON(file))
    base_name = str(uuid.uuid4())
    uml_path = path + base_name + ".uml"
    with open(uml_path, 'w') as fp:
        fp.write(d)

    if image_type=="svg":
        subprocess.run('java -jar ./YKWIM/static/jar/plantuml*.jar -tsvg ' + uml_path, shell=True) #convert PlantUML file to svg image
        output = base_name+'.svg'
    else : 
        subprocess.run('java -jar ./YKWIM/static/jar/plantuml*.jar ' + uml_path, shell=True) #convert PlantUML file to png image
        output = base_name+'.png'

    os.remove(uml_path) #remove PlantUML file and keep image only
    return output
