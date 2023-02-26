from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from database import get_credentials, post_data_image, get_data_image
from azure_api import read_image
from preprocessing import preprocess_data
from json import loads

# getting the credentials
credentials = get_credentials()

app = FastAPI()

# CORS middleware to allow requests from a specific origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/read-image")
async def read_image_api(request: Request):
    try:
        # parsing the request body
        user_data = loads((await request.body()).decode('utf-8'))
        image = user_data['image']
        output_list, image_url = read_image(image, credentials)

        # storing the data into the database
        post_data_image(output_list, image_url)

        return {"success": 200}

    except KeyError as e:
        return {"error": f"KeyError in read_image_api: {str(e)}"}

    except Exception as e:
        return {"error": f"Exception in read_image_api: {str(e)}"}

@app.get("/data-image")
async def data_image():
    try:
        # getting the last stored data from the database
        data, url = get_data_image()
        output_data = preprocess_data(data, credentials, url)
        return output_data

    except Exception as e:
        return {"error": f"Exception in data_image: {str(e)}"}