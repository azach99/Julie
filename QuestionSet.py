from Question import Question
class QuestionSet:
    def __init__(self):
        self.list = []
        self.num_of_entries = 0
    def get_list(self):
        return self.list
    def get_num_of_entries(self):
        return self.num_of_entries
    def add_question(self, question, answer):
        question = Question(question, answer)
        self.get_list().append(question)
        self.num_of_entries += 1
