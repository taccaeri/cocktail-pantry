from __future__ import unicode_literals

from django.db import migrations
from django.db import transaction


def populate_ingredient(apps, schema_editor):
    Ingredient = apps.get_model("cocktails", "Ingredient")
    db_alias = schema_editor.connection.alias

    ing_list = [
        # {"name":"", "cat":""},

        # Spirits:
        {"name":"Bourbon", "cat":"spirits"},
        {"name":"Vodka", "cat":"spirits"},
        {"name":"Gin", "cat":"spirits"},

        {"name":"Blanco Tequila", "cat":"spirits"},
        {"name":"Reposado Tequila", "cat":"spirits"},
        {"name":"Anejo Tequila", "cat":"spirits"},
        {"name":"Mezcal", "cat":"spirits"},

        {"name":"Aged English Rum", "cat":"spirits"},
        {"name":"White English Rum", "cat":"spirits"},
        {"name":"Aged Spanish Rum", "cat":"spirits"},
        {"name":"White Spanish Rum", "cat":"spirits"},
        {"name":"Aged French Rhum", "cat":"spirits"},
        {"name":"White French Rhum", "cat":"spirits"},
        {"name":"Aged Jamaican Rum", "cat":"spirits"},
        {"name":"White Jamaican Rum", "cat":"spirits"},
        {"name":"Cachaça", "cat":"spirits"},
        {"name":"White Batavia Arrack", "cat":"spirits"},
        {"name":"Aged Batavia Arrack", "cat":"spirits"},

        {"name":"American Whiskey", "cat":"spirits"},
        {"name":"Scotch Whisky", "cat":"spirits"},
        {"name":"Irish Whiskey", "cat":"spirits"},
        {"name":"Japanese Whisky", "cat":"spirits"},
        {"name":"Canadian Whisky", "cat":"spirits"},

        {"name":"Brandy", "cat":"spirits"},
        {"name":"Aquavit", "cat":"spirits"},

        # Liqueur:
        {"name":"Strega", "cat":"liqueur"},
        {"name":"Drambuie", "cat":"liqueur"},
        {"name":"Maraschino Liqueur", "cat":"liqueur"},
        {"name":"Bénédictine", "cat":"liqueur"},
        {"name":"Absinthe", "cat":"liqueur"},

        # Fortified Wine:
        {"name":"Red Vermouth", "cat":"wine"},
        {"name":"Dry Vermouth", "cat":"wine"},
        {"name":"Blanc Vermouth", "cat":"wine"},

        # Sweetener:
        {"name":"Sugar", "cat":"sweetener"},
        {"name":"Sugar Cube", "cat":"sweetener"},
        {"name":"Simple Syrup", "cat":"sweetener"},
        {"name":"Demerara Syrup", "cat":"sweetener"},
        {"name":"Cane Sugar Syrup", "cat":"sweetener"},
        {"name":"Honey", "cat":"sweetener"},
        {"name":"Honey Syrup", "cat":"sweetener"},

        # Bitters:
        {"name":"Angostura Bitters", "cat":"bitters"},
        {"name":"Orange Bitters", "cat":"bitters"},
        {"name":"Death&Co House Orange Bitters", "cat":"bitters"},

        # Other:
        {"name":"Lemon", "cat":["citrus", "garnish"]},
        {"name":"Fresh Lemon Juice", "cat":"citrus"},
        {"name":"Lime", "cat":["citrus", "garnish"]},
        {"name":"Fresh Lime Juice", "cat":"citrus"},
        {"name":"Orange", "cat":["citrus", "garnish"]},

        {"name":"Olive", "cat":"garnish"},
    ]

    for ing in ing_list:
        new_ing = Ingredient.objects.using(db_alias).create(name=ing["name"])
        new_ing.category = ing["cat"]
        new_ing.save()


def populate_cocktail(apps, schema_editor):
    Cocktail = apps.get_model("cocktails", "Cocktail")
    db_alias = schema_editor.connection.alias

    coc_list = [
        # {"name":"", "cat":"", "bar":"", "glass":""},

        # Old Fashioned and variants:
        {"name":"Classic Old Fashioned", "cat":"classic", "glass":"single"},
        {"name":"Fancy Free", "cat":["classic", "OF-V"], "glass":"single"},
        {"name":"Chrysanthemum", "cat":["classic", "OF-V"], "glass":"coupe"},
        {"name":"Tiki-Tiki Tom-Tom", "cat":"OF-V", "bar":"Thomas Waugh", "glass":"double"},

        # Martini and variants:
        {"name":"Classic Martini", "cat":"classic", "glass":"martini"},

        # Daiquiri and variants:
        {"name":"Classic Daiquiri", "cat":"classic", "glass":"coupe"},
        {"name":"D.W.B.", "cat":"daq-V", "glass":"coupe"},
    ]

    for coc in coc_list:
        new_coc = Cocktail.objects.using(db_alias).create(name=coc["name"])
        new_coc.category = coc["cat"]
        if coc.get("bar") is not None:
            new_coc.bartender = coc["bar"]
        new_coc.glassware = coc["glass"]
        new_coc.save()


def populate_recipedetail(apps,schema_editor):
    RecipeDetail = apps.get_model("cocktails", "RecipeDetail")
    Ingredient = apps.get_model("cocktails", "Ingredient")
    Cocktail = apps.get_model("cocktails", "Cocktail")
    db_alias = schema_editor.connection.alias

    recipe_list = [
        # {"coc":"", "ing":"", "aged":"", "quant":, "unit":"", "rec":""},
        # Old Fashioned and variants:
        {"coc":"Classic Old Fashioned", "ing":"Bourbon", "quant": 2, "unit":"oz"},
        {"coc":"Classic Old Fashioned", "ing":"Sugar Cube", "quant": 1, "unit":""},
        {"coc":"Classic Old Fashioned", "ing":"Angostura Bitters", "quant": 2, "unit":"dash"},
        {"coc":"Classic Old Fashioned", "ing":"Lemon", "quant": 1, "unit":"twist"},
        {"coc":"Classic Old Fashioned", "ing":"Orange", "quant": 1, "unit":"twist"},

        {"coc":"Fancy Free", "ing":"American Whiskey", "quant": 2, "unit":"oz", "rec":"Rittenhouse Rye"},
        {"coc":"Fancy Free", "ing":"Maraschino Liqueur", "quant": 0.5, "unit":"oz", "rec":"Luxardo Maraschino Liqueur"},
        {"coc":"Fancy Free", "ing":"Angostura Bitters", "quant": 1, "unit":"dash"},
        {"coc":"Fancy Free", "ing":"Death&Co House Orange Bitters", "quant": 1, "unit":"dash"},
        {"coc":"Fancy Free", "ing":"Orange", "quant": 1, "unit":"twist"},

        {"coc":"Chrysanthemum", "ing":"Dry Vermouth", "quant": 2.5, "unit":"oz", "rec":"Dolin Dry Vermouth"},
        {"coc":"Chrysanthemum", "ing":"Bénédictine", "quant": 0.5, "unit":"oz"},
        {"coc":"Chrysanthemum", "ing":"Absinthe", "quant": 1, "unit":"tsp", "rec":"Pernod Absinthe"},
        {"coc":"Chrysanthemum", "ing":"Orange", "quant": 1, "unit":"twist"},

        {"coc":"Tiki-Tiki Tom-Tom", "ing":"Aged English Rum", "quant": 1.5, "unit":"oz", "rec":"El Dorado 15-Year"},
        {"coc":"Tiki-Tiki Tom-Tom", "ing":"Aged English Rum", "quant": 0.5, "unit":"oz", "rec":"Scarlet Ibis Rum"},
        {"coc":"Tiki-Tiki Tom-Tom", "ing":"Drambuie", "quant": 0.5, "unit":"oz"},
        {"coc":"Tiki-Tiki Tom-Tom", "ing":"Strega", "quant": 1, "unit":"tsp"},
        {"coc":"Tiki-Tiki Tom-Tom", "ing":"Honey Syrup", "quant": 0.5, "unit":"tsp"},

        # Martini and variants:
        {"coc":"Classic Martini", "ing":"Gin", "quant": 2, "unit":"oz"},
        {"coc":"Classic Martini", "ing":"Dry Vermouth", "quant": 0.75, "unit":"oz"},
        {"coc":"Classic Martini", "ing":"Lemon", "quant": 1, "unit":"twist"},
        {"coc":"Classic Martini", "ing":"Olive", "quant": 1, "unit":"", "opt":True},

        # Daiquiri and variants:
        {"coc":"Classic Daiquiri", "ing":"White Spanish Rum", "quant": 2, "unit":"oz"},
        {"coc":"Classic Daiquiri", "ing":"White French Rhum", "quant": 0.25, "unit":"oz", "opt":True},
        {"coc":"Classic Daiquiri", "ing":"Fresh Lime Juice", "quant": 0.75, "unit":"oz"},
        {"coc":"Classic Daiquiri", "ing":"Simple Syrup", "quant": 0.75, "unit":"oz"},
        {"coc":"Classic Daiquiri", "ing":"Lime", "quant": 1, "unit":"wedge"},

        {"coc":"D.W.B.", "ing":"White French Rhum", "quant": 2, "unit":"oz", "rec":"La Favorite Rhum Agricole Blanc"},
        {"coc":"D.W.B.", "ing":"White Batavia Arrack", "quant": 0.5, "unit":"oz", "rec":"Van Oosten Batavia Arrack"},
        {"coc":"D.W.B.", "ing":"Fresh Lime Juice", "quant": 0.75, "unit":"oz"},
        {"coc":"D.W.B.", "ing":"Cane Sugar Syrup", "quant": 0.5, "unit":"oz"},
        {"coc":"D.W.B.", "ing":"Lime", "quant": 1, "unit":"wedge"},
    ]

    for rd in recipe_list:
        new_recipe = RecipeDetail(cocktail=Cocktail.objects.using(db_alias).get(name=rd["coc"]), ingredient=Ingredient.objects.using(db_alias).get(name=rd["ing"]))
        if rd.get("aged") is not None:
            new_recipe.aged = rd["aged"]
        new_recipe.quantity = rd["quant"]
        new_recipe.unit = rd["unit"]
        if rd.get("rec") is not None:
            new_recipe.recommended = rd["rec"]
        if rd.get("opt") is not None:
            new_recipe.optional = rd["opt"]
        new_recipe.save()

class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_ingredient),
        migrations.RunPython(populate_cocktail),
        migrations.RunPython(populate_recipedetail)
    ]
