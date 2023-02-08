from django.db import migrations

from cocktails.models import Cocktail, Ingredient

import json


def fill_ing(apps, schema_editor):
    Ingredient = apps.get_model("cocktails", "Ingredient")
    db_alias = schema_editor.connection.alias

    ing_list = [
        # {"name":"", "rel":"", "note":"", "method":""},
        
        # Spirits:
        # Gin:
        {
        "name":"Gin",
        "rel":["Plymouth Gin", "London Dry Gin", "Old Tom Gin"],
        "note":"Neutral grain spirit, distilled water, and botanicals. Originally from Holland, gin is now made all over the world. Most major gin brands are distilled in the United Kingdom, with a growing roster of independent brands in the United States."
        },
        {
        "name":"Plymouth Gin",
        "rel":["Gin"],
        "note":"A gentle, citrus-forward style of gin similar to the traditional London dry gins, with a ABV of 41.22%. Distilled in a single distillery in Plymouth, England."
        },
        {
        "name":"London Dry Gin",
        "rel":["Gin"],
        "note":"A big, crisp, high-proof, and aggressive style of gin with prominent flavors of juniper and citrus. Widely considered the benchmark for all other gin styles."
        },
        {
        "name":"Old Tom Gin",
        "rel":["Gin"],
        "note":"London dry's predecessor, with a similar juniper-forward flavor but richer body and sweeter flavor profile. Most old cocktail recipes that call for gin are actually referring to the Old Tom style."
        },
        {
        "name":"Genever",
        "note":"The grandfather of all gin, created by the Dutch as a delivery system for juniper, which was thought to offer protection from the plague. Distilled from a base of malted-barely wine, then redistilled with botanicals. The flavor profile is sweeter and richer than any other style of gin."
        },
        # Modifiers:
        # Fortified Wine:
        {
        "name":"Cocchi Americano",
        "rel":["Chamomile-Infused Cocchi Americano"]
        },
        # Sweetener:
        {
        "name":"Granulated Sugar",
        "rel":["Sugar Cube", "Simple Syrup", "Cane Sugar Syrup"],
        },
        {
        "name":"Sugar Cube",
        "rel":["Granulated Sugar", "Simple Syrup", "Cane Sugar Syrup"],
        },
        {
        "name":"Simple Syrup",
        "rel":["Granulated Sugar", "Sugar Cube", "Cane Sugar Syrup"],
        "method":"Mixture of equal parts white sugar and water. Whisk in warm water or stir constantly over medium heat (do not boil) until the sugar has dissolved. Refrigerate up to 2 weeks."
        },
        {
        "name":"Demerara Syrup",
        "rel":["Demerara Gum Syrup"],
        "method":"Mixture of 2:1 demerara sugar and water. Combine in blender or stir constantly over medium heat (do not boil) until the sugar is dissovled. Refrigerate up to 2 weeks."
        },
        {
        "name":"Demerara Gum Syrup",
        "rel":["Demerara Syrup"],
        "note":"Demerara Gum Syrup rounds off the edges of intense spirits, as in Old-Fashioneds, or adds richness. If seeking clean or sharp flavor in a cocktail, it is not recommended to use this syrup as it could muddy the drink.",
        "method":"300 grams demerara sugar, 18 grams gum arabic, 150 grams filtered water.Combine the demerara sugar and gum arabic in a blender and process for 30 seconds. With the blender running, slowly add the water and continue to process until all dry ingredients have dissolved. Refrigerate up to 2 weeks."
        },
        {
        "name":"Cane Sugar Syrup",
        "rel":["Granulated Sugar", "Sugar Cube", "Simple Syrup"],
        "method":"Mixture of 2:1 cane sugar (often labeled 'evaporated cane juice') and water. Combine in blender or stir constantly over medium heat (do not boil) until the sugar is dissovled. Refrigerate up to 2 weeks."
        },
        {
        "name":"Honey",
        "rel":["Honey Syrup"]
        },
        {
        "name":"Honey Syrup",
        "rel":["Honey"],
        "method":"In a bottle or other container witha a tight lid, combine 2 cups of (acacia) honey with 1 cup of warm water. Shake vigorously until the honey is dissolved."
        },
        {
        "name":"Ginger Syrup",
        "rel":["Ginger"],
        "method":"Juice the ginger and pass the ginger through a fine-mesh sieve. Weigh the ginger juice, then miltiply the weight by 1.5 and weight out that much sugar. Combine the ginger juice and sugar in a blender and process until the sugar has dissolved. Pour into a storage container and regrigerate up to 2 weeks."
        },
        {
        "name":"Cinnamon Syrup",
        "rel":["Cinnamon Stick"],
        "method":"Steep cinnamon sticks in simple syrup overnight (mild, somewhat bitter syrup) or boil simple syrup and cinnamon sticks together (pungent flavor but on the sweeter side). Refrigerate up to 2 weeks."
        },

        # Bitters:
        {
        "name":"Orange Bitters",
        "rel":["Death&Co House Orange Bitters"]
        },
        {
        "name":"Death&Co House Orange Bitters",
        "rel":["Orange Bitters"],
        "method":"Equal parts Fee Brothers West Indian orange bitters, Angostura orange bitters, and Regans' orange bitters. Combine in a bowl."
        },

        # Emulsifiers:
        {
        "name":"Egg White",
        "rel":["Aquafaba"]
        },
        {
        "name":"Aquafaba",
        "rel":["Egg White"],
        "method": "Drain a can of chickpeas and reserve the liquid (recommended) or use leftover cooking liquid from boiling chickpeas (not as reliable). Whip aquafaba with stand or hand mixer for 3-6 minutes. Throw in some cream of tartar for easier whipping."
        },

        # Dry:
        {
        "name":"Salt",
        "rel":["Salt Solution"]
        },
        {
        "name":"Chipotle Salt",
        "rel":["Salt"],
        "method":"Mix ground chipotle and salt.",
        },
        {
        "name":"Cinnamon Stick",
        "rel":["Cinnamon Syrup"]
        },

        # Fresh:
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
        "rel":["Fresh Orange Juice"]
        },
        {
        "name":"Fresh Orange Juice",
        "rel":["Orange"]
        },
        {
        "name":"Grapefruit",
        "rel":["Fresh Grapefruit Juice"]
        },
        {
        "name":"Fresh Grapefruit Juice",
        "rel":["Grapefruit"]
        },
        {
        "name":"Ginger",
        "rel":["Ginger Syrup"]
        },
        {
        "name":"Celery",
        "rel":["Fresh Celery Juice"]
        },
        {
        "name":"Fresh Celery Juice",
        "rel":["Celery"]
        },
        {
        "name":"Cantaloupe",
        "rel":["Fresh Cantaloupe Juice"]
        },
        {
        "name":"Fresh Cantaloupe Juice",
        "rel":["Cantaloupe"]
        },
        {
        "name":"Apple",
        "rel":["Fresh Apple Juice"]
        },
        {
        "name":"Fresh Apple Juice",
        "rel":["Apple"]
        },
        {
        "name":"Peach",
        "rel":["Nectarine"]
        },
        {
        "name":"Nectarine",
        "rel":["Peach"]
        },
        {
        "name":"Carrot",
        "rel":["Fresh Carrot Juice"]
        },
        {
        "name":"Fresh Carrot Juice",
        "rel":["Carrot"]
        },
        {
        "name":"Watermelon",
        "rel":["Fresh Watermelon Juice"]
        },
        {
        "name":"Fresh Watermelon Juice",
        "rel":["Watermelon"]
        },
        {
        "name":"Pineapple",
        "rel":["Fresh Pineapple Juice"]
        },
        {
        "name":"Fresh Pineapple Juice",
        "rel":["Pineapple"]
        },

        # Concoctions:
        # Infusions:
        {
        "name":"Chamomile-Infused Cocchi Americano",
        "rel":["Cocchi Americano"],
        "method":"Place the Cocchi Americano (750 ml) and the 5 grams of chamomile flowers in a bowl and stir to combine. Let stand at room temperature for 1 hour, stirring occasionally. Strain through a fine-mesh sieve lined with several layers of cheesecloth, then funnel back into the original bottle and refrigerate up to 3 months."
        },
        # Solutions:
        {
        "name":"Salt Solution",
        "rel":["Salt"],
        "method":"Combine 4:1 ratio of filtered water and kosher salt in a container and stir or shake until the salt has dissolved. Refrigerate up to 6 months."
        },
        {
        "name":"Champagne Acid Solution",
        "method":"Combine 94 grams of filtered water, 3 grams tartaric acid powder, 3 grams lactic acid powder in a glass bowl and stir until the powders have dissolved. Transfer to a glass dropper bottle or other glass container and refrigerate up to 6 months."
        },
    ]

    for ing in ing_list:
        ing_obj = Ingredient.objects.using(db_alias).get(name=ing["name"])
        if ing.get("rel") is not None:
            for rel in ing["rel"]:
                ing_obj.related.add(Ingredient.objects.get(name=rel))
        if ing.get("note") is not None:
            ing_obj.notes = ing["note"]
        if ing.get("method") is not None:
            ing_obj.method = ing["method"]
        ing_obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0004_populate_rec_detail'),
    ]

    operations = [
        migrations.RunPython(fill_ing)
    ]
