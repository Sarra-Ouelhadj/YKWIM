import pyexcel as p
import sys
import json
from YKWIM import app

def generateJSON(file, path=app.config["UPLOAD_FOLDER"]):
    """generate JSON from template"""
    book=p.get_book_dict(file_name=file)
    
    #classes sheet parsing
    list=[]
    d={}
    for cl in filter(lambda value:True if value[0]!='' else False,book["Classes"][1:]): 
        element={}
        element["name"]= cl[0]
        element["definition"]= cl[2]
        element["IRI"]= cl[1]
        list.append(element)
    d["classes"]=list

    list_of_all_values = [elem["name"] for elem in d["classes"]]

    #attributes sheet parsing
    list=[]
    classe=book["Attributs"][1][0] #à valider 
    index= list_of_all_values.index(classe)
    for attr in filter(lambda value:True if value[1]!='' else False,book["Attributs"][1:]): 
        if (classe != attr[0] and attr[0]!=''):
            classe=attr[0]
            index= list_of_all_values.index(classe)
            list=[]
        element={}
        element["name"]= attr[1]
        element["definition"]= attr[3]
        element["IRI"]= attr[2]
        element["source"]= attr[4]
        element["id"]= attr[5]
        list.append(element)
        d["classes"][index]["attributes"]=list
    
    #associations sheet parsing
    list=[]
    association= book["Associations"][1][0]
    for ass in filter(lambda value:True if value[2]!='' else False,book["Associations"][1:]): 
        if (association != ass[0] and ass[0]!=''): association=ass[0]
        element={}
        element["name"]= ass[2]
        element["source"]= association
        element["destination"]= ass[1]
        element["definition"]= ass[4]
        element["IRI"]= ass[3]
        list.append(element)
    d["associations"]=list

    #enumerations sheet parsing
    list=[]
    for enum in filter(lambda value:True if value[0]!='' else False, book["Énumérations"][1:]): 
        element={}
        element["name"]= enum[0]
        element["definition"]= enum[2]
        element["IRI"]= enum[1]
        list.append(element)
    d["enumerations"]=list

    list_of_all_values = [elem["name"] for elem in d["enumerations"]]

    #enumeration values sheet parsing
    list=[]
    enumeration=book["Valeurs d'énumération"][1][0] #à valider 
    index= list_of_all_values.index(enumeration)
    for enum in filter(lambda value:True if value[1]!='' else False,book["Valeurs d'énumération"][1:]): 
        if (enumeration != enum[0] and enum[0]!=''):
            enumeration=attr[0]
            index= list_of_all_values.index(enumeration)
            list=[]
        element={}
        element["name"]= enum[1]
        element["definition"]= enum[3]
        element["IRI"]= enum[2]
        list.append(element)
        d["enumerations"][index]["values"]=list

    json_path = path + "parsing_result.json"
    with open(json_path, 'w') as fp:
        json.dump(d,fp)
    return d
