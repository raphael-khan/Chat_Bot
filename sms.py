from twilio.rest import Client 

account_sid = '' # account sid from twilio
auth_token = '' # auth token from twilio 
client = Client(account_sid, auth_token) 

message = client.messages.create(  
                              messaging_service_sid='MGae2fdb196c2c961a03974f1c759f72ff', 
                              body='Hi, I can believe this works ',      
                              to=''  #  number you want to text. 
                          )
message.sid
print('message you sent successfully ! ')