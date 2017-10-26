g__author__ = 'william'

import PlayerLan
import ProcessorLan
import AssignerLan

print 'What mode, Processor, Game, or Assigner(p/a/G)?'
mode = raw_input().lower()
if mode == 'a':
    messages = open('messagesA.txt', 'w')
    messages.close()
    Program = AssignerLan.Assigner()
    Program.start()
elif mode == 'p':
    messages = open('messagesPR.txt', 'w')
    messages.close()
    Program = ProcessorLan.Processor()
    Program.start()
else:
    messages = open('messagesPL.txt', 'w')
    messages.close()
    Program = PlayerLan.Player()
    Program.start()

print 'Done With chess'
