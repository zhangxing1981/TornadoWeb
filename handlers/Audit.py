import dbconfig
from handlers.base import BaseHandler



class AuditHandler(BaseHandler):
    dbconfig.init()

    def get(self, data):
        ProjectID = data
        sql = 'SELECT * FROM Tbl_Project where ProjectID = "'+ ProjectID +'"'
        tabledata = dbconfig.db.get(sql)


        self.render("audit.html", values=tabledata)