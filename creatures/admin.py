from django.contrib import admin
from .models import Planet, Creature

# Register your models here.
# This makes the models visible and editable in the Django Admin panel.
admin.site.register(Planet)
admin.site.register(Creature)
