from __future__ import unicode_literals

from django.db import migrations
from django.db import transaction


def populate_recipedetail(apps,schema_editor):
    RecipeDetail = apps.get_model("cocktails", "RecipeDetail")
    Ingredient = apps.get_model("cocktails", "Ingredient")
    Cocktail = apps.get_model("cocktails", "Cocktail")
    db_alias = schema_editor.connection.alias

    recipe_list = [
        # {"coc":"", "ing":"", "quant":, "unit":"", "rec":""},

        # Gin Shaken:
        {"coc":"Bella Luna", "ing":"Plymouth Gin", "quant":2, "unit":"oz"},
        {"coc":"Bella Luna", "ing":"Elderflower Liqueur", "quant":0.75, "unit":"oz"},
        {"coc":"Bella Luna", "ing":"Creme Yvette", "quant":0.5, "unit":"oz"},
        {"coc":"Bella Luna", "ing":"Fresh Lemon Juice", "quant":0.75, "unit":"oz"},
        {"coc":"Bella Luna", "ing":"Simple Syrup", "quant":1, "unit":"tsp"},

        # Gin Stirred:
        {"coc":"European Union", "ing":"Old Tom Gin", "quant":1.5, "unit":"oz", "rec":"Hayman's Old Tom Gin"},
        {"coc":"European Union", "ing":"Red Vermouth", "quant":1, "unit":"oz", "rec":"Martini Sweet Vermouth"},
        {"coc":"European Union", "ing":"Calvados", "quant":0.5, "unit":"oz", "rec":"Busnel VSOP Calvados"},
        {"coc":"European Union", "ing":"Strega", "quant":1, "unit":"tsp"},
        {"coc":"European Union", "ing":"Bitter Truth Aromatic Bitters", "quant":1, "unit":"dash"},

        # Rum Shaken:
        {"coc":"Flor de Jerez", "ing":"Aged Jamaican Rum", "quant":0.5, "unit":"oz", "rec":"Appleton Estate Reserve Rum"},
        {"coc":"Flor de Jerez", "ing":"Sherry", "quant":1.5, "unit":"oz", "rec":"Lustau Amontillado Sherry"},
        {"coc":"Flor de Jerez", "ing":"Apricot Liqueur", "quant":0.25, "unit":"oz", "rec":"Rothman & Winter Apricot Liqueur"},
        {"coc":"Flor de Jerez", "ing":"Fresh Lemon Juice", "quant":0.75, "unit":"oz"},
        {"coc":"Flor de Jerez", "ing":"Cane Sugar Syrup", "quant":0.5, "unit":"oz"},
        {"coc":"Flor de Jerez", "ing":"Angostura Bitters", "quant":1, "unit":"dash"},

        # Rum Stirred:
        {"coc":"Arrack Strap", "ing":"Black Strap Rum", "quant":1, "unit":"oz", "rec":"Cruzan Black Strap Rum"},
        {"coc":"Arrack Strap", "ing":"White Batavia Arrack", "quant":1, "unit":"oz", "rec":"Van Oosten Batavia Arrack"},
        {"coc":"Arrack Strap", "ing":"Red Vermouth", "quant":1, "unit":"oz", "rec":"Cocchi Vermouth di Torino"},
        {"coc":"Arrack Strap", "ing":"Campari", "quant":1, "unit":"tsp"},
        {"coc":"Arrack Strap", "ing":"Demerara Syrup", "quant":0.5, "unit":"oz"},
        {"coc":"Arrack Strap", "ing":"Xocolatl Mole Bitters", "quant":2, "unit":"dash"},
        {"coc":"Arrack Strap", "ing":"Orange Bitters", "quant":2, "unit":"dash"},
        {"coc":"Arrack Strap", "ing":"Orange", "quant":1, "unit":"twist"},

        # Agave Shaken:
        {"coc":"Ghost of Mazagran", "ing":"Blanco Tequila", "quant": 1, "unit":"oz"},
        {"coc":"Ghost of Mazagran", "ing":"Blanco Mezcal", "quant": 1, "unit":"oz"},
        {"coc":"Ghost of Mazagran", "ing":"Coffee Liqueur", "quant": 0.5, "unit":"oz", "rec":"Mr.Black"},
        {"coc":"Ghost of Mazagran", "ing":"Red Vermouth", "quant": 0.5, "unit":"oz", "rec":"Punt e Mes"},
        {"coc":"Ghost of Mazagran", "ing":"Fresh Lemon Juice", "quant": 0.5, "unit":"oz"},
        {"coc":"Ghost of Mazagran", "ing":"Egg White", "quant": 0.5},
        {"coc":"Ghost of Mazagran", "ing":"Chipotle Salt", "quant": 1, "unit":"pinch"},
        {"coc":"Ghost of Mazagran", "ing":"Xocolatl Mole Bitters", "quant":3, "unit":"dash"},

        {"coc":"Almond Brother", "ing":"Reposado Tequila", "quant":2, "unit":"oz", "rec":"Siete Leguas Reposado Tequila"},
        {"coc":"Almond Brother", "ing":"Amaretto", "quant":0.25, "unit":"oz"},
        {"coc":"Almond Brother", "ing":"Apricot Liqueur", "quant":1, "unit":"tsp", "rec":"Rothman & Winter Apricot Liqueur"},
        {"coc":"Almond Brother", "ing":"Fresh Lime Juice", "quant":0.75, "unit":"oz"},
        {"coc":"Almond Brother", "ing":"Orgeat", "quant":0.25, "unit":"oz"},
        {"coc":"Almond Brother", "ing":"Maple Syrup", "quant":0.25, "unit":"oz"},

        # Agave Stirred:
        {"coc":"Coralillo", "ing":"Anejo Tequila", "quant":1.5, "unit":"oz", "rec":"El Tesoro Anejo Tequila"},
        {"coc":"Coralillo", "ing":"Yellow Chartreuse", "quant":0.75, "unit":"oz"},
        {"coc":"Coralillo", "ing":"Calvados", "quant":0.75, "unit":"oz", "rec":"Busnel VSOP Calvados"},
        {"coc":"Coralillo", "ing":"Pear Brandy", "quant":0.25, "unit":"oz", "rec":"Clear Creek Pear Brandy"},
        {"coc":"Coralillo", "ing":"Apple", "quant":1, "unit":"slice"},

        # Whisk(e)y Shaken:
        {"coc":"Ginger Man", "ing":"Islay Scotch Whisky", "quant":1.5, "unit":"oz", "rec":"Laphroaig 10-Year Single Malt Scotch"},
        {"coc":"Ginger Man", "ing":"Fresh Cantaloupe Juice", "quant":0.75, "unit":"oz"},
        {"coc":"Ginger Man", "ing":"Fresh Lemon Juice", "quant":0.75, "unit":"oz"},
        {"coc":"Ginger Man", "ing":"Ginger Syrup", "quant":0.5, "unit":"oz"},
        {"coc":"Ginger Man", "ing":"Angostura Bitters", "quant":1, "unit":"dash"},

        {"coc":"19th Century", "ing":"Bourbon", "quant":1.5, "unit":"oz", "rec":"Woodford Reserve Bourbon"},
        {"coc":"19th Century", "ing":"Lillet Rouge", "quant":0.75, "unit":"oz"},
        {"coc":"19th Century", "ing":"Creme de Cacao", "quant":0.75, "unit":"oz"},
        {"coc":"19th Century", "ing":"Fresh Lemon Juice", "quant":0.75, "unit":"oz"},

        # Whisk(e)y Stirred:
        {"coc":"The Dangerous Summer", "ing":"Japanese Whisky", "quant":1.5, "unit":"oz", "rec":"Yamazaki 12-Year Whiskey"},
        {"coc":"The Dangerous Summer", "ing":"Red Vermouth", "quant":0.75, "unit":"oz", "rec":"Dolin Rouge Vermouth"},
        {"coc":"The Dangerous Summer", "ing":"Blood Orange Liqueur", "quant":0.5, "unit":"oz", "rec":"Solerno Blood Orange Liqueur"},
        {"coc":"The Dangerous Summer", "ing":"Cherry Brandy", "quant":0.5, "unit":"oz", "rec":"Massenez Kirsch Vieux Cherry Brandy"},
        {"coc":"The Dangerous Summer", "ing":"Orange", "quant":1, "unit":"twist"},

        # Brandy Shaken:
        {"coc":"Enchanted Orchard", "ing":"Pisco", "quant":1.5, "unit":"oz", "rec":"Campo de Encanto Acholado Pisco"},
        {"coc":"Enchanted Orchard", "ing":"Calvados", "quant":0.5, "unit":"oz", "rec":"Busnel VSOP Calvados"},
        {"coc":"Enchanted Orchard", "ing":"Benedictine", "quant":0.5, "unit":"oz"},
        {"coc":"Enchanted Orchard", "ing":"Fresh Pineapple Juice", "quant":0.5, "unit":"oz"},
        {"coc":"Enchanted Orchard", "ing":"Fresh Lemon Juice", "quant":0.5, "unit":"oz"},
        {"coc":"Enchanted Orchard", "ing":"Honey Syrup", "quant":0.5, "unit":"oz"},
        {"coc":"Enchanted Orchard", "ing":"Cinnamon Stick", "quant":1},

        # Brandy Stirred:

        # Sparkling Cocktail:
        {"coc":"Champagne Cocktail", "ing":"Dry Champagne", "quant":2, "unit":"oz"},
        {"coc":"Champagne Cocktail", "ing":"Sugar Cube", "quant":1},
        {"coc":"Champagne Cocktail", "ing":"Angostura Bitters", "quant":3, "unit":"dash"},

        {"coc":"The Field Marshall", "ing":"Armagnac", "quant":1, "unit":"oz", "rec":"Tariquet Classique VS Bas-Armagnac"},
        {"coc":"The Field Marshall", "ing":"Orange Liqueur", "quant":0.5, "unit":"oz", "rec":"Royal Combier"},
        {"coc":"The Field Marshall", "ing":"Angostura Bitters", "quant":2, "unit":"dash"},
        {"coc":"The Field Marshall", "ing":"Peychaud's Bitters", "quant":2, "unit":"dash"},
        {"coc":"The Field Marshall", "ing":"Dry Champagne", "quant":4, "unit":"oz"},
        {"coc":"The Field Marshall", "ing":"Lemon", "quant":1, "unit":"twist"},

        {"coc":"Pretty Wings", "ing":"Chamomile-Infused Cocchi Americano", "quant":0.5, "unit":"oz"},
        {"coc":"Pretty Wings", "ing":"Suze", "quant":1, "unit":"tsp"},
        {"coc":"Pretty Wings", "ing":"Bittermens Hopped Grapefruit Bitters", "quant":1, "unit":"dash"},
        {"coc":"Pretty Wings", "ing":"Dry Champagne", "quant":5, "unit":"oz"},
        {"coc":"Pretty Wings", "ing":"Lemon", "quant":1, "unit":"wheel"},

        {"coc":"Celebrate", "ing":"Pear Brandy", "quant":0.5, "unit":"oz", "rec":"Clear Creek"},
        {"coc":"Celebrate", "ing":"Sherry", "quant":0.25, "unit":"oz", "rec":"Lustau Jarana Fino Sherry"},
        {"coc":"Celebrate", "ing":"Reposado Tequila", "quant":1, "unit":"tsp", "rec":"Fortaleza Reposado Tequila"},
        {"coc":"Celebrate", "ing":"Cinnamon Syrup", "quant":0.25, "unit":"oz"},
        {"coc":"Celebrate", "ing":"Champagne Acid Solution", "quant":0.5, "unit":"tsp"},
        {"coc":"Celebrate", "ing":"Dry Champagne", "quant":4, "unit":"oz"},

        # Fortified Wine Cocktails:

        # Punch:

        # Julep:
        {"coc":"Mint Julep", "ing":"Bourbon", "quant":2, "unit":"oz", "rec":"Buffalo Trace Bourbon"},
        {"coc":"Mint Julep", "ing":"Simple Syrup", "quant":0.25, "unit":"oz"},
        {"coc":"Mint Julep", "ing":"Mint", "quant":1, "unit":"bqt"},

        # Flips and Fizzes:

        # Swizzles:

        # Aquavit:

        # Martini and variants:
        {"coc":"Classic Martini", "ing":"Gin", "quant": 2, "unit":"oz"},
        {"coc":"Classic Martini", "ing":"Dry Vermouth", "quant": 0.75, "unit":"oz"},
        {"coc":"Classic Martini", "ing":"Lemon", "quant": 1, "unit":"twist"},
        {"coc":"Classic Martini", "ing":"Olive", "quant": 1, "unit":"", "opt":True},

        # Sazerac and variants: 
        {"coc":"Sazerac", "ing":"Absinthe", "quant": 1, "unit":"rinse", "rec":"Pontarlier Absinthe"},
        {"coc":"Sazerac", "ing":"Rye Whiskey", "quant": 1.5, "unit":"oz", "rec":"Rittenhouse Rye"},
        {"coc":"Sazerac", "ing":"Cognac", "quant": 0.5, "unit":"oz", "rec":"Pierre Ferrand 1840 Cognac"},
        {"coc":"Sazerac", "ing":"Demerara Gum Syrup", "quant": 1, "unit":"tsp"},
        {"coc":"Sazerac", "ing":"Peychaud's Bitters", "quant": 4, "unit":"dash"},
        {"coc":"Sazerac", "ing":"Angostura Bitters", "quant": 1, "unit":"dash"},
        {"coc":"Sazerac", "ing":"Lemon", "quant": 1, "unit":"twist"},

        # Negroni and variants:

        # Daiquiri and variants:
        {"coc":"Classic Daiquiri", "ing":"White Spanish Rum", "quant": 2, "unit":"oz"},
        {"coc":"Classic Daiquiri", "ing":"Rhum Agricole Blanc", "quant": 0.25, "unit":"oz", "opt":True},
        {"coc":"Classic Daiquiri", "ing":"Fresh Lime Juice", "quant": 0.75, "unit":"oz"},
        {"coc":"Classic Daiquiri", "ing":"Simple Syrup", "quant": 0.75, "unit":"oz"},
        {"coc":"Classic Daiquiri", "ing":"Lime", "quant": 1, "unit":"wedge"},

        {"coc":"D.W.B.", "ing":"Rhum Agricole Blanc", "quant": 2, "unit":"oz", "rec":"La Favorite Rhum Agricole Blanc"},
        {"coc":"D.W.B.", "ing":"White Batavia Arrack", "quant": 0.5, "unit":"oz", "rec":"Van Oosten Batavia Arrack"},
        {"coc":"D.W.B.", "ing":"Fresh Lime Juice", "quant": 0.75, "unit":"oz"},
        {"coc":"D.W.B.", "ing":"Cane Sugar Syrup", "quant": 0.5, "unit":"oz"},
        {"coc":"D.W.B.", "ing":"Lime", "quant": 1, "unit":"wedge"},

        {"coc":"Rumor Mill", "ing":"Dry Champagne", "quant":1.5, "unit":"oz"},
        {"coc":"Rumor Mill", "ing":"Rhum Agricole Blanc", "quant":1, "unit":"oz", "rec":"La Favorite Rhum Agricole Blanc"},
        {"coc":"Rumor Mill", "ing":"Dry Vermouth", "quant":0.5, "unit":"oz", "rec":"Dolin Dry Vermouth"},
        {"coc":"Rumor Mill", "ing":"Cane Sugar Syrup", "quant":0.5, "unit":"oz"},
        {"coc":"Rumor Mill", "ing":"Fresh Celery Juice", "quant":0.5, "unit":"oz"},
        {"coc":"Rumor Mill", "ing":"Fresh Lime Juice", "quant":0.5, "unit":"oz"},
        {"coc":"Rumor Mill", "ing":"Absinthe", "quant":1, "unit":"dash"},

        # Manhattan and variants:

        # Old Fashioned and variants:
        {"coc":"Classic Old Fashioned", "ing":"Bourbon", "quant": 2, "unit":"oz"},
        {"coc":"Classic Old Fashioned", "ing":"Sugar Cube", "quant": 1, "unit":""},
        {"coc":"Classic Old Fashioned", "ing":"Angostura Bitters", "quant": 2, "unit":"dash"},
        {"coc":"Classic Old Fashioned", "ing":"Lemon", "quant": 1, "unit":"twist"},
        {"coc":"Classic Old Fashioned", "ing":"Orange", "quant": 1, "unit":"twist"},

        {"coc":"Fancy Free", "ing":"Rye Whiskey", "quant": 2, "unit":"oz", "rec":"Rittenhouse Rye"},
        {"coc":"Fancy Free", "ing":"Maraschino Liqueur", "quant": 0.5, "unit":"oz", "rec":"Luxardo Maraschino Liqueur"},
        {"coc":"Fancy Free", "ing":"Angostura Bitters", "quant": 1, "unit":"dash"},
        {"coc":"Fancy Free", "ing":"Orange Bitters", "quant": 1, "unit":"dash"},
        {"coc":"Fancy Free", "ing":"Orange", "quant": 1, "unit":"twist"},

        {"coc":"Chrysanthemum", "ing":"Dry Vermouth", "quant": 2.5, "unit":"oz", "rec":"Dolin Dry Vermouth"},
        {"coc":"Chrysanthemum", "ing":"Benedictine", "quant": 0.5, "unit":"oz"},
        {"coc":"Chrysanthemum", "ing":"Absinthe", "quant": 1, "unit":"tsp", "rec":"Pernod Absinthe"},
        {"coc":"Chrysanthemum", "ing":"Orange", "quant": 1, "unit":"twist"},

        {"coc":"Tiki-Tiki Tom-Tom", "ing":"Aged English Rum", "quant": 1.5, "unit":"oz", "rec":"El Dorado 15-Year"},
        {"coc":"Tiki-Tiki Tom-Tom", "ing":"Aged English Rum", "quant": 0.5, "unit":"oz", "rec":"Scarlet Ibis Rum"},
        {"coc":"Tiki-Tiki Tom-Tom", "ing":"Drambuie", "quant": 0.5, "unit":"oz"},
        {"coc":"Tiki-Tiki Tom-Tom", "ing":"Strega", "quant": 1, "unit":"tsp"},
        {"coc":"Tiki-Tiki Tom-Tom", "ing":"Honey Syrup", "quant": 0.5, "unit":"tsp"},

        {"coc":"Exit Strategy", "ing":"Amaro Nonino", "quant": 1.5, "unit":"oz"},
        {"coc":"Exit Strategy", "ing":"Aged Brandy", "quant": 0.75, "unit":"oz", "rec":"Germain-Robin Craft-Method brandy"},
        {"coc":"Exit Strategy", "ing":"Amaro Meletti", "quant": 0.25, "unit":"oz"},
        {"coc":"Exit Strategy", "ing":"Salt Solution", "quant": 6, "unit":"drop"},
        {"coc":"Exit Strategy", "ing":"Orange", "quant": 1, "unit":"twist"},

        {"coc":"Ti' Punch", "ing":"Lime", "quant": 1, "unit":"peel"},
        {"coc":"Ti' Punch", "ing":"Cane Sugar Syrup", "quant": 1, "unit":"tsp"},
        {"coc":"Ti' Punch", "ing":"Rhum Agricole Blanc", "quant": 2, "unit":"oz", "rec":"La Favorite Couer de Canne"},

        {"coc":"Stinger", "ing":"Cognac", "quant": 2, "unit":"oz", "rec":"Pierre Ferrand Ambre Cognac"},
        {"coc":"Stinger", "ing":"Mint Liqueur", "quant": 0.5, "unit":"oz"},
        {"coc":"Stinger", "ing":"Simple Syrup", "quant": 1, "unit":"tsp"},
        {"coc":"Stinger", "ing":"Mint", "quant": 1, "unit":"sprig"},

        {"coc":"Monte Carlo", "ing":"Rye Whiskey", "quant": 2, "unit":"oz", "rec":"Rittenhouse Rye"},
        {"coc":"Monte Carlo", "ing":"Benedictine", "quant": 0.5, "unit":"oz"},
        {"coc":"Monte Carlo", "ing":"Angostura Bitters", "quant": 2, "unit":"dash"},
        {"coc":"Monte Carlo", "ing":"Lemon", "quant": 1, "unit":"twist"},
    ]

    for rd in recipe_list:
        new_recipe = RecipeDetail(cocktail=Cocktail.objects.using(db_alias).get(name=rd["coc"]), ingredient=Ingredient.objects.using(db_alias).get(name=rd["ing"]))
        new_recipe.quantity = rd["quant"]
        if rd.get("unit") is not None:
            new_recipe.unit = rd["unit"]
        if rd.get("rec") is not None:
            new_recipe.recommended = rd["rec"]
        if rd.get("opt") is not None:
            new_recipe.optional = rd["opt"]
        new_recipe.save()


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0003_populate_coc'),
    ]

    operations = [
        migrations.RunPython(populate_recipedetail)
    ]
