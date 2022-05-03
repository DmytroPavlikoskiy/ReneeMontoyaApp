import json
list_json = []
def convert_list(list):
    for el in list:
        list_json.append(json.dumps(el.serialize))
    return list_json
