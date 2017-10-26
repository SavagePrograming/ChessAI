# module for receiving emails
from Send import *
from email import parser
from socket import *
import poplib


def log(text):
    print str(text)
    file_ = open("Log.txt", "a")
    file_.write(str(text) + "\n")
    file_.close()


def log1(text):
    print str(text)
    file_ = open("Log(1).txt", "a")
    file_.write(str(text) + "\n")
    file_.close()


def isint(num):
    works = True
    try:
        int(num)
    except ValueError:
        works = False
    return works


def receivemsg():
    host = ""
    port = 13000
    buf = 2048*2
    addr = (host, port)
    UDPSock = socket(AF_INET, SOCK_DGRAM)
    UDPSock.bind(addr)
    while True:
        (data, addr) = UDPSock.recvfrom(buf)
        if data == "exit":
            break
        else:
            data = data.split("-")
            name = data[0]
##            print data
            data = '-'.join(data[1:(data.__len__())])
##            print data
            messages = open('messages'+name+'.txt', 'a')
            messages.write(data+'\n')
            messages.close()
    UDPSock.close()


def receive(name, msgList):
    try:
        test = False
        messages = open('messages'+name+'.txt', 'r')
        return_messages = messages.readlines()
        for msg in return_messages:
            return_messages[return_messages.index(msg)] = msg.strip('\n')
        messages.close()
        if return_messages[0:msgList.__len__()] == msgList:
            return_messages = return_messages[msgList.__len__():return_messages.__len__()]
            test = True
        #print msgList
        #print return_messages
        return [return_messages, test]
    except IOError:
        messages = open('messages'+name+'.txt', 'w')
        messages.close()
        return []

def receiveemail(game, type_, name):
    true = True
    Kill = False
    fullname = game + '.' + type_ + '.' + name
    return_messages = []
    while true:
        try:
            return_messages = []
            #pygame.time.delay(100)
            pop_conn = poplib.POP3_SSL('pop.gmail.com')
            pop_conn.user('vigilchess@gmail.com')
            pop_conn.pass_('(he55vg1')
            #:
            messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
            # Concat message pieces:
            messages = ["\n".join(mssg[1]) for mssg in messages]
            #Parse message intom an email object:
            messages = [parser.Parser().parsestr(mssg) for mssg in messages]
            for message in messages:
                if message['from'].__contains__("vigilchess@gmail.com"):
                    if message['subject'][0:len(fullname)] == fullname:
                        return_messages.append(message['subject'])
                    else:
                        send_email('vigilchess@gmail.com', 'che55vg1', 'vigilchess@gmail.com',
                                   'vigilchess@gmail.com', message['subject'], '')
            pop_conn.quit()
            true = False
        except BaseException as inst:
            if str(type(inst)).__contains__("KeyboardInterrupt"):
                true = False
                Kill = True
            else:
                print inst.message, inst.args
    if Kill:
        raise KeyboardInterrupt()
    return return_messages
