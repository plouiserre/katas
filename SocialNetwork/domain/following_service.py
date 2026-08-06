from SocialNetwork.domain.models.author import Author

class FollowingService : 
    def __init__(self):
        pass

    def author_follows_some_one(self, author_account : Author, following_person : Author) : 
        author_account.following_persons.append(following_person)

    def see_followers_from_author(self, author_account : Author) -> list[Author] : 
        return author_account.following_persons