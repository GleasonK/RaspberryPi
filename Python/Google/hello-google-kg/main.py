## Hello Google.py


from google.appengine.api import users
## Users is module in app engine. Learn about modules

import webapp2


class MainPage(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()
        ## Get current user to get page viewer


        if user:
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('Hello, ' + user.nickname())
            ## Google nickname = user.nickname()
        else:
            self.redirect(users.create_login_url(self.request.uri))
             ## Redirect command 'redirect()'


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)