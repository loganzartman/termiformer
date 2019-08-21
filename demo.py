import termiformer

def input_name_simple():
    data = {}
    with termiformer.form(data) as f:
        f.label("Name Input Form")
        f.text("first_name", label="First name")
        f.text("last_name", label="Last name")
    return "{} {}".format(data["first_name"], data["last_name"])

# functionally the same as above
def input_name():
    layout = termiformer.FormLayout()
    layout.label("Name Input Form")
    layout.text("first_name", label="First name")
    layout.text("last_name", label="Last name")
    data = {}
    termiformer.present(layout, data)
    return "{} {}".format(data["first_name"], data["last_name"])

# functionally the same as above
def input_name_json():
    json_data = """
    [
        {
            "type": "label",
            "label": "Name Input Form" 
        },
        {
            "type": "text",
            "name": "first_name",
            "label": "First name"
        },
        {
            "type": "text",
            "name": "last_name",
            "label": "Last name"
        }
    ]
    """
    layout = termiformer.FormLayout(json_data=json_data)
    data = {}
    termiformer.present(layout, data)
    return "{} {}".format(data["first_name"], data["last_name"])


if __name__ == "__main__":
    print("Hi, ", input_name_json(), "!")
