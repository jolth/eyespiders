#!/usr/bin/env python
#
#import web
from web import application
from config import *
from urls import urls
from views import *


app = application(urls, globals())

if __name__ == "__main__":
    app.run()
