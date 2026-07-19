from BirthdayGreetings.adapters.Mapper.TemplateMapper import txt_to_template
from BirthdayGreetings.domain.Template import Template
from BirthdayGreetings.domain.TemplateManager import TemplateManager

class TemplateManagerTxt(TemplateManager):
    def get_template_message()->Template :
        template = None
        with open("BirthdayGreetings/data/template.txt", "r") as file : 
            content = file.read()
            template = txt_to_template(content)
        return template
