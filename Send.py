def truefalse(text):
    tf = False
    if text.lower() == "t":
        tf = True
    return tf


def send_email(gmail_user, gmail_pwd, from_, to, subject, text):
            import smtplib

            # Prepare actual message
            message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
            """ % (from_, "".join(to), subject, text)
            try:
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.ehlo()
                server.starttls()
                server.login(gmail_user, gmail_pwd)
                server.sendmail(from_, to, message)
                server.close()
                return True
            except smtplib.SMTPException as e:
                print e.args, e.message
                return False

def send_msg(IP, message):
    import socket
    host = IP
    port = 13000
    addr = (host, port)
    UDPSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = message
    UDPSock.sendto(data, addr)

def chess_email(game, from_, to_, msg):
    send_email('vigilchess@gmail.com', '(he55vg1',
               'vigilchess@gmail.com', 'vigilchess@gmail.com',
               (game + '.' + '.'.join(to_) + '-' + game + '.' + '.'.join(from_) + '-' + msg), '')
