##### to review completly
import sys
import subprocess
import generateJSON as g
import generateSparqlGenerateQuery as q
import uuid
import os

def generateRDF (file, dataset) :
    """generate RDF data from SPARQL Generate query"""

    query_file=q.generateSparqlGenerateQuery(g.generateJSON(file),dataset)
    base_name = str(uuid.uuid4())
    result_file = base_name + ".ttl"
    subprocess.run('java -jar sparql-generate*.jar --query-file '+ query_file+' --output '+result_file, shell=True)
    
    return result_file

if __name__ == "__main__":
    #dataset = "https://download.data.grandlyon.com/wfs/grandlyon?SERVICE=WFS&VERSION=2.0.0&request=GetFeature&typename=adr_voie_lieu.adrcomgl&outputFormat=application/json;%20subtype=geojson&SRSNAME=EPSG:4171"
    print (generateRDF(sys.argv[1], sys.argv[2]))