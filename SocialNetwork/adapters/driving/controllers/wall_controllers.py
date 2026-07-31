from fastapi import APIRouter, Depends, status

from SocialNetwork.adapters.driving.controllers.context.wall_context import get_wall_context, WallContext
from SocialNetwork.adapters.driving.request.post_request import PostRequest

router = APIRouter()

@router.post("/wall/message/", status_code= status.HTTP_201_CREATED)
async def post_message(post : PostRequest, wall_context : WallContext = Depends(get_wall_context) ):
    wall_context.get_wall().post_messages(post.author_name, post.message)
    return {"auteur" : post.author_name, "message" : post.message}

@router.get("/wall/messages/", status_code= status.HTTP_200_OK)
async def get_all_messages(wall_context : WallContext = Depends(get_wall_context)):
    all_messages = wall_context.get_wall().get_all_messages_from_all_accounts()
    return all_messages

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="127.0.0.1", port=8000)