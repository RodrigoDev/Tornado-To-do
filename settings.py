import tornado

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)
define("config", default=None, help="tornado config file")
define("debug", default=False, help="debug mode")
tornado.options.parse_command_line()

settings = {}
settings['debug'] = options.debug
settings['mongo.host'] = 'localhost'
settings['mongo.port'] = 27017
