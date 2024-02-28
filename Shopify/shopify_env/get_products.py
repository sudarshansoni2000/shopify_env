from fastapi import FastAPI , HTTPException
import requests

#URL_Template = https://apikey:apitoken@storename/admin/api/api_version/products.json

version='2024-01'
store_Link ='0c34f2-d4.myshopify.com'
API_KEY='9e641ee1a4c8dadf4ff75f09afc395ae'
API_SECRET_KEY='33c1902f92bb8b4fc1c7267f48f30718'
url="https://9e641ee1a4c8dadf4ff75f09afc395ae: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@0c34f2-d4.myshopify.com/admin/api/2024-01/products.json"


app = FastAPI()


@app.get("/products")
async def get_products():
    try:
        #Shopify url
        shopify_api_url=url

        #Headers setup
        headers={
            'Content-type':"application/json"
        }

        # Make a GET request to the shopify api
        response = requests.get(url,headers=headers)
        response.raise_for_status() # raise exception when error came 

        # Extract product data
        products= response.json()["products"]

        return products
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving products: {e}")








