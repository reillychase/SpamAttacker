from twilio.rest import Client
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

number = client.lookups.v2.phone_numbers(args.number).fetch(fields='line_type_intelligence')

print(number.line_type_intelligence["carrier_name"])
