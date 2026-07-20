from fastapi import APIRouter

from BirthdayGreetings.adapters.driven.ContactManagerJson import ContactManagerJson
from BirthdayGreetings.adapters.driven.TemplateManagerJson import TemplateManagerJson
from BirthdayGreetings.domain.BirthdayCollaborators import BirthdayCollaborators
from BirthdayGreetings.domain.DateOfTheDay import DateOfTheDay

router = APIRouter()

@router.get("/greetings/{year}/{month}/{day}")
async def get_greetings(year : str, month : str, day : str):
    date_to_evaluate = year+"/"+month+"/"+day
    contact_manager_txt = ContactManagerJson()
    date_of_the_day = DateOfTheDay(date_to_evaluate)
    template_manager_txt = TemplateManagerJson()
    birthday_collaborators = BirthdayCollaborators(contact_manager_txt, date_of_the_day, template_manager_txt)
    messages_birthday_employees = birthday_collaborators.GreetingsBirthday(date_to_evaluate)
    return {"all messages for birthday":messages_birthday_employees}