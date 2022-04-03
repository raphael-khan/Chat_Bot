from twilio.rest import Client 

account_sid = 'ACf8c1f39d0febe3e02c6f384afae51a10' # account sid from twilio
auth_token = '164f5edc118443f46df57c17fac9a7b5' # auth token from twilio 
client = Client(account_sid, auth_token)

message = client.messages.create(  
                              messaging_service_sid='MGae2fdb196c2c961a03974f1c759f72ff', 
                              body='Just look at this and you will know ! '  
                              'https://media.giphy.com/media/126OMdMaXFWLL2/giphy.gif',      
                              to=''  #  number you want to text / sms......
                          )
message.sid
print('message you sent successfully !!')