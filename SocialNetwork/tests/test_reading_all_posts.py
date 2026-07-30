from SocialNetwork.tests.driver_test import DriverTest

def test_get_messages_from_peter_unique_user():
    reading_driver = ReadingDriver()
    all_messages = (reading_driver
                        .posts_messages_peter_alone()
                        .read_all_messages())
    assert(len(all_messages) == 1)
    assert(len(all_messages["Peter"]) == 4)
    assert(all_messages["Peter"][0] == "Hello every body")
    assert(all_messages["Peter"][1] == "Some one is here")
    assert(all_messages["Peter"][2] == "I will enjoy this meal!!!")
    assert(all_messages["Peter"][3] == "Why my soccer team is bad?")

def test_get_messages_from_three_friends_separate():
    reading_driver = ReadingDriver()
    all_messages_harry = (reading_driver
                        .posts_messages_harry_ron_hermione()
                        .read_all_messages())

    all_messages = reading_driver.read_all_messages()

    all_messages_harry = all_messages["Harry"]
    all_messages_ron = all_messages["Ron"]
    all_messages_hermione = all_messages["Hermione"]

    assert(len(all_messages) == 3)

    assert(len(all_messages_harry) == 2)
    assert(all_messages_harry[0] == "Some one want to go eat some Pizza?")
    assert(all_messages_harry[1] == "Hermione be nice we do not stop to study")
    assert(len(all_messages_ron) == 2)
    assert(all_messages_ron[0] == "Yes me!!!")
    assert(all_messages_ron[1] == "Stop to be boring!!!!")
    assert(len(all_messages_hermione) == 1)
    assert(all_messages_hermione[0] == "Harry, Ron go back to study for the exams!!!!")

class ReadingDriver(DriverTest): 
    def __init__(self):
        super().__init__()

    def post_message(self, account_name :str , message : str): 
        return super().post_message(account_name, message)

    def posts_messages_peter_alone(self):
        return super().posts_messages_peter_alone()

    def posts_messages_harry_ron_hermione(self):
        return super().posts_messages_harry_ron_hermione()

    def read_all_messages(self): 
        messages = self.wall.get_all_messages_from_all_accounts()
        return messages