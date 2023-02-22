from __future__ import unicode_literals

from django.db import migrations
from django.db import transaction


def populate_recipedetail(apps,schema_editor):
    RecipeDetail = apps.get_model("cocktails", "RecipeDetail")
    Ingredient = apps.get_model("cocktails", "Ingredient")
    Cocktail = apps.get_model("cocktails", "Cocktail")
    db_alias = schema_editor.connection.alias

    recipe_list = [
        # {"coc":"", "ing":"", "quant":, "unit":"", "rec":""},

        # Gin Shaken: 
        {"coc":"Bella Luna", "ing":"Plymouth Gin", "quant":2, "unit":"oz"}, 
        {"coc":"Bella Luna", "ing":"Elderflower Liqueur", "quant":0.75, "unit":"oz"}, 
        {"coc":"Bella Luna", "ing":"Creme Yvette", "quant":0.5, "unit":"oz"}, 
        {"coc":"Bella Luna", "ing":"Fresh Lemon Juice", "quant":0.75, "unit":"oz"}, 
        {"coc":"Bella Luna", "ing":"Simple Syrup", "quant":1, "unit":"tsp"}, 
  
        # Gin Stirred: 
        {"coc":"European Union", "ing":"Old Tom Gin", "quant":1.5, "unit":"oz", "rec":"Hayman's Old Tom Gin"}, 
        {"coc":"European Union", "ing":"Red Vermouth", "quant":1, "unit":"oz", "rec":"Martini Sweet Vermouth"}, 
        {"coc":"European Union", "ing":"Calvados", "quant":0.5, "unit":"oz", "rec":"Busnel VSOP Calvados"}, 
        {"coc":"European Union", "ing":"Strega", "quant":1, "unit":"tsp"}, 
        {"coc":"European Union", "ing":"Bitter Truth Aromatic Bitters", "quant":1, "unit":"dash"}, 
  
        # Rum Shaken: 
        {"coc":"Flor de Jerez", "ing":"Jamaican Rum", "quant":0.5, "unit":"oz", "rec":"Appleton Estate Reserve Rum"}, 
        {"coc":"Flor de Jerez", "ing":"Amontillado Sherry", "quant":1.5, "unit":"oz", "rec":"Lustau Amontillado Sherry"}, 
        {"coc":"Flor de Jerez", "ing":"Apricot Liqueur", "quant":0.25, "unit":"oz", "rec":"Rothman & Winter Apricot Liqueur"}, 
        {"coc":"Flor de Jerez", "ing":"Fresh Lemon Juice", "quant":0.75, "unit":"oz"}, 
        {"coc":"Flor de Jerez", "ing":"Cane Sugar Syrup", "quant":0.5, "unit":"oz"}, 
        {"coc":"Flor de Jerez", "ing":"Angostura Bitters", "quant":1, "unit":"dash"}, 
  
        # Rum Stirred: 
        {"coc":"Arrack Strap", "ing":"Black Strap Rum", "quant":1, "unit":"oz", "rec":"Cruzan Black Strap Rum"}, 
        {"coc":"Arrack Strap", "ing":"Batavia Arrack", "quant":1, "unit":"oz", "rec":"Van Oosten Batavia Arrack"}, 
        {"coc":"Arrack Strap", "ing":"Red Vermouth", "quant":1, "unit":"oz", "rec":"Cocchi Vermouth di Torino"}, 
        {"coc":"Arrack Strap", "ing":"Campari", "quant":1, "unit":"tsp"}, 
        {"coc":"Arrack Strap", "ing":"Demerara Syrup", "quant":0.5, "unit":"oz"}, 
        {"coc":"Arrack Strap", "ing":"Xocolatl Mole Bitters", "quant":2, "unit":"dash"}, 
        {"coc":"Arrack Strap", "ing":"Orange Bitters", "quant":2, "unit":"dash"}, 
        {"coc":"Arrack Strap", "ing":"Orange Twist", "quant":1}, 
  
        # Agave Shaken: 
        {"coc":"Ghost of Mazagran", "ing":"Blanco Tequila", "quant": 1, "unit":"oz"}, 
        {"coc":"Ghost of Mazagran", "ing":"Blanco Mezcal", "quant": 1, "unit":"oz"}, 
        {"coc":"Ghost of Mazagran", "ing":"Coffee Liqueur", "quant": 0.5, "unit":"oz", "rec":"Mr.Black"}, 
        {"coc":"Ghost of Mazagran", "ing":"Red Vermouth", "quant": 0.5, "unit":"oz", "rec":"Punt e Mes"}, 
        {"coc":"Ghost of Mazagran", "ing":"Fresh Lemon Juice", "quant": 0.5, "unit":"oz"}, 
        {"coc":"Ghost of Mazagran", "ing":"Egg White", "quant": 0.5}, 
        {"coc":"Ghost of Mazagran", "ing":"Chipotle Salt", "quant": 1, "unit":"pinch"}, 
        {"coc":"Ghost of Mazagran", "ing":"Xocolatl Mole Bitters", "quant":3, "unit":"dash"}, 
  
        {"coc":"Almond Brother", "ing":"Reposado Tequila", "quant":2, "unit":"oz", "rec":"Siete Leguas Reposado Tequila"}, 
        {"coc":"Almond Brother", "ing":"Amaretto", "quant":0.25, "unit":"oz"}, 
        {"coc":"Almond Brother", "ing":"Apricot Liqueur", "quant":1, "unit":"tsp", "rec":"Rothman & Winter Apricot Liqueur"}, 
        {"coc":"Almond Brother", "ing":"Fresh Lime Juice", "quant":0.75, "unit":"oz"}, 
        {"coc":"Almond Brother", "ing":"Orgeat", "quant":0.25, "unit":"oz"}, 
        {"coc":"Almond Brother", "ing":"Maple Syrup", "quant":0.25, "unit":"oz"}, 
  
        # Agave Stirred: 
        {"coc":"Coralillo", "ing":"Anejo Tequila", "quant":1.5, "unit":"oz", "rec":"El Tesoro Anejo Tequila"}, 
        {"coc":"Coralillo", "ing":"Yellow Chartreuse", "quant":0.75, "unit":"oz"}, 
        {"coc":"Coralillo", "ing":"Calvados", "quant":0.75, "unit":"oz", "rec":"Busnel VSOP Calvados"}, 
        {"coc":"Coralillo", "ing":"Pear Brandy", "quant":0.25, "unit":"oz", "rec":"Clear Creek Pear Brandy"}, 
        {"coc":"Coralillo", "ing":"Apple Slice", "quant":1}, 
  
        # Whisk(e)y Shaken: 
        {"coc":"Ginger Man", "ing":"Islay Scotch", "quant":1.5, "unit":"oz", "rec":"Laphroaig 10-Year Single Malt Scotch"}, 
        {"coc":"Ginger Man", "ing":"Fresh Cantaloupe Juice", "quant":0.75, "unit":"oz"}, 
        {"coc":"Ginger Man", "ing":"Fresh Lemon Juice", "quant":0.75, "unit":"oz"}, 
        {"coc":"Ginger Man", "ing":"Ginger Syrup", "quant":0.5, "unit":"oz"}, 
        {"coc":"Ginger Man", "ing":"Angostura Bitters", "quant":1, "unit":"dash"}, 
  
        {"coc":"19th Century", "ing":"Bourbon", "quant":1.5, "unit":"oz", "rec":"Woodford Reserve Bourbon"}, 
        {"coc":"19th Century", "ing":"Lillet Rouge", "quant":0.75, "unit":"oz"}, 
        {"coc":"19th Century", "ing":"Creme de Cacao", "quant":0.75, "unit":"oz"}, 
        {"coc":"19th Century", "ing":"Fresh Lemon Juice", "quant":0.75, "unit":"oz"}, 
  
        # Whisk(e)y Stirred: 
        {"coc":"The Dangerous Summer", "ing":"Japanese Whisky", "quant":1.5, "unit":"oz", "rec":"Yamazaki 12-Year Whiskey"}, 
        {"coc":"The Dangerous Summer", "ing":"Red Vermouth", "quant":0.75, "unit":"oz", "rec":"Dolin Rouge Vermouth"}, 
        {"coc":"The Dangerous Summer", "ing":"Blood Orange Liqueur", "quant":0.5, "unit":"oz", "rec":"Solerno Blood Orange Liqueur"}, 
        {"coc":"The Dangerous Summer", "ing":"Cherry Brandy", "quant":0.5, "unit":"oz", "rec":"Massenez Kirsch Vieux Cherry Brandy"}, 
        {"coc":"The Dangerous Summer", "ing":"Orange Twist", "quant":1}, 
  
        # Brandy Shaken: 
        {"coc":"Enchanted Orchard", "ing":"Pisco", "quant":1.5, "unit":"oz", "rec":"Campo de Encanto Acholado Pisco"}, 
        {"coc":"Enchanted Orchard", "ing":"Calvados", "quant":0.5, "unit":"oz", "rec":"Busnel VSOP Calvados"}, 
        {"coc":"Enchanted Orchard", "ing":"Benedictine", "quant":0.5, "unit":"oz"}, 
        {"coc":"Enchanted Orchard", "ing":"Fresh Pineapple Juice", "quant":0.5, "unit":"oz"}, 
        {"coc":"Enchanted Orchard", "ing":"Fresh Lemon Juice", "quant":0.5, "unit":"oz"}, 
        {"coc":"Enchanted Orchard", "ing":"Honey Syrup", "quant":0.5, "unit":"oz"}, 
        {"coc":"Enchanted Orchard", "ing":"Cinnamon Stick", "quant":1}, 
  
        # Brandy Stirred: 
        {"coc":"Les Verts Monts", "ing":"Armagnac", "quant":1, "unit":"oz", "rec":"Tariquet VS Classsique Bas-Armagnac"}, 
        {"coc":"Les Verts Monts", "ing":"Cognac", "quant":0.75, "unit":"oz", "rec":"Guillon-Painturaud Cognac Grande Champagne VSOP"}, 
        {"coc":"Les Verts Monts", "ing":"Calvados", "quant":0.75, "unit":"oz", "rec":"Busnel VSOP Calvados"}, 
        {"coc":"Les Verts Monts", "ing":"Blanc Vermouth", "quant":0.75, "unit":"oz", "rec":"Dolin Blanc Vermouth"}, 
        {"coc":"Les Verts Monts", "ing":"Cream Sherry", "quant":0.25, "unit":"oz", "rec":"alvear Festival Pale Cream Sherry"}, 
        {"coc":"Les Verts Monts", "ing":"Maple Syrup", "quant":0.25, "unit":"oz"}, 
        {"coc":"Les Verts Monts", "ing":"Angostura Bitters", "quant":0.25, "unit":"dash"}, 
        {"coc":"Les Verts Monts", "ing":"Lemon Twist", "quant":1}, 
        {"coc":"Les Verts Monts", "ing":"Apple Slice", "quant":1}, 
  
        # Sparkling Cocktail: 
        {"coc":"Champagne Cocktail", "ing":"Dry Champagne", "quant":2, "unit":"oz"}, 
        {"coc":"Champagne Cocktail", "ing":"Sugar Cube", "quant":1}, 
        {"coc":"Champagne Cocktail", "ing":"Angostura Bitters", "quant":3, "unit":"dash"}, 
  
        {"coc":"The Field Marshall", "ing":"Armagnac", "quant":1, "unit":"oz", "rec":"Tariquet Classique VS Bas-Armagnac"}, 
        {"coc":"The Field Marshall", "ing":"Orange Liqueur", "quant":0.5, "unit":"oz", "rec":"Royal Combier"}, 
        {"coc":"The Field Marshall", "ing":"Angostura Bitters", "quant":2, "unit":"dash"}, 
        {"coc":"The Field Marshall", "ing":"Peychaud's Bitters", "quant":2, "unit":"dash"}, 
        {"coc":"The Field Marshall", "ing":"Dry Champagne", "quant":4, "unit":"oz"}, 
        {"coc":"The Field Marshall", "ing":"Lemon Twist", "quant":1}, 
  
        {"coc":"Pretty Wings", "ing":"Chamomile-Infused Cocchi Americano", "quant":0.5, "unit":"oz"}, 
        {"coc":"Pretty Wings", "ing":"Suze", "quant":1, "unit":"tsp"}, 
        {"coc":"Pretty Wings", "ing":"Hopped Grapefruit Bitters", "quant":1, "unit":"dash"}, 
        {"coc":"Pretty Wings", "ing":"Dry Champagne", "quant":5, "unit":"oz"}, 
        {"coc":"Pretty Wings", "ing":"Lemon Wheel", "quant":1}, 
  
        {"coc":"Celebrate", "ing":"Pear Brandy", "quant":0.5, "unit":"oz", "rec":"Clear Creek"}, 
        {"coc":"Celebrate", "ing":"Amontillado Sherry", "quant":0.25, "unit":"oz", "rec":"Lustau Jarana Fino Sherry"}, 
        {"coc":"Celebrate", "ing":"Reposado Tequila", "quant":1, "unit":"tsp", "rec":"Fortaleza Reposado Tequila"}, 
        {"coc":"Celebrate", "ing":"Cinnamon Syrup", "quant":0.25, "unit":"oz"}, 
        {"coc":"Celebrate", "ing":"Champagne Acid Solution", "quant":0.5, "unit":"tsp"}, 
        {"coc":"Celebrate", "ing":"Dry Champagne", "quant":4, "unit":"oz"}, 
  
        # Fortified Wine Cocktails: 
        {"coc":"Derby Girl", "ing":"Nectarine Slice", "quant":3}, 
        {"coc":"Derby Girl", "ing":"Lillet Blanc", "quant":1.5, "unit":"oz"}, 
        {"coc":"Derby Girl", "ing":"Suze", "quant":0.5, "unit":"oz", "rec":"Suze Saveur D'Autrefois Liqueur"}, 
        {"coc":"Derby Girl", "ing":"Rose Hip Liqueur", "quant":0.5, "unit":"oz", "rec":"Koval Rose Hip Liqueur"}, 
        {"coc":"Derby Girl", "ing":"Honey Syrup", "quant":0.25, "unit":"oz"}, 
        {"coc":"Derby Girl", "ing":"Mint Bouquet", "quant":1}, 

        {"coc":"Sherry Cobbler", "ing":"Orange Slice", "quant":3},
        {"coc":"Sherry Cobbler", "ing":"Cane Sugar Syrup", "quant":1, "unit":"tsp"},
        {"coc":"Sherry Cobbler", "ing":"Amontillado Sherry", "quant":3.5, "unit":"oz"},
        {"coc":"Sherry Cobbler", "ing":"Mint Bouquet", "quant":1},
        {"coc":"Sherry Cobbler", "ing":"Orange Wheel", "quant":1},

        {"coc":"Traction", "ing":"Lemon Wedge", "quant":3},
        {"coc":"Traction", "ing":"Strawberry", "quant":1.5},
        {"coc":"Traction", "ing":"Amontillado Sherry", "quant":1.5, "unit":"oz", "rec":"Lustau Los Arcos amontillado Sherry"},
        {"coc":"Traction", "ing":"Spanish Rum", "quant":0.5, "unit":"oz", "rec":"Santa Teresa 1796 Rum"},
        {"coc":"Traction", "ing":"Milk & Honey House Curacao", "quant":0.75, "unit":"oz"},
        {"coc":"Traction", "ing":"Mint Sprig", "quant":1},

        # Punch: 
        {"coc":"Kill-Devil Punch", "ing":"Sugar Cube", "quant":12}, 
        {"coc":"Kill-Devil Punch", "ing":"Raspberry", "quant":27}, 
        {"coc":"Kill-Devil Punch", "ing":"Seltzer", "quant":3, "unit":"oz"}, 
        {"coc":"Kill-Devil Punch", "ing":"Jamaican Rum", "quant":6, "unit":"oz", "rec":"Appleton Estate V/X Rum"}, 
        {"coc":"Kill-Devil Punch", "ing":"Fresh Lime Juice", "quant":3, "unit":"oz"}, 
        {"coc":"Kill-Devil Punch", "ing":"Fresh Pineapple Juice", "quant":3, "unit":"oz"}, 
        {"coc":"Kill-Devil Punch", "ing":"Dry Champagne", "quant":3, "unit":"oz"},  
  
        # Julep: 
        {"coc":"Mint Julep", "ing":"Bourbon", "quant":2, "unit":"oz", "rec":"Buffalo Trace Bourbon"}, 
        {"coc":"Mint Julep", "ing":"Simple Syrup", "quant":0.25, "unit":"oz"}, 
        {"coc":"Mint Julep", "ing":"Mint Bouquet", "quant":1}, 

        {"coc":"Last One Standing", "ing":"Mint Bouquet", "quant":1}, 
        {"coc":"Last One Standing", "ing":"Cognac", "quant":1, "unit":"oz"}, 
        {"coc":"Last One Standing", "ing":"Jamaican Rum", "quant":1, "unit":"oz"}, 
        {"coc":"Last One Standing", "ing":"Amaro CioCiaro", "quant":1, "unit":"oz"}, 
        {"coc":"Last One Standing", "ing":"Creme de Peche", "quant":1, "unit":"tsp"}, 
        {"coc":"Last One Standing", "ing":"Peach Slice", "quant":1}, 
        {"coc":"Last One Standing", "ing":"Confectionery Sugar", "quant":1, "unit":"pinch"}, 

        {"coc":"Heritage Julep", "ing":"Mint Bouquet", "quant":1}, 
        {"coc":"Heritage Julep", "ing":"Calvados", "quant":1.25, "unit":"oz", "rec":"Busnel Pays d’Auge VSOP Calvados"}, 
        {"coc":"Heritage Julep", "ing":"Pear Liqueur", "quant":0.5, "unit":"oz", "rec":"Clear Creek Pear Liqueur"}, 
        {"coc":"Heritage Julep", "ing":"Pear Brandy", "quant":0.25, "unit":"oz", "rec":"Clear Creek Pear Brandy"}, 
        {"coc":"Heritage Julep", "ing":"Amaro Montenegro", "quant":0.25, "unit":"oz"}, 
        {"coc":"Heritage Julep", "ing":"Cinnamon Syrup", "quant":1, "unit":"tsp"}, 
        {"coc":"Heritage Julep", "ing":"Phosphoric Acid Solution", "quant":2, "unit":"dash"}, 
        {"coc":"Heritage Julep", "ing":"Apple Slice", "quant":3}, 
        {"coc":"Heritage Julep", "ing":"Confectionery Sugar", "quant":1, "unit":"pinch"}, 
  
        # Flips and Fizzes: 
        {"coc":"Chinese Fizz", "ing":"Jamaican Rum", "quant":2, "unit":"oz", "rec":"Apple Estate V/X Rum"}, 
        {"coc":"Chinese Fizz", "ing":"Orange Liqueur", "quant":0.25, "unit":""}, 
        {"coc":"Chinese Fizz", "ing":"Maraschino Liqueur", "quant":0.25, "unit":"oz", "rec":"Luxardo Maraschino Liqueur"}, 
        {"coc":"Chinese Fizz", "ing":"Fresh Lemon Juice", "quant":0.5, "unit":"oz"}, 
        {"coc":"Chinese Fizz", "ing":"Simple Syrup", "quant":0.5, "unit":"oz"}, 
        {"coc":"Chinese Fizz", "ing":"Grenadine", "quant":0.25, "unit":"oz"}, 
        {"coc":"Chinese Fizz", "ing":"Egg White", "quant":1}, 
        {"coc":"Chinese Fizz", "ing":"Angostura Bitters", "quant":1, "unit":"dash"}, 
        {"coc":"Chinese Fizz", "ing":"Orange Wheel", "quant":1}, 
  
        # Swizzles: 
        {"coc":"Dolores Park Swizzle", "ing":"Anejo Tequila", "quant":1, "unit":"oz"}, 
        {"coc":"Dolores Park Swizzle", "ing":"Amontillado Sherry", "quant":1, "unit":"oz", "rec":"Lustau Amontillado Sherry"}, 
        {"coc":"Dolores Park Swizzle", "ing":"Velvet Falernum", "quant":0.25, "unit":"oz"}, 
        {"coc":"Dolores Park Swizzle", "ing":"Fresh Lime Juice", "quant":0.75, "unit":"oz"}, 
        {"coc":"Dolores Park Swizzle", "ing":"Ginger Syrup", "quant":0.75, "unit":"oz"}, 
        {"coc":"Dolores Park Swizzle", "ing":"Angostura Bitters", "quant":3, "unit":"dash"}, 
        {"coc":"Dolores Park Swizzle", "ing":"Mint Sprig", "quant":1}, 
  
        # Aquavit: 
        {"coc":"Slap 'N' Pickle", "ing":"Cucumber Wheel", "quant":3},
        {"coc":"Slap 'N' Pickle", "ing":"Aquavit", "quant":2, "unit":"oz", "rec":"Krogstad Aquavit"},
        {"coc":"Slap 'N' Pickle", "ing":"Fresh Lime Juice", "quant":0.75, "unit":"oz"},
        {"coc":"Slap 'N' Pickle", "ing":"Simple Syrup", "quant":0.75, "unit":"oz"},
        {"coc":"Slap 'N' Pickle", "ing":"Grenadine", "quant":1, "unit":"tsp"},
        {"coc":"Slap 'N' Pickle", "ing":"Celery Bitters", "quant":2, "unit":"dash"},
        {"coc":"Slap 'N' Pickle", "ing":"Cucumber Spear", "quant":1},
  
        # Martini and variants: 
        {"coc":"Classic Martini", "ing":"Old Tom Gin", "quant": 2, "unit":"oz"}, 
        {"coc":"Classic Martini", "ing":"Dry Vermouth", "quant": 0.75, "unit":"oz"}, 
        {"coc":"Classic Martini", "ing":"Lemon Twist", "quant": 1}, 
        {"coc":"Classic Martini", "ing":"Olive", "quant": 1, "opt":True}, 
  
        # Sazerac and variants:  
        {"coc":"Sazerac", "ing":"Absinthe", "quant": 1, "unit":"rinse", "rec":"Vieux Pontarlier Absinthe"}, 
        {"coc":"Sazerac", "ing":"Rye Whiskey", "quant": 1.5, "unit":"oz", "rec":"Rittenhouse Rye"}, 
        {"coc":"Sazerac", "ing":"Cognac", "quant": 0.5, "unit":"oz", "rec":"Pierre Ferrand 1840 Cognac"}, 
        {"coc":"Sazerac", "ing":"Demerara Gum Syrup", "quant": 1, "unit":"tsp"}, 
        {"coc":"Sazerac", "ing":"Peychaud's Bitters", "quant": 4, "unit":"dash"}, 
        {"coc":"Sazerac", "ing":"Angostura Bitters", "quant": 1, "unit":"dash"}, 
        {"coc":"Sazerac", "ing":"Lemon Twist", "quant": 1}, 

        {"coc":"Cut and Paste", "ing":"Absinthe", "quant":1, "unit":"rinse", "rec":"Vieux Pontarlier Absinthe"},
        {"coc":"Cut and Paste", "ing":"Apple Brandy", "quant":1.5, "unit":"oz", "rec":"Clear Creek 8-year Apple Brandy"},
        {"coc":"Cut and Paste", "ing":"Irish Whiskey", "quant":0.75, "unit":"oz", "rec":"Redbreast 12-year Irish Whiskey"},
        {"coc":"Cut and Paste", "ing":"Honey Syrup", "quant":0.25, "unit":"oz"},
        {"coc":"Cut and Paste", "ing":"Peychaud's Bitters", "quant":3, "unit":"dash"},
        {"coc":"Cut and Paste", "ing":"Angostura Bitters", "quant":1, "unit":"dash"},

        {"coc":"Bananarac", "ing":"Absinthe", "quant":1, "unit":"rinse", "rec":"Pernod Absinthe"},
        {"coc":"Bananarac", "ing":"Cognac", "quant":1, "unit":"oz", "rec":"Pierre Ferrand 1840 Cognac"},
        {"coc":"Bananarac", "ing":"Rye Whiskey", "quant":1, "unit":"oz", "rec":"Old Overholt Rye"},
        {"coc":"Bananarac", "ing":"Banane du Bresil", "quant":0.5, "unit":"oz"},
        {"coc":"Bananarac", "ing":"Demerara Gum Syrup", "quant":0.5, "unit":"tsp"},
        {"coc":"Bananarac", "ing":"Lemon Twist", "quant":1},
  
        # Negroni and variants: 
        {"coc":"Fail-Safe", "ing":"Navy-Strength Gin", "quant":0.75, "unit":"oz", "rec":"Perry's Tot Navy-Strength Gin"}, 
        {"coc":"Fail-Safe", "ing":"Sloe Berry Liqueur", "quant":0.5, "unit":"oz", "rec":"Plymouth Sloe Gin"}, 
        {"coc":"Fail-Safe", "ing":"Aperol", "quant":0.5, "unit":"oz"}, 
        {"coc":"Fail-Safe", "ing":"Orange Liqueur", "quant":0.5, "unit":"oz", "rec":"Pierre Ferrand Dry Curacao"}, 
        {"coc":"Fail-Safe", "ing":"Angostura Bitters", "quant":2, "unit":"dash"}, 
  
        # Daiquiri and variants: 
        {"coc":"Classic Daiquiri", "ing":"Spanish White Rum", "quant": 2, "unit":"oz"}, 
        {"coc":"Classic Daiquiri", "ing":"Rhum Agricole Blanc", "quant": 0.25, "unit":"oz", "opt":True}, 
        {"coc":"Classic Daiquiri", "ing":"Fresh Lime Juice", "quant": 0.75, "unit":"oz"}, 
        {"coc":"Classic Daiquiri", "ing":"Simple Syrup", "quant": 0.75, "unit":"oz"}, 
        {"coc":"Classic Daiquiri", "ing":"Lime Wedge", "quant": 1}, 
  
        {"coc":"D.W.B.", "ing":"Rhum Agricole Blanc", "quant": 2, "unit":"oz", "rec":"La Favorite Rhum Agricole Blanc"}, 
        {"coc":"D.W.B.", "ing":"Batavia Arrack", "quant": 0.5, "unit":"oz", "rec":"Van Oosten Batavia Arrack"}, 
        {"coc":"D.W.B.", "ing":"Fresh Lime Juice", "quant": 0.75, "unit":"oz"}, 
        {"coc":"D.W.B.", "ing":"Cane Sugar Syrup", "quant": 0.5, "unit":"oz"}, 
        {"coc":"D.W.B.", "ing":"Lime Wedge", "quant": 1}, 
  
        {"coc":"Rumor Mill", "ing":"Dry Champagne", "quant":1.5, "unit":"oz"}, 
        {"coc":"Rumor Mill", "ing":"Rhum Agricole Blanc", "quant":1, "unit":"oz", "rec":"La Favorite Rhum Agricole Blanc"}, 
        {"coc":"Rumor Mill", "ing":"Dry Vermouth", "quant":0.5, "unit":"oz", "rec":"Dolin Dry Vermouth"}, 
        {"coc":"Rumor Mill", "ing":"Cane Sugar Syrup", "quant":0.5, "unit":"oz"}, 
        {"coc":"Rumor Mill", "ing":"Fresh Celery Juice", "quant":0.5, "unit":"oz"}, 
        {"coc":"Rumor Mill", "ing":"Fresh Lime Juice", "quant":0.5, "unit":"oz"}, 
        {"coc":"Rumor Mill", "ing":"Absinthe", "quant":1, "unit":"dash"}, 
  
        # Manhattan and variants: 
        {"coc":"The Black Prince", "ing":"Spanish Rum", "quant":2, "unit":"oz", "rec":"Zacapa 23-Year Rum"},
        {"coc":"The Black Prince", "ing":"Red Vermouth", "quant":0.75, "unit":"oz", "rec":"Punt e Mes"},
        {"coc":"The Black Prince", "ing":"Amaro Averna", "quant":0.5, "unit":"oz"},
        {"coc":"The Black Prince", "ing":"Death & Co House Orange Bitters", "quant":1, "unit":"dash"},
  
        # Old Fashioned and variants: 
        {"coc":"Classic Old Fashioned", "ing":"Bourbon", "quant": 2, "unit":"oz"}, 
        {"coc":"Classic Old Fashioned", "ing":"Sugar Cube", "quant": 1, "unit":""}, 
        {"coc":"Classic Old Fashioned", "ing":"Angostura Bitters", "quant": 2, "unit":"dash"}, 
        {"coc":"Classic Old Fashioned", "ing":"Lemon Twist", "quant": 1}, 
        {"coc":"Classic Old Fashioned", "ing":"Orange Twist", "quant": 1}, 
  
        {"coc":"Fancy Free", "ing":"Rye Whiskey", "quant": 2, "unit":"oz", "rec":"Rittenhouse Rye"}, 
        {"coc":"Fancy Free", "ing":"Maraschino Liqueur", "quant": 0.5, "unit":"oz", "rec":"Luxardo Maraschino Liqueur"}, 
        {"coc":"Fancy Free", "ing":"Angostura Bitters", "quant": 1, "unit":"dash"}, 
        {"coc":"Fancy Free", "ing":"Death & Co House Orange Bitters", "quant": 1, "unit":"dash"}, 
        {"coc":"Fancy Free", "ing":"Orange Twist", "quant": 1}, 
  
        {"coc":"Chrysanthemum", "ing":"Dry Vermouth", "quant": 2.5, "unit":"oz", "rec":"Dolin Dry Vermouth"}, 
        {"coc":"Chrysanthemum", "ing":"Benedictine", "quant": 0.5, "unit":"oz"}, 
        {"coc":"Chrysanthemum", "ing":"Absinthe", "quant": 1, "unit":"tsp", "rec":"Pernod Absinthe"}, 
        {"coc":"Chrysanthemum", "ing":"Orange Twist", "quant": 1}, 
  
        {"coc":"Ti' Punch", "ing":"Lime Peel", "quant": 1}, 
        {"coc":"Ti' Punch", "ing":"Cane Sugar Syrup", "quant": 1, "unit":"tsp"}, 
        {"coc":"Ti' Punch", "ing":"Rhum Agricole Blanc", "quant": 2, "unit":"oz", "rec":"La Favorite Couer de Canne"}, 
  
        {"coc":"Stinger", "ing":"Cognac", "quant": 2, "unit":"oz", "rec":"Pierre Ferrand Ambre Cognac"}, 
        {"coc":"Stinger", "ing":"Creme de Menthe", "quant": 0.5, "unit":"oz"}, 
        {"coc":"Stinger", "ing":"Simple Syrup", "quant": 1, "unit":"tsp"}, 
        {"coc":"Stinger", "ing":"Mint Sprig", "quant": 1}, 
  
        {"coc":"Monte Carlo", "ing":"Rye Whiskey", "quant": 2, "unit":"oz", "rec":"Rittenhouse Rye"}, 
        {"coc":"Monte Carlo", "ing":"Benedictine", "quant": 0.5, "unit":"oz"}, 
        {"coc":"Monte Carlo", "ing":"Angostura Bitters", "quant": 2, "unit":"dash"}, 
        {"coc":"Monte Carlo", "ing":"Lemon Twist", "quant": 1}, 

        {"coc":"Vermouth Cocktail", "ing":"Red Vermouth", "quant":2, "unit":"oz", "rec":"Carpano Antica Formula Vermouth"},
        {"coc":"Vermouth Cocktail", "ing":"Simple Syrup", "quant":1.5, "unit":"oz"},
        {"coc":"Vermouth Cocktail", "ing":"Angostura Bitters", "quant":2, "unit":"dash"},
        {"coc":"Vermouth Cocktail", "ing":"Orange Bitters", "quant":1, "unit":"dash"},
        {"coc":"Vermouth Cocktail", "ing":"Lemon Twist", "quant":1},

        {"coc":"Improved Whiskey Cocktail", "ing":"Bourbon", "quant":2, "unit":"oz", "rec":"Elijah Craig Small Batch bourbon"},
        {"coc":"Improved Whiskey Cocktail", "ing":"Maraschino Liqueur", "quant":1, "unit":"tsp", "rec":"Maraska Maraschino Liqueur"},
        {"coc":"Improved Whiskey Cocktail", "ing":"Absinthe", "quant":1, "unit":"dash"},
        {"coc":"Improved Whiskey Cocktail", "ing":"Angostura Bitters", "quant":1, "unit":"dash"},
        {"coc":"Improved Whiskey Cocktail", "ing":"Peychaud's Bitters", "quant":1, "unit":"dash"},
        {"coc":"Improved Whiskey Cocktail", "ing":"Lemon Twist", "quant":1},

        {"coc":"Pop Quiz", "ing":"Bourbon", "quant":2, "unit":"oz", "rec":"Elijah Craig Small Batch Bourbon"},
        {"coc":"Pop Quiz", "ing":"Ramazzotti", "quant":0.5, "unit":"oz"},
        {"coc":"Pop Quiz", "ing":"Simple Syrup", "quant":1, "unit":"tsp"},
        {"coc":"Pop Quiz", "ing":"Xocolatl Mole Bitters", "quant":2, "unit":"dash"},
        {"coc":"Pop Quiz", "ing":"Orange Twist", "quant":1},

        {"coc":"Snowbird", "ing":"Rye Whiskey", "quant":1.5, "unit":"oz", "rec":"Rittenhouse Rye"},
        {"coc":"Snowbird", "ing":"Apple Brandy", "quant":0.5, "unit":"oz", "rec":"Clear Creek 2-year Apple Brandy"},
        {"coc":"Snowbird", "ing":"Cardamom-Infused St-Germain", "quant":0.5, "unit":"oz"},
        {"coc":"Snowbird", "ing":"Demerara Gum Syrup", "quant":0.5, "unit":"tsp"},
        {"coc":"Snowbird", "ing":"Celery Bitters", "quant":4, "unit":"drop"},
        {"coc":"Snowbird", "ing":"Grapefruit Twist", "quant":1},

        {"coc":"Ned Ryerson", "ing":"Rye Whiskey", "quant":1.5, "unit":"oz", "rec":"Bulleit Rye"},
        {"coc":"Ned Ryerson", "ing":"Apple Brandy", "quant":0.5, "unit":"oz", "rec":"Clear Creek 2-year Apple Brandy"},
        {"coc":"Ned Ryerson", "ing":"Demerara Gum Syrup", "quant":1, "unit":"tsp"},
        {"coc":"Ned Ryerson", "ing":"Castilian Bitters", "quant":2, "unit":"dash"},
        {"coc":"Ned Ryerson", "ing":"Death & Co House Orange Bitters", "quant":1, "unit":"dash"},
        {"coc":"Ned Ryerson", "ing":"Lemon Twist", "quant":1},

        {"coc":"Tiki-Tiki Tom-Tom", "ing":"English Rum", "quant": 1.5, "unit":"oz", "rec":"El Dorado 15-Year"}, 
        {"coc":"Tiki-Tiki Tom-Tom", "ing":"English Rum", "quant": 0.5, "unit":"oz", "rec":"Scarlet Ibis Rum"}, 
        {"coc":"Tiki-Tiki Tom-Tom", "ing":"Drambuie", "quant": 0.5, "unit":"oz"}, 
        {"coc":"Tiki-Tiki Tom-Tom", "ing":"Strega", "quant": 1, "unit":"tsp"}, 
        {"coc":"Tiki-Tiki Tom-Tom", "ing":"Honey Syrup", "quant": 0.5, "unit":"tsp"}, 
  
        {"coc":"Exit Strategy", "ing":"Amaro Nonino", "quant": 1.5, "unit":"oz"}, 
        {"coc":"Exit Strategy", "ing":"American Brandy", "quant": 0.75, "unit":"oz", "rec":"Germain-Robin Craft-Method brandy"}, 
        {"coc":"Exit Strategy", "ing":"Amaro Meletti", "quant": 0.25, "unit":"oz"}, 
        {"coc":"Exit Strategy", "ing":"Salt Solution", "quant": 6, "unit":"drop"}, 
        {"coc":"Exit Strategy", "ing":"Orange Twist", "quant": 1}, 
     ]


    for rd in recipe_list:
        new_recipe = RecipeDetail(cocktail=Cocktail.objects.using(db_alias).get(name=rd["coc"]), ingredient=Ingredient.objects.using(db_alias).get(name=rd["ing"]))
        new_recipe.quantity = rd["quant"]
        if rd.get("unit") is not None:
            new_recipe.unit = rd["unit"]
        if rd.get("rec") is not None:
            new_recipe.recommended = rd["rec"]
        if rd.get("opt") is not None:
            new_recipe.optional = rd["opt"]
        new_recipe.save()


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0003_populate_coc'),
    ]

    operations = [
        migrations.RunPython(populate_recipedetail)
    ]
