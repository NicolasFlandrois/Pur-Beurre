import operator
from .models import Product
# Remplacer Parser par: https://stackoverflow.com/questions/7088173/how-to-query-model-where-name-contains-any-word-in-python-list

def parser(query: str):
  """
  Given a string, this function will split the string into
  a set of words, and then output relevent/targeted set of words.
  This function returns the PK, of product in DB with max matching set.
  """
  products = Product.objects.all()

  products_compare = [(product.pk, set(str(product.name).lower().replace("'", " ")
                                       .replace(".", "").replace(",", "")
                                       .replace("?", "").replace(";", "")
                                       .replace(":", "").replace("à", "")
                                       .replace("-", "").replace("%", "")
                                       .replace("0", "").replace("4", "")
                                       .replace("1", "").replace("5", "")
                                       .replace("2", "").replace("6", "")
                                       .replace("3", "").replace("7", "")
                                       .replace("8", "").replace("9", "")
                                       .replace("!", "").split()))
                      for product in products]

  print(products_compare)

  query_set = set(str(query).lower().replace("'", " ")
                            .replace(".", "").replace(",", "")
                            .replace("?", "").replace(";", "")
                            .replace(":", "").replace("à", "")
                            .replace("-", "").replace("%", "")
                            .replace("0", "").replace("4", "")
                            .replace("1", "").replace("5", "")
                            .replace("2", "").replace("6", "")
                            .replace("3", "").replace("7", "")
                            .replace("8", "").replace("9", "")
                            .replace("!", "").split())

  # From Tuple: product[0] = pk ; product[1] = set(parsed name)

  compare_set = {product[0]: len(query_set.intersection(product[1]))
                 for product in products_compare}

  print("Query", query)
  print("Query Set", query_set)
  print(compare_set)

  print(max(compare_set.items(), key=operator.itemgetter(1))[0])

  return max(compare_set.items(), key=operator.itemgetter(1))
