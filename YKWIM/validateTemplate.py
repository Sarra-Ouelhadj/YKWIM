import pyexcel as p

def validateTemplate(file):
    
    book=p.get_book_dict(file_name=file)
    
    #------------------------
    #classes sheet validation
    #------------------------

    #0. La feuille classe doit contenir au moins une classe
    if (book["Classes"][1][0]=='') : return "La feuille classe doit contenir au moins une classe"

    #1. Chaque classe doit avoir un lien de référence ou une définition
    for cl in filter(lambda value:True if value[0]!='' else False, book["Classes"][1:]): 
        if (cl[1]=='' and cl[2]==''): return f"La classe {cl[0]} doit avoir un lien de référence ou une définition" 

    #------------------------
    #attributes sheet validation
    #------------------------

    #0. Le nom de la classe du 1er attribut est obligatoire
    if (book["Attributs"][1][0]=='') : return "Le nom de la classe du 1er attribut est obligatoire"

    list=[]
    classe=book["Attributs"][1][0] 
        
    #1. Tous les champs doivent être remplis. Le choix existe uniquement entre lien de référence et définition.
    for attr in filter(lambda value:True if value[1]!='' else False,book["Attributs"][1:]):
        if (attr[4]==''): return f"L'attribut {attr[1]} doit avoir une source"
        if (attr[5]==''): return f"Le champs \"Identifiant\" n'est pas précisé pour l'attribut {attr[1]}"
        if (attr[2]=='' and attr[3]==''): return f"L'attribut {attr[1]} doit avoir un lien de référence ou une définition"
        
        #2. Chaque classe doit avoir au minimum un identifiant
        if (classe != attr[0] and attr[0]!=''):# si on passe à une autre classe, vérifier que la classe d'avant a un identifiant
            if ("oui" not in list) : return f"la classe {classe} n'a pas d'identifiant"
            classe=attr[0]
            list=[]
        list.append(attr[5])

    # vérifier l'identifiant de la dernière classe
    if ("oui" not in list) : return f"la classe {classe} n'a pas d'identifiant"
    
    #------------------------
    #associations sheet validation
    #------------------------

    #0. Chaque association doit avoir un lien de référence ou une définition
    for ass in filter(lambda value:True if value[2]!='' else False,book["Associations"][1:]):
        if (ass[3]=='' and ass[4]==''): return f"L'association {ass[2]} doit avoir un lien de référence ou une définition" 

    #------------------------
    #enumerations sheet validation
    #------------------------

    #0. Chaque énumération doit avoir un lien de référence ou une définition
    for enum in filter(lambda value:True if value[0]!='' else False, book["Énumérations"][1:]): 
        if (enum[1]=='' and enum[2]==''): return f"L'énumération {enum[0]} doit avoir un lien de référence ou une définition" 
        enum_exit=True #une énumération existe dans le diagramme UML
    
    #------------------------
    #enumeration values sheet validation
    #------------------------

    if enum_exit :
        
        #0. Le nom de l'énumération de la 1ère valeur est obligatoire
        if (book["Valeurs d'énumération"][1][0]=='') : return "Le nom de l'énumération de la 1ère valeur est obligatoire"

        #1. Chaque valeur d'énumération doit avoir un lien de référence ou une définition
        for enum in filter(lambda value:True if value[1]!='' else False,book["Valeurs d'énumération"][1:]):
            if (enum[2]=='' and enum[3]==''): return f"La valeur d'énumération {enum[1]} doit avoir un lien de référence ou une définition"