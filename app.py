''' Module aciklama alani '''
import tornado.autoreload
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import options
from configuration import config
import handlers


class Application(tornado.web.Application):
    ''' Uygulama ana sinifi '''

    def __init__(self):
        _handlers = [
            (r'/', handlers.MainHandler),
        ]
        settings = {
            "template_path": config.TEMPLATE_PATH,
            "static_path": config.STATIC_PATH,
            "debug": config.DEBUG,
            "compress_response": config.COMPRESS_RESPONSE
        }
        tornado.web.Application.__init__(self, _handlers, **settings)

if __name__ == "__main__":
    HTTP_SERVER = tornado.httpserver.HTTPServer(Application())
    HTTP_SERVER.listen(config.PORT)
    tornado.ioloop.IOLoop.instance().start()
