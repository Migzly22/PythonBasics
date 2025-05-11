def dataTypeTeller(paramValue):

    typeContainer = {
        int : "Integer", 
        float : "Float", 
        str : "String", 
        bool : "Boolean", 
        list : "List", 
        tuple : "Tuple", 
        set : "Set", 
        dict : "Dictionary"
    }


    for key, value in typeContainer.items():
        if isinstance(paramValue, key):
            return f"{value}"