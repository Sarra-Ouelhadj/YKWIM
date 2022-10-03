import subprocess
#from YKWIM import generateJSON as g
#import generateSparqlGenerateQuery as q, generateOntology as onto

def generateRDF (path="./",ontology_namespace = "https://data.grandlyon.com/onto/", vocabulary_namespace ="https://data.grandlyon.com/vocab/", instances_namespace = "https://data.grandlyon.com/id/") :
    """generate RDF data from SPARQL Generate query"""
    #g.generateJSON(file, path)
    #onto.generateOntology(path, ontology_namespace,vocabulary_namespace)
    query_file="query.rq"

    result_file = path + "instances.ttl"
    subprocess.run('java -jar sparql-generate*.jar --query-file '+ query_file+' --output '+result_file, shell=True)
    
    return result_file

print(generateRDF())