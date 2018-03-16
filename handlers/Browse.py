from handlers.base import BaseHandler

class BrowseHandler(BaseHandler):
    def get(self):
        self.render("browse.html")