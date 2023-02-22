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
        # "var":"",
        # "ref":""
        # },

        # Gin Shaken:
        {
        "name":"Bella Luna",
        "rel":"",
        "met":"Shake all the ingredients with ice, then strain into a port glass. No garnish.",
        "ref":"Death & Co: Modern Classic Cocktails, Pg 154"
        },

        # Gin Stirred:
        {
        "name":"European Union",
        "rel":"",
        "note":"The sweetness of the Old Tom gin is softened by calvados in this Martinez variation. -AD",
        "met":"Stir all ingredients over ice, then strain into a coupe. No garnish.",
        "ref":"Death & Co: Modern Classic Cocktails, Pg 162"
        },

        # Rum Shaken:
        {
        "name":"Flor de Jerez",
        "rel":"",
        "note":"Apricots are such a frustrating fresh fruit towork with because they're so inconsistent. That's why I use a good apricot liqueur in this drink instead. I was after a light-bodied cocktail that shone forth with fruit and nuts yet remain dry and refreshing. -JS",
        "met":"Shake all the ingredients with ice, then strain into a coupe. No garnish.",
        "ref":"Death & Co: Modern Classic Cocktails, Pg 171"
        },

        # Rum Stirred:
        {
        "name":"Arrack Strap",
        "rel":"",
        "note":"One of the best ways to combat arrack is by balancing it with another strong flavor, in this case Black Strap rum. -BF",
        "met":"Stir all ingredients over ice, then strain into an double rocks glass over 1 large ice cube. Garnish with the orange twist.",
        "ref":"Death & Co: Modern Classic Cocktails, Pg 175"
        },

        # Agave Shaken:
        {
        "name":"Ghost of Mazagran",
        "rel":"",
        "note":"A recreation of a cocktail served at Fancy Radish in DC.",
        "met":"Dry shake all ingredients first (except chipotle salt and bitters), then shake with ice. Strain and serve in a tea cup. Garnish with a pinch of chipotle salt and xocolatl mole bitters.",
        "ref":"Fancy Radish DC, 2022 drink menu"
        },
        {
        "name":"Almond Brother",
        "rel":"",
        "met":"Shake all the ingredients with ice, then strain into a coupe. No garnish.",
        "ref":"Death & Co: Modern Classic Cocktails, Pg 181"
        },

        # Agave Stirred:
        {
        "name":"Coralillo",
        "rel":"",
        "met":"Stir all the ingredients over ice, then strain into a coupe. Garnish with the apple slice.",
        "ref":"Death & Co: Modern Classic Cocktails, Pg 190"
        },

        # Whisk(e)y Shaken:
        {
        "name":"Ginger Man",
        "rel":"",
        "note":"I love finding ways to take aggressive or esoteric spirits and make them approachable to all drinkers, and this simple spec does just that. Malt whiskey and melon are a dream pairing, and the spicy ginger is powerful enough to stand up to the Islay scotch and lends a familiar flavor profile. -TB",
        "met":"Shake all the ingredients with ice, then double strain into a chilled coupe. No garnish.",
        "ref":"Death & Co Welcome Home, Pg 196"
        },
        {
        "name":"19th Century",
        "rel":"",
        "met":"Shake all the ingredients with ice, then strain into a coupe. No garnish.",
        "ref":"Death & Co: Modern Classic Cocktails, Pg 197"
        },

        # Whisk(e)y Stirred:
        {
        "name":"The Dangerous Summer",
        "rel":"",
        "note":"The stirred variation of the classic Blood and Sand is named after a Hemingway book about bullfighters. The rich Cherry Heering is replaced with dry cherry brandy and the orange juice with blood orange liqueur. -JS",
        "met":"Stir all the ingredients (except the orange twist) over ice, then strain into a martini glass. Flame the orange twist over the drink and discard. No garnish.",
        "ref":"Death & Co: Modern Classic Cocktails, Pg 205"
        },

        # Brandy Shaken:
        {
        "name":"Enchanted Orchard",
        "rel":"",
        "met":"Shake all the ingredients with ice, then strain into a double rocks glass over 1 large ice cube. Garnish with the cinnamon stick.",
        "ref":"Death & Co: Modern Classic Cocktails, Pg 210"
        },

        # Brandy Stirred:
        {
        "name":"Les Verts Monts",
        "rel":"",
        "met":"Stir all the ingredinets (except the lemon twist) over ice, then strain into a Nick & Nora glass. Squeeze the lemon twist over the drink and discard. Garnish with the apple slice.",
        "ref":"Death & Co: Modern Classic Cocktails, Pg 217"
        },

        # Sparkling Cocktail:
        {
        "name":"Champagne Cocktail",
        "rel":"Classic Old Fashioned",
        "note":"Essentially an Old-Fashioned in which Champagne stands in for the whiskey. Because of the lower alcohol content of the Champagne, partially diluting the drink as you would an Old-Fashioned doesn't make sense, and, of course, the bubbles in the Champagne wouldn't be well served by stirring. Therefore, this drink is built in a flute. Given that it isn't stirred over ice, be sure to start with cold Champagne.",
        "met":"Place the sugar cube on a paper towel. Dash the bitters over the sugar cube until it's completely saturated. Drop the sugar cube into a chilled flute and slowly top with champagne; don't stir. Express the lemon twist over the drink, then place it into the drink.",
        "ref":"Cocktail Codex: Fundamentals, Formulas, Evolutions, Pg 26"
        },
        {
        "name":"The Field Marshall",
        "rel":"Champagne Cocktail",
        "note":"This cocktail lies somewhere between a classic Champagne Cocktail and an Old-Fashioned, being made with Armagnac and Champagne instead of whiskey. The sugar is swapped out for a sweet liqueur.",
        "met":"Stir all the ingredients (escept the Champagne) over ice, then strain into a chilled flute. Pour in the Champagne, and quickly dip the barspoon into the glass to mix gently. Express the lemon twist over the drink, then place it into the drink.",
        "ref":"Cocktail Codex: Fundamentals, Formulas, Evolutions, Pg 29"
        },
        {
        "name":"Pretty Wings",
        "rel":"Champagne Cocktail",
        "note":"Inspired by famed bartender Dave Kupchinsky's Lemonade cocktail at the Everleigh in West Hollywood. This Champagne Cocktail variation incorporates flavorful chamomile in an infusion of softly herbaceous and slightly bitter Cocchi Americano.",
        "met":"Stir all the ingredients (except the Champagne) over ice, then strain into a chilled flute. Pour in the Champagne, and quickly dip the barspoon into the glass to mix gently. Garnish with the lemon wheel.",
        "ref":"Cocktail Codex: Fundamentals, Formulas, Evolutions, Pg 29"
        },
        {
        "name":"Celebrate",
        "rel":"Champagne Cocktail",
        "note":"While the components of this cocktail other than the Champagne take up little volume, they enhance the main spirit by amplifying flavors it already possesses: stone fruit, breadiness, nuttiness, and spice. The Champagne acid, a combination of tartaric and lactic acid, enhances the tang of dry Champagne.",
        "met":"Stir all the ingredients (except the Champagne) over ice, then strain into a chilled flute. Pour in the Champagne and quickly dip the barspoon into the glass to mix gently. No garnish.",
        "ref":"Cocktail Codex: Fundamentals, Formulas, Evolutions, Pg 29"
        },

        # Fortified Wine Cocktails:
        {
        "name":"Derby Girl",
        "rel":"",
        "note":"Juleps are typically boozy, one-and-done affairs. This drink is a lower-octane, aperitif-style julep.",
        "met":"In a shaker, muddle the nectarine slices. Add the remaining ingredients and short shake with ice. Strain into a julep tin filled with crushed ice. Garnish with the mint bouquet in the center of the ice and serve with a straw.",
        "ref":"Death & Co: Modern Classic Cocktails, Pg 229"
        },
        { 
        "name":"Sherry Cobbler", 
        "rel":"", 
        "note":"Replace the high-proof whiskey in an Old-Fashioned with a larger quantity of low-proof amontillado sherry, and swap muddled orange slices for the bitters, and you have a Cobbler. Amontillado sherry is a fortified wine that gives the cocktail both body and acidity, making it a strong backbone for the drink. When muddled, the orange wheels add not only a touch of sweetness from the flesh but also some seasoning from the bitter pith and the vibrant oils in the skin. This complexity is nicely counterbalanced by the levity and bright aroma of the fresh mint garnish.", 
        "met":"In a Collins glass, muddle the orange slices and syrup. Add the sherry and stir briefly. Top with crushed ice and stir a few times to chill the cocktail. Top with more crushed ice, packing the glass fully. Garnish with the orange half wheel and mint bouquet and serve with a straw.",
        "ref":"Cocktail Codex: Fundamentals, Formulas, Evolutions, Pg 37"
        },
        { 
        "name":"Traction", 
        "rel":"", 
        "note":"In this drink, rum shines a light on the dried fruit flavors that are often somewhat hidden in amontillado sherry.", 
        "met":"In a shaker, muddle the lemon wedges and strawberry halves. Add the remaining ingredients and shake with ice. Double strain into an double rocks glass filled with crushed ice. Garnish with the strawberry half, lemon wedge, and mint sprig and serve with a straw.", 
        "ref":"Cocktail Codex: Fundamentals, Formulas, Evolutions, Pg 29"
        },


        # Punch:
        {
        "name":"Kill-Devil Punch",
        "rel":"",
        "met":"In a pitcher, muddle the sugar cubes with 15 raspberries and club soda until the sugar is fully broken up. Add the remaining ingredients (except the champagne) and fill the pitcher three-quarters full with ice cubes. Stir until cold, then strain into a punch bowl over 1 large block of ice. Top with the champagne. Garnish with the remaining raspberries and serve with a ladle and punch glasses.",
        "ref":"Death & Co: Modern Classic Cocktails, Pg 236"
        },

        # Julep:
        {
        "name":"Mint Julep",
        "rel":"",
        "met":"Rub the interior of a Julep tin with the mint bouquet, then set the mint aside. Add the bourbon and syrup and fill the tin halfway with crushed ice. Holding the tin by the rim, stir, churning the ice as you go, for about 10 seconds. Add more crushed ice to fill the tin about two-thirds full and stir until the tin is completely frosted. Add more ice to form a cone above the rim. Farnish with the mint bouquet and serve with a straw.",
        "ref":"Cocktail Codex: Fundamentals, Formulas, Evolutions, Pg 31"
        },
        {
        "name":"Last One Standing",
        "rel":"",
        "note":"The combination of Cognac and Jamaican rum appears frequently in older cocktail recipes. Here, the duo creates a big, funky core flavor that plays off the bright fruit of the peach liqueur. The amaro acts as a bridge between these two opposing camps, working in much the same way that bitters do, balancing other disparate flavors.",
        "met":"Rub the interior of a Julep tin with the mint bouquet, then set the mint aside. Add the remaining ingredients and fill the tin halfway with crushed ice. Holding the tin by the rim, stir, churning the ice as you go, for about 10 seconds. Add more crushed ice to fill the tin about two-thirds full and stir until the tin is completely frosted. Add more ice to form a cone above the rim. Garnish with the mint bouquet and peach slice, then lightly dust the top of the mint with confectionery sugar. Serve with a straw.",
        "ref":"Cocktail Codex: Fundamentals, Formulas, Evolutions, Pg 32"
        },
        {
        "name":"Heritage Julep",
        "rel":"",
        "note":"The baked stone fruit and warm autumn flavors of this cocktail make it a great option for an Old-Fashioned lover who’s looking for something on the more refreshing side. We double down on pear, bringing the spirituous heat and pear-like gritty texture thanks to pear brandy and the supple fruitiness of the pear liqueur. The addition of Amaro Montenegro brings this drink into the aperitif category.",
        "met":"Rub the interior of a Julep tin with the mint bouquet, then set the mint aside. Add the remaining ingredients and fill the tin halfway with crushed ice. Holding the tin by the rim, stir, churning the ice as you go, for about 10 seconds. Add more crushed ice to fill the tin about two-thirds full and stir until the tin is completely frosted. Add more ice to form a cone above the rim. Garnish with the mint bouquet and the apple slices, then lightly dust the top of the mint with confectionery sugar. Serve with a straw.",
        "ref":"Cocktail Codex: Fundamentals, Formulas, Evolutions, Pg 32"
        },

        # Flips and Fizzes:
        {
        "name":"Chinese Fizz",
        "rel":"",
        "note":"A fizz variation on the Chinese cocktail from The Savoy Cocktail Book, by Harry Craddock. -PW",
        "met":"Dry Shake all the ingredients, then shake again with ice. Double strain into a fizz glass filled with ice cubes. Garnish with the orange wheel and serve with a straw.",
        "ref":"Death & Co: Modern Classic Cocktails, Pg 245"
        },

        # Swizzles:
        {
        "name":"Dolores Park Swizzle",
        "rel":"",
        "met":"Dry shake all the ingredients (except the bitters), then dump into a pilsner glass filled with crushed ice. Add the bitters and swizzle them into the top of the drink. Garnish with the mint sprig and serve with a straw.",
        "ref":"Death & Co: Modern Classic Cocktails, Pg 249"
        },

        # Aquavit:
        {
        "name":"Slap 'N' Pickle",
        "rel":"",
        "met":"In a shaker, muddle the cucumber wheels. Add the remaining ingredients and shake with ice, then double strain into a double rocks glass over 1 large ice cube. Garnish with the cucumber spear.",
        "ref":"Death & Co: Modern Classic Cocktails, Pg 254"
        },

        # Martini and variants:
        {
        "name":"Classic Martini",
        "rel":"",
        "note":"Gin paired with dry vermouth, served up and garnished with either a lemon twist or an olive.",
        "met":"Stir all the ingredients over ice, then strain into a Martini glass. Garnish with the lemon twist (expressed over the drink and set on the edge of the glass) or olive.",
        "var": json.dumps(["Sasha Petraske: straight 2:1 ratio.",
               "Death&co: 2 oz Plymouth gin, 1 oz Dolin dry vermouth, 1 dash of house orange bitters, 1 lemon twist for garnish.",
               "My ideal martini: 2 1/2 oz gin to 3/4 oz Dolin dry vermouth. Optional bitters."]),
        "ref":"Cocktail Codex: Fundamentals, Formulas, Evolutions, Pg 61"
        },
        
        # Sazerac and variants:
        {
        "name":"Sazerac",
        "rel":"",
        "note":"When you look at the Sazerac's composition- spirit, sugar, bitters, citrus- it's so obviously linked to the Old-Fashioned. Yet, while the Old-Fashioned is served on ice and expressed and garnished with an orange twist, the Sazerac is served neat and expressed with a lemon twist which is then discarded. Rinsing the glass with absinthe, a highly aromatic spirt, sets the Sazerac apart and defines it and the variations on it that follow.",
        "met":"Rinse a single rocks glass with absinthe and dump. Stir the remaining ingredients over ice, then strain into the glass. Express the lemon twist over the drink and discard.",
        "ref":"Cocktail Codex: Fundamentals, Formulas, Evolutions, Pg 33"
        },

        { 
        "name":"Cut and Paste", 
        "rel":"", 
        "note":"Although aged for eight years, the apple brandy in this drink doesn’t taste much like an aged spirit, so we also include pot-distilled Irish whiskey, with its vanilla and spice flavors, in the core. And because Irish whiskey has a nice affinity for honey, we use a honey syrup for the sweetener, which keeps the drink light and crisp, whereas Demerara Gum Syrup would probably be too cloying.", 
        "met":"Rinse a chilled single rocks glass with absinthe and dump. Stir the remaining ingredients over ice, then strain into the glass. No garnish.",
        "ref":"Cocktail Codex: Fundamentals, Formulas, Evolutions, Pg 35"
        },

        { 
        "name":"Bananarac", 
        "rel":"", 
        "note":"The idea of putting bananas in a boozy cocktail once seemed questionable at best. Then the liqueur company Giffard introduced Banane du Brésil to the US market, a banana liqueur that far exceeded expectations.", 
        "met":"Rinse a chilled Old-Fashioned glass with absinthe and dump. Stir the remaining ingredients over ice, then strain into the glass. Express the lemon twist over the drink and discard.",
        "ref":"Cocktail Codex: Fundamentals, Formulas, Evolutions, Pg 35"
        },


        # Negroni and variants:
        {
        "name":"Fail-Safe",
        "rel":"",
        "note":"Some drinks are just happy accidents. One night I saw several bottles sitting next to each other behind the bar, and I thought, Why not? I started playing around with them in Negroni proportions, and it worked. -ST",
        "met":"Stir all the ingredients over ice, then strain into a double rocks glass over 1 large ice cube. No garnish.",
        "ref":"Death & Co: Modern Classic Cocktails, Pg 258"
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
               "Tip: Add grapefruit peel when shaking for 'Regal Daiquiri'"]),
        "ref":"Cocktail Codex: Fundamentals, Formulas, Evolutions, Pg 103,104"
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
        {
        "name":"The Black Prince",
        "rel":"",
        "met":"Stir all the ingredients over ice, then strain into a coupe. No garnish.",
        "ref":"Death & Co: Modern Classic Cocktails, Pg 267"
        },

        # Old Fashioned and variants:
        {
        "name":"Classic Old Fashioned",
        "rel":"",
        "note":"Simplest form: Just spirit, sugar, bitters, and water",
        "met":"Muddle the sugar cube and bitters in an Old-Fashioned glass. Add the bourbon and 1 large ice cube and stir until chilled. Garnish with the lemon and orange twists.",
        "var": json.dumps(["Death&Co: 1 oz Elijah Craig Small Batch bourbon, 1 tsp Demerara Syrup, 2 dashes Angostura bitters, 1 dash Bitter Truth aromatic bitters. Same garnish."]),
        "ref":"Cocktail Codex: Fundamentals, Formulas, Evolutions, Pg 3,4"
        },
        {
        "name":"Fancy Free",
        "rel":"Classic Old Fashioned",
        "note":"Early example of bartenders swapping out sugar for a sweet, flavorful liqueur.",
        "met":"Stir all the ingredients over ice, then strain into an Old-Fashioned glass over 1 large ice cube. Express the orange twist over the drink, then gently rub it around the rim of the glass and place it into the drink.",
        "ref":"Cocktail Codex: Fundamentals, Formulas, Evolutions, Pg 13"
        },
        {
        "name":"Chrysanthemum",
        "rel":"Classic Old Fashioned",
        "note":"A low-proof Old-Fashioned that doesn't contain a base spirit, sugar-based sweetner, or traditional bitters served it a coupe. However, the propotion of ingredients gives away its lineage.", 
        "met":"Stir all the ingredients over ice, then strain them into a chilled coupe. Express the orange twist over the drink, then gently rub it around the rim of the glass and place it into the drink.",
        "ref":"Cocktail Codex: Fundamentals, Formulas, Evolutions, Pg 13"
        },
        {
        "name":"Ti' Punch",
        "rel":"Classic Old Fashioned",
        "note":"It's said that in Martinique, where the drink originated, Ti' Punches are served up and consumed in one gulp. This version is served over ice and meant to be sipped. If you were to change the proportions of the ingredients and shake the drink, you'd have yourself a Daiquiri, but the Ti' Punch is an Old-Fashioned, through and through, with the lime peel standing in for the bitters to season the drink. Make sure you inclue a bit of the lime flesh, as it will brighten the drink nicely.",
        "met":"In a double rocks glass, muddle the 1 1/2 inch thick disk of lime peel (with some flesh attached) and syrup. Add the rum, fill the glass with cracked ice, and stir briefly. No garnish.",
        "ref":"Cocktail Codex: Fundamentals, Formulas, Evolutions, Pg 11"
        },
        {
        "name":"Stinger",
        "rel":"Classic Old Fashioned",
        "note":"The Stinger, a pre-Prohibition drink of untraceable origin, classically consisted of just brandy and crème de menthe, the latter providing both seasoning and sweetening. This version of the classic includes a bit of simple syrup to boost the flavor of the crème de menthe and curtail the brandy's strength.",
        "met":"Shake all the ingredients with ice for about 5 seconds, then strain into a double rocks glass filled with crushed ice. Garnish with the mint sprig and serve with a straw.",
        "ref":"Cocktail Codex: Fundamentals, Formulas, Evolutions, Pg 13"
        },
        {
        "name":"Monte Carlo",
        "rel":"Classic Old Fashioned",
        "note":"In the classic Monte Carlo, Bénédictine, a sweet liquer with herbal and honey flavor, stands in for sugar.",
        "met":"Stir all the ingredients over ice, then strain into an Old-Fashioned glass over 1 large ice cube. Express the lemon twist over the glass and place it into the drink.",
        "ref":"Cocktail Codex: Fundamentals, Formulas, Evolutions, Pg 13"
        },

        { 
        "name":"Vermouth Cocktail", 
        "rel":"Classic Old Fashioned", 
        "note":"In the early days of cocktails, vermouth was becoming popular in America and found its way into the Old-Fashioned template, resulting in this nuanced, low-ABV sipper. This classic recipe also demonstrates that not all Old-Fashioned-style drinks are served over ice in rocks glasses.", 
        "met":"Stir all the ingredients over ice, then strain into a chilled coupe. Express the lemon twist over the drink, then set it on the edge of the glass.", 
        "ref":"Cocktail Codex: Fundamentals, Formulas, Evolutions, Pg 11"
        },

        { 
        "name":"Improved Whiskey Cocktail", 
        "rel":"Classic Old Fashioned", 
        "note":"The Improved Whiskey Cocktail, which was probably one of the first popular Old-Fashioned variations, turns to absinthe for seasoning, which adds a deep complexity to the cocktail. The sweet red-licorice and anise flavors from the Peychaud’s bitters dial up the seasoning even more, while also increasing the impression of sweetness.", 
        "met":"Stir all the ingredients over ice, then strain into an Old-Fashioned glass over 1 large ice cube. Express the lemon twist over the drink, then place it into the drink.", 
        "ref":"Cocktail Codex: Fundamentals, Formulas, Evolutions, Pg 17"
        },

        { 
        "name":"Pop Quiz", 
        "rel":"Classic Old Fashioned", 
        "note":"Substituting a sweet liqueur or amaro for the sugar in an Old-Fashioned style cocktail is an amazing way to balance a drink while incorporating a unique seasoning. In the Pop Quiz, Devon includes an orange-flavored amaro, Ramazzotti, and swaps in spicy, chocolaty bitters.", 
        "met":"Stir all the ingredients over ice, then strain into an Old-Fashioned glass over 1 large ice cube. Express the orange twist over the drink, then gently rub it around the rim of the glass and place it into the drink.", 
        "ref":"Cocktail Codex: Fundamentals, Formulas, Evolutions, Pg 17"
        },

        { 
        "name":"Snowbird", 
        "rel":"Classic Old Fashioned", 
        "note":"Together, rye and apple brandy are a magical, crowd-pleasing combination, and St-Germain makes everything it touches taste better. A dash of celery bitters adds just enough savoriness to pull the drink back from excessive sweetness.", 
        "met":"Stir all the ingredients over ice, then strain into an Old-Fashioned glass over 1 large ice cube. Express the grapefruit twist over the drink and place it into the glass.",
        "ref":"Cocktail Codex: Fundamentals, Formulas, Evolutions, Pg 22"
        },

        { 
        "name":"Ned Ryerson", 
        "rel":"Classic Old Fashioned", 
        "note":"In the Ned Ryerson, the core includes a small portion of young apple brandy, which adds a juicy flavor to the cocktail, and the Miracle Mile Castilian bitters in the seasoning are full of orange, licorice, and sarsaparilla notes. The result is an Old-Fashioned that’s been reimagined with just modest changes.", 
        "met":"Stir all the ingredients over ice, then strain into an Old-Fashioned glass over 1 large ice cube. Express the lemon twist over the drink, then place it into the drink.",
        "ref":"Cocktail Codex: Fundamentals, Formulas, Evolutions, Pg 23"
        },
        {
        "name":"Tiki-Tiki Tom-Tom",
        "rel":"Classic Old Fashioned",
        "met":"Stir all the ingredients over ice, then strain into a double rocks glass over 1 large ice cube. No garnish.",
        "ref":"Death & Co: Modern Classic Cocktails, Pg 273"
        },
        {
        "name":"Exit Strategy",
        "rel":"Classic Old Fashioned",
        "note":"Amaro shows off its versatility when used as the core of an Old-Fashioned; it also provides seasoning and sweetness, so neither bitters nor sugar syrup is needed. In this recipe, the brandy primarily provides a focused booxy flavor and dries the drink out, and a generous amount of salt solution rounds off the bitter edges.",
        "met":"Stir all the ingredients over ice, then strain into an Old-Fashioned glass over 1 large ice cube. Express the orange twist over the drink, then gently rub it around the rim of the flass and place it into the drink.",
        "ref":"Cocktail Codex: Fundamentals, Formulas, Evolutions, Pg 11"
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
        if coc.get("ref") is not None:
            coc_obj.reference = coc["ref"]
        coc_obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0005_fill_ing_desc'),
    ]

    operations = [
        migrations.RunPython(fill_coc)
    ]
