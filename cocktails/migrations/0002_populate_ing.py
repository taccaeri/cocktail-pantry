from __future__ import unicode_literals

from django.db import migrations
from django.db import transaction


def populate_ingredient(apps, schema_editor):
    Ingredient = apps.get_model("cocktails", "Ingredient")
    db_alias = schema_editor.connection.alias

    ing_list = [
        # {"name":"", "cat":""},

        # Spirits:
        # Gin
        {"name":"Gin", "cat":"gin"},
        {"name":"Aged Gin", "cat":"gin"},
        {"name":"Navy-Strength Gin", "cat":"gin"},
        {"name":"Old Tom Gin", "cat":"gin"},
        {"name":"Sloe Gin", "cat":"gin"},
        {"name":"Genever", "cat":"gin"},
        {"name":"Borovička", "cat":"gin"},
        # Agave
        {"name":"Blanco Tequila", "cat":"agave"},
        {"name":"Reposado Tequila", "cat":"agave"},
        {"name":"Anejo Tequila", "cat":"agave"},
        {"name":"Mezcal", "cat":"agave"},
        # Rum
        {"name":"Aged English Rum", "cat":"rum"},
        {"name":"White English Rum", "cat":"rum"},
        {"name":"Aged Spanish Rum", "cat":"rum"},
        {"name":"White Spanish Rum", "cat":"rum"},
        {"name":"Aged Jamaican Rum", "cat":"rum"},
        {"name":"White Jamaican Rum", "cat":"rum"},
        {"name":"Rhum Agricole Aged", "cat":"rum"},
        {"name":"Rhum Agricole Blanc", "cat":"rum"},
        {"name":"White Batavia Arrack", "cat":"rum"},
        {"name":"Aged Batavia Arrack", "cat":"rum"},
        {"name":"Cachaça", "cat":"rum"},
        # Whisk(e)y
        {"name":"American Whiskey", "cat":"whisky"},
        {"name":"Irish Whiskey", "cat":"whisky"},
        {"name":"Japanese Whisky", "cat":"whisky"},
        {"name":"Rye Whiskey", "cat":"whisky"},

        {"name":"Islay Scotch Whisky", "cat":"whisky"},
        {"name":"Campbeltown Scotch Whisky", "cat":"whisky"},
        {"name":"Highland Scotch Whisky", "cat":"whisky"},
        {"name":"Lowland Scotch Whisky", "cat":"whisky"},
        {"name":"Speyside Scotch Whisky", "cat":"whisky"},
        
        {"name":"Bourbon", "cat":"whisky"},
        # Brandy
        {"name":"Brandy", "cat":"brandy"},
        {"name":"Pear Brandy", "cat":"brandy"},
        {"name":"Cognac", "cat":"brandy"},
        {"name":"Pisco", "cat":"brandy"},
        {"name":"Calvados", "cat":"brandy"},
        {"name":"Grappa", "cat":"brandy"},
        {"name":"Armagnac", "cat":"brandy"},
        {"name":"Eau de Vie", "cat":"brandy"},
        # Aquavit
        {"name":"Aquavit", "cat":"aquavit"},
        {"name":"Danish Aquavit", "cat":"aquavit"},
        {"name":"Swedish Aquavit", "cat":"aquavit"},
        {"name":"Norwegian Aquavit", "cat":"aquavit"},
        # Etc:
        {"name":"Vodka", "cat":"etc"},

        # Modifiers:
        # Liqueur:
        {"name":"Strega", "cat":"liqueur"},
        {"name":"Drambuie", "cat":"liqueur"},
        {"name":"Maraschino Liqueur", "cat":"liqueur"},
        {"name":"Bénédictine", "cat":"liqueur"},
        {"name":"Absinthe", "cat":"liqueur"},
        {"name":"Coffee Liqueur", "cat":"liqueur"},
        {"name":"White Crème De Menthe", "cat":"liqueur"},
        {"name":"Green Crème De Menthe", "cat":"liqueur"},
        {"name":"Royal Combier", "cat":"liqueur"},
        # Amaro:
        {"name":"Amaro Nonino", "cat":"amaro"},
        {"name":"Amaro Meletti", "cat":"amaro"},
        # Fortified Wine:
        {"name":"Red Vermouth", "cat":"wine"},
        {"name":"Dry Vermouth", "cat":"wine"},
        {"name":"Blanc Vermouth", "cat":"wine"},
        {"name":"Cocchi Americano", "cat":"wine"},
        {"name":"Suze", "cat":"wine"},
        {"name":"Sherry", "cat":"wine"},

        # Sweetener:
        {"name":"Granulated Sugar", "cat":"sweeteners"},
        {"name":"Sugar Cube", "cat":"sweeteners"},
        {"name":"Simple Syrup", "cat":"sweeteners"},
        {"name":"Demerara Syrup", "cat":"sweeteners"},
        {"name":"Demerara Gum Syrup", "cat":"sweeteners"},
        {"name":"Cane Sugar Syrup", "cat":"sweeteners"},
        {"name":"Honey", "cat":"sweeteners"},
        {"name":"Honey Syrup", "cat":"sweeteners"},
        {"name":"Ginger Syrup", "cat":"sweeteners"},
        {"name":"Maple Syrup", "cat":"sweeteners"},
        {"name":"Cinnamon Syrup", "cat":"sweeteners"},

        # Bitters:
        {"name":"Angostura Bitters", "cat":"bitters"},
        {"name":"Orange Bitters", "cat":"bitters"},
        {"name":"Death&Co House Orange Bitters"},
        {"name":"Peychaud's Bitters", "cat":"bitters"},
        {"name":"Xocolatl Mole Bitters", "cat":"bitters"},
        {"name":"Bittermens Hopped Grapefruit Bitters", "cat":"bitters"},

        # Emulsifiers:
        {"name":"Egg White", "cat":"emulsifiers"},
        {"name":"Aquafaba", "cat":"emulsifiers"},

        # Toppers:
        {"name":"Dry Sparkling Wine", "cat":"toppers"},
        {"name":"Dry Champagne", "cat":"toppers"},

        # Dry:
        {"name":"Salt", "cat":"dry"},
        {"name":"Chipotle Salt", "cat":"dry"},
        {"name":"Cinnamon", "cat":"dry"},

        # Fresh:
        {"name":"Lemon", "cat":"fresh"},
        {"name":"Fresh Lemon Juice"},
        {"name":"Lime", "cat":"fresh"},
        {"name":"Fresh Lime Juice"},
        {"name":"Orange", "cat":"fresh"},
        {"name":"Fresh Orange Juice"},
        {"name":"Grapefruit", "cat":"fresh"},
        {"name":"Fresh Grapefruit Juice"},
        {"name":"Celery", "cat":"fresh"},
        {"name":"Fresh Celery Juice"},
        {"name":"Cantaloupe", "cat":"fresh"},
        {"name":"Fresh Cantaloupe Juice"},
        {"name":"Ginger", "cat":"fresh"},
        {"name":"Mint", "cat":"fresh"},

        # Other:
        {"name":"Olive", "cat":"other"},

        # Concoctions:
        # Infusions:
        {"name":"Chamomile-Infused Cocchi Americano", "cat":"infusions"},
        # Solutions:
        {"name":"Salt Solution", "cat":"solutions"},
        {"name":"Champagne Acid Solution", "cat":"solutions"},

    ]

    for ing in ing_list:
        new_ing = Ingredient.objects.using(db_alias).create(name=ing["name"])
        if ing.get("cat") is not None:
            new_ing.category = ing["cat"]
        new_ing.save()


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_ingredient)
    ]
