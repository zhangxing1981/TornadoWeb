from handlers.base import BaseHandler



class MainHandler(BaseHandler):

    def get(self):
        tabledata = {}
        self.render("main.html", values=tabledata)