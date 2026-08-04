from fastapi import APIRouter, Depends, status

from SocialNetwork.state import db_context
from SocialNetwork.adapters.driving.request.post_request import PostRequest

router = APIRouter()

@router.post("/wall/message/", status_code= status.HTTP_201_CREATED)
async def post_message(post : PostRequest):
    db_context["wall"].get_wall_service().post_messages(post.author_name, post.message)
    return {"auteur" : post.author_name, "message" : post.message}

@router.get("/wall/messages/", status_code= status.HTTP_200_OK)
async def get_all_messages():
    all_messages = db_context["wall"].get_wall_service().get_all_messages_from_all_accounts()
    return all_messages

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="127.0.0.1", port=8000)