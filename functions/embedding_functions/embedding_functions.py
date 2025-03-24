import os
import httpx
from openai import OpenAI
from scipy.spatial import distance

client = OpenAI(
    http_client = httpx.Client(verify=False)
)

def create_embeddings(texts):
  response = client.embeddings.create(
    model="text-embedding-3-small",
    input=texts
  )
  response_dict = response.model_dump()
  return [data['embedding'] for data in response_dict['data']]

def create_product_text(product):
  return f"""Title: {product['title']}
Description: {product['short_description']}
Category: {product['category']}
Features: {', '.join(product['features'])}"""

def find_n_closest(query_vector, embeddings, n=3):
  distances = []
  for index, embedding in enumerate(embeddings):
    dist = distance.cosine(query_vector, embedding)
    distances.append({"distance": dist, "index": index})
    distances_sorted = sorted(distances, key=lambda x: x['distance'])
  return distances_sorted[:n]