from twilio.rest import Client 

account_sid = '' # account sid from Twilio.
auth_token = '' # auth token from Twilio.
client = Client(account_sid, auth_token)

message = client.messages.create(  
                              messaging_service_sid='MGae2fdb196c2c961a03974f1c759f72ff', 
                              body='Just look at this and you will know ! ',      
                              to=''  #  number you want to send the message
                              )
message.sid
print('message you sent successfully !!')