import subprocess
from YKWIM import app, generateSparqlGenerateQuery as q, generateOntology as onto

def generateRDF (dataset, path=app.config["UPLOAD_FOLDER"],ontology_namespace = "https://data.grandlyon.com/onto/", vocabulary_namespace ="https://data.grandlyon.com/vocab/", instances_namespace = "https://data.grandlyon.com/id/") :
    """generate RDF data from SPARQL Generate query"""

    onto.generateOntology(path, ontology_namespace,vocabulary_namespace)
    query_file=q.generateSparqlGenerateQuery(dataset, path,vocabulary_namespace, instances_namespace)

    result_file = "instances.ttl"
    subprocess.run('java -jar ./YKWIM/static/jar/sparql-generate*.jar --query-file '+ query_file+' --output '+result_file, shell=True)
    return result_file