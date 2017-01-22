import webapp2, jinja2, os, logging
from google.appengine.api import users
from google.appengine.ext import ndb

import classes
import inputhandler
import infohandler

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(template_dir))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        # If the user is logged in...
        if user:
            email_address = user.nickname()
            cssi_user = classes.CssiUser.get_by_id(user.user_id())

            template = jinja_environment.get_template("welcome.html")
            html = template.render({})
            self.response.write(html)

            signout_link_html = '<a style="color:white;" href="%s">Sign Out</a>' % (
                  users.create_logout_url('/'))
            # If the user has previously been to our site, we greet them!
            if cssi_user:
                self.response.write('''
                    <center><div style="color:white;" id = "welcome">Welcome %s %s (%s)! <br> %s <br></div></center>''' % (
                    cssi_user.first_name,
                    cssi_user.last_name,
                    email_address,
                    signout_link_html))
            # If the user hasn't been to our site, we ask them to sign up
            else:
                self.response.write('''
                    Welcome to our site, %s!  Please sign up! <br>
                    <form method="post" action="/">
                    <input type="text" name="first_name">
                    <input type="text" name="last_name">
                    <input type="submit">
                    </form><br> %s <br>
                    ''' % (email_address, signout_link_html))
                    # Otherwise, the user isn't logged in!

        else:
            template = jinja_environment.get_template("index.html")
            html = template.render({})
            self.response.write(html)

            self.response.write('''
                <center><a style="color:white;" href="%s">Sign in</a></center>''' % (
                users.create_login_url('/')))
    def post(self):
        logging.info("main post")

        template = jinja_environment.get_template("welcome.html")
        html = template.render({})
        self.response.write(html)

        user = users.get_current_user()
        if not user:
          # You shouldn't be able to get here without being logged in
          self.error(500)
          return

        cssi_user = classes.CssiUser(
            first_name=self.request.get('first_name'),
            last_name=self.request.get('last_name'),
            id=user.user_id(),
            )
        cssi_user.put()

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/input', inputhandler.InputHandler),
    ('/info', infohandler.InfoHandler)
], debug=True)
