# from __future__ import unicode_literals
#
# from django.db import migrations
# from django.core.management import call_command
#
# import sys
# import logging
# logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
#
#
# def delete_cocktails(apps, schema_editor):
#     Cocktail = apps.get_model("Cocktail")
#     Cocktail.objects.all().delete()
#
#     logging.info("Sucessful deleting all cocktail entries")
#
#
# def delete_ingredients(apps, schema_editor):
#     Ingredient = apps.get_model("Ingredient")
#     Ingredient.objects.all().delete()
#
#     logging.info("Sucessful deleting all ingredient entries")
#
#
# def populate_cocktail_db(apps, schema_editor):
#     call_command("loaddata", "cocktail")
#
#     logging.info("Sucessful populating cocktail table")
#
#
# def populate_ingredient_db(apps, schema_editor):
#     call_command("loaddata", "ingredient")
#
#     logging.info("Sucessful populating ingredient table")
#
#
# class Migration(migrations.Migration):
#
#     dependencies = [
#         ('cocktails', '0001_initial'),
#     ]
#
#     operations = [
#         migrations.RunPython(
#                             delete_cocktails,
#                             delete_ingredients,
#                             populate_cocktail_db,
#                             populate_ingredient_db,
#                             ),
#     ]
