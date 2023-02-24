from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from api.database import get_credentials, post_data_image, get_data_image
from model.azure_api import read_image
from model.preprocessing import preprocess_data
from json import loads

# getting the credentials
credentials = get_credentials()

app = FastAPI()

# CORS middleware to allow requests from a specific origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/read-image")
async def read_image_api(request: Request):
    # parsing the request body
    user_data = loads((await request.body()).decode('utf-8'))

    image = user_data['image']
    with_price = user_data['withPrice']
    condition = user_data['condition']

    output_list, image_url = read_image(image, credentials)

    # storing the data into the database
    post_data_image(output_list, image_url, with_price, condition)

    return {"success": 200}

@app.get("/data-image")
async def read_image_api():
    # getting the last stored data from the database
    data, url, with_price, condition = get_data_image()
    output_data = preprocess_data(data, credentials, url, with_price, condition)
    return output_data