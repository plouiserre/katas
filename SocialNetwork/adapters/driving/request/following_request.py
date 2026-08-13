from dataclasses import dataclass

@dataclass(frozen=True)
class FollowingRequest : 
    account_name : str
    following_name : str