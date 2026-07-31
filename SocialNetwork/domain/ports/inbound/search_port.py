from abc import ABC, abstractmethod

class SearchServicePort(ABC):
    @abstractmethod
    def load_wall_and_run_search_posts_from_specific_user(self, all_accounts, account_name):
        pass