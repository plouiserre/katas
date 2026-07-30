from fastapi import APIRouter

from SocialNetwork.adapters.driving.request.post_request import PostRequest

router = APIRouter()

@router.post("/wall/")
async def post_message(post : PostRequest):
    return {"auteur" : post.author_name, "message" : post.message}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="127.0.0.1", port=8000)

# from fastapi import APIRouter

# from BirthdayGreetings.adapters.driven.ContactManagerJson import ContactManagerJson
# from BirthdayGreetings.adapters.driven.TemplateManagerJson import TemplateManagerJson
# from BirthdayGreetings.domain.BirthdayCollaborators import BirthdayCollaborators

# router = APIRouter()

# @router.get("/greetings/{year}/{month}/{day}")
# async def get_greetings(year : str, month : str, day : str):
#     date_to_evaluate = year+"/"+month+"/"+day
#     contact_manager_txt = ContactManagerJson()
#     template_manager_txt = TemplateManagerJson()
#     birthday_collaborators = BirthdayCollaborators(contact_manager_txt, template_manager_txt)
#     messages_birthday_employees = birthday_collaborators.GreetingsBirthday(date_to_evaluate)
#     return {"all messages for birthday":messages_birthday_employees}