import datetime
from fastapi import APIRouter, Depends, status

from SocialNetwork.state import db_context
from SocialNetwork.adapters.driving.request.post_request import PostRequest
from SocialNetwork.adapters.driving.response.author_response import AuthorResponse
from SocialNetwork.adapters.driving.response.post_response import PostResponse
from SocialNetwork.adapters.driving.response.wall_response import WallResponse

router = APIRouter()

@router.post("/wall/message/", status_code= status.HTTP_201_CREATED)
async def post_message(post : PostRequest):
    db_context["wall"].get_wall_service().post_messages(post.author_name, post.message)
    return PostResponse(AuthorResponse(post.author_name), post.message, datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S"))

@router.get("/wall/messages/", status_code= status.HTTP_200_OK)
async def get_all_messages():
    all_posts = db_context["wall"].get_wall_service().get_all_messages_from_all_accounts()
    wall_response = WallResponse.to_response(all_posts)
    return wall_response

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="127.0.0.1", port=8000)