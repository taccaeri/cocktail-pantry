from django.db import migrations

from cocktails.models import Cocktail, Ingredient

import json


def fill_ing(apps, schema_editor):
    Ingredient = apps.get_model("cocktails", "Ingredient")
    db_alias = schema_editor.connection.alias

    ing_list = [
        # {"name":"", "rel":"", "note":"", "method":""},
        
        # Modifiers:

        # Liqueur:
        {
        "name":"Orange Liqueur",
        "rel":["Milk & Honey House Curacao"]
        },
        {
        "name":"Milk & Honey House Curacao",
        "rel":["Orange Liqueur"],
        "method":"1:1 Grand Marnier and Simple Syrup. Place the Grand Marnier and syrup in a bowl and stir to combine. Refrigerate up to 6 months."
        },
        {
        "name":"Elderflower Liqueur",
        "rel":["Cardamom-Infused St-Germain"]
        },

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
        "name":"Honey Syrup",
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
        {
        "name":"Orgeat",
        "note":"Orgeat is an almond-based syrup that has been part of cocktail culture since the mid-nineteenth century. It's a key ingredients in the vintage Japanese Cocktail (brandy, orgeat, and Angostura bitters) and especially the Mai Tai and its tiki brethren. Made primarily from water and almongs, along with other ingredients such as orange flower water and cognac, it has a unique flavor that's more than the sum of its ingredients. It deepens the flavors of other ingredients and bridges magically between refreshing and savory.",
        "method":"12 oz toasted almong milk, 16 oz fine sugar, 2 1/2 tsp Pierre Ferrand Ambre Cognac, 1/4 tsp Rose Water. In a sauce pan, combine the almong milk and sugar. Cook over medium-low heat, stirring occasionally and without bringing to a boil, until the sugar is dissolved. Remove from the heat and stir in the cognac, amaretto, and rose water. Store in the refrigerator for up to one month."
        },
        {
        "name":"Grenadine",
        "method":"In a saucepan, combine 4:3 ratio of organic unfilteresd, unsweetened pomegranate juice and organic cane sugar. Cook over medium heat, stirring constantly and withoutbringing to a boil, until the sugar is dissolved. Remove from the heat and let cool at room temperature. Transfer to a container and stir in 6 oz pomegranate molasses. Squeeze 8 half-dollar-size orange twists over the surface, discarding the twists and stir well. Store in the refrigerator for up to 2 weeks."
        },
        # {
        # "name":"Vanilla Syrup",
        # "method":"Split 1 Tahitan vanilla bean in half lengthwise and put it in a saucepan. Add 2 cups of water and 2 cups of fine sugar. Bring to a boil, stirring occasionally. Lower the heat, cover, and simmer gently for 4 minutes. Remove from heat and let stand overnight. Strain through a cheesecloth-lined sieve."
        # },


        # Bitters:
        {
        "name":"Orange Bitters",
        "rel":["Death & Co House Orange Bitters"]
        },
        {
        "name":"Death & Co House Orange Bitters",
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

        # Toppers:
        {
        "name":"Dry Sparkling Wine",
        "rel":["Dry Champagne"]
        },
        {
        "name":"Dry Champagne",
        "rel":["Dry Sparkling Wine"]
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
        "rel":["Fresh Lemon Juice", "Lemon Twist", "Lemon Wheel", "Lemon Peel", "Lemon Wedge"]
        },
        {
        "name":"Fresh Lemon Juice",
        "rel":["Lemon"]
        },
        {
        "name":"Lemon Twist",
        "rel":["Lemon"]
        },
        {
        "name":"Lemon Wheel",
        "rel":["Lemon"]
        },
        {
        "name":"Lemon Peel",
        "rel":["Lemon"]
        },
        {
        "name":"Lemon Wedge",
        "rel":["Lemon"]
        },

        {
        "name":"Lime",
        "rel":["Fresh Lime Juice", "Lime Twist", "Lime Wheel", "Lime Peel", "Lime Wedge"]
        },
        {
        "name":"Fresh Lime Juice",
        "rel":["Lime"]
        },
        {
        "name":"Lime Twist",
        "rel":["Lime"]
        },
        {
        "name":"Lime Wheel",
        "rel":["Lime"]
        },
        {
        "name":"Lime Peel",
        "rel":["Lime"]
        },
        {
        "name":"Lime Wedge",
        "rel":["Lime"]
        },

        {
        "name":"Orange",
        "rel":["Fresh Orange Juice", "Orange Twist", "Orange Wheel", "Orange Peel", "Orange Slice", "Orange Crescent"]
        },
        {
        "name":"Fresh Orange Juice",
        "rel":["Orange"]
        },
        {
        "name":"Orange Twist",
        "rel":["Orange"]
        },
        {
        "name":"Orange Wheel",
        "rel":["Orange"]
        },
        {
        "name":"Orange Peel",
        "rel":["Orange"]
        },
        {
        "name":"Orange Slice",
        "rel":["Orange"]
        },
        {
        "name":"Orange Crescent",
        "rel":["Orange"]
        },

        {
        "name":"Grapefruit",
        "rel":["Fresh Grapefruit Juice", "Grapefruit Twist", "Grapefruit Wheel", "Grapefruit Peel"]
        },
        {
        "name":"Fresh Grapefruit Juice",
        "rel":["Grapefruit"]
        },
        {
        "name":"Grapefruit Twist",
        "rel":["Grapefruit"]
        },
        {
        "name":"Grapefruit Wheel",
        "rel":["Grapefruit"]
        },
        {
        "name":"Grapefruit Peel",
        "rel":["Grapefruit"]
        },

        {
        "name":"Ginger",
        "rel":["Ginger Syrup"]
        },

        {
        "name":"Mint",
        "rel":["Mint Bouquet", "Mint Sprig"]
        },
        {
        "name":"Mint Bouquet",
        "rel":["Mint"]
        },
        {
        "name":"Mint Sprig",
        "rel":["Mint"]
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
        "rel":["Fresh Apple Juice", "Apple Slice"]
        },
        {
        "name":"Fresh Apple Juice",
        "rel":["Apple"]
        },
        {
        "name":"Apple Slice",
        "rel":["Apple"]
        },

        # {
        # "name":"Carrot",
        # "rel":["Fresh Carrot Juice"]
        # },
        # {
        # "name":"Fresh Carrot Juice",
        # "rel":["Carrot"]
        # },
        # {
        # "name":"Watermelon",
        # "rel":["Fresh Watermelon Juice"]
        # },
        # {
        # "name":"Fresh Watermelon Juice",
        # "rel":["Watermelon"]
        # },

        {
        "name":"Pineapple",
        "rel":["Fresh Pineapple Juice"]
        },
        {
        "name":"Fresh Pineapple Juice",
        "rel":["Pineapple"]
        },

        {
        "name":"Cucumber",
        "rel":["Cucumber Spear", "Cucumber Wheel"]
        },
        {
        "name":"Cucumber Spear",
        "rel":["Cucumber"]
        },
        {
        "name":"Cucumber Wheel",
        "rel":["Cucumber"]
        },

        {
        "name":"Peach",
        "rel":["Peach Slice"]
        },
        {
        "name":"Peach Slice",
        "rel":["Peach"]
        },

        {
        "name":"Nectarine",
        "rel":["Nectarine Slice"]
        },
        {
        "name":"Nectarine Slice",
        "rel":["Nectarine"]
        },


        # Concoctions:

        # Infusions:
        {
        "name":"Chamomile-Infused Cocchi Americano",
        "rel":["Cocchi Americano"],
        "method":"Place the Cocchi Americano (750 ml) and the 5 grams of chamomile flowers in a bowl and stir to combine. Let stand at room temperature for 1 hour, stirring occasionally. Strain through a fine-mesh sieve lined with several layers of cheesecloth, then funnel back into the original bottle and refrigerate up to 3 months."
        },
        {
        "name":"Cardamom-Infused St-Germain", 
        "rel":["Elderflower Liqueur"],
        "method":"1 (750 ml) bottle St-Germain. 10 grams green cardamom pods. Place the St-Germain and cardamom in a bowl and stir to combine. Let stand at room temperature for about 12 hours. Strain through a fine-mesh sieve lined with several layers of cheesecloth, then funnel back into the St-Germain bottle and refrigerate until ready to use, up to 3 months."
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
        {
        "name":"Phosphoric Acid Solution",
        "note":"Phosphoric acid solution is responsible for most of the acidity in commercial sodas—that refreshing quality that makes us come back for more. It is an odorless and flavorless liquid on its own, so it does not contribute flavor, as many other acids do; instead, it adds a tongue-tingly tartness.",
        "method":"A ready-to-use product by the name of Extinct Acid Phosphate can be purchased online at Art of Drink. If purchasing bulk phosphoric acid, it must be diluted since it is usually very concentrated."
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
