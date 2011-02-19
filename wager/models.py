from google.appengine.ext import db

class Wager(db.Model):
    """Wager model detailing the agreement of participants"""    
    
    name = db.StringProperty(required=True)
    stub = db.StringProperty(required=True)
    details = db.StringProperty(multiline=True, required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    
class User(db.User):
    """User model detailing the name and email address of the users in a wager"""

    name = db.StringProperty(required=True)
    email = db.EmailProperty()
    wager = db.ReferenceProperty(Wager)

class Award(db.Model):
    """Award model detailing the name of the award"""
    
    name = db.StringProperty(required=True)
    
class Entry(db.Model):
    """Entry model detailing the name of the entry(film, actor) 
       and a reference of where/why nominated(film, director)"""
    
    name = db.StringProperty(required=True)
    award = db.ReferenceProperty(Award)
    reference = db.StringProperty(max_length=255, null=True)
    
class Vote(db.Model):
    """Vote model detailing the selection of votes made against a user for a """
    
    entry = db.ReferenceProperty(Entry)
    wager = db.ReferenceProperty(Wager)
    user = db.ReferenceProperty (User)