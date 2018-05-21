#_*_encoding:utf-8_*_
import random
import string
import os
import docx2txt
import sys
import json

from aip import AipNlp


from handlers.base import BaseHandler
#from elasticsearch import Elasticsearch
from datetime import datetime

class UploadHandler(BaseHandler):


    APP_ID = '10925040'
    API_KEY = '55v6GscmAG9qoV7eziHFUrqk'
    SECRET_KEY = 'mcobAhRM6Pu7GgKuaMiqCwtWIl4faN4S'
    client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
    client

    reload(sys)
    sys.setdefaultencoding('utf-8')

    def get(self):
        self.render("upload.html")

    def post(self, *args, **kwargs):
        #upload and save file on server
        pjfile = self.request.files['pjfile'][0]
        original_fname = pjfile['filename']
        extension = os.path.splitext(original_fname)[1]
        fname = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(6))
        final_filename = fname + extension
        output_file = open("uploads/" + final_filename, 'wb')
        output_file.write(pjfile['body'])
        output_file.close()
        #analyze file
        values = {}
        filecontent = docx2txt.process("uploads/" + final_filename)
        values["filecontent"] = filecontent

        pos = {}
        pos["n"] = 0
        pos["nr"] = 0
        pos["nz"] = 0
        pos["a"] = 0
        pos["m"] = 0
        pos["c"] = 0
        pos["f"] = 0
        pos["ns"] = 0
        pos["v"] = 0
        pos["ad"] = 0
        pos["q"] = 0
        pos["u"] = 0
        pos["s"] = 0
        pos["nt"] = 0
        pos["vd"] = 0
        pos["an"] = 0
        pos["r"] = 0
        pos["xc"] = 0
        pos["t"] = 0
        pos["nw"] = 0
        pos["vn"] = 0
        pos["d"] = 0
        pos["p"] = 0
        pos["w"] = 0
        wordsvalue = UploadHandler.client.lexer(filecontent.encode('GBK','ignore').decode('GBK'))
        wordsdata = json.loads(json.dumps(wordsvalue,encoding="utf-8",ensure_ascii=False))
        words= ''
        wordcount = {}
        wordsplite = ''
        for item in wordsdata["items"]:
            if(item["pos"] != ''):
                pos[item["pos"]] += 1
                if(item["pos"] == 'n' or  item["pos"] == 'm' or  item["pos"] == 'v' or  item["pos"] == 'nt' or  item["pos"] == 'vn'):
                    if(item["item"] in wordcount):
                        wordcount[item["item"]] +=1
                    else:
                        wordcount[item["item"]] =1
            wordsplite += item["item"] + ','

        for index,item in list(enumerate(pos)):
            words += item + ":" + str(pos[item]) + "</br>"

        for index,item in list(enumerate(wordcount)):
            if(wordcount[item] >1):
                words += item + ":" + str(wordcount[item]) + "</br>"

        keyvalue = UploadHandler.client.keyword("title",filecontent.encode('GBK', 'ignore').decode('GBK'))
        keydata = json.loads(json.dumps(keyvalue, encoding="utf-8", ensure_ascii=False))
        keys = ''
        for item in keydata["items"]:
            keys += item["tag"] + ', '




        #values["tag"] = json.dumps(returnvalue,encoding="utf-8",ensure_ascii=False)
        values["words"] = wordsplite
        values["keys"] = keys



        #insert data into elasticsearch
        #es = Elasticsearch([
         #   {'host':'106.75.218.230','port':9200}
        #])
        #es.indices.create(index='fileindex', ignore = 400)
        #{u'acknowledged': True}
        #es.index(
        #    index="fileindex", doc_type ="word", id = 42, body = {"filecontent": filecontent, "timestamp": datetime.now()})
        #{u'_id': u'42', u'_index': u'fileindex', u'_type': u'word', u'_version': 1, u'ok': True}


        self.render("result.html",values = values)