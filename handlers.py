''' Handlers.py '''
import os
import uuid
import requests
from custom_modules.MilliPiyango.MPParser import MPParser
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    ''' Route\'ta tanimli istek url\'ini karsilayacak nesne '''

    def get(self):
        mp_response = requests.request(
            "GET", "http://www.millipiyango.gov.tr/sonuclar/cekilissontarihlerinumaralar.php", timeout=3)
        mp_response.headers["Host"] = "www.millipiyango.gov.tr"
        mp_response.headers["Referrer"] = "http://www.millipiyango.gov.tr/"
        result = MPParser(mp_response.json())
        self.render("index.html", unescape = tornado.escape.xhtml_unescape, sayisal=result.GetCekilisSonuclari(
            "sayisal"), sanstopu=result.GetCekilisSonuclari("sanstopu"), superloto=result.GetCekilisSonuclari("superloto"))

    def data_received(self, data):
        pass
