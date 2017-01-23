import webapp2, jinja2, os, logging, csv
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
            """
            Pull up major reqs for each major
            """
            # template = jinja_environment.get_template("info.html")
            # html = template.render({"major_name": major.major_name})
            # self.response.write(html)

            reqs = []

            with open("data.csv") as fin:
                f1 = list(csv.reader(fin))
                for area_study in f1:
                    if major.major_name == area_study[0]:
                        reqs.append(area_study[2:])

            major.major_reqs = str(reqs)

            template = jinja_environment.get_template("info.html")
            html = template.render({"major_name": major.major_name,
                                    "major_reqs": major.major_reqs})
            self.response.write(html)
