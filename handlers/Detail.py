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
                if object["objecttype"] == "PJ":
                    values["objectdescription"] = "项目名称：" + object["objectfields"][0]["projectname"]  + "</br>项目背景：" + object["objectfields"][0]["background"] + "</br>项目目标：" + object["objectfields"][0]["target"]
                else:
                    values["objectdescription"] = object["objectdescription"]
                break
            else:
                values["objectname"] = "尚未创建该词条"
                values["objectdescription"] = "我来创建"
        else:
            #Some default action
            print("no object in json")

        self.render("detail.html", values=values)