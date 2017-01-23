import webapp2, jinja2, os, logging
from google.appengine.api import users
from google.appengine.ext import ndb

import classes

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
#tells which directory file is in
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(template_dir))

class InfoHandler(webapp2.RequestHandler):
    def get(self):
        #getting current user key
        user = users.get_current_user().user_id()

        major_query = classes.Major.query(classes.Major.userID == user)
        majors = major_query.fetch()

        for major in majors:

            # if datetime.datetime.today().date() == datetime.datetime.combine(contact.dateOfReminder, datetime.time.min).date():
            #     self.response.write("<script> alert('CALL " + contact.contactName.upper() + "'); </script>")
            """
            Pull up major reqs for each major
            """
            data_grab.data_grab()

            template = jinja_environment.get_template("info.html")
            html = template.render({"major_name": major.major_name})
            self.response.write(html)
