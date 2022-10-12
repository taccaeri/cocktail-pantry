from cocktails.models import Ingredient, Cocktail, RecipeDetail

from rest_framework import serializers
#


class RecipeDetailSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(source='ingredient.id')
    ingredient = serializers.ReadOnlyField(source='ingredient.name')

    class Meta:
        model = RecipeDetail
        fields = [
            "id",
            "ingredient",
            "quantity",
            "unit"
            "recommended"
            ]


class CocktailSerializer(serializers.ModelSerializer):

    ingredients = RecipeDetailSerializer(source="recipedetail_set", many=True)

    def create(self, validated_data):
        ingredients = validated_data.pop("recipedetail_set", [])
        instance = Cocktail.objects.create(**validated_data)
        for ingredient_data in ingredients:
            ingredient = Ingredient.objects.get(
                id=ingredient_data.get("ingredient").get("id"))
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
               ingredient=current_ingredient, cocktail=instance)
           rd.delete()
       for ingredient_data in ingredients:
           ingredient = Ingredient.objects.get(
               id=ingredient_data.get("ingredient").get('id'))
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
            "bartender",
            "ingredients",
            "glassware",
            "flavor_profile",
            "description",
            "method"
            ]
        depth = 1


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = [
            "id",
            "name",
            "category",
            "description"
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
