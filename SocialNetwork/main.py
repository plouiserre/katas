from fastapi import FastAPI
from SocialNetwork.adapters.driving.cli.cli_app import cliApp
from SocialNetwork.adapters.driving.controllers import wall_controllers
from SocialNetwork.domain.search_service import SearchService
from SocialNetwork.domain.wall import Wall

# app = cliApp()
# wall = Wall()
# search_service = SearchService(wall)
# app.run(search_service, wall)

app = FastAPI()

app.include_router(wall_controllers.router)

@app.get("/")
async def root():
    return {"Welcome in my RS :)"}