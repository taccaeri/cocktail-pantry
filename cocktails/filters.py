from cocktails.models import Ingredient, Cocktail, RecipeDetail
from django_filters import rest_framework as filters


class CocktailFilter(filters.FilterSet):

    class Meta:
        model = Cocktail
        fields = ['flavor_profile', 'bartender']
