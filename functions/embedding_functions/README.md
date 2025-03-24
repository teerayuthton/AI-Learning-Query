# How Embedding function working

Question: Why we should to embedding for search something?

Answer: On LLMs we can use semantic search for find the meaning of the keyword instead matched with keyword.
- Like "Comfortable shoes"
- Semantic serach Result: Matched with "Lightweight shoes", "Soft shoes"
- General search Result: Matched with "Comfortable" and "shes" keywords


Question: Why we need to embedding before search?

Answer: We can't use text for search to find the meaning, We need to change it to be numerical(Vector) then we will use math matic
to find closest points of the Query and Datasets.

# Functions and Data stucture

![Screenshot 2568-03-24 at 13 36 51](https://github.com/user-attachments/assets/aaa68cda-9774-4ae9-93f4-51b2e434f8fa)

JSON structure for testing
```
{
      "title":"Smartphone X1",
      "short_description":"The latest flagship smartphone with AI-powered features and 5G connectivity.",
      "price":799.99,
      "category":"Electronics",
      "features":[
         "6.5-inch AMOLED display",
         "Quad-camera system with 48MP main sensor",
         "Face recognition and fingerprint sensor",
         "Fast wireless charging"
      ]
}
```
# Explain the functions

`create_embeddings`
- This function will transform from texts to be vector before use to find the closest points.

![Screenshot 2568-03-24 at 14 09 33](https://github.com/user-attachments/assets/e31a2de5-c87e-47f8-9519-cf1ffda165ed)

- The Input for use this function.
```
['Title: Smartphone X1\n
Description: The latest flagship smartphone with AI-powered features and 5G connectivity.\n
Category: Electronics\n
Features: 6.5-inch AMOLED display, Quad-camera system with 48MP main sensor, Face recognition and fingerprint sensor, Fast wireless charging',
'Title: ...',
...
]
```
- The result after use this function.
```
[[0.027226606383919716, -0.0037901306059211493, -0.033660367131233215,...]]
```

`create_product_text`
- This function will transform from ductionary to be once text.

![Screenshot 2568-03-24 at 14 15 41](https://github.com/user-attachments/assets/9b9f95b2-2141-409c-aac6-01ba6565f954)

- The Input for use this function.
```
{
      "title":"Smartphone X1",
      "short_description":"The latest flagship smartphone with AI-powered features and 5G connectivity.",
      "price":799.99,
      "category":"Electronics",
      "features":[
         "6.5-inch AMOLED display",
         "Quad-camera system with 48MP main sensor",
         "Face recognition and fingerprint sensor",
         "Fast wireless charging"
      ]
}
```
- The result after use this function.
```
['Title: Smartphone X1\n
Description: The latest flagship smartphone with AI-powered features and 5G connectivity.\n
Category: Electronics\n
Features: 6.5-inch AMOLED display, Quad-camera system with 48MP main sensor, Face recognition and fingerprint sensor, Fast wireless charging',
'Title: ...',
...
]
```

`find_n_closest`
- This function will use to find the closest point between Query(`query_vector`) from Users and Data(`embeddings`) that we have and
the default of the result that we want to return N('n=3')(If user didn't input, We will reture 3)

![Screenshot 2568-03-24 at 14 15 46](https://github.com/user-attachments/assets/847f2f2b-9e9b-4575-8ac9-f2c39d94b824)

- The Input for use this function.
```
hits = find_n_closest(query_vector, product_embeddings)
```

- The result after use this function.
```
hits: [{'distance': 0.7250869422593675, 'index': 11}, {'distance': 0.7559535791154627, 'index': 10}, {'distance': 0.7733542929319654, 'index': 0}]
```

# For get the result from hit matched with our data we should to mapping by index.
- The Example is
```
for hit in hits:
  product = products[hit['index']]
  print(product["title"])
```
- Then result after we matched.
```
Search results for "computer"
High-Performance Gaming Laptop
Robot Building Kit
Smartphone X1
```
