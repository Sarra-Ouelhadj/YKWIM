# Dataset_URL = "https://download.data.grandlyon.com/wfs/grandlyon?SERVICE=WFS&VERSION=2.0.0&request=GetFeature&typename=adr_voie_lieu.adrcomgl&outputFormat=application/json;%20subtype=geojson&SRSNAME=EPSG:4171"

class Config(object):
    DEBUG = False
    TESTING = False
    UPLOAD_FOLDER = ""

class ProductionConfig(Config):
    pass

class DevelopementConfig(Config):
    DEBUG = True
    UPLOAD_FOLDER = "/home/sarra/Documents/Doctorat/Python/SemanticLifting/YKWIM/results/"

class TestingConfig(Config):
    TESTING = True
    UPLOAD_FOLDER = "/home/sarra/Documents/Doctorat/Python/SemanticLifting/YKWIM/tests/results/"
