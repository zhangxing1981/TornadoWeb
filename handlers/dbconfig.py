import torndb

def init():
    global db
    db= torndb.Connection("127.0.0.1:3306", "Project_Atlas", user="root", password="1qaz@WSX")