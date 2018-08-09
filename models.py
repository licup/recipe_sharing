from google.appengine.ext import ndb

class Recipe(ndb.Model):
    line1 = ndb.StringProperty(required=True)
    line2 = ndb.StringProperty(required=True)
    line3 = ndb.StringProperty(required=True)
    image_url = ndb.StringProperty(required=False)
