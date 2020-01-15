from django.core.management.base import BaseCommand, CommandError
import json
from snacks.models import Product


class Command(BaseCommand):
    help = """This function will update the products' database, from db.json
    file."""

    # def add_arguments(self, parser):
    #     parser.add_argument('db_file', nargs='+', type=str)

    def handle(self, *args, **options):
        """
        This function will update the products' database, from db.json file.
        """
        try:
            # print("We are checking informations from: ", options['db_file'])
            print(
                "We are checking informations from the new databases settings\
 in db.json")
            with open('db.json') as f:
                prod_json = json.load(f)

            for prod in prod_json:
                if not Product.objects.filter(ean=prod['ean'].lower()).exists():
                    prod = Product(ean=prod['ean'].lower(),
                                   name=prod['name'].lower(),
                                   category=prod['category'].lower(),
                                   image=prod['image'].lower(),
                                   nutriscore=prod['nutriscore'].lower())
                    prod.save()
                    print(f'Added to the database :    {prod.name} \
(EAN: {prod.ean}). ')
                else:
                    print(f'This product already part of this database :    \
{Product.objects.get(ean=prod["ean"]).name} (EAN: {prod["ean"]}).')

        except:
            raise CommandError('Something went wrong here')
