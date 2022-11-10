from django.contrib import admin
from django.urls import path, include
from . import views

from cocktails.models import Ingredient, Cocktail


urlpatterns = [
    #cocktail urls:
    path('cocktails/', views.CocktailViewSet.as_view({"get":"list", "post":"create"}), name = 'Cocktails'),
    path('cocktails/<int:pk>/', views.CocktailViewSet.as_view({"get":"retrieve", "post":"update", "delete":"destroy"})),
    #ingredient urls:
    path('ingredients/', views.IngredientViewSet.as_view({"get":"list", "post":"create"}), name = 'Ingredients'),
    path('ingredients/<int:pk>/', views.IngredientViewSet.as_view({"get":"retrieve", "post":"update", "delete":"destroy"})),
    path('categories/', views.list_categories)
    # path('list/', views.CocktailViewSet.cocktail_by_bartender, name="Bartender")
]
