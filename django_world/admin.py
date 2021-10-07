from django.contrib import admin
from .models import Succession,Succession_Seasons,Succession_Casts,Succession_Season_Episodes

# Register your models here.
# If a model is abstract it can't be registered with admin
admin.site.register(Succession)
admin.site.register(Succession_Seasons)
admin.site.register(Succession_Casts)
admin.site.register(Succession_Season_Episodes)
