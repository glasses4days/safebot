from twilio.rest import TwilioRestClient
import os


def send_unsafe_text():

    # get users friend info and send the text that user is feeling unsafe
    # along with their geolocation 
    account_sid = os.environ["TWILIO_ACCOUNT_SID"]
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    sender = os.environ["SENDER"]
    friends = Friend.query.filter_by(user_id=user_id).all()
    contact_numbers = friends.contact_numbers
  

    for num in contact_numbers:
        recipient = num
        client = TwilioRestClient(account_sid, auth_token)
        message = client.sms.messages.create(to=recipient, from_=sender, body="I'm feeling unsafe")
        print(message.sid)
