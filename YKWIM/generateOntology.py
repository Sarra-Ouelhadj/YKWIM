from YKWIM import helpers as h
import json
from YKWIM import app
from rdflib.namespace import RDF, RDFS, OWL, SKOS
from rdflib import Graph, Literal, URIRef, Namespace

def generateOntology(path=app.config["UPLOAD_FOLDER"],ontology_namespace = "https://data.grandlyon.com/onto/",vocabulary_namespace ="https://data.grandlyon.com/vocab/"):
    """generate ontology files from JSON"""
    f=open(path + "parsing_result.json")

    VS = Namespace("http://www.w3.org/2003/06/sw-vocab-status/ns#")
    d=json.load(f)
    g = Graph()
    g2 = Graph ()
    
    #------------------------
    #Classes
    #------------------------
    for cl in filter (lambda value: False if value["IRI"]!='' else True,d["classes"]):
        classeURI = URIRef(ontology_namespace + h.convertToPascalcase(cl["name"]))

        #update json file 
        list_of_all_values = [elem["name"] for elem in d["classes"]]
        index= list_of_all_values.index(cl["name"])
        d["classes"][index]["IRI"]=str(classeURI)
        
        g.add((classeURI,RDF.type, OWL.Class))    
        g.add((classeURI,RDFS.label, Literal(cl["name"])))
        g.add((classeURI,RDFS.comment, Literal(cl["definition"])))
        g.add((classeURI,RDFS.isDefinedBy, URIRef(ontology_namespace)))
        g.add((classeURI,VS.term_status, Literal("testing")))

    #------------------------
    #Data Properties
    #------------------------
    for cl in d["classes"]:
        for attr in filter (lambda value: False if value["IRI"]!='' else True,cl["attributes"]):
            attributeURI = URIRef(ontology_namespace + h.convertToCamelcase(attr["name"]))

            #update json file
            list_of_all_values1 = [elem["name"] for elem in d["classes"]]
            index1= list_of_all_values1.index(cl["name"])
            
            list_of_all_values2 = [elem["name"] for elem in d["classes"][index1]["attributes"]]
            index2= list_of_all_values2.index(attr["name"])
            d["classes"][index1]["attributes"][index2]["IRI"]=str(attributeURI)

            g.add((attributeURI,RDF.type, OWL.DatatypeProperty))    
            g.add((attributeURI,RDFS.label, Literal(attr["name"])))
            g.add((attributeURI,RDFS.comment, Literal(attr["definition"])))
            g.add((attributeURI,RDFS.isDefinedBy, URIRef(ontology_namespace)))
            g.add((attributeURI,VS.term_status, Literal("testing")))

    #------------------------
    #Object Properties
    #------------------------
    for ass in filter (lambda value: False if value["IRI"]!='' else True,d["associations"]):
        associationURI = URIRef(ontology_namespace + h.convertToCamelcase(ass["name"]))

        #update json file
        list_of_all_values = [elem["name"] for elem in d["associations"]]
        index= list_of_all_values.index(ass["name"])
        d["associations"][index]["IRI"]=str(associationURI)
        
        g.add((associationURI,RDF.type, OWL.ObjectProperty))    
        g.add((associationURI,RDFS.label, Literal(ass["name"])))
        g.add((associationURI,RDFS.comment, Literal(ass["definition"])))
        g.add((associationURI,RDFS.isDefinedBy, URIRef(ontology_namespace)))
        g.add((associationURI,VS.term_status, Literal("testing")))

    #------------------------
    #Individuals
    #------------------------
    index = None
    for enum in d["enumerations"]:
        if enum["IRI"]!="":
            enumerationURI = URIRef(enum["IRI"])
        else :
            enumerationURI = URIRef(vocabulary_namespace + h.convertToPascalcase(enum["name"]))

            #update json file
            list_of_all_values = [elem["name"] for elem in d["enumerations"]]
            index= list_of_all_values.index(enum["name"])
            d["enumerations"][index]["IRI"]=str(enumerationURI)

            g2.add((enumerationURI, RDF.type, SKOS.ConceptScheme))
            g2.add((enumerationURI,SKOS.prefLabel, Literal(enum["name"])))
            g2.add((enumerationURI,SKOS.definition, Literal(enum["definition"])))
            g2.add((enumerationURI,RDFS.isDefinedBy, URIRef(vocabulary_namespace)))
            g2.add((enumerationURI,VS.term_status, Literal("testing")))
            
        for val in filter(lambda value: False if value["IRI"]!="" else True, enum["values"]):     
            valueURI = URIRef(vocabulary_namespace + h.convertToSnakecase(val["name"]))

            if index!=None : #previous creation of an enumeration URI, the index is already known
                list_of_all_values2 = [elem["name"] for elem in d["enumerations"][index]["values"]]
                index2= list_of_all_values2.index(val["name"])
                d["enumerations"][index]["values"][index2]["IRI"]=str(valueURI)
            else :
                list_of_all_values = [elem["name"] for elem in d["enumerations"]]
                index= list_of_all_values.index(enum["name"])
                
                list_of_all_values2 = [elem["name"] for elem in d["enumerations"][index]["values"]]
                index2= list_of_all_values2.index(val["name"])
                d["enumerations"][index]["values"][index2]["IRI"]=str(valueURI)

            g2.add((valueURI,RDF.type, SKOS.Concept))    
            g2.add((valueURI,SKOS.prefLabel, Literal(val["name"])))
            g2.add((valueURI,SKOS.definition, Literal(val["definition"])))
            g2.add((valueURI,RDFS.isDefinedBy, URIRef(vocabulary_namespace)))
            g2.add((valueURI,SKOS.inScheme, enumerationURI))
            g2.add((valueURI,VS.term_status, Literal("testing")))

    ontology_path = path + "ontology.ttl"
    vocabulary_path = path + "vocabulary.ttl"
    json_path = path + "parsing_result_completed.json"
    with open(ontology_path, 'w') as fo, open(vocabulary_path, 'w') as fv, open(json_path, 'w') as fp :
        fo.write(g.serialize(format="turtle"))
        fv.write(g2.serialize(format="turtle"))
        json.dump(d,fp)
    
    return g.serialize(format="turtle") + g2.serialize(format="turtle")
    
