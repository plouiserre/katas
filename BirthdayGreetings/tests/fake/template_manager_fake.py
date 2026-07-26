from BirthdayGreetings.domain.Template import Template
from BirthdayGreetings.domain.TemplateManager import TemplateManager

class TemplateManagerFake(TemplateManager):
    def __init__(self, template_message, code_to_replace):
        super().__init__()
        self.template_message_memory = Template(template_message, code_to_replace)

    def get_template_message(self):
        return self.template_message_memory