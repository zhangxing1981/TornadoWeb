#_*_encoding:utf-8_*_
import dbconfig

from handlers.base import BaseHandler
from elasticsearch import Elasticsearch
from datetime import datetime

class BrowseHandler(BaseHandler):

    dbconfig.init()

    def get(self):
        sql = 'SELECT * FROM Tbl_Project order by CreateTime '
        datalist = dbconfig.db.query(sql)
        tabledata = ""
        es = Elasticsearch([
            {'host': '106.75.218.230', 'port': 9200}
        ])
        for datarow in datalist:
            tabledata += '<tr class="odd gradeA"><td title="'+ datarow["ProjectDesc"] +'">'+ datarow["ProjectTitle"] +'</td><td>'+ datarow["CreateTime"] +'</td><td>'+ datarow["DevPeriod"]  +'</td><td>'+ datarow["ProjectRequirement"] +'</td><td>'+ str(datarow["Price"]) +'元</td><td><a href="../audit/'+ datarow["ProjectID"]  +'">审核</td></tr>'
            # insert data into elasticsearch

            es.indices.create(index='projectindex', ignore=400)
            {u'acknowledged': True}
            es.index(
                index="projectindex", doc_type="mysql", id=datarow["ProjectID"],
                body={"projectdesc": datarow["ProjectDesc"], "timestamp": datetime.now(), "publishtime":datarow["CreateTime"],"devperiod":datarow["DevPeriod"],"price":str(datarow["Price"]),"req":datarow["ProjectRequirement"],"title":datarow["ProjectTitle"]})
            {u'_id': datarow["ProjectID"], u'_index': u'projectindex', u'_type': u'mysql', u'_version': 1, u'ok': True}


        dbconfig.db.close()
        self.render("browse.html", tabledata = tabledata)