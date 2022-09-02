from cocktails.models import Ingredient, Cocktail, RecipeDetail

from rest_framework import serializers
from rest_framework.serializers import ReadOnlyField

class RecipeDetailSerializer(serializers.ModelSerializer):
    id = ReadOnlyField(source = 'ingredient.id')
    ingredient = ReadOnlyField(source = 'ingredient.name')

    class Meta:
        model = RecipeDetail
        fields = (
            "id",
            "ingredient",
            "quantity",
            "unit"
            )

class CocktailSerializer(serializers.ModelSerializer):
    ingredients = RecipeDetailSerializer(source = "recipedetail_set", many = True)

    class Meta:
        model = Cocktail
        fields = (
            "id",
            "name",
            "bartender",
            "ingredients",
            "flavor_profile",
            "description",
            "method"
            )
        depth = 1

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = (
            "id",
            "name",
            "category",
            "flavor_profile",
            "description"
            )
