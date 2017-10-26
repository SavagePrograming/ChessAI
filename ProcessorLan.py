__author__ = 'william'

import Board
import Recieve
import Move
import Send
import Player
import func
import multiprocessing
import Square
import os
import Functions


class Processor():
    def __init__(self):
        self.used = []
        self.ip = ''
        self.name = ''
        self.assigner = ''
        self.board = Board.Board('pictures/chess2.jpg', [0, 0], 'b1')
        for i in xrange(0, 8):
            for ii in xrange(0, 8):
                self.board.multiarray_square_Board[i][ii] = Square.Square(0, [i, ii], str(i) + str(ii))
        self.level = 0
        self.move = Move.Move([0, 0], [0, 0], self.board, 'b')


    def start(self):
        print 'What is your IP:'
        self.ip = raw_input()
        print 'Name:'
        self.name = raw_input()
        print 'What is the Assigner IP:'
        self.assigner = raw_input()
        Functions.RunFile("Reciever.py")
        true = True
        self.send_register()
        while true:
            # try:
            self.mainloop()
            #except Player.BreakError:
            #    print '2'
            #    true = False
            #except KeyboardInterrupt:
            #    print '1'
            #    true = False
            #except Exception as e:
            #    print e.args
        print 'close'

    def mainloop(self):
        messages = self.receive()
        for message in messages:
            message = message.split('-')
            if message[0] == 'Measure':
                self.move = Move.Move('', '', '', '', func.strip(func.strip(message[1], '\n'), ' '))
                self.board.FromString(func.strip(func.strip(message[2], '\n'), ' '))
                #print self.board.PrintString(
##                for sq in self.board.sq:
##                    print sq.name
                self.level = int(message[3])
                self.move.remote_check( self.board, self.level, self.move.color, [0, 0], self.level)
##                print func.strip(str(self.move.av) + '^' + str(self.move.max) + '^' + str(self.move.min), '\n')
                self.send_move()
            if message[0] == 'Exit':
                raise Player.BreakError(message[1])

    def receive(self):
        msgs, test= Recieve.receive('PR', self.used)
        if test:
            self.used.extend(msgs)
        else:
            self.used = msgs
        return msgs

    def send_move(self):
        Send.send_msg(self.assigner, ('A-Done' + '-' + self.ip + '-' +self.move.toString(self.board) + '-' +
                                      func.strip((str(self.move.av) + '^' +
                                                  str(self.move.max) + '^' +
                                                  str(self.move.min)).replace('-', '?'), '\n')))

    def send_register(self):
        Send.send_msg(self.assigner, 'A-Reg-pr-' + self.ip)
