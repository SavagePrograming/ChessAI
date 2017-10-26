__author__ = 'william'

import Board
import Recieve
import Move
import Send
import Player
import func


class Processor():
    def __init__(self):
        self.game = ''
        self.name = ''
        self.board = Board.Board('pictures/chess2.jpg', [0, 0], 'b1')
        self.level = 0
        self.move = Move.Move([0, 0], [0, 0], self.board, 'b')

    def start(self):
        print 'Game:'
        self.game = raw_input()
        print 'Name:'
        self.name = raw_input()
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
            if message[2] == 'Measure':
                self.move = Move.Move('', '', '', '', func.strip(func.strip(message[3], '\n'), ' '))
                self.board.FromString(func.strip(func.strip(message[4], '\n'), ' '))
                for sq in self.board.array_square_Squares:
                    print sq.name
                self.level = int(message[5])
                self.move.remote_check(self.board, self.level, self.move.color, [0, 0], self.level)
                print func.strip(str(self.move.av) + '^' + str(self.move.max) + '^' + str(self.move.min), '\n')
                self.send_move()
            if message[2] == 'Exit':
                raise Player.BreakError(message[3])

    def receive(self):
        msgs = Recieve.receive(self.game, 'Processor', self.name)
        msg1 = []
        for msg in msgs:
            msg1.append(func.strip(msg, '\n'))
        return msg1

    def send_move(self):
        Send.chess_email(self.game, ['Processor', self.name], ['Assigner', 'assigner'], ('Done' +
                         '-' + self.move.toString(self.board) + '-' +
                         func.strip((str(self.move.av) + '^' +
                                    str(self.move.max) + '^' + str(self.move.min)).replace('-', '?'), '\n')))

    def send_register(self):
        Send.chess_email(self.game, ['Processor', self.name], ['Assigner', 'assigner'], 'Reg')
