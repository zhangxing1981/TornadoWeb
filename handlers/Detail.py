from handlers.base import BaseHandler


class DetailHandler(BaseHandler):
    def get(self, data):
        self.render("detail.html", values=data)