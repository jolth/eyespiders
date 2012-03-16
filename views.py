#import web
from  web import template

# Templates:
render = template.render('templates/')


class login:
    def GET(self):
        company = "G-mys"
        pagename = "Login"
        return render.login(company, pagename)
