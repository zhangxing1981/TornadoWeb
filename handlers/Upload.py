#_*_encoding:utf-8_*_
import random
import string
import os
import docx2txt
import sys
import json

from aip import AipNlp


from handlers.base import BaseHandler

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

        wordsvalue = UploadHandler.client.lexer(filecontent.encode('GBK','ignore').decode('GBK'))
        wordsdata = json.loads(json.dumps(wordsvalue,encoding="utf-8",ensure_ascii=False))
        words= ''
        for item in wordsdata["items"]:
            words += item["item"] + ', '

        keyvalue = UploadHandler.client.keyword("title",filecontent.encode('GBK', 'ignore').decode('GBK'))
        keydata = json.loads(json.dumps(keyvalue, encoding="utf-8", ensure_ascii=False))
        keys = ''
        for item in keydata["items"]:
            keys += item["tag"] + ', '




        #values["tag"] = json.dumps(returnvalue,encoding="utf-8",ensure_ascii=False)
        values["words"] = words
        values["keys"] = keys


        self.render("result.html",values = values)