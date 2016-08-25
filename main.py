#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import jinja2
import webapp2
from random import randint


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))

skrito = randint(1, 100)
class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("sstevilo.html")

    def post(self):
        ugibanje = self.request.get("vnos")

        try:
            if int(ugibanje) == skrito:
                a= {"b": "PRAVILNO! Uganili ste skrito stevilo."}
                return self.render_template("sstevilo.html", params=a)
            elif int(ugibanje) > skrito:
                a={"b":"Stevilo je preveliko."}
                return self.render_template("sstevilo.html",params=a)
            elif int(ugibanje) < skrito:
                a={"b": "Stevilo je premajhno."}
                return self.render_template("sstevilo.html",params=a)
            else:
                a = {"b": "Vpisite stevilo."}
                return self.render_template("sstevilo.html", params=a)

        except ValueError:
            a = {"b": "Napisite stevilo."}
            return self.render_template("sstevilo.html", params=a)

        except KeyError:
            pass



app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)
