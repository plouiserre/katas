from SocialNetwork.adapters.driving.cli.cli_app import cliApp
from SocialNetwork.domain.search_service import SearchService
from SocialNetwork.domain.wall import Wall

app = cliApp()
wall = Wall()
search_service = SearchService(wall)
app.run(search_service, wall)