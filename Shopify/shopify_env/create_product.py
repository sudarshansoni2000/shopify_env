from fastapi import FastAPI , HTTPException
import requests

version='2024-01'
store_Link ='0c34f2-d4.myshopify.com'
API_KEY='9e641ee1a4c8dadf4ff75f09afc395ae'
API_SECRET_KEY='33c1902f92bb8b4fc1c7267f48f30718'
url="https://9e641ee1a4c8dadf4ff75f09afc395ae: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@0c34f2-d4.myshopify.com/admin/api/2024-01/products.json"


app = FastAPI()

@app.post("/products")
async def create_products():
    try:
    #HEADERS
        headers= {
            "Content-Type":"application/json",
        }

        # Product data

        product_data = {
            "product":{
                "title":"Test Product",
                "body_html": "<p> Test Product Description",
                "vendor":"Vendor Name",
                "product_type":"Type",
                "varients":[
                    {
                        
                        "price":"9000.00",
                        "sku":"NEW-SKU-99000",
                        "invetory_quantity":10,
                        "inventory_management":"shopify"
                    }
                ],

            }
        }
        
        # Make a POST request to create product
        response=requests.post(url,json=product_data ,headers=headers)
        response.raise_for_status()

        # Extract created product
        created_product = response.json()["product"]

        return created_product
    
    except Exception as e:
        raise HTTPException(status_code=500 , detail=f"Error creating product: {e}")



