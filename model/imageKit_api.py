from imagekitio import ImageKit
from base64 import b64encode

def upload_file_imageKit(image, credentials: list):
    imageKit_public_key = credentials[0]
    imageKit_private_key =  credentials[1]
    imageKit_url_endpoint = credentials[2]

    imagekit = ImageKit(
                public_key = imageKit_public_key,
                private_key = imageKit_private_key,
                url_endpoint = imageKit_url_endpoint
            )

    result = imagekit.upload_file(file=image, file_name=f'{image[:10]}.jpg')

    return result.response_metadata.raw