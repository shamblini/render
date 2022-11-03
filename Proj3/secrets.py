import json 

def GetSecret(value):
    with open('.secrets.json', 'r') as file:
        json_object = json.load(file)
        
    return json_object[value]
    