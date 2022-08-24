from YKWIM import app, generateJSON as g

def test_generateJSON():
    assert g.generateJSON(app.config["UPLOAD_FOLDER"]+"template.ods")
     