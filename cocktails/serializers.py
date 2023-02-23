from cocktails.models import Ingredient, Cocktail, RecipeDetail, INGREDIENT_CATEGORY, COCKTAIL_CATEGORY, GLASSWARE, UNIT_CHOICES

from rest_framework import serializers, fields

import json


class RecipeDetailSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(source='ingredient.id')
    ingredient = serializers.ReadOnlyField(source='ingredient.name')

    display_unit = serializers.SerializerMethodField('get_display_unit')
    unit = str(fields.MultipleChoiceField(choices=UNIT_CHOICES))

    notes = serializers.SerializerMethodField('get_notes')

    def get_notes(self, item):
        return item.ingredient.notes

    def get_display_unit(self, item):
        for choice_tuple in UNIT_CHOICES:
            if choice_tuple[0] == item.unit:
                return choice_tuple[1]
        return ''

    class Meta:
        model = RecipeDetail
        fields = [
            "id",
            "ingredient",
            "quantity",
            "unit",
            "display_unit",
            "recommended",
            "optional",
            "notes"
            ]


class CocktailSerializer(serializers.ModelSerializer):
    ingredients = RecipeDetailSerializer(source="recipedetail_set", many=True)

    display_category = serializers.SerializerMethodField('get_display_category')
    category = fields.MultipleChoiceField(choices=COCKTAIL_CATEGORY)
    
    def get_display_category(self, item):
        display_category_list = []
        for category in item.category:
            for category_tuple in COCKTAIL_CATEGORY:
                if category_tuple[0] == category:
                    display_category_list.append(category_tuple[1])

        return display_category_list

    display_glassware = serializers.SerializerMethodField('get_display_glassware')
    glassware = str(fields.MultipleChoiceField(choices=GLASSWARE))

    def get_display_glassware(self, item):
        for choice_tuple in GLASSWARE:
            if choice_tuple[0] == item.glassware:
                return choice_tuple[1]

    variations = serializers.SerializerMethodField('get_variations')

    def get_variations(self, item):
        # the variation field is a JSON object that has been serialized to a string
        # do a json.loads here to deserialize it 
        if(type(item.variations == str) and item.variations != ''):
            # print(item.name)
            return json.loads(item.variations)

    def create(self, validated_data):
        ingredients = validated_data.pop("recipedetail_set", [])
        instance = Cocktail.objects.create(**validated_data)
        for ingredient_data in ingredients:
            ingredient = Ingredient.objects.get(id=ingredient_data.get("ingredient").get("id"))
            recipe_detail = RecipeDetail.objects.create(
                                                        ingredient=ingredient,
                                                        quantity=ingredient_data.get("quantity"),
                                                        cocktail=instance
                                                        )
        instance.save()
        return instance

    def update(self, instance, validated_data):
       ingredients = validated_data.pop('recipedetail_set', [])
       instance = super().update(instance, validated_data)
       # pprint(vars(instance.ingredients.through))
       for current_ingredient in instance.ingredients.all():
           rd = RecipeDetail.objects.get(
                                        ingredient=current_ingredient,
                                        cocktail=instance
                                        )
           rd.delete()
       for ingredient_data in ingredients:
           ingredient = Ingredient.objects.get(id=ingredient_data.get("ingredient").get('id'))
           recipe_detail = RecipeDetail.objects.create(
                                                       ingredient=ingredient,
                                                       quantity=ingredient_data.get("quantity"),
                                                       cocktail=instance
                                                       )
       instance.save()
       return instance


    class Meta:
        model = Cocktail
        fields = [
            "id",
            "name",
            "category",
            "display_category",
            "related",
            "bartender",
            "ingredients",
            "glassware",
            "display_glassware",
            "notes",
            "method",
            "variations",
            "reference"
            ]
        depth = 1


class IngredientSerializer(serializers.ModelSerializer):

    display_category = serializers.SerializerMethodField('get_display_category')
    category = fields.MultipleChoiceField(choices=INGREDIENT_CATEGORY)

    def get_display_category(self, ing):
        display_list = []
        for category in ing.category:
            for choice_tuple in INGREDIENT_CATEGORY:
                if type(choice_tuple[1]) is str:
                    if choice_tuple[0] == category:
                        display_list.append(choice_tuple[1])
                elif type(choice_tuple[1]) is tuple:
                    for nested_choice in choice_tuple[1]:
                        if nested_choice[0] == category:
                            display_list.append(nested_choice[1])

        return display_list

    category = serializers.SerializerMethodField('get_category_parent')

    def get_category_parent(self, ing):
        for choice_tuple in INGREDIENT_CATEGORY:
            if type(choice_tuple[1]) is tuple: # Checking for nested choices
                for nested_choice in choice_tuple[1]:
                    for category in ing.category:
                        if nested_choice[0] == category and (choice_tuple[0] not in ing.category):
                            ing.category.insert(0, choice_tuple[0]) # Prepending parent choice to category list

        return ing.category

    class Meta:
        model = Ingredient
        fields = [
            "id",
            "name",
            "altname",
            "category",
            "display_category",
            "related",
            "method",
            "notes"
            ]