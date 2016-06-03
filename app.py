from MyMessenger import MyMessenger

def print_message(message=''):
    messenger_obj = MyMessenger()
    messenger_obj.new_message(message)
    print messenger_obj.get_message() 
    

if __name__ == "__main__":
    print_message('Hello Python2')
