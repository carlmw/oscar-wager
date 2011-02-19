from django.contrib import admin

from wager import models

admin.site.register(models.Wager)
admin.site.register(models.Award)
admin.site.register(models.Entry)
admin.site.register(models.User)
admin.site.register(models.Vote)

