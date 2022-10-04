from YKWIM import app, helpers as h
import json

def generateSparqlGenerateQuery (dataset,path=app.config["UPLOAD_FOLDER"],vocabulary_namespace ="https://data.grandlyon.com/vocab/", instances_namespace = "https://data.grandlyon.com/id/") :
    """generate SPARQL Generate query"""

    s = """PREFIX iter: <http://w3id.org/sparql-generate/iter/>
    PREFIX fun: <http://w3id.org/sparql-generate/fn/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    GENERATE {\n"""

    f=open(path + "parsing_result_completed.json")
    d=json.load(f)
    
    #iterate over classes
    for list in d["classes"]:
        s+=("?{} a <{}>".format(h.convertToPascalcase(list["name"]),list["IRI"]))+ ";\n"

        #iterate over attributes
        l=len(list["attributes"])
        for i , attr in enumerate(list["attributes"]):
            s+=("\t<{}> ?{}".format(attr["IRI"],h.convertToPascalcase(attr["name"])))
            s+=";\n" if (i<l-1) else ".\n"
    
    #iterate over associations
    for list in d["associations"]:
        s += ("?{} <{}> ?{}".format(h.convertToPascalcase(list["source"]),list["IRI"],h.convertToPascalcase(list["destination"]))) + ".\n"
    
    s+=("}} \n SOURCE <{}> AS ?source \nITERATOR iter:GeoJSON(?source) AS ?geometricCoordinates ?properties \n WHERE {{\n".format(dataset))

    #bindings
    for list in d["classes"]:
        for attr in list["attributes"]:
            s+=('BIND (fun:JSONPath(?properties,"$.{}") AS ?{})\n'.format(attr["source"], h.convertToPascalcase(attr["name"]))) 
            if (attr["id"]=="oui") :
                s+=('BIND(IRI(CONCAT("{}/",fun:JSONPath(?properties,"$.{}"))) AS ?{})\n'.format(instances_namespace+ h.convertToPascalcase(list["name"]),attr["source"],h.convertToPascalcase(list["name"])))
        
    for enum in d["enumerations"]:
        s+=('BIND(IRI(CONCAT("{}",REPLACE(LCASE(fun:JSONPath(?properties,"$.{}"))," ","_"))) AS ?{})\n'.format(vocabulary_namespace,enum["source"],h.convertToPascalcase(enum["name"])))
    
    s+= "}\n"
    query_path = "query.rq"
    with open(query_path, 'w') as fp:
        fp.write(s)
    return query_path