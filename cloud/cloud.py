#### Cloud layer ####
# Receives subscribed data and sends a text via Twilio api
#######


from concurrent.futures import TimeoutError
from google.cloud import pubsub_v1
from twilio.rest import Client
import time
import json
# TODO(developer)
ap = 0
db = 0
utc = 0
project_id = "cs190-xxxxxx"
subscription_id = ""
# Number of seconds the subscriber should listen for messages
#timeout =
subscriber = pubsub_v1.SubscriberClient()
# The `subscription_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/subscriptions/{subscription_id}`
subscription_path = subscriber.subscription_path(project_id, subscription_id)
account_sid = "xxxxxxxxx"
auth_token = "xxxxxxxxxxxx"
client = Client(account_sid, auth_token)
#time.sleep(10)
def callback(message):
    #print("message: {}".format(message))
    global ap
    global db
    global utc
    if "Aldrich_Park" in str(message.data) and ap==3:
        ap=0
        client.api.account.messages.create(
        to="+11234567890",
        from_="+19998887654",
        body="Too many social distancing violations detected around Aldrich_Park -- please wear masks and stay at least 6 feet away from members outside your household.")
    elif "Aldrich_Park" in str(message.data):
        ap+=1
        print("skipping ap\n")
    #repeat for each location