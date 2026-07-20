from fastapi import APIRouter

from BirthdayGreetings.adapters.driven.ContactManagerTxt import ContactManagerTxt
from BirthdayGreetings.adapters.driven.TemplateManagerTxt import TemplateManagerTxt
from BirthdayGreetings.domain.BirthdayCollaborators import BirthdayCollaborators
from BirthdayGreetings.domain.DateOfTheDay import DateOfTheDay

router = APIRouter()

@router.get("/greetings/{year}/{month}/{day}")
async def get_greetings(year : str, month : str, day : str):
    date_to_evaluate = year+"/"+month+"/"+day
    contact_manager_txt = ContactManagerTxt()
    date_of_the_day = DateOfTheDay(date_to_evaluate)
    template_manager_txt = TemplateManagerTxt()
    birthday_collaborators = BirthdayCollaborators(contact_manager_txt, date_of_the_day, template_manager_txt)
    messages_birthday_employees = birthday_collaborators.GreetingsBirthday(date_to_evaluate)
    return {"all messages for birthday":messages_birthday_employees}