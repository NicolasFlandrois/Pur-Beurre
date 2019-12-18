import json
from urllib.request import urlopen


def nutriments(ean):
    with urlopen(
            f'https://world.openfoodfacts.org/api/v0/product/{ean}.json') as f:
        data = f.read()
        return json.loads(data)['product']['nutriments']
