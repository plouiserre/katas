import json

from BirthdayGreetings.Template import Template

def json_to_template(template_json : str) -> Template:
    datas = json.loads(template_json)
    result = Template(datas["message"], datas["template"])
    return result

def txt_to_template(template_txt : str) -> Template:
    elements = template_txt.split("|")
    template = Template(elements[0],elements[1])
    return template