from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from msrest.authentication import CognitiveServicesCredentials
from time import sleep
from model.imageKit_api import upload_file_imageKit

def read_image(image: str, credentials: list):
    subscription_key = credentials[3]
    endpoint = credentials[4]

    computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

    image = upload_file_imageKit(image, credentials)
    read_image_url = image['url']

    # Call API with URL and raw response (allows you to get the operation location)
    read_response = computervision_client.read(read_image_url,  raw=True)

    # Get the operation location (URL with an ID at the end) from the response
    read_operation_location = read_response.headers["Operation-Location"]

    # Grab the ID from the URL
    operation_id = read_operation_location.split("/")[-1]

    # Call the "GET" API and wait for it to retrieve the results 
    while True:
        read_result = computervision_client.get_read_result(operation_id)
        if read_result.status not in ['notStarted', 'running']:
            break
        sleep(1)

    # Print the detected text, line by line
    if read_result.status == OperationStatusCodes.succeeded:
        for text_result in read_result.analyze_result.read_results:
            output_text = [line.text for line in text_result.lines]
    
    return output_text, read_image_url