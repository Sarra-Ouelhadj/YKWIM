##### to review completly
import sys
import subprocess
import generateJSON as g
import uuid
import os

def generateSparqlGenerateQuery (d, dataset) :
    """generate SPARQL Generate query"""

    s = """PREFIX iter: <http://w3id.org/sparql-generate/iter/>
    PREFIX fun: <http://w3id.org/sparql-generate/fn/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    GENERATE {\n"""

    #iterate over classes
    for list in d["classes"]:
        if (list["IRI"]!=""):
            s+=("?{} a <{}>".format(list["name"],list["IRI"]))+ ";\n"
        else: s+=("?{} a <http://data.grandlyon.com/ontology/{}".format(list["name"],list["name"]))+ ">;\n"
        
        #iterate over attributes
        l=len(list["attributes"])
        for i , attr in enumerate(list["attributes"]):
            if (attr["IRI"]!=""):
                s+=("\t<{}> ?{}".format(attr["IRI"],attr["name"]))
            else: s+=("\t<http://data.grandlyon.com/ontology/{}> ?{}".format(attr["name"],attr["name"]))
            s+=";\n" if (i<l-1) else ".\n"
    
    #iterate over associations
    for list in d["associations"]:
        if (list["IRI"]!=""):
            s += ("?{} <{}> ?{}".format(list["source"],list["IRI"],list["destination"])) + ".\n"
        else : s += ("?{} <http://data.grandlyon.com/ontology/{}> ?{}".format(list["source"],list["name"],list["destination"])) + ".\n"
    
    #iterate over enumerations
    for list in d["enumerations"]:
        if (list["IRI"]!=""):
            s+=("?{} a <{}>".format(list["name"],list["IRI"]))+ ".\n"
        else: s+=("?{} a <http://data.grandlyon.com/vocabulary/{}".format(list["name"],list["name"]))+ ">.\n"
    
    s+=("}} \n SOURCE <{}> AS ?source \nITERATOR iter:GeoJSON(?source) AS ?geometricCoordinates ?properties \n WHERE {{\n".format(dataset))

    #bindings
    for list in d["classes"]:
        for attr in list["attributes"]:
            s+=('BIND (fun:JSONPath(?properties,"$.{}") AS ?{})\n'.format(attr["source"], attr["name"])) 
            if (attr["id"]=="oui") :
                s+=('BIND(IRI(CONCAT("http://data.grandlyon.com/id/{}/",fun:JSONPath(?properties,"$.{}"))) AS ?{})\n'.format(list["name"],attr["source"],list["name"]))
    
    for enum in d["enumerations"]:
        s+=('BIND(IRI("http://data.grandlyon.com/vocabulary/Cadres_administratifs") AS ?{})\n'.format(enum["name"]))
    
    s+= "}\n"
    base_name = "query_"+str(uuid.uuid4())
    query_path = base_name + ".rq"
    with open(query_path, 'w') as fp:
        fp.write(s) 
    return query_path

if __name__ == "__main__":
    #dataset = "https://download.data.grandlyon.com/wfs/grandlyon?SERVICE=WFS&VERSION=2.0.0&request=GetFeature&typename=adr_voie_lieu.adrcomgl&outputFormat=application/json;%20subtype=geojson&SRSNAME=EPSG:4171"
    print (generateSparqlGenerateQuery(g.generateJSON(sys.argv[1]), sys.argv[2]))