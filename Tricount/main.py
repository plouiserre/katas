from Tricount.cli.cli_app import cliApp

app = cliApp()
# # wall_repository = MemoryWallRepository()
# wall_repository = JsonWallRepository()
# clock = SystemClock()
# json_account_repository = JsonAccountRepository()
# following_service = FollowingService(json_account_repository)
# account_service = AccountService(json_account_repository, following_service)
# wall_service = WallService(account_service, wall_repository, clock)
# search_service = SearchService(wall_service)
app.run()