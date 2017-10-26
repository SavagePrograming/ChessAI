__author__ = 'william'
import Functions
import func
import Board
import Recieve
import Move
import Send
import Player


class Assigner():
    def __init__(self):
        self.testl = []
        self.yking = 0
        self.game = ''
        self.player
        self.processors = []
        self.finished_moves = []
        self.new_moves = []
        self.working_moves = []
        self.board = Board.Board('pictures/chess2.jpg', [0, 0], 'b1')
        self.working = False
        self.endgame = False
        self.win = ''
        self.color = ''
        self.king = 0
        self.best_move = Move.Move([0, 0], [0, 0], self.board, 'w')
        self.level = 0

    def start(self):
        print 'Name of Game:'
        self.game = raw_input()
        true = True
        while true:
            #try:
            self.mainloop()
            #except Player.BreakError as e:

            #   print e.value
            #  true = False
            #except KeyboardInterrupt:
            #   break

    def mainloop(self):
        messages = self.receive()
        print messages
        print self.processors
        for message in messages:
            message = message.split('-')
            if message[0] == 'Calc':
                self.working = True
                self.board.FromString(message[1])
                self.board.check()
                self.color = message[2]
                self.level = int(message[3])
                self.new_moves = Functions.generate_moves(self.board, self.color)
                for move in self.new_moves:
                    print move
                self.send_processors()
            elif message[0] == 'Reg':
                print ''
                contained = False
                if message[1] == 'pr':
                    for i in self.processors:
                        if i[0] == message[2]:
                            contained = True
                    if not contained:
                        self.processors.append([message[2], True])
                elif message[1] == "pl":
                    self.player = message[2]

            elif message[0] == 'Done':
                for processor in self.processors:
                    if message[1] == processor[0]:
                        processor[1] = True
                move_ = Move.Move([], [], '', '', message[2])
                for move in self.working_moves:
                    if move.tarsq.name == move_.tarsq.name and move.locsq.name == move_.locsq.name:
                        self.working_moves.remove(move)
                        break
                message[3] = message[3].replace('?', '-')
                print '>', message[3], '<'
                stats = message[3].split('^')
                print stats
                move_.av = float(func.strip(func.strip(stats[0], '\n'), ' '))
                move_.max = float(func.strip(func.strip(stats[1], '\n'), ' '))
                move_.min = float(func.strip(func.strip(stats[2], '\n'), ' '))
                self.finished_moves.append(move_)

        if not self.working_moves and not self.new_moves and self.working:
            self.working = False
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Detects a stalemate
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            if not self.finished_moves:
                self.win = 'stalemate'
                self.send_exit()
                raise Player.BreakError
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #clears king
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            self.king = 0
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #detects if its king is still alive
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            for i in self.board.array_square_Squares:
                if i.color == self.color:
                    if i.rule_num == 6:
                        self.king = i
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #if it is not then it knows you won
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            if self.king == 0:
                self.win = 'You Win'
                self.send_exit()
                raise Player.BreakError
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Clears "your king"
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            self.yking = 0
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Detects if your king is still alive
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            for i in self.board.array_square_Squares:
                if not i.color == self.color:
                    if i.rule_num == 6:
                        self.yking = i
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #if it is not then it knows it won
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            if self.yking == 0:
                self.win = 'I Win'
                self.send_exit()
                raise Player.BreakError
                #print 'm',func.length(moves)

            ##        for move in moves:
            ##            #print move.min_
            ##            pass
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Creates List of moves to delet because king is in check
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            self.testl = []
            for move in self.finished_moves:
                #print 'move',move.score
                if move.min_ == -1000:
                    self.testl.append(self.finished_moves.index(move))
            self.testl.sort()
            self.testl.reverse()
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #removes those moves
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            for z in self.testl:
                self.finished_moves.__delitem__(z)
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #If There are no moves left it calls it Check mate
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            if not self.finished_moves:
                self.win = 'Check mate, You win'
                self.send_exit()
                raise Player.BreakError
                #for move in moves:
                #print move.av_
            #    pass
            #print 'm',func.length(moves)
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Calculating best move
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Caluclating ranks of average
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            s_av = []
            for move in self.finished_moves:
                t = False
                for move_s in s_av:
                    if move_s.av < move.av:
                        s_av.insert(s_av.index(move_s), move)
                        t = True
                        break
                if not t:
                    s_av.append(move)
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #setting those ranks
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            for move in s_av:
                if move.av == s_av[(s_av.index(move) - 1)].av:
                    move.s_avg = s_av[(s_av.index(move) - 1)].s_avg
                else:
                    move.s_avg = s_av.index(move)
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Calulating  ranks of minimum
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            s_min = []
            for move in self.finished_moves:
                t = False
                for move_s in s_min:
                    if move_s.min < move.min:
                        s_min.insert(s_min.index(move_s), move)
                        t = True
                        break
                if not t:
                    s_min.append(move)
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Setting ranks of minimum
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            for move in s_min:
                if move.min == s_min[(s_min.index(move) - 1)].min:
                    move.s_min = s_min[(s_min.index(move) - 1)].s_min
                else:
                    move.s_min = s_min.index(move)
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Calulating ranks Of Maximum
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            s_max = []
            for move in self.finished_moves:
                t = False
                for move_s in s_max:
                    if move_s.max > move.max:
                        continue
                    s_max.insert(s_max.index(move_s), move)
                    t = True
                    break
                if not t:
                    s_max.append(move)
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Setting ranks of maximum
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            for move in s_max:
                if move.max == s_max[(s_max.index(move) - 1)].max:
                    move.s_max = s_max[(s_max.index(move) - 1)].s_max
                else:
                    move.s_max = s_max.index(move)
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Calulating total rank
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            for move in self.finished_moves:
                move.s_total = move.s_avg + (move.s_min * 2) + move.s_max
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Calulating best move
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            best1 = self.finished_moves[0]
            for move in self.finished_moves:
                if move.s_total < best1.s_total:
                    best1 = move
                    #print best1
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Prints info about all moves
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            for move in self.finished_moves:
                move.PrintStats()
                print move.s_avg, move.s_min, move.s_max, move.s_total
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Prints info about the best move
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            print "Best"
            ##        print "Max:" + str(best1.max) ,"Min:" + str(best1.min) ,"Avg:" + str(best1.max) ,
            best1.PrintStats()
            print "Average Score:", best1.s_avg, "Minimum Score:", best1.s_min, "Maximum Score:",\
                best1.s_max, 'Total Score:', best1.s_total
            self.best_move = best1
            self.send_move()
        elif self.working:
            self.send_processors()

    def receive(self):
        msgs = Recieve.receive(self.game, 'Assigner', 'assigner')
        return msgs

    def send_processors(self):
        for move in self.new_moves:
            for processor in self.processors:
                if processor[1]:
                    Send.send_msg(processor[0], 'Measure-' + move.toString(self.board) + '-' +
                                      self.board.ToString() + '-' + str(self.level))
                    processor[1] = False
                    self.new_moves.remove(move)
                    self.working_moves.append(move)
                    break

    def send_exit(self):
        for processor in self.processors:
            Send.send_msg(processor[0], 'Exit-' + self.win)
        Send.send_msg(self.player, ('Exit-' + self.win))

    def send_move(self):
        Send.send_msg(self.game, ['Assigner', 'assigner'],
                         ['Player', 'player'],
                         ('Done-' + self.best_move.toString(self.board)))