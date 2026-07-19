from BirthdayGreetings.domain.Template import Template
from BirthdayGreetings.adapters.Mapper.TemplateMapper import json_to_template, txt_to_template

def test_map_template_from_txt_file_to_template():
    text = "Happy birthday, dear <first_name>!|<first_name>"
    assert(Template("Happy birthday, dear <first_name>!", "<first_name>") == txt_to_template(text))

def test_map_template_from_json_file_to_template():
    text = '{"message":"Happy birthday, dear <first_name>!", "template":"<first_name>"}'
    assert(Template("Happy birthday, dear <first_name>!", "<first_name>") == json_to_template(text))