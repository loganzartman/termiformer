import json

class FormLayout:
    def __init__(self, json_data=None):
        self.items = []
        if json_data:
            self.items = json.loads(json_data)

    def label(self, label):
        self.items.append({
            "type": "label",
            "label": label
            })
    
    def text(self, name, *, label):
        self.items.append({
            "type": "text",
            "name": name,
            "label": label
            })
    
    def to_json(self):
        return json.dumps(self.items)


default_data_value = {
    "text": ""
}

def item_value(data, item):
    name = item["name"]
    if name in data:
        return data[name]
    item_type = item["type"]
    if item_type in default_data_value:
        return default_data_value[item_type]
    return None

def item_focusable(item):
    return item["type"] in {
        "text"
    }
