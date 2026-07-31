from fastapi import APIRouter, Depends, status

from SocialNetwork.adapters.driving.controllers.context.search_context import get_search_context, SearchContext

router = APIRouter()

@router.get("/search/autor/{autor_name}", status_code= status.HTTP_200_OK)
async def get_message_from_author(autor_name : str, search_context : SearchContext = Depends(get_search_context)):
    all_messages = search_context.get_search_service().load_wall_and_run_search_posts_from_specific_user(autor_name)
    return all_messages