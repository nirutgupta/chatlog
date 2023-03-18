from dao import ChatlogDAO


class MySQLDao(ChatlogDAO):
    def add_chatlog(self, doc):
        """ INSERT INTO chatlogs WITH VALUES () """
        pass

    def get_chatlog(self, username, message_id):
        """ SELECT * from chatlogs WHERE username = username and message_id = message_id """
        pass

    def get_all_chatlogs(self, username, limit, start_message_id):
        """ SELECT * from chatlogs where username = username LIMIT limit"""
        pass

    def delete_chatlog(self, username, message_id):
        """ DELETE from chatlogs where username = username and message_id = message_id """
        pass

    def delete_all_chatlogs(self, username):
        """ DELETE from chatlogs where username = username"""
        pass
