class Joke:
    def __init__(self, joke):
        self.joke = joke
    def get_joke(self):
        return self.joke

class JokeSet:
    def __init__(self):
        self.list = []
        self.num_of_entries = 0
        self.add_joke("your gpa")
        self.add_joke("your beauty")
        self.add_joke("your sanity")
    def get_list(self):
        return self.list
    def get_num_of_entries(self):
        return self.num_of_entries
    def add_joke(self, joke):
        joke = Joke(joke)
        self.get_list().append(joke)
        self.num_of_entries += 1