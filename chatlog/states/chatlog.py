import uuid
from typing import List, Optional

from dao.in_memory import InMemoryChatlogDAO
from exceptions import MessageNotFoundException
from states import StateInterface


class Chatlog(StateInterface):
    def __init__(self, username, message_id=""):
        self.db = InMemoryChatlogDAO.get_instance()
        self.username = username
        self.message_id = message_id

    def add(self, doc: dict):
        doc["message_id"] = str(uuid.uuid4())[:4]
        doc["username"] = self.username
        self.message_id = doc["message_id"]
        self.db.add_chatlog(doc)

    def get(self, fields: Optional[List] = None) -> dict:
        message_doc = self.db.get_chatlog(self.username, self.message_id)
        return message_doc

    def set(self, doc):
        raise NotImplementedError(
            "Update chatlog is not implemented yet!"
        )

    def delete(self, fields: Optional[List] = None):
        self.db.delete_chatlog(self.username, self.message_id)

    def get_all(self, fields: Optional[List] = None, limit=10, start_message_id=None):
        message_docs = self.db.get_all_chatlogs(self.username, limit, start_message_id)
        return message_docs

    def delete_all(self):
        deleted_count = self.db.delete_all_chatlogs(self.username)
        if deleted_count == 0:
            raise MessageNotFoundException(f"No chatlogs were present for user {self.username}")
