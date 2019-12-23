#!/usr/bin/python3.7
# UTF8
# Date:
# Author: Nicolas Flandrois

import json
import urllib.request
from io import BytesIO

from snacks.nutriment import nutriments

# Mock Testing Json API Open Food Facts


def test_nutriments(monkeypatch):
    results = {"product":
               {"nutriments": {
                   "sugars_unit": "g",
                   "energy_100g": 1660,
                   "proteins_100g": 8.97,
                   "saturated-fat_unit": "g",
                   "saturated-fat_100g": 1.28,
                   "sodium_100g": 0.819,
                   "proteins_unit": "g",
                   "salt_100g": 2.05,
                   "nutrition-score-fr_100g": 16,
                   "fiber_unit": "g",
                   "fiber_100g": 0,
                   "energy_unit": "kcal",
                   "sodium_unit": "g",
                   "fat_unit": "g",
                   "salt_unit": "g",
                   "sugars_100g": 12.8,
                   "fat_100g": 8.97,
                   "carbohydrates_100g": 70.5
               },
               },
               }

    def mockreturn(request):
        return BytesIO(json.dumps(results, sort_keys=True, indent=4,
                                  separators=(',', ': ')).encode())

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)

    test_ean = '1234567890123'

    assert results == nutriments(test_ean)
