class MyMessenger:
    def __init__(self):
        self.message = ''

    def new_message(self,message):
        self.message = message
        

    def get_message(self):
        return self.message
