from __future__ import annotations
from dataclasses import dataclass
from SocialNetwork.domain.models.author import Author


@dataclass(frozen=True)
class AuthorResponse : 
    name : str

    @staticmethod
    def to_response(author : Author) -> AuthorResponse:
        return AuthorResponse(author.name)