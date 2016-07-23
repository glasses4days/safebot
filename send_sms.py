from twilio.rest import TwilioRestClient
import os

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
sender = os.environ["SENDER"]
recipient = os.environ["RECIPIENT"]
client = TwilioRestClient(account_sid, auth_token)
message = client.sms.messages.create(to=recipient, from_=sender, body="I'm feeling unsafe")

print(message.sid)
