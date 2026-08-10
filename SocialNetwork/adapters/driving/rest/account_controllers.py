from fastapi import APIRouter, status

from SocialNetwork.adapters.driving.request.account_request import AccountRequest
from SocialNetwork.adapters.driving.response.account_response import AccountResponse
from SocialNetwork.state import db_context

router = APIRouter()

@router.post("/account/", status_code= status.HTTP_201_CREATED)
async def create_account(account : AccountRequest):
    return db_context["account"].account_service.add_account(account.account_name)

@router.get("/account/{account_name}", status_code= status.HTTP_200_OK)
async def get_account(account_name : str): 
    account_response = AccountResponse.to_response(db_context["account"].account_service.search_account(account_name))
    return account_response

# @router.post("/account/following/", status_code=status.HTTP_201_CREATED)
# async def follow_someone_more(account_request : AccountRequest):
#     return db_context["account"].get_following_service().account_follows_some_one(account_request.account_name, account_request.following_name)

# # @router.post("/wall/message/", status_code= status.HTTP_201_CREATED)
# # async def post_message(post : PostRequest):
# #     db_context["wall"].get_wall_service().post_messages(post.account_name, post.message)
# #     return PostResponse(AccountResponse(post.account_name), post.message, datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S"))
