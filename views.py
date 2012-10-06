#import web
from  web import template

# Templates:
render = template.render('templates/')


class login:
    def GET(self):
        company = "Dev Microsystem"
        pagename = "Login"
        return render.login(company, pagename)
