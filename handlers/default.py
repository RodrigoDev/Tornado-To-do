from handlers.base import BaseHandler

class DefaultHandler(BaseHandler):
    def get(self):
        import ipdb; ipdb.set_trace()
        self.write("Hello, world")
