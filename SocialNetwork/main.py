from SocialNetwork.adapters.driving.cli_app import cliApp
from SocialNetwork.domain.search import Search
from SocialNetwork.domain.wall import Wall

app = cliApp()
app.run(Search(), Wall())