from __future__ import unicode_literals

from django.db import migrations
from django.db import transaction

import json

def populate_cocktail(apps, schema_editor):
    Cocktail = apps.get_model("cocktails", "Cocktail")
    db_alias = schema_editor.connection.alias

    coc_list = [
        # {"name":"", "cat":"", "bar":"", "glass":""},

        # Gin Shaken:
        {"name":"Bella Luna", "cat":"gin-SH", "bar":"Brian Miller", "glass":"port"},
        {"name":"Cadiz Collins", "cat":"gin-SH", "bar":"Alex Day", "glass":"HB"},
        {"name":"20th Century", "cat":["classic", "gin-SH"], "glass":"coupe"},

        # Gin Stirred:
        {"name":"European Union", "cat":"gin-ST", "bar":"Alex Day", "glass":"coupe"},

        # Rum Shaken:
        {"name":"Flor de Jerez", "cat":"rum-SH", "bar":"Joaquín Simó", "glass":"coupe"},

        # Rum Stirred:
        {"name":"Arrack Strap", "cat":"rum-ST", "bar":"Brad Farran", "glass":"double"}, 

        # Agave Shaken:
        {"name":"Ghost of Mazagran", "cat":"agave-SH", "glass":"tea"}, 
        {"name":"Almond Brother", "cat":"agave-SH", "bar":"Jason Littrell", "glass":"coupe"},

        # Agave Stirred: 
        {"name":"Coralillo", "cat":"agave-ST", "bar":"Thomas Waugh", "glass":"coupe"},

        # Whisk(e)y Shaken:
        {"name":"Ginger Man", "cat":"whi-SH", "bar":"Tyson Buhler", "glass":"coupe"},
        {"name":"19th Century", "cat":"whi-SH", "bar":"Brian Miller", "glass":"coupe"},

        # Whisk(e)y Stirred:
        {"name":"The Dangerous Summer", "cat":"whi-ST", "bar":"Joaquín Simó", "glass":"martini"},

        # Brandy Shaken:
        {"name":"Enchanted Orchard", "cat":"bra-SH", "bar":"Joaquín Simó", "glass":"double"},       

        # Brandy Stirred:
        {"name":"Les Verts Monts", "cat":"bra-ST", "bar":"Jillian Vose", "glass":"NN"}, 

        # Sparkling Cocktails:
        {"name":"Champagne Cocktail", "cat":["classic", "OF-V", "SC"], "glass":"flute"},
        {"name":"The Field Marshall", "cat":["OF-V", "SC"], "bar": "Alex Day", "glass":"flute"},
        {"name":"Pretty Wings", "cat":["OF-V", "SC"], "bar": "Devon Tarby", "glass":"flute"},
        {"name":"Celebrate", "cat":["OF-V", "SC"], "bar": "Devon Tarby", "glass":"flute"},
        {"name":"Airmail", "cat":["classic", "SC"], "glass":"flute"},

        # Fortified Wine Cocktails:
        {"name":"Derby Girl", "cat":"FWC", "bar":"Jillian Vose", "glass":"julep"}, 
        {"name":"Sherry Cobbler", "cat":["classic", "FWC"], "glass":"collins"},
        {"name":"Traction", "cat":"FWC", "bar":"Devon Tarby", "glass":"double"},

        # Punch:
        {"name":"Kill-Devil Punch", "cat":"punch", "bar":"Phil Ward", "glass":"punch"}, 
        
        # Julep:   
        {"name":"Mint Julep", "cat":["classic", "jul"], "glass":"julep"},
        {"name":"Last One Standing", "cat":["jul"], "bar":"Natasha David", "glass":"julep"},
        {"name":"Heritage Julep", "cat":["jul"], "bar":"Alex Day", "glass":"julep"},

        # Flips and Fizzes:
        {"name":"Chinese Fizz", "cat":"fizz", "bar":"Phil Ward", "glass":"fizz"},

        # Swizzles:
        {"name":"Dolores Park Swizzle", "cat":"swiz", "bar":"Thomas Waugh", "glass":"pil"},

        # Aquavit:
        {"name":"Slap 'N' Pickle", "cat":"aqua", "bar":"Brian Miller", "glass":"double"},

        # Martini and variants:
        {"name":"Classic Martini", "cat":["classic", "mar-V"], "glass":"martini"},

        # Sazerac and variants: 
        {"name":"Sazerac", "cat":"classic", "glass":"single"},
        {"name":"Cut and Paste", "cat":"saz-V", "bar":"Alex Day", "glass":"single"},
        {"name":"Bananarac", "cat":"saz-V", "bar":"Natasha David", "glass":"single"},

        # Negroni and variants:
        {"name":"Fail-Safe", "cat":"neg-V", "bar":"Scott Teague", "glass":"double"},

        # Daiquiri and variants:
        {"name":"Classic Daiquiri", "cat":"classic", "glass":"coupe"},
        {"name":"D.W.B.", "cat":"daq-V", "glass":"coupe"},
        {"name":"Rumor Mill", "cat":["daq-V", "SC"], "bar":"Jarred Weigand", "glass":"flute"},

        # Manhattan and variants:
        {"name":"The Black Prince", "cat":"man-V", "bar":"Phil Ward", "glass":"coupe"},

        # Old Fashioned and variants:
        {"name":"Classic Old Fashioned", "cat":"classic", "glass":"single"},
        {"name":"Fancy Free", "cat":["classic", "OF-V"], "glass":"single"},
        {"name":"Chrysanthemum", "cat":["classic", "OF-V"], "glass":"coupe"},
        {"name":"Ti' Punch", "cat":["classic", "OF-V"], "glass":"double"},
        {"name":"Stinger", "cat":["classic", "OF-V"], "glass":"double"},
        {"name":"Monte Carlo", "cat":["classic", "OF-V"], "glass":"single"},
        {"name":"Vermouth Cocktail", "cat":["classic", "OF-V"], "glass":"coupe"},
        {"name":"Improved Whiskey Cocktail", "cat":["classic", "OF-V"], "glass":"single"},

        {"name":"Pop Quiz", "cat":"OF-V", "bar":"Devon Tarby", "glass":"single"},
        {"name":"Snowbird", "cat":"OF-V", "bar":"Devon Tarby", "glass":"single"},
        {"name":"Ned Ryerson", "cat":"OF-V", "bar":"Devin Tarby", "glass":"single"},
        {"name":"Tiki-Tiki Tom-Tom", "cat":"OF-V", "bar":"Thomas Waugh", "glass":"double"},
        {"name":"Exit Strategy", "cat":"OF-V", "bar":"Natasha David", "glass":"single"},

    ]

    for coc in coc_list:
        new_coc = Cocktail.objects.using(db_alias).create(name=coc["name"])
        new_coc.category = coc["cat"]
        if coc.get("bar") is not None:
            new_coc.bartender = coc["bar"]
        new_coc.glassware = coc["glass"]
        new_coc.save()


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0002_populate_ing'),
    ]

    operations = [
        migrations.RunPython(populate_cocktail)
    ]

