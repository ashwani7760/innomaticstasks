from fastapi import FastAPI,Query

app = FastAPI()

products = [
    {"id": 1, "name": "Wireless Mouse", "price": 599, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Notebook", "price": 99, "category": "Stationery", "in_stock": True},
    {"id": 3, "name": "Pen Set", "price": 49, "category": "Stationery", "in_stock": True},
    {"id": 4, "name": "USB Cable", "price": 199, "category": "Electronics", "in_stock": False},
    {"id": 5, "name": "Laptop Stand", "price": 1299, "category": "Electronics", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 2499, "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 1899, "category": "Electronics", "in_stock": False}
]

@app.get("/")
def home():
    return {"message": "Welcome to our app"}

@app.get("/products")
def get_products():
    return {"products":products,"count":len(products)}

@app.get("/products/category/{category_name}")
def get_product_by_category(category_name):
    result = [p for p in products if category_name == p["category"]]
    if len(result)==0:
        result = "product not found"
    return result

@app.get("/products/instock")
def get_instock():
    result = [p for p in products if True == p["in_stock"]]
    return {"product": result, "count":len(result)}

@app.get("/store/summary")
def summary():
    total_product = len(products)
    in_stock = len([p for p in products if True == p["in_stock"]])
    out_of_stock = total_product - in_stock
    category = set([p["category"] for p in products ])
    return  { "store_name": "My E-commerce Store",
             "total_products": total_product,
             "in_stock": in_stock,
            "out_of_stock": out_of_stock,
            "categories": list(category) }

@app.get("/products/search/{keyword}")
def get_search(keyword):
    result = [p for p in products if keyword.lower() in p["name"].lower()] 
    if len(result)==0 : 
        return {"message": "No products matched your search"}
    else:
        return {"keyword": keyword, "results": result, "total_matches": len(result)}
    
@app.get("/products/deals")
def deals():
    cheapest = min(products, key=lambda p: p["price"]) 
    expensive = max(products, key=lambda p: p["price"]) 
    return { "best_deal": cheapest, "premium_pick": expensive, }