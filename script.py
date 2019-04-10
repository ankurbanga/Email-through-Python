import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender= "bangaankur803@gmail.com" 
receiver = "kushgpt99@gmail.com"
password = input("Type your password and press enter: ")
message = """\
Subject: Subject CHM101A
Bura na maano Holi hai 
'Fraud na maaro' PClub ki boli hai

~~~~python here don't mind hissss~~~~
"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, message)

