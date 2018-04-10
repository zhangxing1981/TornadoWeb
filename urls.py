from handlers.foo import FooHandler
from handlers.DashboardHandler import  DashboardHandler
from handlers.Upload import UploadHandler
from handlers.Browse import BrowseHandler
from handlers.Detail import DetailHandler
from handlers.Audit import AuditHandler
from handlers.Main import MainHandler

url_patterns = [
    (r"/base", FooHandler),
    (r"/", MainHandler),
    (r"/upload", UploadHandler),
    (r"/browse", BrowseHandler),
    (r"/detail/([^/]+)", DetailHandler),
    (r"/audit/([^/]+)", AuditHandler),

]

