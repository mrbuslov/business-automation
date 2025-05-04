import base64
import os

from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()  # take environment variables


# Fill in your Anthropic API key here
ANTHROPIC_API_KEY = "" or os.getenv("ANTHROPIC_API_KEY")
# Fill in your folder path here
FOLDER_PATH = "" or os.getenv("FOLDER_PATH")

# if folder does not exist, create it
if not os.path.exists(FOLDER_PATH):
    os.mkdir(FOLDER_PATH)
# -------------------
ROLE_DESCRIPTION = """
You are an assistant that heps with filling the information to the html table based on provided receipts images
"""
LATEST_MODEL = 'claude-3-7-sonnet-latest'
ALLOWED_IMAGE_FORMATS = ('jpeg', 'png', 'gif', 'webp')

OUTPUT_STRUCTURE = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Generated schema for Root",
    "type": "object",
    "properties": {
        "html": {
            "type": "string"
        },
        "message_to_user": {
            "type": "string"
        }
    },
    "required": [
        "html",
        "message_to_user"
    ]
}
with open("app/report-struct.html", "r") as f:
    HTML_TEMPLATE = f.read()

images_contents = {}
for filename in os.listdir(FOLDER_PATH):
    if not filename.endswith(ALLOWED_IMAGE_FORMATS):
        raise Exception(f"{filename} has not an allowed image format. Allowed formats: {ALLOWED_IMAGE_FORMATS}")
    if not os.path.isfile(os.path.join(FOLDER_PATH, filename)):
        print(f"{filename} is not a file")
        continue

    images_contents[filename] = {
        "type": "base64",
        "media_type": f"image/{filename.split('.')[-1]}",
        "data": base64.b64encode(
            open(os.path.join(FOLDER_PATH, filename), "rb").read()
        ).decode("utf-8")
    }

INITIAL_CHAT_HISTORY = [
    SystemMessage(content=ROLE_DESCRIPTION),
    SystemMessage(content="Here's html template you must follow \n" + HTML_TEMPLATE),
    HumanMessage(content=[
        {
            "type": "image",
            "source": value
        }
        for key, value in images_contents.items()
    ])
]
