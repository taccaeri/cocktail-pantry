from __future__ import unicode_literals

from django.db import migrations
from django.db import transaction


def populate_cocktail(apps, schema_editor):
    Cocktail = apps.get_model("cocktails", "Cocktail")
    db_alias = schema_editor.connection.alias

    coc_list = [
        # {"name":"", "cat":"", "bar":"", "glass":""},

        # Agave Shaken:
        {"name":"Ghost of Mazagran", "cat":"agave-SH", "glass":"tea"},         

        # Whisk(e)y Shaken:
        {"name":"Ginger Man", "cat":"whi-SH", "bar":"Tyson Buhler", "glass":"coupe"},

        # Sparkling Cocktail:
        {"name":"Champagne Cocktail", "cat":["classic", "OF-V", "SC"], "glass":"flute"},
        {"name":"The Field Marshall", "cat":["OF-V", "SC"], "bar": "Alex Day", "glass":"flute"},
        {"name":"Pretty Wings", "cat":["OF-V", "SC"], "bar": "Devon Tarby", "glass":"flute"},
        {"name":"Celebrate", "cat":["OF-V", "SC"], "bar": "Devon Tarby", "glass":"flute"},
        
        # Julep:   
        {"name":"Mint Julep", "cat":["classic", "jul"], "glass":"julep"},

        # Martini and variants:
        {"name":"Classic Martini", "cat":["classic", "mar-V"], "glass":"martini"},

        # Sazerac and variants: 
        {"name":"Sazerac", "cat":"classic", "glass":"single"},

        # Daiquiri and variants:
        {"name":"Classic Daiquiri", "cat":"classic", "glass":"coupe"},
        {"name":"D.W.B.", "cat":"daq-V", "glass":"coupe"},
        {"name":"Rumor Mill", "cat":["daq-V", "SC"], "bar":"Jarred Weigand", "glass":"flute"},

        # Old Fashioned and variants:
        {"name":"Classic Old Fashioned", "cat":"classic", "glass":"single"},
        {"name":"Fancy Free", "cat":["classic", "OF-V"], "glass":"single"},
        {"name":"Chrysanthemum", "cat":["classic", "OF-V"], "glass":"coupe"},
        {"name":"Tiki-Tiki Tom-Tom", "cat":"OF-V", "bar":"Thomas Waugh", "glass":"double"},
        {"name":"Exit Strategy", "cat":"OF-V", "bar":"Natasha David", "glass":"single"},
        {"name":"Ti' Punch", "cat":["classic", "OF-V"], "glass":"double"},
        {"name":"Stinger", "cat":["classic", "OF-V"], "glass":"double"},
        {"name":"Monte Carlo", "cat":["classic", "OF-V"], "glass":"single"},
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

