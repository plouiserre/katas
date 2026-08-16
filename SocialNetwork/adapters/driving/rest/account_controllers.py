from fastapi import APIRouter, status

from SocialNetwork.adapters.driving.request.account_request import AccountRequest
from SocialNetwork.adapters.driving.request.following_request import FollowingRequest
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

@router.post("/account/following/", status_code=status.HTTP_201_CREATED)
async def follow_someone_more(following_request : FollowingRequest):
    return db_context["account"].account_service.follow_new_account(following_request.account_name, following_request.following_name)

@router.delete("/account/{account_name}/following/{follow_account_name}", status_code= status.HTTP_204_NO_CONTENT)
async def delete_follow(account_name : str, follow_account_name : str): 
    db_context["account"].account_service.delete_follow_account(account_name, follow_account_name)

@router.get("/account/{account_name}/following/", status_code=status.HTTP_200_OK)
async def get_all_following_persons(account_name : str): 
    return db_context["account"].account_service.get_all_following_accounts(account_name)