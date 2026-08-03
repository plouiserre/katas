from fastapi import FastAPI
from SocialNetwork.adapters.driven.wall.json_wall_repository import JsonWallRepository
from SocialNetwork.adapters.driven.wall.memory_wall_repository import MemoryWallRepository
from SocialNetwork.adapters.driving.cli.cli_app import cliApp
from SocialNetwork.adapters.driving.controllers import wall_controllers, search_controllers
from SocialNetwork.domain.search_service import SearchService
from SocialNetwork.domain.wall import Wall

app = cliApp()
wall_repository = JsonWallRepository()
wall = Wall(wall_repository)
search_service = SearchService(wall)
app.run(search_service, wall)

# app = FastAPI()

# app.include_router(search_controllers.router)
# app.include_router(wall_controllers.router)

# @app.get("/")
# async def root():
#     return {"Welcome in my RS :)"}