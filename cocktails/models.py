from django.db import models
from multiselectfield import MultiSelectField


INGREDIENT_CATEGORY = [
    ('spirits', (
        ('gin', 'Gin'),
        ('rum', 'Rum'),
        ('agave', 'Agave'),
        ('whisky', 'Whisk(e)y'),
        ('A-brandy', 'Aged Brandy'),
        ('UA-brandy', 'Unaged Brandy'),
        ('aquavit', 'Aquavit'),
        ('vodka', 'Vodka'),
        )
    ),
    ('modifiers', (
        ('liqueur', 'Liqueur'),
        ('amari', 'Amari'),
        ('wine', 'Fortified Wine'),
        )
    ),
    ('bitters', 'Bitters'),
    ('sweeteners', 'Sweeteners'),
    ('toppers', 'Toppers'),
    ('emulsifiers', 'Emulsifiers'),
    ('dry', 'Dry'),
    ('fresh', 'Fresh'),
    ('other', 'Other'),
    ('concoctions', (
        ('concentrates', 'Concentrates'),
        ('infusions', 'Infusions'),
        ('cordials', 'Cordials'),
        ('solutions', 'Solutions'),
        ('tinctures', 'Tinctures'),
        ('puree', 'Purees'),
        )
    )
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
    ('slice', 'slice(s)'),
    ('twist', 'twist'),
    ('peel', 'peel'),
    ('wheel', 'wheel'),
    ('wedge', 'wedge'),
    ('rinse', 'rinse'),
    ('rim', 'rim'),
    ('drop', 'drop(s)'),
    ('sprig', 'sprig'),
    ('bqt', 'bouquet')
]

GLASSWARE = [
    ('single', 'Single Rocks Glass'),
    ('double', 'Double Rocks Glass'),
    ('coupe', 'Coupe'),
    ('NN', 'Nick & Nora'),
    ('martini', 'Martini Glass'),
    ('collins', 'Collins Glass'),
    ('beer', 'Beer Glass'),
    ('fizz', 'Fizz Glass'),
    ('julep', 'Julep Tin'),
    ('port', 'Port'),
    ('flute', 'Flute'),
    ('tiki', 'Tiki Mug'),
    ('HB', 'Highball'),
    ('snif', 'Snifter'),
    ('tea', 'Tea Cup')
]

COCKTAIL_CATEGORY = [
    ('classic', 'Classic & Vintage'),
    ('gin-SH', 'Gin Shaken'),
    ('gin-ST', 'Gin Stirred'),
    ('rum-SH', 'Rum Shaken'),
    ('rum-ST', 'Rum Stirred'),
    ('agave-SH', 'Agave Shaken'),
    ('agave-ST', 'Agave Stirred'),
    ('whi-SH', 'Whisk(e)y Shaken'),
    ('whi-ST', 'Whisk(e)y Stirred'),
    ('bra-SH', 'Brandy Shaken'),
    ('bra-ST', 'Brandy Stirred'),
    ('SC', 'Sparkling Cocktails'),
    ('FWC', 'Fortified Wine Cocktails'),
    ('punch', 'Punch'),
    ('jul', 'Julep'),
    ('fizz', 'Flips and Fizzes'),
    ('swiz', 'Swizzles'),
    ('aqua', 'Aquavit'),
    ('mar-V', 'Martini Variation'),
    ('saz-V', 'Sazerac Variation'),
    ('neg-V', 'Negroni Variation'),
    ('daq-V', 'Daiquiri Variation'),
    ('man-V', 'Manhattan Variation'),
    ('OF-V', 'Old Fashioned Variation')
]


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    altname = models.CharField(max_length=100)
    category = MultiSelectField(choices=INGREDIENT_CATEGORY, blank=True)
    related = models.ManyToManyField(
                                "self",
                                symmetrical=False,
                                blank=True,
                                related_name='related_ingredient',
                                )
    method = models.TextField(blank=True)
    notes = models.TextField(blank=True)

    def _str__(self):
        return self.name


class Cocktail(models.Model):
    name = models.CharField(max_length=50)
    category = MultiSelectField(choices=COCKTAIL_CATEGORY, blank=True)
    related = models.ManyToManyField(
                                "self",
                                symmetrical=False,
                                blank=True,
                                related_name='related_cocktail',
                                )
    bartender = models.CharField(max_length=40, blank=True)
    ingredients = models.ManyToManyField(
                                        Ingredient,
                                        through='RecipeDetail',
                                        blank=True
                                        )
    glassware = models.CharField(
                                max_length=50,
                                choices=GLASSWARE,
                                blank=True
                                )
    notes = models.TextField(blank=True)
    method = models.TextField(blank=True)
    variations = models.TextField(blank=True)

    def __str__(self):
        return self.name


class RecipeDetail(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE)
    quantity = models.FloatField(blank=True)
    unit = models.CharField(
        max_length=15,
        choices=UNIT_CHOICES,
        blank=True
        )
    recommended = models.CharField(max_length=40, blank=True)
    optional = models.BooleanField(blank=True, null=True)


    class Meta:
        unique_together = ('ingredient', 'cocktail', 'recommended')

    def __str__(self):
        return self.ingredient.name
