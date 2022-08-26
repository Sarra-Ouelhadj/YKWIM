from YKWIM import app, plantUML2Image as pl
from flask import render_template, request, url_for, send_from_directory, redirect
from werkzeug.utils import secure_filename
import os

@app.route("/",methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        datasetURL=request.form["datasetURL"]
        file = request.files["templateFile"]
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
        uml_image = pl.plantUML2Image(app.config['UPLOAD_FOLDER']+secure_filename(file.filename), "svg")
        return render_template("index.html", uml_image=url_for('getDocumentLink',document_link=uml_image))
    else:            
        return render_template("index.html")


@app.route("/<document_link>")
def getDocumentLink(document_link):
    return redirect("/tmp/"+document_link)
    #send_from_directory(app.config['UPLOAD_FOLDER'],document_link)
