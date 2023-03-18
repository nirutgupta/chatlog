from dao import ChatlogDAO
from exceptions import MessageNotFoundException


class InMemoryChatlogDAO(ChatlogDAO):
    __instance = None

    def __init__(self):
        self.chatlogs = []

    def add_chatlog(self, doc):
        self.chatlogs.append(doc)

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = InMemoryChatlogDAO()
        return cls.__instance

    def get_chatlog(self, username, message_id):
        for user_chatlog in self.chatlogs:
            if user_chatlog.get("message_id") == message_id:
                return user_chatlog
        # raise not found

    def get_all_chatlogs(self, username, limit, start_message_id=""):
        idx = len(self.chatlogs) - 1
        if start_message_id:
            idx = self.__find_chatlog_position(start_message_id)
        if limit == -1:
            limit = len(self.chatlogs)
        res = []
        while limit > 0 and idx >= 0:
            if self.chatlogs[idx].get("username") == username:
                res.append(self.chatlogs[idx])
                limit -= 1
            idx -= 1
        return res

    def __find_chatlog_position(self, message_id):
        for idx, user_chatlog in enumerate(self.chatlogs):
            if user_chatlog.get("message_id") == message_id:
                return idx
        raise MessageNotFoundException(f"No chatlog found with id {message_id}")

    def delete_chatlog(self, username, message_id):
        idx = self.__find_chatlog_position(message_id)
        self.chatlogs.pop(idx)
        return 1

    def delete_all_chatlogs(self, username) -> int:
        """
        returns number of documents deleted
        """
        all_chatlogs = self.get_all_chatlogs(username, -1)
        delete_count = 0
        for chatlog in all_chatlogs:
            delete_count += self.delete_chatlog(username, chatlog.get("message_id"))
        return delete_count
