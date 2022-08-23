from YKWIM import generateJSON as g

def generatePlantUML (d) :
    """generate PlantUML code from a dictionary"""

    s = "@startuml\n"
    #iterate over classes and their attributes
    for list in d["classes"]: 
        s += ("class {} {{".format(list["name"])) + "\n"

        for attr in list["attributes"]:
            s += "\t" + attr["name"] + "\n"
        s += "}" + "\n"
    
    #iterate over enumerations and their values
    for list in d["enumerations"]: 
        s += ("enum {} {{".format(list["name"])) + "\n"
        for value in list["values"]:
            s += "\t" + value["name"] + "\n..\n"
        s += "}" + "\n"
    
    #iterate over associations
    for list in d["associations"]: 
        s += ("{} --> {} : {}".format(list["source"],list["destination"], list["name"])) + "\n"

    return s + "@enduml"
