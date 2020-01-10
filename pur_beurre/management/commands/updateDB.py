from django.core.management.base import BaseCommand, CommandError
import json
from snacks.models import Product


class Command(BaseCommand):
  help = """This function will update the products' database, from db.json
    file."""

  def handle(self, *args, **options):
    """
    This function will update the products' database, from db.json file.
    """
    try:
      self.stdout.write(self.style.SUCCESS("Hello World"))
      # with open('db.json') as f:
      #   prod_json = json.load(f)

      # for prod in prod_json:
      #   if not Product.objects.filter(ean=prod['ean'].lower()).exists():
      #     prod = Product(ean=prod['ean'].lower(),
      #                    name=prod['name'].lower(),
      #                    category=prod['category'].lower(),
      #                    image=prod['image'].lower(),
      #                    nutriscore=prod['nutriscore'].lower())
      #     prod.save()
    except:
      raise CommandError('Something went wrong here')