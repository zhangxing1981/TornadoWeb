#_*_encoding:utf-8_*_
import dbconfig

from handlers.base import BaseHandler

class BrowseHandler(BaseHandler):

    dbconfig.init()

    def get(self):
        sql = 'SELECT * FROM Tbl_Project order by CreateTime desc limit 1000'
        datalist = dbconfig.db.query(sql)
        tabledata = ""
        for datarow in datalist:
            tabledata += '<tr class="odd gradeA"><td title="'+ datarow["ProjectDesc"] +'">'+ datarow["ProjectTitle"] +'</td><td>'+ datarow["CreateTime"] +'</td><td>'+ datarow["DevPeriod"]  +'</td><td>'+ datarow["ProjectRequirement"] +'</td><td>'+ str(datarow["Price"]) +'元</td><td><a href="../audit/'+ datarow["ProjectID"]  +'">审核</td></tr>'

        dbconfig.db.close()
        self.render("browse.html", tabledata = tabledata)