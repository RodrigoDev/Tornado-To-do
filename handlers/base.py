import json
import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    """
        A class to collect common handler methods - all other handlers should
        subclass this one.
    """
