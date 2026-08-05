from contextlib import asynccontextmanager
from fastapi import FastAPI
from SocialNetwork.adapters.driven.system_clock import SystemClock
from SocialNetwork.adapters.driven.wall.json_wall_repository import JsonWallRepository
from SocialNetwork.adapters.driven.wall.memory_wall_repository import MemoryWallRepository
from SocialNetwork.adapters.driving.cli.cli_app import cliApp
from SocialNetwork.adapters.driving.controllers import wall_controllers, search_controllers
from SocialNetwork.adapters.driving.controllers.context.search_context import get_search_context, SearchContext
from SocialNetwork.adapters.driving.controllers.context.wall_context import get_wall_context, WallContext
from SocialNetwork.domain.search_service import SearchService
from SocialNetwork.domain.wall_service import WallService
from SocialNetwork.state import db_context

app = cliApp()
# wall_repository = MemoryWallRepository()
wall_repository = JsonWallRepository()
clock = SystemClock()
wall_service = WallService(wall_repository, clock)
search_service = SearchService(wall_service)
app.run(search_service, wall_service)

# @asynccontextmanager 
# async def lifespan(app : FastAPI):
#     search_context = get_search_context()
#     wall_context = get_wall_context()
#     db_context["search"] = search_context
#     db_context["wall"] = wall_context
#     yield

# app = FastAPI(lifespan=lifespan)

# app.include_router(search_controllers.router)
# app.include_router(wall_controllers.router)

# @app.get("/")
# async def root():
#     return {"Welcome in my RS :)"}