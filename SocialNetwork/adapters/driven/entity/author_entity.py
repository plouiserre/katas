from dataclasses import dataclass

from SocialNetwork.domain.models.message import Author

@dataclass(frozen=True)
class AuthorEntity :
    name : str

    @staticmethod
    def create_from_domain(author : Author):
        return AuthorEntity(author.name)