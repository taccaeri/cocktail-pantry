from django.db import migrations

from cocktails.models import Cocktail, Ingredient

import json


def fill_ing(apps, schema_editor):
    Ingredient = apps.get_model("cocktails", "Ingredient")
    db_alias = schema_editor.connection.alias

    ing_list = [
        # {"name":"", "rel":"", "note":""},

        # Sweetener:
        {
        "name":"Sugar",
        "rel":["Sugar Cube", "Simple Syrup", "Demerara Syrup", "Cane Sugar Syrup"],
        },
        {
        "name":"Sugar Cube",
        "rel":["Sugar", "Simple Syrup", "Demerara Syrup", "Cane Sugar Syrup"],
        },
        {
        "name":"Simple Syrup",
        "rel":["Sugar", "Sugar Cube", "Demerara Syrup", "Cane Sugar Syrup"],
        "note":"Mixture of equal parts white sugar and water. Whisk in warm water or stir constantly over medium heat (do not boil) until the sugar has dissolved. Refrigerate up to 2 weeks."
        },
        {
        "name":"Demerara Syrup",
        "rel":["Sugar", "Sugar Cube", "Simple Syrup", "Cane Sugar Syrup"],
        "note":"Mixture of 2:1 demerara sugar and water. Combine in blender or stir constantly over medium heat (do not boil) until the sugar is dissovled. Refrigerate up to 2 weeks."
        },
        {
        "name":"Cane Sugar Syrup",
        "rel":["Sugar", "Sugar Cube", "Simple Syrup", "Demerara Syrup"],
        "note":"Mixture of 2:1 cane sugar (often labeled 'evaporated cane juice') and water. Combine in blender or stir constantly over medium heat (do not boil) until the sugar is dissovled. Refrigerate up to 2 weeks."
        },
        {
        "name":"Honey",
        "rel":["Honey Syrup"]
        },
        {
        "name":"Honey Syrup",
        "rel":["Honey"],
        "note":"In a bottle or other container witha a tight lid, combine 2 cups of (acacia) honey with 1 cup of warm water. Shake vigorously until the honey is dissolved."
        },

        # Bitters:
        {
        "name":"Orange Bitters",
        "rel":["Death&Co House Orange Bitters"]
        },
        {
        "name":"Death&Co House Orange Bitters",
        "rel":["Orange Bitters"],
        "note":"Equal parts Fee Brothers West Indian orange bitters, Angostura orange bitters, and Regans' orange bitters. Combine in a bowl."
        },

        # Other:
        {
        "name":"Lemon",
        "rel":["Fresh Lemon Juice"]
        },
        {
        "name":"Fresh Lemon Juice",
        "rel":["Lemon"]
        },
        {
        "name":"Lime",
        "rel":["Fresh Lime Juice"]
        },
        {
        "name":"Fresh Lime Juice",
        "rel":["Lime"]
        },
        {
        "name":"Orange",
        },
    ]

    for ing in ing_list:
        ing_obj = Ingredient.objects.using(db_alias).get(name=ing["name"])
        if ing.get("rel") is not None:
            for rel in ing["rel"]:
                ing_obj.related.add(Ingredient.objects.get(name=rel))
        if ing.get("note") is not None:
            ing_obj.notes = ing["note"]
        ing_obj.save()


def fill_coc(apps, schema_editor):
    Cocktail = apps.get_model("cocktails", "Cocktail")
    db_alias = schema_editor.connection.alias

    coc_list = [
        # {
        # "name":"",
        # "rel":"",
        # "note":"",
        # "met":""
        # "var":""
        # },

        # Old Fashioned and variants:
        {
        "name":"Classic Old Fashioned",
        "rel":"",
        "note":"Simplest form: Just spirit, sugar, bitters, and water",
        "met":"Muddle the sugar cube and bitters in an Old-Fashioned glass. Add the bourbon and 1 large ice cube and stir until chilled. Garnish with the lemon and orange twists.",
        "var": json.dumps(["Death&Co: 1 oz Elijah Craig Small Batch bourbon, 1 tsp Demerara Syrup, 2 dashes Angostura bitters, 1 dash Bitter Truth aromatic bitters. Same garnish."])
        },
        {
        "name":"Fancy Free",
        "rel":"Classic Old Fashioned",
        "note":"Early example of bartenders swapping out sugar for a sweet, flavorful liqueur.",
        "met":"Stir all the ingredients over ice, then strain into an Old-Fashioned glass over 1 large ice cube. Express the orange twist over the drink, then gently rub it around the rim of the glass and place it into the drink."
        },
        {
        "name":"Chrysanthemum",
        "rel":"Classic Old Fashioned",
        "note":"A low-proof Old-Fashioned that doesn't contain a base spirit, sugar-based sweetner, or traditional bitters served it a coupe. However, the propotion of ingredients gives away its lineage.", 
        "met":"Stir all the ingredients over ice, then strain them into a chilled coupe. Express the orange twist over the drink, then gently rub it around the rim of the glass and place it into the drink."
        },
        {
        "name":"Tiki-Tiki Tom-Tom",
        "rel":"Classic Old Fashioned",
        "met":"Stir all the ingredients over ice, then strain into a double rocks glass over 1 large ice cube. No garnish."
        },
        # Martini and variants:
        {
        "name":"Classic Martini",
        "rel":"",
        "note":"Gin paired with dry vermouth, served up and garnished with either a lemon twist or an olive.",
        "met":"Stir all the ingredients over ice, then strain into a Martini glass. Garnish with the lemon twist (expressed over the drink and set on the edge of the glass) or olive.",
        "var": json.dumps(["Sasha Petraske: straight 2:1 ratio.",
               "Death&co: 2 oz Plymouth gin, 1 oz Dolin dry vermouth, 1 dash of house orange bitters, 1 lemon twist for garnish.",
               "My ideal martini: 2 1/2 oz gin to 3/4 oz Dolin dry vermouth. Optional bitters."])
        },
        # Daiquiri and variants:
        {
        "name":"Classic Daiquiri",
        "rel":"",
        "note":"Modest combination of rum, lime juice, and sugar, shaken and served up. Requires a level of improvisation due to the inconsistency of citrus juices.",
        "met":"Shake all the ingredients with ice, then strain into a chilled coupe. Garnish with the lime wedge.",
        "var": json.dumps(["Sasha Petraske: 2 oz white rum, 1 oz lime juice, 3/4 oz simple syrup.",
               "Death&Co: 1 3/4 oz Caña Brava white rum, 1/4 oz La Favorite Rhum Agricole Blanc Coeur de Canne, 1 oz lime juice, 3/4 oz simple syrup. Garnish with 1 lime wedge.",
               "My ideal daiquiri: 1 1/2 Flor de Caña white rum, 1/4 Rhum Agricole, 1 oz lime juice, 1/2 oz simple syrup.",
               "Tip: Add grapefruit peel when shaking for 'Regal Daiquiri'"])
        },
        {
        "name":"D.W.B.",
        "rel":"Classic Daiquiri",
        "note":"The cocktail's name is short for 'Daiquiri with Benefits.'",
        "met":"Shake all ingredients with ice, then strain into a coupe. Garnish with a lime wedge."
        },
    ]

    for coc in coc_list:
        coc_obj = Cocktail.objects.using(db_alias).get(name=coc["name"])
        if coc["rel"] != "":
            coc_obj.related.add(Cocktail.objects.get(name=coc["rel"]))
        if coc.get("note") is not None:
            coc_obj.notes = coc["note"]
        coc_obj.method = coc["met"]
        if coc.get("var") is not None:
            coc_obj.variations = coc["var"]
        coc_obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0002_populate_db'),
    ]

    operations = [
        migrations.RunPython(fill_ing),
        migrations.RunPython(fill_coc)
    ]
