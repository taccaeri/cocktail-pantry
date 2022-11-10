import json
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from cocktails.models import Ingredient, Cocktail, RecipeDetail, INGREDIENT_CATEGORY
from cocktails.serializers import CocktailSerializer, IngredientSerializer
from cocktails.filters import CocktailFilter

from rest_framework.response import Response
# from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework import viewsets, serializers # generics
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer

from django_filters import rest_framework as filters

from pprint import pprint

class CocktailViewSet(viewsets.ModelViewSet):

    serializer_class = CocktailSerializer
    queryset = Cocktail.objects.all()

    # returns all possible cocktails within searched ingredient parameters
    def list(self, request, *args, **kwargs):
        ingredients = self.request.query_params.getlist("ingredient", [])
        show_related = self.request.query_params.get("show_related")
        # check box for substitutions

        if len(ingredients) == 0:
            queryset = self.filter_queryset(Cocktail.objects.all())
        else:
            ing = Ingredient.objects.filter(id__in=ingredients)
            ing_expanded = []
            for ingredient in ing:
                ing_expanded.append(ingredient.id)
                if show_related == "true":
                    for i in ingredient.related.all():
                        ing_expanded.append(i.id)

            pprint(ing_expanded)

            ing_filtered = Ingredient.objects.exclude(id__in=ing_expanded)
            queryset = Cocktail.objects.exclude(ingredients__id__in=ing_filtered)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)


class IngredientViewSet(viewsets.ModelViewSet):

    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()

@api_view(["GET"])
@renderer_classes([JSONRenderer])
def list_categories(request):
    category_dict = {}
    for ing in INGREDIENT_CATEGORY:
        if(type(ing[1]) is str):
            category_dict[ing[0]] = ing[1]
        elif(type(ing[1]) is tuple):
            sub_cat_dict = {}
            for sub_category in ing[1]:
                sub_cat_dict[sub_category[0]] = sub_category[1]
            category_dict[ing[0]] = sub_cat_dict

    return Response(category_dict)


# class CocktailListView(generics.ListAPIView):
#
#     serializer_class = CocktailSerializer
#     queryset = Cocktail.objects.all()
#     filter_backends = [filters.DjangoFilterBackend]
#     filterset_class = CocktailFilter
