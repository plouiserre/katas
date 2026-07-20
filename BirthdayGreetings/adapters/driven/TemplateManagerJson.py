from BirthdayGreetings.adapters.Mapper.TemplateMapper import json_to_template
from BirthdayGreetings.domain.Template import Template
from BirthdayGreetings.domain.TemplateManager import TemplateManager

class TemplateManagerJson(TemplateManager):
    def get_template_message(self)->Template :
        template = None
        with open("BirthdayGreetings/data/template.json", "r") as file : 
            content = file.read()
            template = json_to_template(content)
        return template
