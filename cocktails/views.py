import json
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from cocktails.models import Ingredient, Cocktail, RecipeDetail, INGREDIENT_CATEGORY, COCKTAIL_CATEGORY
from cocktails.serializers import CocktailSerializer, IngredientSerializer, RecipeDetailSerializer

from rest_framework.response import Response
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
        # check box for substitutions
        show_related = self.request.query_params.get("show_related")
        # will add toggle button to switch between results limited and not limited to selected ingredients
        including_not_limited = self.request.query_params.get("including_not_limited") 
        
        if len(ingredients) == 0:
            queryset = self.filter_queryset(Cocktail.objects.all())
        else:
            # fetch user supplied list of ingredient objects from the Database
            ing = Ingredient.objects.filter(id__in=ingredients)
            ing_expanded = []
            # do a loop through the ingredients and append related ingredients to our list if show_related
            for ingredient in ing:
                ing_expanded.append(ingredient.id)
                if show_related == "true":
                    for i in ingredient.related.all():
                        ing_expanded.append(i.id)

            # this creates a list of ingredients we DO NOT want in our dataset
            # exclude optional ingredients here to allow them into the final filter
            rec_filtered = RecipeDetail.objects.exclude(ingredient__id__in=ing_expanded).exclude(optional = True)
            id_list = rec_filtered.values_list("cocktail__id")
            # this creates a list of cocktails that we CAN NOT create
            inverse = Cocktail.objects.filter(pk__in=id_list)
            # subtract the list of cocktails we CAN NOT create from the full list of cocktails
            # to find the list of cocktails that we can make
            queryset = Cocktail.objects.all().difference(inverse)

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
    # iterate through ingredient categories and expand subcategories
    for ing in INGREDIENT_CATEGORY:
        if(type(ing[1]) is str):
            category_dict[ing[0]] = ing[1]
        elif(type(ing[1]) is tuple):
            sub_cat_dict = {}
            for sub_category in ing[1]:
                sub_cat_dict[sub_category[0]] = sub_category[1]
            category_dict[ing[0]] = sub_cat_dict

    return Response(category_dict)

@api_view(["GET"])
@renderer_classes([JSONRenderer])
def list_cocktail_categories(request):
    category_dict = {}
    # iterate through ingredient categories and expand subcategories
    for ing in COCKTAIL_CATEGORY:
        if(type(ing[1]) is str):
            category_dict[ing[0]] = ing[1]
        elif(type(ing[1]) is tuple):
            sub_cat_dict = {}
            for sub_category in ing[1]:
                sub_cat_dict[sub_category[0]] = sub_category[1]
            category_dict[ing[0]] = sub_cat_dict

    return Response(category_dict)
