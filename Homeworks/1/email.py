import requests


class SendEmail():
    def __init__(self):
        self.DOMAIN = "sandboxf826f427e71541e8b26ef39e34e74055.mailgun.org"
        self.API_KEY = "76fa836da8d0fa323b075f872a9e36a1-69210cfc-a1dec9c0"

    def send_message(self, email, subject, text):
        '''Send an email using Mailgun's API.'''
        return requests.post(
            f"https://api.mailgun.net/v3/{self.DOMAIN}/messages",
            auth=("api", self.API_KEY),
            data={"from": f"Mailgun Sandbox <postmaster@{self.DOMAIN}>",
                  "to": email,
                  "subject": subject,
                  "text": text})


# EMAIL_ADDRESS = "hastii.jalaliii@gmail.com"
# TEXT = "testtttttt"
# SUBJECT = "Cloud Computing HW1"

# email_response = SendEmail().send_message(EMAIL_ADDRESS, SUBJECT, TEXT)

# print(email_response)


# print(image.tagging_obj())