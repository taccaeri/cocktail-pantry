# Register your models here.
from django.contrib import admin

from .models import Ingredient
from .models import Cocktail

admin.site.register(Ingredient)
admin.site.register(Cocktail)
