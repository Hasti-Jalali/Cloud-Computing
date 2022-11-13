import requests


class SendEmail():
    def __init__(self):
        self.DOMAIN = "sandboxea9c004cefa840e19efa1b740a8263d0.mailgun.org"
        self.API_KEY = "e8f00bed28567c185c4a79f1c54f0d99-48c092ba-2aa2328c"

    def send_message(self, email, subject, text):
        return requests.post(
            f"https://api.mailgun.net/v3/{self.DOMAIN}/messages",
            auth=("api", self.API_KEY),
            data={"from": f"<mailgun@{self.DOMAIN}>",
                  "to": [email],
                  "subject": subject,
                  "text": text})


# EMAIL_ADDRESS = "hastii.jalali@gmail.com"
# TEXT = "testtttttt"
# SUBJECT = "Cloud Computing HW1"

# email_response = SendEmail().send_message(EMAIL_ADDRESS, SUBJECT, TEXT)

# print(email_response)


# print(image.tagging_obj())
