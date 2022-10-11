from django.db import models
from multiselectfield import MultiSelectField

INGREDIENT_CATEGORY = [
    ('spirit', 'Spirit'),
    ('liquor', 'Liquor'),
    ('sweetener', 'Sweetener'),
    ('citrus', 'Citrus'),
    ('soda', 'Soda'),
    ('emulsifier', 'Emulsifier'),
    ('muddler', 'Muddler'),
    ('bitters', 'Bitters'),
    ('garnish', 'Garnish'),
    ('concentrate', 'Concentrate'),
    ('infusion', 'Infusion'),
    ('cordial', 'Cordial'),
    ('solutions', 'Solutions'),
    ('tinctures', 'Tinctures')
]

TASTING_NOTES = [

    ('astringent', 'Astringent'),
    ('bitter', 'Bitter'),
    ('boozy', 'Boozy'),
    ('complex', 'Complex'),
    ('fresh', 'Fresh'),
    ('rich', 'Rich'),
    ('salty', 'Salty'),
    ('sharp', 'Sharp'),
    ('silky', 'Silky'),
    ('smoky', 'Smoky'),
    ('sour', 'Sour'),
    ('spicy', 'Spicy'),
    ('subtle', 'Subtle'),
    ('sweet', 'Sweet'),
    ('tannic', 'Tannic'),
    ('umami', 'Umami')
]

UNIT_CHOICES = [
    ('oz', 'ounce(s)'),
    ('ml', 'milliliter(s)'),
    ('g', 'gram(s)'),
    ('tsp', 'teaspoon(s)'),
    ('tbsp', 'tablespoon(s)'),
    ('dash', 'dash(es)'),
    ('barspoon', 'barspoon(s)'),
    ('pinch', 'pinch(es)'),
    ('bunch', 'bunch(es)'),
    ('twist', 'twist(s)'),
    ('peel', 'peel(s)')
]

COCKTAIL_CATEGORY = [

]


# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    category = MultiSelectField(choices=INGREDIENT_CATEGORY)
    description = models.TextField(blank=True)

    def _str__(self):
        return self.name


class Cocktail(models.Model):
    name = models.CharField(max_length=50)
    bartender = models.CharField(max_length=40, blank=True)
    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeDetail'
        )
    flavor_profile = MultiSelectField(choices=TASTING_NOTES, blank=True)
    description = models.TextField(blank=True)
    method = models.TextField(blank=True)

    def __str__(self):
        return self.name


class RecipeDetail(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE)
    quantity = models.FloatField()
    unit = models.CharField(
        max_length=15,
        choices=UNIT_CHOICES,
        blank=True
        )
    recommended = models.CharField(max_length=40, blank=True)

    class Meta:
        unique_together = ('ingredient', 'cocktail')

    def __str__(self):
        return self.ingredient.name
