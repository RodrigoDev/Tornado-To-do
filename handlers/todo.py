from handlers.base import BaseHandler

class ToDoHandler(BaseHandler):
    def get(self):
        self.write("Hello, world")

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
