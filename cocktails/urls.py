from django.contrib import admin
from django.urls import path, include
from . import views

from cocktails.models import Ingredient, Cocktail


urlpatterns = [
    #cocktail urls:
    path('cocktails/', views.CocktailViewSet.as_view({"get":"list"}), name = 'Cocktails'),
    path('cocktails/<int:pk>/', views.CocktailViewSet.as_view({"get":"retrieve"})),
    #ingredient urls:
    path('ingredients/', views.IngredientViewSet.as_view({"get":"list"}), name = 'Ingredients'),
    path('ingredients/<int:pk>/', views.IngredientViewSet.as_view({"get":"retrieve"})),
    path('categories/', views.list_categories), 
    path('cocktail_categories/', views.list_cocktail_categories)
]
