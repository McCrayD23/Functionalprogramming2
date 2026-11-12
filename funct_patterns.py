from functools import reduce


products = [
    {"name": "Laptop", "price": 999.99, "category": "electronics", "in_stock": True},
    {"name": "Python Book", "price": 39.99, "category": "books", "in_stock": True},
    {"name": "Headphones", "price": 149.99, "category": "electronics", "in_stock": False},
    {"name": "Desk Lamp", "price": 29.99, "category": "home", "in_stock": True},
    {"name": "AI Textbook", "price": 89.99, "category": "books", "in_stock": True},
    {"name": "Monitor", "price": 349.99, "category": "electronics", "in_stock": True},
    {"name": "Notebook", "price": 4.99, "category": "office", "in_stock": True},
    {"name": "Keyboard", "price": 79.99, "category": "electronics", "in_stock": False},
    ]

# Get all in-stock products (filter) (using lambda)
in_stock_products = list(filter(lambda product: product["in_stock"], products))


"""Add a "discounted_price" field that's 10% off the original (map- create new dicts, don't mutate)"""
discounted_products = list(map(lambda product: {**product, "discounted_price": round(product["price"] * 0.90, 2)}, products))

"""Get only electronics under $200 (filter with two conditions)"""
electronics_under_200 = list(filter(lambda product: product["category"] == "electronics" and product["price"] < 200, products))

"""Sort all products by price, lowest first (use sorted with a key lambda)"""
sorted_products = sorted(products, key=lambda product: product["price"])

"""Calculate the total value of all in-stock products (reduce or sum with comprehension)"""
total_stock_value = reduce(lambda acc, product: acc + product["price"], in_stock_products, 0)

"""Group products by category, return a dictionary like {"electronics": [...], "books": [...], ...}"""

from functools import reduce

grouped_products = reduce(lambda acc, product: {**acc, product["category"]: acc.get(product["category"], []) + [product]}, products, {})
   
print(f"In-stock products: {in_stock_products}")
    
print(f"Discounted products: {discounted_products}")
print(f"Electronics under $200: {electronics_under_200}")
print(f"Products sorted by price: {sorted_products}")
print(f"Total value of in-stock products: ${total_stock_value:.2f}")
print(f"Products grouped by category: {grouped_products}")