from dotenv import load_dotenv
import os
load_dotenv()
cloud_key = os.getenv('CLOUD_KEY')
cloud_bucket = os.getenv('BUCKET')
urlTemplate = os.getenv('CLOUD_URL_TEMPLATE')

from google.cloud import storage
storage_client = storage.Client.from_service_account_json(cloud_key)
bucket = storage_client.bucket(cloud_bucket)

from PIL import Image
import PIL

from selenium import webdriver

from flask import Flask
from flask import request


import asyncio
import random
import string

app = Flask(__name__)

driver = webdriver.Chrome(executable_path="chromedriver-2")

@app.route('/screenshot')
async def screenshot():
    if request.args.get("url") == None:
        return 500, "No URL specified."
    if request.args.get("delay") == None:
        delay = 1
    else:
        delay = int(request.args.get("delay"))
    driver.get(request.args.get("url"))
    await asyncio.sleep(delay)
    idParts = string.ascii_lowercase + string.ascii_uppercase + string.digits
    idParts = str(idParts)
    while True:
        fileName = ''.join(random.choice(idParts))
        if bucket.get_blob(fileName) == None and os.path(fileName) == False:
            break
    fileName = fileName = ".png"
    driver.get_screenshot_as_file(fileName)
    thePhoto = Image.open(fileName)
    os.remove(fileName)
    thePhoto.save(fileName,optimize=True,quality=85)
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)
    os.remove(fileName)
    link = urlTemplate.replace("{filename}",fileName)
    toReturn = {"cloudURL":link}
    return toReturn

if __name__ == "__main__":
    app.run()