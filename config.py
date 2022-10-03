# Dataset_URL = "https://download.data.grandlyon.com/wfs/grandlyon?SERVICE=WFS&VERSION=2.0.0&request=GetFeature&typename=adr_voie_lieu.adrcomgl&outputFormat=application/json;%20subtype=geojson&SRSNAME=EPSG:4171"
import os

MYDIR = os.getcwd()

class Config(object):
    DEBUG = False
    TESTING = False
    UPLOAD_FOLDER = ""
    ONTOLOGY_NAMESPACE = "https://data.grandlyon.com/onto/"
    VOCABULARY_NAMESPACE ="https://data.grandlyon.com/vocab/"
    INSTANCES_NAMESPACE = "https://data.grandlyon.com/id/"

class ProductionConfig(Config):
    UPLOAD_FOLDER = MYDIR + "/tmp/"

class DevelopmentConfig(Config):
    DEBUG = True
    UPLOAD_FOLDER = MYDIR+"/YKWIM/results/"

class TestingConfig(Config):
    TESTING = True
    UPLOAD_FOLDER = MYDIR+"/YKWIM/tests/results/"
    