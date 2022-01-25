from twilio.rest import Client

account_sid = "***************"
auth_token = "****************"

client = Client(account_sid, auth_token)

message = client.messages.create(
    body = "This is sent from python",
    from_ = "+16067310828",
    to = "+923407538427"
)

print(message.sid)