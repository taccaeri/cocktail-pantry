from django.shortcuts import render, get_object_or_404
from cocktails.models import Ingredient, Cocktail, RecipeDetail
from cocktails.serializers import CocktailSerializer, IngredientSerializer

from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework import viewsets


class CocktailViewSet(viewsets.ModelViewSet):

    serializer_class = CocktailSerializer
    queryset = Cocktail.objects.all()

class IngredientViewSet(viewsets.ModelViewSet):

    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()
