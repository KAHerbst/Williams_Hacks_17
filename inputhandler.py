import webapp2, jinja2, os, logging
from google.appengine.api import users
from google.appengine.ext import ndb

import classes

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
#tells which directory file is in
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(template_dir))

class InputHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("input.html")
        html = template.render({})
        self.response.write(html)

    def post(self):
        template = jinja_environment.get_template("input.html")
        html = template.render({})
        self.response.write(html)

        logging.info("input post") #???

        major_name = self.request.get("major_name")

        #getting user key
        current_user = users.get_current_user()
        userID = current_user.user_id()

        major = classes.Major(
            major_name=major_name,
            userID=userID,
            )
        major.put()

        template = jinja_environment.get_template("input.html")
        html = template.render({"major name": major_name,})
