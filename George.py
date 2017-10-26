g__author__ = 'william'

import PlayerLan
import ProcessorLan
import AssignerLan

messages = open('messagesPL.txt', 'w')
messages.close()
Program = PlayerLan.Player()
Program.start(2,'b',False,False)

print 'Done With chess'
