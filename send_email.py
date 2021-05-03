
# libraries to be imported
import smtplib, ssl
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(msg):

    try:

        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = ""  # Enter your address
        receiver_email = ""  # Enter receiver address
        password = ""

        message = """\nSubject: Face mask ouputs\n"""+str(msg)

        message=str(message)


        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
    
    except Exception as e:

        print("Exceptoin in send_email",e)

def send_email_with_attachement(filename,file_path,msg_text):

    fromaddr = "--"
    password = "--"
    toaddr = "--"

    print(filename)
    print(file_path)

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = "Face Mask Detection Output"

    # string to store the body of the mail
    body = msg_text+" :: not weared Mask"

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # open the file to be sent
    attachment = open(file_path, "rb")

    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p.set_payload((attachment).read())

    # encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # attach the instance 'p' to instance 'msg'
    msg.attach(p)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, password)

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()


# filename='un_mask'
# file_path='C:/Users/Radha/Desktop/Notes/Jerome/Face-Mask-Detection-master/Face-Mask-Detection-master/Final_output/un_mask.png'
# msg='welcome'


# send_email_with_attachement(filename,file_path,msg)

# send_email("filename : images/pic2.jpg \n:  Objects [0,2] Not weired mask in this image")



