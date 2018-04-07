#_*_encoding:utf-8_*_
from handlers.base import BaseHandler
import torndb

class BrowseHandler(BaseHandler):


    def get(self):
        db = torndb.Connection("127.0.0.1:3306", "Project_Atlas", user="root", password="1qaz@WSX")
        sql = 'SELECT * FROM Tbl_Project order by CreateTime desc limit 500'
        datalist = db.query(sql)
        tabledata = ""
        for datarow in datalist:
            tabledata += '<tr class="odd gradeA"><td title="'+ datarow["ProjectDesc"] +'">'+ datarow["ProjectTitle"] +'</td><td>'+ datarow["CreateTime"] +'</td><td>'+ datarow["DevPeriod"]  +'</td><td>'+ datarow["ProjectRequirement"] +'</td><td>'+ str(datarow["Price"]) +'元</td></tr>'

        db.close()
        self.render("browse.html", tabledata = tabledata)