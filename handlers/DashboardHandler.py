from handlers.base import BaseHandler

class DashboardHandler(BaseHandler):
    def get(self):
        self.render("dashboard.html")