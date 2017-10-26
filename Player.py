__author__ = 'william'

import pygame
import Functions
import Square
import Board
import Recieve
import Move
import Send


class BreakError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class Player():
    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #sets up starting variables
    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def __init__(self):
        self.msg = []
        self.game = ''
        self.emailprocess = True
        self.done = ''
        self.TEST = True
        self.name2 = ''
        self.name1 = ''
        self.y = 0
        self.x = 'a'
        self.s_max = []
        self.s_min = []
        self.t = True
        self.s_av = []
        self.testl = []
        self.yking = 0
        self.intNumber = 0
        self.intLevel = 0
        self.strColorAI = ''
        self.bolSafeMode = False
        self.bolFast = False
        self.Screen = 0
        self.MainBoard = Board.Board('pictures/chess2.jpg', [0, 0], 'b1')
        self.lstLocation = []
        self.true = False
        self.selected = False
        self.turn = 'w'
        self.win = 'yes'
        self.moves = []
        self.king = 0
        self.best1 = 0
        self.FileLoc = ''
        self.File = ''
        self.SquareString = ''
        self.loc = ''
        self.Type = ''
        self.color = ''
        self.intNumber2 = 0
        self.From = ''
        self.To = ''
        self.mousex, self.mousey = [0, 0]
        self.number = 0

    def start(self):
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Getting Game stats
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        print 'Name of Game:'
        self.game = raw_input()
        print 'What level?'
        self.intLevel = 1 + int(raw_input())
        print 'What color is ai?'
        self.strColorAI = raw_input()
        print 'Safe Mode: T/F'
        self.bolSafeMode = ("t" == raw_input().lower())
        print 'Email Process: T/F'
        self.emailprocess = ("t" == raw_input().lower())

        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Initalizing Pygame for visuals
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        pygame.init()
        self.Screen = pygame.display.set_mode([450, 450])
        self.Screen.fill([255, 255, 255])
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Making Squares
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        for chrLetter in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'):
            for intNumber1 in range(1, 9):
                self.lstLocation = [self.intNumber * 50, (intNumber1 - 1) * 50]
                self.MainBoard.array_square_Squares.append(Square.Square(0, self.lstLocation, chrLetter + str(intNumber1)))
            self.intNumber += 1
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Setting squares up for starting positions
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        for square in self.MainBoard.array_square_Squares:
            if square.name == 'a5':
                square.image = pygame.image.load('pictures/king.png')
                square.image_loc = 'pictures/king.png'
                square.color = 'w'
                square.rule_num = 6
            if square.name == 'a4':
                square.image = pygame.image.load('pictures/queen.png')
                square.image_loc = 'pictures/queen.png'
                square.color = 'w'
                square.rule_num = 5
            if square.name == 'a3' or square.name == 'a6':
                square.image = pygame.image.load('pictures/bishup.png')
                square.image_loc = 'pictures/bishup.png'
                square.color = 'w'
                square.rule_num = 4
            if square.name == 'a7' or square.name == 'a2':
                square.image = pygame.image.load('pictures/knight.png')
                square.image_loc = 'pictures/knight.png'
                square.color = 'w'
                square.rule_num = 3
            if square.name == 'a1' or square.name == 'a8':
                square.image = pygame.image.load('pictures/rook.png')
                square.image_loc = 'pictures/rook.png'
                square.color = 'w'
                square.rule_num = 2
            if square.name.__contains__('b'):
                square.image = pygame.image.load('pictures/pawn.png')
                square.image_loc = 'pictures/pawn.png'
                square.color = 'w'
                square.rule_num = 1
            if square.name == 'h5':
                square.image = pygame.image.load('pictures/bking.png')
                square.image_loc = 'pictures/bking.png'
                square.color = 'b'
                square.rule_num = 6
            if square.name == 'h4':
                square.image = pygame.image.load('pictures/bqueen.png')
                square.image_loc = 'pictures/bqueen.png'
                square.color = 'b'
                square.rule_num = 5
            if square.name == 'h3' or square.name == 'h6':
                square.image = pygame.image.load('pictures/bbishup.png')
                square.image_loc = 'pictures/bbishup.png'
                square.color = 'b'
                square.rule_num = 4
            if square.name == 'h7' or square.name == 'h2':
                square.image = pygame.image.load('pictures/bknight.png')
                square.image_loc = 'pictures/bknight.png'
                square.color = 'b'
                square.rule_num = 3
            if square.name == 'h1' or square.name == 'h8':
                square.image = pygame.image.load('pictures/brook.png')
                square.image_loc = 'pictures/brook.png'
                square.color = 'b'
                square.rule_num = 2
            if square.name.__contains__('g'):
                square.image = pygame.image.load('pictures/bpawn.png')
                square.image_loc = 'pictures/bpawn.png'
                square.color = 'b'
                square.rule_num = 1
        while not self.true:
            try:
                if self.emailprocess:
                    self.emailloop()
                else:
                    self.mainloop()
                self.eventhandler()
            except BreakError:
                break
            except KeyboardInterrupt:
                break

        print self.win
        print 'Done?'
        self.done = raw_input()
        while self.done == 'done':
            self.done = raw_input()
        pygame.quit()

    def mainloop(self):
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Prints the board
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.MainBoard.show(self.Screen)
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Sorts squares
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.MainBoard.check()
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Runs the Ai if it is it's turn
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if self.turn == self.strColorAI:
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #gets moves, (longest part)
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            self.moves = Functions.check(self.MainBoard, self.MainBoard, self.strColorAI, self.intLevel,
                                         self.strColorAI, [0, 0], self.bolFast, self.intLevel, self.Screen,
                                         self.bolFast)
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Detects a stalemate
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            if not self.moves:
                self.true = True
                self.win = 'stalemate'
                raise BreakError('Stalemate')
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #clears king
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            self.king = 0
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #detects if its king is still alive
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            for i in self.MainBoard.array_square_Squares:
                if i.color == self.strColorAI:
                    if i.rule_num == 6:
                        self.king = i
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #if it is not then it knows you won
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            if self.king == 0:
                self.true = True
                self.win = 'you win'
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Clears "your king"
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            self.yking = 0
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Detects if your king is still alive
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            for i in self.MainBoard.array_square_Squares:
                if not i.color == self.strColorAI:
                    if i.rule_num == 6:
                        self.yking = i
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #if it is not then it knows it won
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            if self.yking == 0:
                self.true = True
                self.win = 'I win'
                #print 'm',func.length(moves)

            ##        for move in moves:
            ##            #print move.min_
            ##            pass
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Creates List of moves to delet because king is in check
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            self.testl = []
            for move in self.moves:
                #print 'move',move.score
                if move.min_ == -1000:
                    self.testl.append(self.moves.index(move))
            self.testl.sort()
            self.testl.reverse()
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #removes those moves
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            for z in self.testl:
                self.moves.__delitem__(z)
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #If There are no moves left it calls it Check mate
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            if not self.moves:
                self.true = True
                self.win = 'Check mate\nYou win'
                raise BreakError(self.win)
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
            self.s_av = []
            for move in self.moves:
                self.t = False
                for move_s in self.s_av:
                    if move_s.av < move.av:
                        self.s_av.insert(self.s_av.index(move_s), move)
                        self.t = True
                        break
                if not self.t:
                    self.s_av.append(move)
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #setting those ranks
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            for move in self.s_av:
                if move.av == self.s_av[(self.s_av.index(move) - 1)].av:
                    move.s_avg = self.s_av[(self.s_av.index(move) - 1)].s_avg
                else:
                    move.s_avg = self.s_av.index(move)
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Calulating  ranks of minimum
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            self.s_min = []
            for move in self.moves:
                self.t = False
                for move_s in self.s_min:
                    if move_s.min < move.min:
                        self.s_min.insert(self.s_min.index(move_s), move)
                        self.t = True
                        break
                if not self.t:
                    self.s_min.append(move)
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Setting ranks of minimum
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            for move in self.s_min:
                if move.min == self.s_min[(self.s_min.index(move) - 1)].min:
                    move.s_min = self.s_min[(self.s_min.index(move) - 1)].s_min
                else:
                    move.s_min = self.s_min.index(move)
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Calulating ranks Of Maximum
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            self.s_max = []
            for move in self.moves:
                self.t = False
                for move_s in self.s_max:
                    if move_s.max > move.max:
                        continue
                    self.s_max.insert(self.s_max.index(move_s), move)
                    self.t = True
                    break
                if not self.t:
                    self.s_max.append(move)
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Setting ranks of maximum
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            for move in self.s_max:
                if move.max == self.s_max[(self.s_max.index(move) - 1)].max:
                    move.s_max = self.s_max[(self.s_max.index(move) - 1)].s_max
                else:
                    move.s_max = self.s_max.index(move)
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Calulating total rank
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            for move in self.moves:
                move.s_total = move.s_avg + (move.s_min * 2) + move.s_max
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Calulating best move
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            self.best1 = self.moves[0]
            for move in self.moves:
                if move.s_total < self.best1.s_total:
                    self.best1 = move
                    #print best1
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Prints info about all moves
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            for move in self.moves:
                move.PrintStats()
                print move.s_avg, move.s_min, move.s_max, move.s_total
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Prints info about the best move
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            print "Best"
            ##        print "Max:" + str(best1.max) ,"Min:" + str(best1.min) ,"Avg:" + str(best1.max) ,
            self.best1.PrintStats()
            print "Average Score:", self.best1.s_avg, "Minimum Score:", self.best1.s_min, "Maximum Score:",\
                self.best1.s_max, 'Total Score:', self.best1.s_total
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Moves the best move
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            self.best1.MOVE(self.MainBoard)
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Change turns
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            if self.turn == 'w':
                self.turn = 'b'
            else:
                self.turn = 'w'

    def emailloop(self):
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Prints the board
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.MainBoard.show(self.Screen)
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Sorts squares
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.MainBoard.check()
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Runs the Ai if it is it's turn
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if self.turn == self.strColorAI:
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #sends board
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            self.send()
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Gets the best move
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            self.best1 = self.receive()
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Moves the best move
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            self.best1.MOVE(self.MainBoard)
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Change turns
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            if self.turn == 'w':
                self.turn = 'b'
            else:
                self.turn = 'w'

    def send(self):

        print self.game
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Sends board to Assigner
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        Send.chess_email(self.game, ['Player', 'player'], ['Assigner', 'assigner'],
                         ('Calc-' + self.MainBoard.ToString() + '-' + self.turn + '-' + str(self.intLevel))) #str(self.turn_number)

    def receive(self):
        self.msg = []
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Receives message
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.number = 0
        while not self.msg:
            self.eventhandler()
            self.msg = Recieve.receive(self.game, 'Player', 'player')
            self.number += 1
            #if self.number > 1000
            #   print 'no response'
            #  self.win = 'no response'
            # raise BreakError
        if len(self.msg) > 1:
            print self.msg
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Converts Message to string
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.msg = self.msg[0].split('-')
        if self.msg[2] == 'Exit':
            self.win = self.msg[3]
            raise BreakError(self.win)
        else:
            move = Move.Move([], [], 0, '', self.msg[3])
        return move

    def eventhandler(self):
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Event handler
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        for event in pygame.event.get():
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #A key is pressed
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            if event.type == pygame.KEYDOWN:
                ##            if event.key==pygame.K_b:
                ##                for sq in board.sq:
                ##                    if sq.rule_num==5:
                ##                        sq.self_create(board)
                ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                #If that key is 'x'
                ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                if event.key == pygame.K_x:
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    #Deselect the selected piece
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    self.selected = False
                    for square in self.MainBoard.array_square_Squares:
                        square.selected = False
                ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                #If the key is 's' saves the board
                ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                if event.key == pygame.K_s:
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    #Save to inputed location
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    print "What File:"
                    self.FileLoc = raw_input()
                    self.File = open(self.FileLoc, 'w')
                    self.SquareString = self.MainBoard.ToString()
                    self.File.write(self.SquareString)
                    self.File.write('\n' + self.turn)
                    self.File.close()
                    print "Done"
                ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                #If the key is o loads a save
                ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                if event.key == pygame.K_o:
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    #Load a save from inputed location
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    print "What File:"
                    self.FileLoc = raw_input()
                    self.File = open(self.FileLoc, 'r')
                    self.SquareString = self.File.readline()
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    #Loads Board from string
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    self.MainBoard.FromString(self.SquareString)
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    #Sets the turn to saved turn
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    self.turn = self.File.readline()
                    print "Done"
                ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                #if / pressed creates a new piece
                ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                if event.key == pygame.K_SLASH:
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    #Gets data
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    print '>Where'
                    self.loc = raw_input('>')
                    print '>What peice'
                    self.Type = raw_input('>')
                    print '>What color'
                    self.color = raw_input('>')
                    print '>What number'
                    self.intNumber2 = int(raw_input('>'))
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    #Creates piece
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    Functions.create(self.MainBoard, self.loc, self.color, self.Type, self.intNumber2)
                ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                #if space pressed moves a piece
                ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                if event.key == pygame.K_SPACE:
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    #Gets input
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    print '>From where'
                    self.From = raw_input('>')
                    print '>To where'
                    self.To = raw_input('>')
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    #Moves piece
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    Functions.move_(self.MainBoard, self.From, self.To)
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    #Prints piece moved
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    print self.turn + ':', self.From, ">", self.To
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    #Changes turn
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    if self.turn == 'w':
                        self.turn = 'b'
                    else:
                        self.turn = 'w'
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #If the mouse is pressed
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.x = 'a'
                self.y = 0
                ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                #if a piece has already been selected
                ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                if self.selected:
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    #Sets variables to location of mouse
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    self.mousex, self.mousey = event.pos
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    #Determins squares name based on location
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    if self.mousex < 50:
                        self.x = 'a'
                    elif self.mousex < 100:
                        self.x = 'b'
                    elif self.mousex < 150:
                        self.x = 'c'
                    elif self.mousex < 200:
                        self.x = 'd'
                    elif self.mousex < 250:
                        self.x = 'e'
                    elif self.mousex < 300:
                        self.x = 'f'
                    elif self.mousex < 350:
                        self.x = 'g'
                    elif self.mousex < 400:
                        self.x = 'h'
                    self.y = int(self.mousey / 50) + 1
                    self.name2 = self.x + str(self.y)

                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    #
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    if not self.name1 == self.name2:
                        if self.bolSafeMode:
                            self.TEST = "Y" == raw_input("Move " + self.name1 + " to " + self.name2 +
                                                         " Are you sure(Y/N):").upper()
                        else:
                            self.TEST = True
                        if self.TEST:
                            Functions.move_(self.MainBoard, self.name1, self.name2)
                            print self.turn + ':', self.name1, ">", self.name2
                            self.selected = False
                            for sq in self.MainBoard.array_square_Squares:
                                sq.selected = False
                            if self.turn == 'w':
                                self.turn = 'b'
                            else:
                                self.turn = 'w'
                            continue

                    if self.name1 == self.name2:
                        self.selected = False
                        for sq in self.MainBoard.array_square_Squares:
                            sq.selected = False
                else:
                    self.mousex, self.mousey = event.pos
                    if self.mousex < 50:
                        self.x = 'a'
                    elif self.mousex < 100:
                        self.x = 'b'
                    elif self.mousex < 150:
                        self.x = 'c'
                    elif self.mousex < 200:
                        self.x = 'd'
                    elif self.mousex < 250:
                        self.x = 'e'
                    elif self.mousex < 300:
                        self.x = 'f'
                    elif self.mousex < 350:
                        self.x = 'g'
                    elif self.mousex < 400:
                        self.x = 'h'
                    self.y = int(self.mousey / 50) + 1
                    self.name1 = self.x + str(self.y)
                    for sq in self.MainBoard.array_square_Squares:
                        if sq.name == self.name1:
                            sq.selected = True
                    self.selected = True
                    continue
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #If exit was hit then stop
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            if event.type == pygame.QUIT:
                self.true = True
                raise BreakError('Quit')