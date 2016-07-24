from twilio.rest import TwilioRestClient
import os
from sqlalchemy import func


def send_unsafe_text(user_id):

    # get users friend info and send the text that user is feeling unsafe
    # along with their geolocation 
    account_sid = os.environ["TWILIO_ACCOUNT_SID"]
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    sender = os.environ["SENDER"]
    friends = Friend.query.filter_by(user_id=user_id).all()
    contact_numbers = friends.contact_numbers
    unsafe_instances = Unsafe.query.filter_by(user_id=user_id).all()
    max_unsafe_instance = db.session.query(func.max(Unsafe.unsafe_id)).one()
    location = max_unsafe_instance.geolocation

    for num in contact_numbers:
        recipient = num
        client = TwilioRestClient(account_sid, auth_token)
        message = client.sms.messages.create(to=recipient, from_=sender, body="I'm feeling unsafe. I am at" + location)
        print(message.sid)
