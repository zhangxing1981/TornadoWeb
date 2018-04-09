from handlers.foo import FooHandler
from handlers.DashboardHandler import  DashboardHandler
from handlers.Upload import UploadHandler
from handlers.Browse import BrowseHandler
from handlers.Detail import DetailHandler
from handlers.Audit import AuditHandler

url_patterns = [
    (r"/base", FooHandler),
    (r"/", DashboardHandler),
    (r"/upload", UploadHandler),
    (r"/browse", BrowseHandler),
    (r"/detail/([^/]+)", DetailHandler),
    (r"/audit/([^/]+)", AuditHandler)
]

