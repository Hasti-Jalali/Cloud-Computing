import requests

class ImageTagging():
    def __init__(self):
        self.API_KEY = 'acc_f596c8c6fe207a0'
        self.API_SECRET = 'b117d89284326d807458a878ceaa29e7'

    def get_tags(self, image_path):
        response = requests.post(
            'https://api.imagga.com/v2/tags',
            auth=(self.API_KEY, self.API_SECRET),
            files={'image': open(image_path, 'rb')})
        # print(response.json())
        check_vehicle = False
        for i in response.json()['result']['tags']:
            if i['tag']['en'] == 'vehicle':
                check_vehicle = True
                break
        tags = response.json()['result']['tags']
        for tag in tags:
            confidence = tag['confidence']
            tag_name = tag['tag']['en']
            print(f'Confidence: {confidence}, tag: {tag_name}, is_vehicle: {check_vehicle}')
            return tag_name, check_vehicle


# test
# tag_name, confidence, _ = ImageTagging().get_tags('./Image Cache/1.jpg')
