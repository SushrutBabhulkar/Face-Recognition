import smtplib
import imghdr
from email.message import EmailMessage
host = 'smtp.gmail.com'
port = 465

username = 'user@mail.com'
password = '*******'

sender = username
receiver = 'receiverid@mail.com'

server = smtplib.SMTP_SSL(host, port)

server.login(username, password)

def recognize():
    
    message = EmailMessage()
    message['subject'] = 'Welcome Message'
    message['from'] = sender
    message['to'] = receiver
    message.set_content(
    """ 
    Greetings, Welcome Back Sushrut !!
   
    Creating Workspace for you.
    
    Regards Workspace Intelligence.
    """)
    server.sendmail(sender, receiver, message.as_string())
    print("Welcome Email Send Successfully")

def unrecognize():

    message = EmailMessage()
    message['subject'] = '❗❗ Workspace Alert ❗❗'
    message['from'] = sender
    message['to'] = receiver
    message.set_content(
    '''
    Greetings,Someone has Checked into system.
    
    Hence,terminating workspace.
    
    Please find attached image of unrecognized person.
     
    Regards Workspace Intelligence
    ''')
    
    with open('unknown-person.jpg', 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = f.name
    message.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
    
    server.sendmail(sender, receiver, message.as_string())
    print("Alert Email Send Successfully")
    
