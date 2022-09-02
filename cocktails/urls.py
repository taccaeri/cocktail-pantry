from django.contrib import admin
from django.urls import path, include
from . import views

from cocktails.models import Ingredient, Cocktail, RecipeDetail


urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.CocktailsListView.as_view(), name = 'Cocktails'),
    path('api-auth/', include('rest_framework.urls'))
]
