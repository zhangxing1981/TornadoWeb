from handlers.foo import FooHandler
from handlers.DashboardHandler import  DashboardHandler
from handlers.Upload import UploadHandler
from handlers.Browse import BrowseHandler

url_patterns = [
    (r"/base", FooHandler),
    (r"/", DashboardHandler),
    (r"/upload", UploadHandler),
    (r"/browse", BrowseHandler),
]

