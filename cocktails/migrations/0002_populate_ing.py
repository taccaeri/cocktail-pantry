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
        {"name":"Plymouth Gin", "cat":"gin"}, 
        # {"name":"London Dry Gin", "cat":"gin"}, 
        {"name":"Old Tom Gin", "cat":"gin"}, 
        # {"name":"Genever", "cat":"gin"}, 
        # {"name":"American Gin", "cat":"gin"}, 
        {"name":"Navy-Strength Gin", "cat":"gin"},
        # {"name":"Aged Gin", "cat":"gin"}, 

        # -- Agave 
        {"name":"Blanco Tequila", "cat":"agave"}, 
        {"name":"Reposado Tequila", "cat":"agave"}, 
        {"name":"Anejo Tequila", "cat":"agave"}, 
        {"name":"Blanco Mezcal", "cat":"agave"}, 
        # {"name":"Madurado Mezcal", "cat":"agave"}, 
        # {"name":"Anejado Mezcal", "cat":"agave"}, 

        # -- Rum 
        {"name":"English Rum", "cat":"rum"}, 
        # {"name":"English White Rum", "cat":"rum"}, 
        {"name":"Spanish Rum", "cat":"rum"}, 
        {"name":"Spanish White Rum", "cat":"rum"}, 
        {"name":"Jamaican Rum", "cat":"rum"}, 
        # {"name":"Jamaican White Rum", "cat":"rum"}, 
        {"name":"Rhum Agricole Blanc", "cat":"rum"}, 
        # {"name":"Rhum Agricole Ambre", "cat":"rum"}, 
        # {"name":"Demerara Rum", "cat":"rum"}, 
        # {"name":"Demerara White Rum", "cat":"rum"},
        # {"name":"Demerara Overproof Rum", "cat":"rum"}, 
        {"name":"Black Strap Rum", "cat":"rum"}, 
        # {"name":"Cachaça", "cat":"rum"}, 
        {"name":"Batavia Arrack", "cat":"rum"}, 

        # --  Whisk(e)y 
        {"name":"Rye Whiskey", "cat":"whisky"}, 
        # {"name":"Oat Whiskey", "cat":"whisky"},
        # {"name":"Wheat Whiskey", "cat":"whisky"},
        {"name":"Bourbon", "cat":"whisky"},
        {"name":"Japanese Whisky", "cat":"whisky"}, 
        {"name":"Irish Whiskey", "cat":"whisky"},	
  
        {"name":"Islay Scotch", "cat":"whisky"}, 
        # {"name":"Campbeltown Scotch", "cat":"whisky"}, 
        # {"name":"Highland Scotch", "cat":"whisky"}, 
        # {"name":"Lowland Scotch", "cat":"whisky"}, 
        # {"name":"Speyside Scotch", "cat":"whisky"}, 
        # {"name":"Blended Scotch", "cat":"whisky"}, 


        # -- Brandy 

        # -- Aged: 
        {"name":"Cognac", "cat":"brandy"},  
        {"name":"Armagnac", "cat":"brandy"},  
        {"name":"Calvados", "cat":"brandy"}, 
        {"name":"Apple Brandy", "cat":"brandy"},  
        {"name":"American Brandy", "cat":"brandy"},
        # -- Unaged: 
        # {"name":"Grappa", "cat":"UA-brandy"},  
        {"name":"Pisco", "cat":"UA-brandy"},  
        {"name":"Pear Brandy", "alt":"Poire Eau de Vie", "cat":"brandy"}, 
        {"name":"Cherry Brandy", "alt":"Kirschwasser Eau de Vie", "cat":"brandy"}, 
        # {"name":"Raspberry Brandy", "alt":"Framboise Eau de Vie", "cat":"UA-brandy"}, 
        # {"name":"Plum Brandy", "alt":"Slivovitz Eau de Vie", "cat":"UA-brandy"}, 
         
        # -- Misc 
        {"name":"Aquavit", "cat":"misc"},
        # {"name":"Chocolate Vodka", "cat":"misc"}, 
  

        # -- Modifiers: 

        # -- Liqueur: 
        {"name":"Orange Liqueur", "alt":["Curacao", "Cointreau"], "cat":"liqueur"}, 
        {"name":"Milk & Honey House Curacao"},
        {"name":"Maraschino Liqueur", "cat":"liqueur"},
        # {"name":"Grapefruit Liqueur", "alt":"Pamplemousse", "cat":"liqueur"}, 
        {"name":"Blood Orange Liqueur", "cat":"liqueur"}, 
        {"name":"Apricot Liqueur", "cat":"liqueur"}, 
        {"name":"Coffee Liqueur", "cat":"liqueur"}, 
        {"name":"Elderflower Liqueur", "alt":"St-Germain", "cat":"liqueur"}, 
        # {"name":"Coconut Liqueur", "cat":"liqueur"}, 
        # {"name":"Alpine Liqueur", "cat":"liqueur"},
        {"name":"Pear Liqueur", "cat":"liqueur"},
        {"name":"Rose Hip Liqueur", "cat":"liqueur"},
        {"name":"Sloe Berry Liqueur", "alt":["Pacharan", "Sloe Gin"],  "cat":"liqueur"}, 
        # {"name":"Caraway Liqueur", "cat":"liqueur"},
        {"name":"Creme Yvette", "cat":"liqueur"}, 
        {"name":"Creme de Cacao", "cat":"liqueur"}, 
        {"name":"Creme de Menthe", "cat":"liqueur"}, 
        {"name":"Creme de Peche", "cat":"liqueur"},
        # {"name":"Creme de Fraise", "cat":"liqueur"},
        {"name":"Banane du Bresil", "alt":"Creme de Banane", "cat":"liqueur"},
        # {"name":"Creme de Mure", "cat":"liqueur"},
        # {"name":"Creme de Violette", "cat":"liqueur"},
        # {"name":"Creme de Cassis", "cat":"liqueur"},
        {"name":"Allspice Dram", "cat":"liqueur"},
        {"name":"Amaretto", "cat":"liqueur"}, 
        {"name":"Strega", "cat":"liqueur"}, 
        {"name":"Drambuie", "cat":"liqueur"},
        {"name":"Velvet Falernum", "cat":"liqueur"},
        {"name":"Benedictine", "cat":"liqueur"}, 
        {"name":"Absinthe", "cat":"liqueur"}, 
        {"name":"Suze", "cat":"liqueur"}, 
        # {"name":"Green Chartreuse", "cat":"liqueur"}, 
        {"name":"Yellow Chartreuse", "cat":"liqueur"}, 
        # {"name":"Swedish Punsch", "cat":"liqueur"},
        # {"name":"Galliano", "cat":"liqueur"},

        # -- Amari:

        {"name":"Amaro Nonino", "cat":"amari"}, 
        {"name":"Amaro Meletti", "cat":"amari"},  
        {"name":"Amaro Averna", "cat":"amari"}, 
        # {"name":"Amaro Abano", "cat":"wine"}, 
        # {"name":"Amaro Lucano", "cat":"wine"}, 
        {"name":"Amaro CioCiaro", "cat":"amari"},
        # {"name":"Amaro Nardini", "cat":"amari"}, 
        {"name":"Amaro Montenegro", "cat":"amari"}, 
        {"name":"Ramazzotti", "cat":"amari"},
        # {"name":"Cynar", "cat":"amari"}, 
        # {"name":"Cardamaro", "cat":"amari"},
        # {"name":"Fernet", "cat":"amari"}, 
        
        # -- Fortified Wine: 

        {"name":"Red Vermouth", "cat":"wine"}, 
        {"name":"Dry Vermouth", "cat":"wine"}, 
        {"name":"Blanc Vermouth", "cat":"wine"}, 
        {"name":"Amontillado Sherry", "cat":"wine"}, 
        {"name":"Cream Sherry", "cat":"wine"},
        # {"name":"Port", "cat":"wine"}, 
         # – Aperitivo:
        {"name":"Campari", "cat":"wine"}, 
        {"name":"Aperol", "cat":"wine"}, 
         # – Aperitif:
        {"name":"Lillet Blanc", "cat":"wine"}, 
        {"name":"Lillet Rouge", "cat":"wine"}, 
        # {"name":"Lillet Rose", "cat":"wine"},
        {"name":"Cocchi Americano", "cat":"wine"},
        # {"name":"Gentian-Quina", "cat":"wine"},

  
        # -- Sweetener: 

        {"name":"Granulated Sugar", "cat":"sweeteners"}, 
        {"name":"Sugar Cube", "cat":"sweeteners"}, 
        {"name":"Simple Syrup", "cat":"sweeteners"}, 
        {"name":"Demerara Syrup", "cat":"sweeteners"}, 
        {"name":"Demerara Gum Syrup", "cat":"sweeteners"}, 
        {"name":"Cane Sugar Syrup", "cat":"sweeteners"}, 
        {"name":"Confectionery Sugar", "cat":"sweeteners"}, 
        # {"name":"Honey", "cat":"sweeteners"}, 
        {"name":"Honey Syrup", "cat":"sweeteners"}, 
        {"name":"Ginger Syrup", "cat":"sweeteners"}, 
        {"name":"Maple Syrup", "cat":"sweeteners"}, 
        {"name":"Cinnamon Syrup", "cat":"sweeteners"}, 
        {"name":"Orgeat", "cat":"sweeteners"},
        {"name":"Grenadine", "cat":"sweeteners"}, 
        # {"name":"Agave Nectar", "cat":"sweeteners"}, 
        # {"name":"Vanilla Syrup", "cat":"sweeteners"}, 
  

        # -- Bitters: 

        {"name":"Orange Bitters", "cat":"bitters"}, 
        {"name":"Death & Co House Orange Bitters"}, 
        {"name":"Angostura Bitters", "cat":"bitters"},
        {"name":"Bitter Truth Aromatic Bitters", "cat":"bitters"}, 
        {"name":"Peychaud's Bitters", "cat":"bitters"},
        {"name":"Xocolatl Mole Bitters", "cat":"bitters"}, 
        {"name":"Hopped Grapefruit Bitters", "cat":"bitters"}, 
        {"name":"Celery Bitters", "cat":"bitters"}, 
        {"name":"Castilian Bitters", "cat":"bitters"},
  

        # -- Emulsifiers: 

        {"name":"Egg White", "cat":"emulsifiers"}, 
        {"name":"Aquafaba", "cat":"emulsifiers"}, 
  

        # -- Toppers:

        {"name":"Dry Sparkling Wine", "cat":"toppers"}, 
        {"name":"Dry Champagne"}, 
        {"name":"Seltzer", "cat":"toppers"},
  
  
        # -- Dry: 

        {"name":"Salt", "cat":"dry"}, 
        {"name":"Chipotle Salt", "cat":"dry"}, 
        {"name":"Cinnamon Stick", "cat":"dry"}, 
        # {"name":"Nutmeg", "cat":"dry"}, 
  

        # -- Fresh: 

        {"name":"Lemon", "cat":"fresh"}, 
        {"name":"Fresh Lemon Juice"}, 
        {"name":"Lemon Twist"}, 
        {"name":"Lemon Wheel"}, 
        {"name":"Lemon Peel"},
        {"name":"Lemon Wedge"},

        {"name":"Lime", "cat":"fresh"}, 
        {"name":"Fresh Lime Juice"}, 
        {"name":"Lime Twist"}, 
        {"name":"Lime Wheel"}, 
        {"name":"Lime Peel"},
        {"name":"Lime Wedge"},

        {"name":"Orange", "cat":"fresh"}, 
        {"name":"Fresh Orange Juice"}, 
        {"name":"Orange Twist"}, 
        {"name":"Orange Wheel"}, 
        {"name":"Orange Peel"},
        {"name":"Orange Slice"},

        {"name":"Grapefruit", "cat":"fresh"}, 
        {"name":"Fresh Grapefruit Juice"}, 
        {"name":"Grapefruit Twist"}, 
        {"name":"Grapefruit Wheel"}, 
        {"name":"Grapefruit Peel"},

        {"name":"Ginger", "cat":"fresh"}, 
         
        {"name":"Mint", "cat":"fresh"}, 
        {"name":"Mint Bouquet"}, 
        {"name":"Mint Sprig"}, 
        # {"name":"Basil", "cat":"fresh"}, 
        # {"name":"Cilantro", "cat":"fresh"}, 
        # {"name":"Sage", "cat":"fresh"}, 

        {"name":"Celery", "cat":"fresh"}, 
        {"name":"Fresh Celery Juice"}, 

        {"name":"Cantaloupe", "cat":"fresh"}, 
        {"name":"Fresh Cantaloupe Juice"}, 

        {"name":"Apple", "cat":"fresh"}, 
        {"name":"Fresh Apple Juice"}, 
        {"name":"Apple Slice"},

        # {"name":"Carrot", "cat":"fresh"}, 
        # {"name":"Fresh Carrot Juice"}, 

        # {"name":"Watermelon", "cat":"fresh"}, 
        # {"name":"Fresh Watermelon Juice"},  

        {"name":"Pineapple", "cat":"fresh"}, 
        {"name":"Fresh Pineapple Juice"}, 

        {"name":"Cucumber", "cat":"fresh"},
        {"name":"Cucumber Spear"}, 
        {"name":"Cucumber Wheel"},

        {"name":"Peach", "cat":"fresh"}, 
        {"name":"Peach Slice"},

        {"name":"Nectarine", "cat":"fresh"}, 
        {"name":"Nectarine Slice"},

        # {"name":"Pear", "cat":"fresh"}, 
        {"name":"Strawberry", "cat":"fresh"}, 
        {"name":"Raspberry", "cat":"fresh"}, 
        # {"name":"Blackberry", "cat":"fresh"}, 
        # {"name":"Cherry", "cat":"fresh"}, 
        # {"name":"Grape", "cat":"fresh"}, 
        # {"name":"Cherry Tomato", "cat":"fresh"}, 
        # {"name":"Kaffir Lime Leaf", "cat":"fresh"}, 
        # {"name":"Curry Leaf", "cat":"fresh"}, 
  

        # Other: 
        {"name":"Olive", "cat":"other"}, 
        # {"name":"Brandied Cherry", "cat":"other"}, 
        # {"name":"Chocolate", "cat":"other"}, 
  

        # Concoctions: 

        # Infusions: 
        {"name":"Chamomile-Infused Cocchi Americano", "cat":"infusions"}, 
        {"name":"Cardamom-Infused St-Germain", "cat":"infusion"},

        # Solutions: 
        {"name":"Salt Solution", "cat":"solutions"}, 
        {"name":"Champagne Acid Solution", "cat":"solutions"}, 
        {"name":"Phosphoric Acid Solution", "cat":"solutions"}, 
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
