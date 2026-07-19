from abc import ABC, abstractmethod
from BirthdayGreetings.domain.Template import Template

class TemplateManager(ABC) : 
    @abstractmethod
    def get_template_message()->Template :
        pass