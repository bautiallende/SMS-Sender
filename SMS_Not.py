from twilio.rest import Client

account_sid = '#####'
auth_token = '######'
client = Client(account_sid, auth_token)

message = client.messages.create(from_ ='Phone Number',
                                 body = 'Body of Message!',
                                 to = "Phone Number")
print(message.sid)