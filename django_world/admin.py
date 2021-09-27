from django.contrib import admin
from .models import Succession,Succession_Seasons,Succession_Casts,Succession_Season_Episodes

# Register your models here.
# admin.site.register(Succession)                # The model Succession is abstract so it can't be registered with admin
admin.site.register(Succession_Seasons)
admin.site.register(Succession_Casts)
admin.site.register(Succession_Season_Episodes)
