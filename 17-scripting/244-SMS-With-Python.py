# 244 : SMS With Python

# TODO: [Twilio]
# - https://www.twilio.com/docs
# - https://console.twilio.com/us1/develop/onboarding-v2?selectedTab=custom

# > pip install twilio                  #  9.2.4

from twilio.rest import Client

# - Get Twilio phone number: +14159361450
# - Account SID:
# - Auth Token:
account_sid = ""
auth_token = ""

client = Client(account_sid, auth_token)

message = client.messages.create(
    from_="+14159361450",
    body="Hello Pavel Klos, this is SMS Python bot! Have a nice day!",
    to="+420734234585",
)

print(message.sid)
