# importing twilio
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com / console
account_sid = 'ACf97d5531f2622bda01c6d1f85b143c44'
auth_token = '1029aa30315a62c343c472080747321e'

client = Client(account_sid, auth_token)

''' Change the value of 'from' with the number
received from Twilio and the value of 'to'
with the number in which you want to send message.'''
message = client.messages.create(
							from_='+19378844535',
							body ='hey there, good job joi',
							to ='2169542422'
						)

print(message.sid)

