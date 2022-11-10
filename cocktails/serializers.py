from cocktails.models import Ingredient, Cocktail, RecipeDetail, INGREDIENT_CATEGORY

from rest_framework import serializers, fields


class RecipeDetailSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(source='ingredient.id')
    ingredient = serializers.ReadOnlyField(source='ingredient.name')

    class Meta:
        model = RecipeDetail
        fields = [
            "id",
            "ingredient",
            "quantity",
            "unit",
            "recommended",
            "optional"
            ]


class CocktailSerializer(serializers.ModelSerializer):
    ingredients = RecipeDetailSerializer(source="recipedetail_set", many=True)

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
            "related",
            "bartender",
            "ingredients",
            "glassware",
            "notes",
            "method",
            "variations"
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
            if type(choice_tuple[1]) is tuple: #checking for nested choices
                for nested_choice in choice_tuple[1]:
                    for category in ing.category:
                        if nested_choice[0] == category and (choice_tuple[0] not in ing.category):
                            ing.category.insert(0, choice_tuple[0]) #prepending parent choice to category list

        return ing.category

    class Meta:
        model = Ingredient
        fields = [
            "id",
            "name",
            "category",
            "related",
            "notes",
            "display_category"
            ]



class DateBeforeValidator:
    """
    Validator for checking if a start date is before an end date field.
    Implementation based on `UniqueTogetherValidator` of Django Rest Framework.
    """
    message = ('{start_date_field} should be before {end_date_field}.')

    def __init__(self, start_date_field="start_date", end_date_field="end_date", message=None):
        self.start_date_field = start_date_field
        self.end_date_field = end_date_field
        self.message = message or self.message

    def __call__(self, attrs):
        if attrs[self.start_date_field] > attrs[self.end_date_field]:
            message = self.message.format(
                                        start_date_field=self.start_date_field,
                                        end_date_field=self.end_date_field,
                                        )
            # Replace the following line with
            #   raise serializers.ValidationError(
            #       {self.end_date_field: message},
            #       code='date_before',
            #   )
            # if you want to raise the error on the field level
            raise serializers.ValidationError(message, code='date_before')

    def __repr__(self):
        return '<%s(start_date_field=%s, end_date_field=%s)>' % (
            self.__class__.__name__,
            smart_repr(self.start_date_field),
            smart_repr(self.end_date_field)
        )
