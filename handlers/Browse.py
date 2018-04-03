from handlers.base import BaseHandler
import torndb

class BrowseHandler(BaseHandler):


    def get(self):
        db = torndb.Connection("106.75.218.199:3306", "Project_Atlas", user="root", password="123456")
        sql = 'SELECT * FROM Tbl_Project limit 100'
        datalist = db.query(sql)
        tabledata = ""
        for datarow in datalist:
            tabledata += '<tr class="odd gradeA"><td>'+ datarow["ProjectTitle"] +'</td><td>Trident</td><td>Trident</td><td>Trident</td><td>Trident</td></tr>'


        self.render("browse.html", tabledata = tabledata)