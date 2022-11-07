import requests

# Data start:
DOMAIN = "sandboxea9c004cefa840e19efa1b740a8263d0.mailgun.org"
API_KEY = "e8f00bed28567c185c4a79f1c54f0d99-48c092ba-2aa2328c"



# End

class Email():
    def send_email(email_address, text, subject):
        return requests.post(
            f"https://api.mailgun.net/v3/{DOMAIN}/messages",
            auth=("api", API_KEY),
            data={"from": f"{DOMAIN}>",
                "to": [email_address],
                "subject": subject,
                "text": text})


# test
EMAIL_ADDRESS = "hastii.jalali@gmail.com"
TEXT = "Your ad has been accepted!"
SUBJECT = "Cloud Computing HW1"
response = Email().send_simple_message(EMAIL_ADDRESS, SUBJECT, TEXT)
print(response.json())