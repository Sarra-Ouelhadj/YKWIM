import pyexcel as p
import sys
import json
from YKWIM import app

def generateJSON(file, path=app.config["UPLOAD_FOLDER"]):
    """generate JSON from template"""
    
    book=p.get_book_dict(file_name=file)
    list=[]
    d={}
    for cl in book["Classes"][1:]: 
        if (cl[0]!=''):
            element={}
            element["name"]= cl[0]
            element["definition"]= cl[2]
            element["IRI"]= cl[1]
            list.append(element)
    d["classes"]=list

    list_of_all_values = [elem["name"] for elem in d["classes"]]

    list=[]
    classe=book["Attributs"][1][0]
    for attr in book["Attributs"][1:]: 
        if (classe == attr[0]):
            element={}
            element["name"]= attr[1]
            element["definition"]= attr[3]
            element["IRI"]= attr[2]
            element["source"]= attr[4]
            element["id"]= attr[5]
            list.append(element)
        else:
            index= list_of_all_values.index(classe)
            d["classes"][index]["attributes"]=list
            if (attr[0]!=''):
                classe=attr[0]
                list=[]
                element={}
                element["name"]= attr[1]
                element["definition"]= attr[3]
                element["IRI"]= attr[2]
                element["source"]= attr[4]
                element["id"]= attr[5]
                list.append(element)

    list=[]
    for ass in book["Associations"][1:]: 
        if (ass[0]!=''):
            element={}
            element["name"]= ass[2]
            element["source"]= ass[0]
            element["destination"]= ass[1]
            element["definition"]= ass[4]
            element["IRI"]= ass[3]
            list.append(element)
    d["associations"]=list

    list=[]
    for enum in book["Énumérations"][1:]: 
        if (enum[0]!=''):
            element={}
            element["name"]= enum[0]
            element["definition"]= enum[2]
            element["IRI"]= enum[1]
            list.append(element)
    d["enumerations"]=list

    list_of_all_values = [elem["name"] for elem in d["enumerations"]]

    list=[]
    enumeration=book["Valeurs d'énumération"][1][0]
    for enum in book["Valeurs d'énumération"][1:]: 
        if (enumeration == enum[0]):
            element={}
            element["name"]= enum[1]
            element["definition"]= enum[3]
            element["IRI"]= enum[2]
            list.append(element)
        else : 
            index= list_of_all_values.index(enumeration)
            d["enumerations"][index]["values"]=list
            if (enum[0]!=''):
                enumeration=enum[0]
                list=[]
                element={}
                element["name"]= enum[1]
                element["definition"]= enum[3]
                element["IRI"]= enum[2]
                list.append(element)
    json_path = path + "parsing_result.json"
    with open(json_path, 'w') as fp:
        json.dump(d,fp)
    return d
