class Todo:
    def __init__(self):
        self.todo_list = []
    def add_item(self, item):
        self.todo_list.append(item)
    def delete_item(self, index):
        self.todo_list.pop(index)
