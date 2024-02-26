from twilio.rest import Client
from urllib.parse import quote
import argparse
import os

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

parser = argparse.ArgumentParser()
parser.add_argument("--number")
args = parser.parse_args()

client = Client()

number_info = client.lookups.v2.phone_numbers(args.number).fetch(fields='line_type_intelligence')
carrier = number_info.line_type_intelligence["carrier_name"]

print("The spammer's carrier is: " + carrier)
if "Twilio" in carrier:
    print("You can report them here: https://www.twilio.com/en-us/help/abuse")

else:
    target = "https://google.com/search?q=" + quote(carrier + " SMS spam abuse report form")
    print("Unable to find the abuse report form but LMGTFY: " + target)
