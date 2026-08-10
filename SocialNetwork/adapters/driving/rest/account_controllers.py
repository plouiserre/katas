from fastapi import APIRouter, status

from SocialNetwork.adapters.driving.request.account_request import AccountRequest
from SocialNetwork.state import db_context

router = APIRouter()

@router.post("/account/following/", status_code=status.HTTP_201_CREATED)
async def follow_someone_more(account_request : AccountRequest):
    return db_context["account"].get_following_service().account_follows_some_one(account_request.account_name, account_request.following_name)

# @router.post("/wall/message/", status_code= status.HTTP_201_CREATED)
# async def post_message(post : PostRequest):
#     db_context["wall"].get_wall_service().post_messages(post.account_name, post.message)
#     return PostResponse(AccountResponse(post.account_name), post.message, datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S"))
