from django.db import models

class Wager(models.Model):
    """Wager model detailing the agreement of participants"""        
    name = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=50, unique=True)
    
class User(models.Model):
    """User model detailing the name and email address of the users in a wager"""
    name = models.CharField(max_length=50)
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
    
class Vote(models.Model):
    """Vote model detailing the selection of votes made against a user for a """
    entry = models.ForeignKey(Entry)
    wager = models.ForeignKey(Wager)
    user = models.ForeignKey(User)