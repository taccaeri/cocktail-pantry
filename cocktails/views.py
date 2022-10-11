from django.shortcuts import render, get_object_or_404
from cocktails.models import Ingredient, Cocktail, RecipeDetail
from cocktails.serializers import CocktailSerializer, IngredientSerializer
from cocktails.filters import CocktailFilter

from rest_framework.response import Response
# from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework import viewsets # generics

from django_filters import rest_framework as filters

# from pprint import pprint

class CocktailViewSet(viewsets.ModelViewSet):

    serializer_class = CocktailSerializer
    queryset = Cocktail.objects.all()

    # returns all possible cocktails within searched ingredient parameters
    def list(self, request, *args, **kwargs):
        ingredients = self.request.query_params.getlist("ingredient", [])

        if len(ingredients) == 0:
            queryset = self.filter_queryset(Cocktail.objects.all())
        else:
            ing = Ingredient.objects.exclude(id__in=ingredients)
            queryset = Cocktail.objects.exclude(ingredients__id__in=ing)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)


class IngredientViewSet(viewsets.ModelViewSet):

    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()

# class CocktailListView(generics.ListAPIView):
#
#     serializer_class = CocktailSerializer
#     queryset = Cocktail.objects.all()
#     filter_backends = [filters.DjangoFilterBackend]
#     filterset_class = CocktailFilter
