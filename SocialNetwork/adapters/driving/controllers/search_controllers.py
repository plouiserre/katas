from fastapi import APIRouter, status

from SocialNetwork.adapters.driving.response.wall_response import WallResponse
from SocialNetwork.state import db_context

router = APIRouter()

@router.get("/search/autor/{autor_name}", status_code= status.HTTP_200_OK)
async def get_message_from_author(autor_name : str):
    all_posts = db_context["search"].get_search_service().load_wall_and_run_search_posts_from_specific_user(autor_name)
    wall_response = WallResponse.to_response(all_posts)
    return wall_response