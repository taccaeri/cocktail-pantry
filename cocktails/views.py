from django.shortcuts import render
from cocktails.models import Ingredient, Cocktail, RecipeDetail
from cocktails.serializers import CocktailSerializer


# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse

from django.views import View
from django.views.generic import ListView
from django.core.serializers import serialize
from rest_framework import serializers


# def index(request):
#     return HttpResponse("Hello, world. You're at the cocktails index.")

class CocktailsListView(ListView):

    # def get(self, request):
    #     qs = Cocktail.objects.all()
    #     data = serialize("json", qs)
    #     return HttpResponse(data, content_type = "application/json")

#class IngredientsListView(ListView):

    def get(self, request):
        qs = Cocktail.objects.all()
        cs = CocktailSerializer("json", qs, many = True)
        cs.is_valid()
        return HttpResponse(cs.data, content_type = "application/json")
