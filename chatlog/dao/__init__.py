from abc import ABC, abstractmethod


class ChatlogDAO(ABC):
    """
    Chatlog DAO interface
    """

    @abstractmethod
    def add_chatlog(self, doc):
        pass

    @abstractmethod
    def get_chatlog(self, username, message_id):
        pass

    @abstractmethod
    def get_all_chatlogs(self, username, limit, start_message_id):
        pass

    @abstractmethod
    def delete_chatlog(self, username, message_id) -> int:
        pass

    @abstractmethod
    def delete_all_chatlogs(self, username) -> int:
        pass
