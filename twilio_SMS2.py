# importing twilio
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com / console
account_sid = 'ACxxxxxxxxxxxxxxxxxxxxxxxx'
auth_token = '1xxxxxxxxxxxxxxxxxxxxxxxxxx'

client = Client(account_sid, auth_token)

''' Change the value of 'from' with the number
received from Twilio and the value of 'to'
with the number in which you want to send message.'''
message = client.messages.create(
							from_='+1xxxxxxxxxx',
							body ='CUSTOM MESSAGE',
							to ='xxx-xxx-xxxx'
						)

print(message.sid)

