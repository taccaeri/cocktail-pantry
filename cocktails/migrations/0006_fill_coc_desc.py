from django.db import migrations

from cocktails.models import Cocktail, Ingredient

import json

def fill_coc(apps, schema_editor):
    Cocktail = apps.get_model("cocktails", "Cocktail")
    db_alias = schema_editor.connection.alias

    coc_list = [
        # {
        # "name":"",
        # "rel":"",
        # "note":"",
        # "met":"",
        # "var":""
        # },

        # Gin Shaken:
        {
        "name":"Bella Luna",
        "rel":"",
        "met":"Shake all the ingredients with ice, then strain into a port glass. No garnish."
        },

        # Gin Stirred:
        {
        "name":"European Union",
        "rel":"",
        "note":"The sweetness of the Old Tom gin is softened by calvados in this Martinez variation. -AD",
        "met":"Stir all ingredients over ice, then strain into a coupe. No garnish."
        },

        # Rum Shaken:
        {
        "name":"Flor de Jerez",
        "rel":"",
        "note":"Apricots are such a frustrating fresh fruit towork with because they're so inconsistent. That's why I use a good apricot liqueur in this drink instead. I was after a light-bodied cocktail that shone forth with fruit and nuts yet remain dry and refreshing. -JS",
        "met":"Shake all the ingredients with ice, then strain into a coupe. No garnish."
        },

        # Rum Stirred:
        {
        "name":"Arrack Strap",
        "rel":"",
        "note":"One of the best ways to combat arrack is by balancing it with another strong flavor, in this case Black Strap rum. -BF",
        "met":"Stir all ingredients over ice, then strain into an double rocks glass over 1 large ice cube. Garnish with the orange twist."
        },

        # Agave Shaken:
        {
        "name":"Ghost of Mazagran",
        "rel":"",
        "note":"A recreation of a cocktail served at Fancy Radish in DC.",
        "met":"Dry shake all ingredients first (except chipotle salt and bitters), then shake with ice. Strain and serve in a tea cup. Garnish with a pinch of chipotle salt and xocolatl mole bitters."
        },
        {
        "name":"Almond Brother",
        "rel":"",
        "met":"Shake all the ingredients with ice, then strain into a coupe. No garnish."
        },

        # Agave Stirred:
        {
        "name":"Coralillo",
        "rel":"",
        "met":"Stir all the ingredients over ice, then strain into a coupe. Garnish with the apple slice."
        },

        # Whisk(e)y Shaken:
        {
        "name":"Ginger Man",
        "rel":"",
        "note":"I love finding ways to take aggressive or esoteric spirits and make them approachable to all drinkers, and this simple spec does just that. Malt whiskey and melon are a dream pairing, and the spicy ginger is powerful enough to stand up to the Islay scotch and lends a familiar flavor profile. -TB",
        "met":"Shake all the ingredients with ice, then double strain into a chilled coupe. No garnish."
        },
        {
        "name":"19th Century",
        "rel":"",
        "met":"Shake all the ingredients with ice, then strain into a coupe. No garnish."
        },

        # Whisk(e)y Stirred:
        {
        "name":"The Dangerous Summer",
        "rel":"",
        "note":"The stirred variation of the classic Blood and Sand is named after a Hemingway book about bullfighters. The rich Cherry Heering is replaced with dry cherry brandy and the orange juice with blood orange liqueur. -JS",
        "met":"Stir all the ingredients (except the orange twist) over ice, then strain into a martini glass. Flame the orange twist over the drink and discard. No garnish."
        },

        # Brandy Shaken:
        {
        "name":"Enchanted Orchard",
        "rel":"",
        "met":"Shake all the ingredients with ice, then strain into a double tocks glass over 1 large ice cube. Garnish with the cinnamon stick."
        },

        # Brandy Stirred:

        # Sparkling Cocktail:
        {
        "name":"Champagne Cocktail",
        "rel":"Classic Old Fashioned",
        "note":"Essentially an Old-Fashioned in which Champagne stands in for the whiskey. Because of the lower alcohol content of the Champagne, partially diluting the drink as you would an Old-Fashioned doesn't make sense, and, of course, the bubbles in the Champagne wouldn't be well served by stirring. Therefore, this drink is built in a flute. Given that it isn't stirred over ice, be sure to start with cold Champagne.",
        "met":"Place the sugar cube on a paper towel. Dash the bitters over the sugar cube until it's completely saturated. Drop the sugar cube into a chilled flute and slowly top with champagne; don't stir. Express the lemon twist over the drink, then place it into the drink."
        },
        {
        "name":"The Field Marshall",
        "rel":"Champagne Cocktail",
        "note":"This cocktail lies somewhere between a classic Champagne Cocktail and an Old-Fashioned, being made with Armagnac and Champagne instead of whiskey. The sugar is swapped out for a sweet liqueur.",
        "met":"Stir all the ingredients (escept the Champagne) over ice, then strain into a chilled flute. Pour in the Champagne, and quickly dip the barspoon into the glass to mix gently. Express the lemon twist over the drink, then place it into the drink."
        },
        {
        "name":"Pretty Wings",
        "rel":"Champagne Cocktail",
        "note":"Inspired by famed bartender Dave Kupchinsky's Lemonade cocktail at the Everleigh in West Hollywood. This Champagne Cocktail variation incorporates flavorful chamomile in an infusion of softly herbaceous and slightly bitter Cocchi Americano.",
        "met":"Stir all the ingredients (except the Champagne) over ice, then strain into a chilled flute. Pour in the Champagne, and quickly dip the barspoon into the glass to mix gently. Garnish with the lemon wheel."
        },
        {
        "name":"Celebrate",
        "rel":"Champagne Cocktail",
        "note":"While the components of this cocktail other than the Champagne take up little volume, they enhance the main spirit by amplifying flavors it already possesses: stone fruit, breadiness, nuttiness, and spice. The Champagne acid, a combination of tartaric and lactic acid, enhances the tang of dry Champagne.",
        "met":"Stir all the ingredients (except the Champagne) over ice, then strain into a chilled flute. Pour in the Champagne and quickly dip the barspoon into the glass to mix gently. No garnish."
        },

        # Fortified Wine Cocktails:

        # Punch:

        # Julep:
        {
        "name":"Mint Julep",
        "rel":"",
        "met":"Rub the interior of a Julep tin with the mint bouquet, then set the mint aside. Add the bourbon and syrup and fill the tin halfway with crushed ice. Holding the tin by the rim, stir, churning the ice as you go, for about 10 seconds. Add more crushed ice to fill the tin about two-thirds full and stir until the tin is completely frosted. Add more ice to form a cone above the rim. Farnish with the mint bouquet and serve with a straw."
        },

        # Flips and Fizzes:

        # Swizzles:

        # Aquavit:

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

        # Negroni and variants:
        
        # Sazeerac and variants:
        {
        "name":"Sazerac",
        "rel":"",
        "note":"When you look at the Sazerac's composition- spirit, sugar, bitters, citrus- it's so obviously linked to the Old-Fashioned. Yet, while the Old-Fashioned is served on ice and expressed and garnished with an orange twist, the Sazerac is served neat and expressed with a lemon twist which is then discarded. Rinsing the glass with absinthe, a highly aromatic spirt, sets the Sazerac apart and defines it and the variations on it that follow.",
        "met":"Rinse a single rocks glass with absinthe and dump. Stir the remaining ingredients over ice, then strain into the glass. Express the lemon twist over the drink and discard.",
        "var":""
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
        {
        "name":"Rumor Mill",
        "rel":"Classic Daiquiri",
        "note":"Celery juice gives this Daiquiri variation its awesome texture. When I started developing the drink it tasted muddy, so I added some dry vermouth to bind the flavors and clean it up. It's amazing what a little dry or blanc vermouth can do to a cocktail. -JW",
        "met":"Pour the sparkling wine into a chilled flute. Shake the remaining ingredients with ice, then double strain into the flute. No garnish."
        },

        # Manhattan and variants:

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
        {
        "name":"Exit Strategy",
        "rel":"Classic Old Fashioned",
        "note":"Amaro shows off its versatility when used as the core of an Old-Fashioned; it also provides seasoning and sweetness, so neither bitters nor sugar syrup is needed. In this recipe, the brandy primarily provides a focused booxy flavor and dries the drink out, and a generous amount of salt solution rounds off the bitter edges.",
        "met":"Stir all the ingredients over ice, then strain into an Old-Fashioned glass over 1 large ice cube. Express the orange twist over the drink, then gently rub it around the rim of the flass and place it into the drink."
        },
        {
        "name":"Ti' Punch",
        "rel":"Classic Old Fashioned",
        "note":"It's said that in Martinique, where the drink originated, Ti' Punches are served up and consumed in one gulp. This version is served over ice and meant to be sipped. If you were to change the proportions of the ingredients and shake the drink, you'd have yourself a Daiquiri, but the Ti' Punch is an Old-Fashioned, through and through, with the lime peel standing in for the bitters to season the drink. Make sure you inclue a bit of the lime flesh, as it will brighten the drink nicely.",
        "met":"In a double rocks glass, muddle the 1 1/2 inch thick disk of lime peel (with some flesh attached) and syrup. Add the rum, fill the glass with cracked ice, and stir briefly. No garnish."
        },
        {
        "name":"Stinger",
        "rel":"Classic Old Fashioned",
        "note":"The Stinger, a pre-Prohibition drink of untraceable origin, classically consisted of just brandy and crème de menthe, the latter providing both seasoning and sweetening. This version of the classic includes a bit of simple syrup to boost the flavor of the crème de menthe and curtail the brandy's strength.",
        "met":"Shake all the ingredients with ice for about 5 seconds, then strain into a double rocks glass filled with crushed ice. Garnish with the mint sprig and serve with a straw."
        },
        {
        "name":"Monte Carlo",
        "rel":"Classic Old Fashioned",
        "note":"In the classic Monte Carlo, Bénédictine, a sweet liquer with herbal and honey flavor, stands in for sugar.",
        "met":"Stir all the ingredients over ice, then strain into an Old-Fashioned glass over 1 large ice cube. Express the lemon twist over the glass and place it into the drink."
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
        ('cocktails', '0005_fill_ing_desc'),
    ]

    operations = [
        migrations.RunPython(fill_coc)
    ]
