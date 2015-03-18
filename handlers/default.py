from handlers.base import BaseHandler

class DefaultHandler(BaseHandler):
    def get(self):
        self.write("Hello, world")
