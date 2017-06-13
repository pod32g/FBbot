import fbchat as fb

class TestBot(fb.Client):
    
    def __init__(self, email, passwd, debug=True, user_agent=None):
        fb.Client.__init__(self, email, passwd, debug, user_agent)
    
    def on_message(self, mid, author_id, author_name, message, metadata):
        self.markAsDelivered(author_id, mid)
        self.markAsRead(author_id)

        print(f"{author_id} said: {message}")

        if str(author_id) is not str(self.uid):
            if message is "k" or message is "K":
                self.send(author_id, ":v")

Bot = TestBot("username", "password")
Bot.listen()