import simplejson, urllib, urllib2, google.appengine.api.urlfetch

from django.db import models
from django.template.defaultfilters import slugify

class Wager(models.Model):
    """Wager model detailing the agreement of participants"""        
    name = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=50, db_index=True, unique=True)
    
    def save(self):
        """Override save to slugify the name to form the URL"""
        self.slug = slugify(self.name)
        super(Wager, self).save()
    
class User(models.Model):
    """User model detailing the name and email address of the users in a wager"""
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=320)
    wager = models.ForeignKey(Wager)

class Award(models.Model):
    """Award model detailing the name of the award"""    
    name = models.CharField(max_length=50)
    
class Entry(models.Model):
    """Entry model detailing the name of the entry(film, actor) 
       and a reference of where/why nominated(film, director)"""
    name = models.CharField(max_length=50)
    award = models.ForeignKey(Award)
    reference = models.CharField(max_length=50, null=True)
    
    def getPoster(self):
        """Retrieves the poster image for the entry film"""
        url  = 'http://www.imdbapi.com/'
        data = urllib.urlencode({'t': str(self.name)})
        req  = urllib2.Request(url + '?' + data)
        conn = urllib2.urlopen(req)
        try:
            resp = simplejson.loads(conn.read())
        finally:
            conn.close()
        if resp.has_key('Poster'):
            return resp['Poster']

class Pick(models.Model):
    """Pick model detailing the selection of votes made against a user for a """
    entry = models.ForeignKey(Entry)
    wager = models.ForeignKey(Wager)
    user = models.ForeignKey(User)