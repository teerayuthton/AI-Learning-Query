import sys
sys.path.append('../')

from functions.import_json_from_local.import_json_from_local import import_json
from functions.embedding_functions.embedding_functions import create_embeddings, create_product_text, find_n_closest

products = import_json("products.json")

product_texts = [create_product_text(product) for product in products]
product_embeddings = create_embeddings(product_texts)

query_text = "computer"
query_vector = create_embeddings(query_text)[0]

hits = find_n_closest(query_vector, product_embeddings)

print(f'Search results for "{query_text}"')
for hit in hits:
  product = products[hit['index']]
  print(product["title"])