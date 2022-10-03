from YKWIM import app, plantUML2Image as pl, validateTemplate as val, generateOntology as onto, generateSparqlGenerateQuery as sq, generateRDF as rdf
from flask import render_template, request, send_from_directory
from werkzeug.utils import secure_filename
import os

@app.route("/",methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        datasetURL=request.form["datasetURL"].replace(' ','%20')
        file = request.files["templateFile"]
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
        error_template = val.validateTemplate(app.config['UPLOAD_FOLDER']+secure_filename(file.filename))
        if error_template == None :
            uml_image = pl.plantUML2Image(app.config['UPLOAD_FOLDER']+secure_filename(file.filename),"svg")
            rdf.generateRDF(datasetURL)
            
            return render_template("index.html", uml_image=uml_image)
            
        else: 
            return render_template("index.html", error_template=error_template)
    else:            
        return render_template("index.html", vocabulary_namespace= app.config['VOCABULARY_NAMESPACE'], 
                                            ontology_namespace=app.config['ONTOLOGY_NAMESPACE'],
                                            instances_namespace=app.config['INSTANCES_NAMESPACE']
                                            )


@app.route("/<document_link>")
def getDocumentLink(document_link):
    return send_from_directory(app.config['UPLOAD_FOLDER'],document_link)
