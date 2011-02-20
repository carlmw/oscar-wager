import simplejson, urllib, urllib2

from django.db import models
from django.core.cache import cache
from django.template.defaultfilters import slugify

class Wager(models.Model):
    """Wager model detailing the agreement of participants."""        
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(db_index=True, unique=True)
    
    def save(self):
        """Override save to slugify the name to form the URL."""
        self.slug = slugify(self.name)
        super(Wager, self).save()
    
class User(models.Model):
    """User model detailing the name and email address of the users in a wager."""
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=320)
    slug = models.SlugField(db_index=True)
    wager = models.ForeignKey(Wager)
    
    class Meta:
        unique_together = ('name', 'email', 'wager')
    
    def save(self):
        self.slug = slugify(self.name)
        super(User, self).save()

class Award(models.Model):
    """Award model detailing the name of the award."""    
    name = models.CharField(max_length=50)
    
class Entry(models.Model):
    """Entry model detailing the name of the entry(film, actor) 
       and a reference of where/why nominated(film, director)."""
    name = models.CharField(max_length=50)
    award = models.ForeignKey(Award, related_name='entries')
    reference = models.CharField(max_length=50, null=True)
    
    def getPoster(self):
        """Retrieves the poster image for the entry film."""
        data = entry_cache_get(self.name)
        return data[0]['posters'][3]['image']['url'] if data[0].has_key('posters') else ''

class Pick(models.Model):
    """Pick model detailing the selection of votes made against a user for a wager."""
    entry = models.ForeignKey(Entry)
    wager = models.ForeignKey(Wager)
    user = models.ForeignKey(User)
    
def entry_cache_key(name):
    """ Builds a key for caching an entry."""
    return slugify(name)+"entry"

def entry_cache_get(name):
    """ Gets a key for caching an entry."""
    c_key = entry_cache_key(name)
    entry = cache.get(c_key)
    if entry == None:
        url = 'http://api.themoviedb.org'
        key = '31978081436f3021d35a3275c385491b'
        title = urllib.quote(name.encode("utf-8"))
        conn  = urllib2.urlopen('%s/2.1/Movie.search/en/json/%s/%s' % (url, key, title))
        try:
            entry = simplejson.loads(conn.read())
        finally:
            conn.close()
        cache.set(c_key, entry, 85000)
    return entry
