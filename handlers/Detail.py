#_*_encoding:utf-8_*_
import json

import simplejson as simplejson

from handlers.base import BaseHandler



class DetailHandler(BaseHandler):
    def get(self, data):
        values = {}
        #python_obj = simplejson.loads("media/data/dictionary.json", encoding="utf-8")
        with open("media/data/dictionary.json") as file:
            python_obj = simplejson.loads(file.read())
        for object in python_obj["objects"]:
            if object["objectname"] == data:
                values["objectname"] = data
                values["objectdescription"] = object["objectdescription"]

                break
            else:
                values["objectname"] = "尚未创建该词条"
                values["objectdescription"] = "我来创建"
        else:
            #Some default action
            print("no object in json")

        self.render("detail.html", values=values)