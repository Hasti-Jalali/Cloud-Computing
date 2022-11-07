import requests
# Data start:
API_KEY = 'acc_f596c8c6fe207a0'
API_SECRET = 'b117d89284326d807458a878ceaa29e7'
IMAGE_URL = 'https://wallpapercave.com/wp/wp3503654.jpg'

# End

class ImageTagging():
    def __init__(self, API_KEY, API_SECRET):
        self.API_KEY = API_KEY
        self.API_SECRET = API_SECRET

    def get_tags(self, image_url):
        response = requests.get(
            'https://api.imagga.com/v2/tags?image_url=%s' % image_url,
                auth=(self.API_KEY, self.API_SECRET))
        tags = response.json()['result']['tags']
        for tag in tags:
            confidence = tag['confidence']
            tag_name = tag['tag']['en']
            print(f'Confidence: {confidence}, tag: {tag_name}')
            return tag_name, confidence


# test
tag_name, confidence = ImageTagging(API_KEY, API_SECRET).get_tags(IMAGE_URL)
