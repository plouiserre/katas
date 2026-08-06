from SocialNetwork.domain.following_service import FollowingService
from SocialNetwork.domain.models.author import Author

def test_peter_follows_alice():
    following_persons = (FollowingDriver("Peter")
                         .follows_someone("Alice")
                         .see_following_persons())
    assert(len(following_persons) == 1)
    assert(following_persons[0] == Author("Alice", []))

def test_alice_follows_peter_and_luke():
    following_persons = (FollowingDriver("Alice")
                         .follows_someone("Peter")
                         .follows_someone("Luke")
                         .see_following_persons())
    assert(len(following_persons) == 2)
    assert(following_persons[0] == Author("Peter" , []))
    assert(following_persons[1] == Author("Luke", []))


class FollowingDriver(): 
    def __init__(self, main_author_name):
        self.main_author = Author(main_author_name, [])
        self.following_service = FollowingService()

    def follows_someone(self, account_to_follow_name):
        self.following_service.author_follows_some_one(self.main_author, Author(account_to_follow_name, []))
        return self

    def see_following_persons(self): 
        return self.following_service.see_followers_from_author(self.main_author)