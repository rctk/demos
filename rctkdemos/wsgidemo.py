import web
from rctkdemos.all import Demo
from rctk.receiver import app

application = app(Demo).wsgifunc()
