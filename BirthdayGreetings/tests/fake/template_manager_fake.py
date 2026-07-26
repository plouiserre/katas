from BirthdayGreetings.domain.TemplateManager import TemplateManager

class TemplateManagerFake(TemplateManager):
    def __init__(self, template):
        super().__init__()
        self.template_message_memory = template

    def get_template_message(self):
        return self.template_message_memory