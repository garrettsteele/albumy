from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time

from albumy.creds.azure import get_key, get_end

'''
Authenticate
Authenticates your credentials and creates a client.
'''
subscription_key = get_key() #"74359e63335b4307aa53221f658d4b12"
endpoint = get_end() #"https://picture-vision.cognitiveservices.azure.com/"

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
'''
END - Authenticate
'''

'''
Quickstart variables
These variables are shared by several examples
'''
# Images used for the examples: Describe an image, Categorize an image, Tag an image, 
# Detect faces, Detect adult or racy content, Detect the color scheme, 
# Detect domain-specific content, Detect image types, Detect objects
# images_folder = os.path.join (os.path.dirname(os.path.abspath(__file__)), "images")



'''
END - Quickstart variables
'''


'''
read and image
'''

# result = computervision_client.read_in_stream(
#     open(local_image_url, "rb")
# )

# print(result)



# # '''
# # Tag an Image - remote
# # This example returns a tag (key word) for each thing in the image.
# # '''
# # print("===== Tag an image - remote =====")
# # # Call API with remote image
# #tags_result_remote = computervision_client.tag_image(remote_image_url )
# tags_result_remote2 = computervision_client.tag_image_in_stream(open(local_image_url, "rb") )
# #print(tags_result_remote)

# description=""

# # # Print results with confidence score
# print("Tags in the remote image: ")
# if (len(tags_result_remote2.tags) == 0):
#     print("No tags detected.")
# else:
#     for tag in tags_result_remote2.tags:
#         description = tag.name + " "+ description
#         #print("'{}' with confidence {:.2f}%".format(tag.name, tag.confidence * 100))
# print(description)
# '''
# END - Tag an Image - remote
# '''
# print("End of Computer Vision quickstart.")


def create_img_text():
    return "vision method"

def desc_image(image, local_path):
    #filename = os.path.splitext(filename)
    #img = Image.open(image)
    # print(local_path)
    # remote_tag = computervision_client.tag_image_in_stream(open(local_path, "rb") )

    # description=""
    # print("Tags in the remote image: ")
    # if (len(remote_tag.tags) == 0):
    #     print("No tags detected.")
    # else:
    #     for tag in remote_tag.tags:
    #         description = tag.name + " "+ description
    # print(description)
    # return description
    desc_result_remote = computervision_client.describe_image_in_stream(open(local_path, "rb") )

    description=""
    if (len(desc_result_remote.captions) == 0):
        description="No objects detected"
    else:
        for cap in desc_result_remote.captions:
            description = cap.text + " "+ description
    print(description)
    return description

def detect_image(image, local_path):
    obj_result_remote = computervision_client.detect_objects_in_stream(open(local_path, "rb") )

    description=""
    if (len(obj_result_remote.objects) == 0):
        description="No objects detected"
    else:
        for obj in obj_result_remote.objects:
            description = obj.object_property + " "+ description
    print(description)
    return description