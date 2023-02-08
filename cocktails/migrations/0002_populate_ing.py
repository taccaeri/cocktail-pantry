from __future__ import unicode_literals

from django.db import migrations
from django.db import transaction


def populate_ingredient(apps, schema_editor):
    Ingredient = apps.get_model("cocktails", "Ingredient")
    db_alias = schema_editor.connection.alias

    ing_list = [
        # {"name":"", "alt":"", "cat":""},

        # -- Spirits:
        # -- Gin
        {"name":"Gin", "cat":"gin"},
        {"name":"Plymouth Gin", "cat":"gin"},
        {"name":"London Dry Gin", "cat":"gin"},
        {"name":"Navy-Strength Gin", "cat":"gin"},
        {"name":"Old Tom Gin", "cat":"gin"},
        {"name":"Genever", "cat":"gin"},
        {"name":"Aged Gin", "cat":"gin"},
        # -- Agave
        {"name":"Blanco Tequila", "cat":"agave"},
        {"name":"Reposado Tequila", "cat":"agave"},
        {"name":"Anejo Tequila", "cat":"agave"},
        {"name":"Blanco Mezcal", "cat":"agave"},
        {"name":"Reposado Mezcal", "alt":"Madurado Mezcal", "cat":"agave"},
        {"name":"Anejo Mezcal", "alt":"Anejado Mezcal", "cat":"agave"},
        # -- Rum
        {"name":"White English Rum", "cat":"rum"},
        {"name":"Aged English Rum", "cat":"rum"},
        {"name":"White Spanish Rum", "cat":"rum"},
        {"name":"Aged Spanish Rum", "cat":"rum"},
        {"name":"White Jamaican Rum", "cat":"rum"},
        {"name":"Aged Jamaican Rum", "cat":"rum"},
        {"name":"White Batavia Arrack", "cat":"rum"},
        {"name":"Aged Batavia Arrack", "cat":"rum"},
        {"name":"Rhum Agricole Blanc", "cat":"rum"},
        {"name":"Rhum Agricole Aged", "cat":"rum"},
        {"name":"White Cachaça", "cat":"rum"},
        {"name":"Aged Cachaça", "cat":"rum"},
        {"name":"Black Strap Rum", "cat":"rum"},
        #--  Whisk(e)y
        {"name":"Rye Whiskey", "cat":"whisky"},
        {"name":"Bourbon", "cat":"whisky"},
        {"name":"Teenessee Sour Mash", "cat":"whisky"},
        {"name":"Japanese Whisky", "cat":"whisky"},
        {"name":"Irish Whiskey", "cat":"whisky"},   

        {"name":"Islay Scotch Whisky", "cat":"whisky"},
        {"name":"Campbeltown Scotch Whisky", "cat":"whisky"},
        {"name":"Highland Scotch Whisky", "cat":"whisky"},
        {"name":"Lowland Scotch Whisky", "cat":"whisky"},
        {"name":"Speyside Scotch Whisky", "cat":"whisky"},
        # -- Brandy
        # -- Aged:
        {"name":"Aged Brandy", "cat":"A-brandy"}, 
        {"name":"Cognac", "cat":"A-brandy"}, 
        {"name":"Armagnac", "cat":"A-brandy"}, 
        {"name":"Brandy de Jerez", "cat":"A-brandy"}, 
        {"name":"Calvados", "cat":"A-brandy"},
        {"name":"Aged Apple Brandy", "cat":"A-brandy"}, 
        # -- Unaged:
        {"name":"Grappa", "cat":"UA-brandy"}, 
        {"name":"Pisco", "cat":"UA-brandy"}, 
        {"name":"Blanche Armagnac", "cat":"UA-brandy"}, 
        {"name":"Pear Brandy", "alt":"Poire Eau de Vie", "cat":"UA-brandy"},
        {"name":"Cherry Brandy", "alt":"Kirschwasser Eau de Vie", "cat":"UA-brandy"},
        {"name":"Apple Brandy", "alt":"Pomme Eau de Vie", "cat":"UA-brandy"},
        {"name":"Raspberry Brandy", "alt":"Framboise Eau de Vie", "cat":"UA-brandy"},
        {"name":"Plum Brandy", "alt":"Slivovitz Eau de Vie", "cat":"UA-brandy"},
        # {"name":"Singani", "cat":"UA-brandy"}, 

        # -- Aquavit
        {"name":"Aquavit", "cat":"aquavit"},
        {"name":"Danish Aquavit", "cat":"aquavit"},
        {"name":"Swedish Aquavit", "cat":"aquavit"},
        {"name":"Norwegian Aquavit", "cat":"aquavit"},
        # -- Vodka:
        {"name":"Vodka", "cat":"vodka"},

        # -- Modifiers:
        # -- Liqueur:
        {"name":"Orange Liqueur", "alt":["Curacao", "Cointreau"], "cat":"gin"},
        {"name":"Mint Liqueur", "alt":["Creme de Menthe", "Menthe-Pastille"], "cat":"liqueur"},
        {"name":"Grapefruit Liqueur", "alt":"Pamplemousse", "cat":"liqueur"},
        {"name":"Blood Orange Liqueur", "cat":"liqueur"},
        {"name":"Apricot Liqueur", "cat":"liqueur"},
        {"name":"Coffee Liqueur", "cat":"liqueur"},
        {"name":"Elderflower Liqueur", "alt":"St-Germain", "cat":"liqueur"},
        {"name":"Strega", "cat":"liqueur"},
        {"name":"Drambuie", "cat":"liqueur"},
        {"name":"Maraschino Liqueur", "cat":"liqueur"},
        {"name":"Benedictine", "cat":"liqueur"},
        {"name":"Absinthe", "cat":"liqueur"},
        {"name":"Green Chartreuse", "cat":"liqueur"},
        {"name":"Yellow Chartreuse", "cat":"liqueur"},
        {"name":"Creme Yvette", "cat":"liqueur"},
        {"name":"Creme de Cacao", "cat":"liqueur"},
        {"name":"Amaretto", "cat":"liqueur"},
        {"name":"Sloe Gin", "cat":"liqueur"},
        # -- Amari:
        # light
        {"name":"Amaro Nonino", "cat":"amaro"},
        {"name":"Amaro Meletti", "cat":"amaro"},
        {"name":"Amaro Montenegro", "cat":"wine"},
        {"name":"Quintessentia", "cat":"wine"},
        # {"name":"Lo-Fi Gentian Amaro", "cat":"wine"},
        # medium
        # {"name":"Amaro Averna", "cat":"wine"},
        # {"name":"Amaro CioCiaro", "cat":"wine"},
        # {"name":"Bigallet China-China Amer", "cat":"wine"},
        {"name":"Ramazzotti", "cat":"wine"},
        {"name":"Cynar", "cat":"wine"},
        # {"name":"Cappelletti Pasubio Vino Amaro", "cat":"wine"},
        # {"name":"Amaro di Angostura", "cat":"wine"},
        # {"name":"Braulio Amaro", "cat":"wine"},
        # {"name":"Amaro Nardini", "cat":"wine"},
        # dense
        {"name":"Fernet", "cat":"wine"},
        {"name":"Luxardo Amaro Abano", "cat":"wine"},
        # {"name":"Capalleti Amaro Sfumato", "cat":"wine"},
        # {"name":"Forthave Spirits Marseille Amaro", "cat":"wine"},
        # {"name":"Fernet-Vallet", "cat":"wine"},
        # -- Fortified Wine:
        {"name":"Red Vermouth", "cat":"wine"},
        {"name":"Dry Vermouth", "cat":"wine"},
        {"name":"Blanc Vermouth", "cat":"wine"},
        {"name":"Cocchi Americano", "cat":"wine"},
        # {"name":"Lillet Blanc", "cat":"wine"},
        {"name":"Lillet Rouge", "cat":"wine"},
        # {"name":"Lillet Rosè", "cat":"wine"},
        {"name":"Aperol", "cat":"wine"},
        {"name":"Campari", "cat":"wine"},
        {"name":"Suze", "cat":"wine"},
        {"name":"Sherry", "cat":"wine"},
        {"name":"Port", "cat":"wine"},

        # -- Sweetener:
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
        {"name":"Orgeat", "cat":"sweeteners"},

        # -- Bitters:
        {"name":"Angostura Bitters", "cat":"bitters"},
        {"name":"Orange Bitters", "cat":"bitters"},
        {"name":"Death&Co House Orange Bitters"},
        {"name":"Peychaud's Bitters", "cat":"bitters"},
        {"name":"Xocolatl Mole Bitters", "cat":"bitters"},
        {"name":"Bittermens Hopped Grapefruit Bitters", "cat":"bitters"},
        {"name":"Bitter Truth Aromatic Bitters", "cat":"bitters"},

        # -- Emulsifiers:
        {"name":"Egg White", "cat":"emulsifiers"},
        {"name":"Aquafaba", "cat":"emulsifiers"},

        # -- Toppers:
        {"name":"Dry Champagne", "cat":"toppers"},

        # -- Dry:
        {"name":"Salt", "cat":"dry"},
        {"name":"Chipotle Salt", "cat":"dry"},
        {"name":"Cinnamon Stick", "cat":"dry"},
        {"name":"Nutmeg", "cat":"dry"},

        # -- Fresh:
        {"name":"Lemon", "cat":"fresh"},
        {"name":"Fresh Lemon Juice"},
        {"name":"Lime", "cat":"fresh"},
        {"name":"Fresh Lime Juice"},
        {"name":"Orange", "cat":"fresh"},
        {"name":"Fresh Orange Juice"},
        {"name":"Grapefruit", "cat":"fresh"},
        {"name":"Fresh Grapefruit Juice"},
        {"name":"Ginger", "cat":"fresh"},
        {"name":"Mint", "cat":"fresh"},
        {"name":"Basil", "cat":"fresh"},
        {"name":"Cilantro", "cat":"fresh"},
        {"name":"Sage", "cat":"fresh"},
        {"name":"Celery", "cat":"fresh"},
        {"name":"Fresh Celery Juice"},
        {"name":"Cantaloupe", "cat":"fresh"},
        {"name":"Fresh Cantaloupe Juice"},
        {"name":"Apple", "cat":"fresh"},
        {"name":"Fresh Apple Juice"},
        {"name":"Carrot", "cat":"fresh"},
        {"name":"Fresh Carrot Juice"},
        {"name":"Watermelon", "cat":"fresh"},
        {"name":"Fresh Watermelon Juice"},       
        {"name":"Pineapple", "cat":"fresh"},
        {"name":"Fresh Pineapple Juice"},
        {"name":"Cucumber", "cat":"fresh"},
        {"name":"Peach", "cat":"fresh"},
        {"name":"Nectarine", "cat":"fresh"},
        {"name":"Pear", "cat":"fresh"},
        {"name":"Strawberry", "cat":"fresh"},
        {"name":"Raspberry", "cat":"fresh"},
        {"name":"Blackberry", "cat":"fresh"},
        {"name":"Cherry", "cat":"fresh"},
        {"name":"Grape", "cat":"fresh"},
        {"name":"Cherry Tomato", "cat":"fresh"},
        {"name":"Kaffir Lime Leaf", "cat":"fresh"},

        # Other:
        {"name":"Olive", "cat":"other"},
        {"name":"Brandied Cherry", "cat":"other"},
        {"name":"Chocolate", "cat":"other"},

        # Concoctions:
        # Infusions:
        {"name":"Chamomile-Infused Cocchi Americano", "cat":"infusions"},
        # Solutions:
        {"name":"Salt Solution", "cat":"solutions"},
        {"name":"Champagne Acid Solution", "cat":"solutions"},
    ]

    for ing in ing_list:
        new_ing = Ingredient.objects.using(db_alias).create(name=ing["name"])
        if ing.get("alt") is not None:
            new_ing.altname = ing["alt"]
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
