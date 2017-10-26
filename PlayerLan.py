__author__ = 'william'
import Images
import pygame
import Functions
import Square
import Board
import Recieve
import Move
import Send
import random
#import datetime
import os



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
        self.array_Used = []
        self.array_Msg = []
        self.str_IP = ''
        self.bol_LanProcess = True
        self.str_Assigner = ''
        self.str_Done = ''
        self.bol_TEST = True
        self.str_Name2 = ''
        self.str_Name1 = ''
        self.int_Y = 0
        self.str_X = 'a'
        self.arraymove_S_Max = []
        self.arraymove_S_Min = []
        self.bol_T = True
        self.arraymove_S_AV = []
        self.array_Testl = []
        self.move_YKing = 0
        self.int_Number = 0
        self.int_Level = 0
        self.str_ColorAI = ''
        self.bol_SafeMode = False
        self.bol_JustAI = False
        self.surface_Screen = 0
        self.board_MainBoard = Board.Board('pictures/chess2.jpg', [0, 0], 'b1')
        self.coordinates_lstLocation = []
        self.bol_True = False
        self.bol_Selected = False
        self.str_Turn = 'w'
        self.str_Win_Message = 'yes'
        self.arraymove_Moves = []
        self.move_King = 0
        self.move_Best1 = 0
        self.arraymove_BestMoves = []
        self.str_path_FileLoc = ''
        self.str_path_File = ''
        self.str_SquareString = ''
        self.str_Loc = ''
        self.str_Type = ''
        self.str_Color = ''
        self.int_Number2 = 0
        self.str_From = ''
        self.str_To = ''
        self.int_MouseX, self.str_MouseY = [0, 0]
        self.bol_Develop = False
        self.game = ''
        #self.number = 0

    def start(self, level=0, color=None, developer=None, lanProcess=None, justAI=None, safeMode=None, ip=None, game=None, assigner=None):
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Getting Game stats
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if level == 0:
            print 'What level?'
            self.int_Level = 1 + int(raw_input())
        else:
            self.int_Level = level
        if color is None:
            print 'What color is ai?'
            self.str_ColorAI = raw_input()
        else:
            self.str_ColorAI = color
        if developer is None:
            print 'Developer Move(Y/N):'
            self.bol_Develop = ("y" == raw_input().lower())
        else:
            self.bol_Develop = developer
        if self.bol_Develop:
            if justAI is None:
                print 'Just AI(Y/N):'
                self.bol_JustAI = ("y" == raw_input().lower())
            else:
                self.bol_JustAI = justAI
            if safeMode is None:
                print 'Safe Mode(Y/N):'
                self.bol_SafeMode = ("y" == raw_input().lower())
            else:
                self.bol_SafeMode = safeMode
        if lanProcess is None:
            print 'Lan Process(Y/N):'
            self.bol_LanProcess = ("y" == raw_input().lower())
        else:
            self.bol_LanProcess = lanProcess
        if self.bol_LanProcess:
            if ip is None:
                print 'What is my IP:'
                self.str_IP = raw_input()
            else:
                self.str_IP = ip
            if game is None:
                print 'What is the game name:'
                self.game = raw_input()
            else:
                self.game = game

            if assigner is None:
                print "What is Assigner's IP:"
                self.str_Assigner = raw_input()
            else:
                self.str_Assigner = assigner


            Functions.RunFile("Reciever.py")
            self.send_reg()
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Initalizing Pygame for visuals
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        pygame.init()
        self.surface_Screen = pygame.display.set_mode([450, 450])
        self.surface_Screen.fill([255, 255, 255])
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Making Squares
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        for chrLetter in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'):
            for intNumber1 in range(0, 8):
                self.coordinates_lstLocation = [self.int_Number, intNumber1]
                x = Square.Square(0, self.coordinates_lstLocation, chrLetter + str(intNumber1 + 1))
                self.board_MainBoard.array_square_Squares.append(x)
                self.board_MainBoard.multiarray_square_Board[self.int_Number][intNumber1] = x
            self.int_Number += 1
        ##for row in self.MainBoard.b:
          ##  for sq in row:
            ##    print sq.loc
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Setting squares up for starting positions
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        for square in self.board_MainBoard.array_square_Squares:
            if square.str_Name == 'a5':
                square.surface_Image = Images.White.king
                square.str_Image_Location  = 'pictures/king.png'
                square.str_color = 'w'
                square.int_Rule_Num = 6
            if square.str_Name == 'a4':
                square.surface_Image = Images.White.queen
                square.str_Image_Location = 'pictures/queen.png'
                square.str_color = 'w'
                square.int_Rule_Num = 5
            if square.str_Name == 'a3' or square.str_Name == 'a6':
                square.surface_Image = Images.White.bishop
                square.str_Image_Location  = 'pictures/bishop.png'
                square.str_color = 'w'
                square.int_Rule_Num = 4
            if square.str_Name == 'a7' or square.str_Name == 'a2':
                square.surface_Image = Images.White.knight
                square.str_Image_Location  = 'pictures/knight.png'
                square.str_color = 'w'
                square.int_Rule_Num = 3
            if square.str_Name == 'a1' or square.str_Name == 'a8':
                square.surface_Image = Images.White.rook
                square.str_Image_Location  = 'pictures/rook.png'
                square.str_color = 'w'
                square.int_Rule_Num = 2
            if square.str_Name.__contains__('b'):
                square.surface_Image = Images.White.pawn
                square.str_Image_Location  = 'pictures/pawn.png'
                square.str_color = 'w'
                square.int_Rule_Num = 1
            if square.str_Name == 'h5':
                square.surface_Image = Images.Black.king
                square.str_Image_Location  = 'pictures/bking.png'
                square.str_color = 'b'
                square.int_Rule_Num = 6
            if square.str_Name == 'h4':
                square.surface_Image = Images.Black.queen
                square.str_Image_Location  = 'pictures/bqueen.png'
                square.str_color = 'b'
                square.int_Rule_Num = 5
            if square.str_Name == 'h3' or square.str_Name == 'h6':
                square.surface_Image = Images.Black.bishop
                square.str_Image_Location  = 'pictures/bbishop.png'
                square.str_color = 'b'
                square.int_Rule_Num = 4
            if square.str_Name == 'h7' or square.str_Name == 'h2':
                square.surface_Image = Images.Black.knight
                square.str_Image_Location  = 'pictures/bknight.png'
                square.str_color = 'b'
                square.int_Rule_Num = 3
            if square.str_Name == 'h1' or square.str_Name == 'h8':
                square.surface_Image = Images.Black.rook
                square.str_Image_Location  = 'pictures/brook.png'
                square.str_color = 'b'
                square.int_Rule_Num = 2
            if square.str_Name.__contains__('g'):
                square.surface_Image = Images.Black.pawn
                square.str_Image_Location  = 'pictures/bpawn.png'
                square.str_color = 'b'
                square.int_Rule_Num = 1
        while not self.bol_True:
            try:
                if self.bol_LanProcess:
                    self.emailloop()
                else:
                    self.mainloop()
                self.eventhandler()
            except BreakError:
                break
            except KeyboardInterrupt:
                break

        print self.str_Win_Message
        print 'Done?'
        self.str_Done = raw_input()
        while not self.str_Done == 'done':
            self.str_Done = raw_input()
        pygame.quit()

        
    def mainloop(self):
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Prints the board
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.board_MainBoard.show(self.surface_Screen)
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Sorts squares
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.board_MainBoard.check()
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Runs the Ai if it is it's turn
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if not self.str_Turn == self.str_ColorAI and self.bol_JustAI:
           raise Exception("Just AI")
        #self.str_ColorAI = self.str_Turn
        if self.str_Turn == self.str_ColorAI:
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #gets moves, (longest part)
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #now = datetime.datetime.now().time()
            self.arraymove_Moves = Functions.check(self.board_MainBoard, self.board_MainBoard, self.str_ColorAI,
                                                   self.int_Level, self.str_ColorAI, [0, 0],
                                                   self.int_Level, self.surface_Screen)
                                         #self.bolFast,self.bolFast
            #after = datetime.datetime.now().time()
            #print (after.minute - now.minute) * 1000000 * 60 + (after.second - now.second) * 1000000 + after.microsecond - now.microsecond
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Detects a stalemate
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            if not self.arraymove_Moves:
                self.bol_True = True
                self.str_Win_Message = 'stalemate'
                raise BreakError('Stalemate')
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #clears king
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            self.move_King = 0
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #detects if its king is still alive
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            for i in self.board_MainBoard.array_square_Squares:
                if i.str_color == self.str_ColorAI and i.int_Rule_Num == 6:
                        self.move_King = i
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #if it is not then it knows you won
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            if self.move_King == 0:
                self.bol_True = True
                self.str_Win_Message = 'You Win'
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Clears "your king"
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            self.move_YKing = 0
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Detects if your king is still alive
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            for i in self.board_MainBoard.array_square_Squares:
                if not i.str_color == self.str_ColorAI and i.int_Rule_Num == 6:
                        self.move_YKing = i
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #if it is not then it knows it won
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            if self.move_YKing == 0:
                self.bol_True = True
                self.str_Win_Message = 'I win'
                #print 'm',func.length(moves)

            ##        for move in moves:
            ##            #print move.min_
            ##            pass
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Creates List of moves to delet because king is in check
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            # self.testl = []
            # for move in self.moves:
            #     #print 'move',move.score
            #     if move.min_ == -1000:
            #         self.testl.append(self.moves.index(move))
            # self.testl.sort()
            # self.testl.reverse()
            # ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            # #removes those moves
            # ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            # for z in self.testl:
            #     self.moves.__delitem__(z)
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #If There are no moves left it calls it Check mate
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            if not self.arraymove_Moves:
                print self.arraymove_Moves  # {{}}
                print len(self.arraymove_Moves)
                self.bol_True = True
                self.str_Win_Message = 'Check mate\nYou win'
                raise BreakError(self.str_Win_Message)

            test = 0
            test2 = 0
            for move in self.arraymove_Moves:
                if move.min > -500:
                    test = 1
                    # if move.max > 500:
                    #     test2 = 1

            if not test:
                # print self.arraymove_Moves  # {{}}
                # print len(self.arraymove_Moves)
                self.bol_True = True
                self.str_Win_Message = 'Check mate\nYou win'
                raise BreakError(self.str_Win_Message)
                #for move in moves:
                #print move.av_
            # if test:
            #     print "Check"
            #    pass
            #print 'm',func.length(moves)
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Calculating best move
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Caluclating ranks of average
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            self.arraymove_S_AV = []
            for move in self.arraymove_Moves:
                self.bol_T = False
                for move_s in self.arraymove_S_AV:
                    if move_s.av < move.av:
                        self.arraymove_S_AV.insert(self.arraymove_S_AV.index(move_s), move)
                        self.bol_T = True
                        break
                if not self.bol_T:
                    self.arraymove_S_AV.append(move)
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #setting those ranks
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            for move in self.arraymove_S_AV:
                if move.av == self.arraymove_S_AV[(self.arraymove_S_AV.index(move) - 1)].av:
                    move.s_avg = self.arraymove_S_AV[(self.arraymove_S_AV.index(move) - 1)].s_avg
                else:
                    move.s_avg = self.arraymove_S_AV.index(move)
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Calulating  ranks of minimum
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            self.arraymove_S_Min = []
            for move in self.arraymove_Moves:
                self.bol_T = False
                for move_s in self.arraymove_S_Min:
                    if move_s.min < move.min:
                        self.arraymove_S_Min.insert(self.arraymove_S_Min.index(move_s), move)
                        self.bol_T = True
                        break
                if not self.bol_T:
                    self.arraymove_S_Min.append(move)
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Setting ranks of minimum
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            for move in self.arraymove_S_Min:
                if move.min == self.arraymove_S_Min[(self.arraymove_S_Min.index(move) - 1)].min:
                    move.s_min = self.arraymove_S_Min[(self.arraymove_S_Min.index(move) - 1)].s_min
                else:
                    move.s_min = self.arraymove_S_Min.index(move)
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Calulating ranks Of Maximum
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            self.arraymove_S_Max = []
            for move in self.arraymove_Moves:
                self.bol_T = False
                for move_s in self.arraymove_S_Max:
                    if move_s.max > move.max:
                        continue
                    self.arraymove_S_Max.insert(self.arraymove_S_Max.index(move_s), move)
                    self.bol_T = True
                    break
                if not self.bol_T:
                    self.arraymove_S_Max.append(move)
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Setting ranks of maximum
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            for move in self.arraymove_S_Max:
                if move.max == self.arraymove_S_Max[(self.arraymove_S_Max.index(move) - 1)].max:
                    move.s_max = self.arraymove_S_Max[(self.arraymove_S_Max.index(move) - 1)].s_max
                else:
                    move.s_max = self.arraymove_S_Max.index(move)
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Calulating total rank
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            for move in self.arraymove_Moves:
                move.s_total = move.s_avg + (move.s_min * 2) + move.s_max
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Calulating best move
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            self.arraymove_BestMoves = []

            self.move_Best1 = self.arraymove_Moves[0]
            for move in self.arraymove_Moves:
                if move.min > self.move_Best1.min:
                    self.move_Best1 = move

            for move in self.arraymove_Moves:
                if move.min == self.move_Best1.min:
                    self.arraymove_BestMoves.append(move)

            #
            self.arraymove_BestMoves1 = []

            for move in self.arraymove_BestMoves:
                if move.av > self.move_Best1.av:
                    self.move_Best1 = move

            for move in self.arraymove_BestMoves:
                if move.av == self.move_Best1.av:
                    self.arraymove_BestMoves1.append(move)

            self.arraymove_BestMoves = []

            for move in self.arraymove_BestMoves1:
                if move.max > self.move_Best1.max:
                    self.move_Best1 = move

            for move in self.arraymove_BestMoves1:
                if move.max == self.move_Best1.max:
                    self.arraymove_BestMoves.append(move)

            self.move_Best1 = self.arraymove_BestMoves[random.randint(0, len(self.arraymove_BestMoves) - 1)]


                    #print best1
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Prints info about all moves
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #for move in self.moves:
             #   move.PrintStats()
                #print move.s_avg, move.s_min, move.s_max, move.s_total
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Prints info about the best move
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            print "Best"
            ##        print "Max:" + str(best1.max) ,"Min:" + str(best1.min) ,"Avg:" + str(best1.max) ,
            self.move_Best1.PrintStats()
            print "Average Score Rank:", self.move_Best1.s_avg, "Minimum Score Rank:", self.move_Best1.s_min, "Maximum Score Rank:",\
                self.move_Best1.s_max, 'Total Rank:', self.move_Best1.s_total
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Moves the best move
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            # if self.move_Best1.
            self.move_Best1.MOVE(self.board_MainBoard)
            for square in self.board_MainBoard.array_square_Squares:
                square.check(self.board_MainBoard) #{{}}
            # print self.move_Best1.max  self.move_Best1.tar.
            if self.move_Best1.min > 900:
                print "Check Mate"
            if self.board_MainBoard.multiarray_square_Board[self.move_Best1.tar[0]][self.move_Best1.tar[1]].\
                    array_coordinate_Possible_Moves.__contains__(self.move_YKing.coordinate_location):
                print "Check"
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Change turns
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            if self.str_Turn == 'w':
                self.str_Turn = 'b'
            else:
                self.str_Turn = 'w'

    def emailloop(self):
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Prints the board
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.board_MainBoard.show(self.surface_Screen)
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Sorts squares
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.board_MainBoard.check()
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Runs the Ai if it is it's turn
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if self.str_Turn == self.str_ColorAI:
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #sends board
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            self.send()
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Gets the best move
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            self.move_Best1 = self.receive()
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Moves the best move
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            self.move_Best1.MOVE(self.board_MainBoard)
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Change turns
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            if self.str_Turn == 'w':
                self.str_Turn = 'b'
            else:
                self.str_Turn = 'w'

    def send_reg(self):
        print self.str_Assigner
        Send.send_msg(self.str_Assigner,('A-Reg-pl-' + self.str_IP)) #str(self.turn_number)

    def send(self):

        print self.game
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Sends board to Assigner
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        Send.send_msg(self.str_Assigner,
                      ('A-Calc-' + self.board_MainBoard.ToString() + '-' + self.str_Turn + '-' + str(self.int_Level))) #str(self.turn_number)

    def receive(self):
        self.array_Msg = []
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Receives message
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #self.number = 0
        while not self.array_Msg:
            self.eventhandler()
            self.array_Msg, test= Recieve.receive('PL', self.array_Used)
            if test:
                self.array_Used.extend(self.array_Msg)
            else:
                self.array_Used = self.array_Msg
            #self.number += 1
            #if self.number > 1000
            #   print 'no response'
            #  self.win = 'no response'
            # raise BreakError
        if len(self.array_Msg) > 1:
            print self.array_Msg
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Converts Message to string
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        for msg in self.array_Msg:
            msg = msg.split('-')
            if msg[0] == 'Exit':
                self.str_Win_Message = msg[1]
                raise BreakError(self.str_Win_Message)
            else:
                move = Move.Move([], [], 0, '', msg[1])
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
                ##                    if sq.int_Rule_Num==5:
                ##                        sq.self_create(board)
                ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                #If that key is 'c'
                ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                if event.key == pygame.K_c:
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    #clear the board
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    self.bol_Selected = False
                    for square in self.board_MainBoard.array_square_Squares:
                        square.str_Image_Location  = 0
                        square.surface_Image = 0 # = self.top, self.left
                        square.int_Rule_Num = 0
                        square.p_m = []
                        square.str_color = 0
                        square.bol_Selected = False
                ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                #If that key is 'x'
                ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                if event.key == pygame.K_x:
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    #Deselect the selected piece
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    self.bol_Selected = False
                    for square in self.board_MainBoard.array_square_Squares:
                        square.bol_Selected = False
                ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                #If the key is 's' saves the board
                ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                if event.key == pygame.K_s:
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    #Save to inputed location
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    print "What File:"
                    self.str_path_FileLoc = raw_input()
                    self.str_path_File = open(self.str_path_FileLoc, 'w')
                    self.str_SquareString = self.board_MainBoard.ToString()
                    self.str_path_File.write(self.str_SquareString)
                    self.str_path_File.write('\n' + self.str_Turn)
                    self.str_path_File.close()
                    print "Done"
                ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                #If the key is o loads a save
                ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                if event.key == pygame.K_o:
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    #Load a save from inputed location
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    print "What File:"
                    self.str_path_FileLoc = raw_input()
                    self.str_path_File = open(self.str_path_FileLoc, 'r')
                    self.str_SquareString = self.str_path_File.readline()
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    #Loads Board from string
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    self.board_MainBoard.FromString(self.str_SquareString)
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    #Sets the turn to saved turn
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    self.str_Turn = self.str_path_File.readline()
                    print "Done"
                ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                #if / pressed creates a new piece
                ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                if event.key == pygame.K_l:
                    pass #
                    Functions.create(self.board_MainBoard, 'a3', "w", "pawn", 1)
                    Functions.create(self.board_MainBoard, 'a4', "w", "pawn", 1)
                    Functions.create(self.board_MainBoard, 'a5', "w", "pawn", 1)
                    Functions.create(self.board_MainBoard, 'b3', "w", "pawn", 1)
                    Functions.create(self.board_MainBoard, 'b4', "w", "king", 6)
                    Functions.create(self.board_MainBoard, 'b5', "w", "pawn", 1)
                    Functions.create(self.board_MainBoard, 'c3', "w", "pawn", 1)
                    Functions.create(self.board_MainBoard, 'c5', "w", "pawn", 1)
                    Functions.create(self.board_MainBoard, 'h8', "b", "queen", 5)
                    Functions.create(self.board_MainBoard, 'h1', "b", "king", 6)
                if event.key == pygame.K_SLASH:
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    #Gets data
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    print '>Where'
                    self.str_Loc = raw_input('>')
                    print '>What peice'
                    self.str_Type = raw_input('>')
                    print '>What color'
                    self.str_Color = raw_input('>')
                    print '>What number'
                    self.int_Number2 = int(raw_input('>'))
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    #Creates piece
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    Functions.create(self.board_MainBoard, self.str_Loc, self.str_Color, self.str_Type, self.int_Number2)
                ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                #if space pressed moves a piece
                ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                if event.key == pygame.K_SPACE:
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    #Gets input
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    print '>From where'
                    self.str_From = raw_input('>')
                    print '>To where'
                    self.str_To = raw_input('>')
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    #Moves piece
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    Functions.move_(self.board_MainBoard, self.str_From, self.str_To)
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    #Prints piece moved
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    print self.str_Turn + ':', self.str_From, ">", self.str_To
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    #Changes turn
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    if self.str_Turn == 'w':
                        self.str_Turn = 'b'
                    else:
                        self.str_Turn = 'w'
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #If the mouse is pressed
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.str_X = 'a'
                self.int_Y = 0
                ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                #if a piece has already been selected
                ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                if self.bol_Selected:
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    #Sets variables to location of mouse
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    self.int_MouseX, self.str_MouseY = event.pos
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    #Determins squares name based on location
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    if self.int_MouseX < 50:
                        self.str_X = 'a'
                    elif self.int_MouseX < 100:
                        self.str_X = 'b'
                    elif self.int_MouseX < 150:
                        self.str_X = 'c'
                    elif self.int_MouseX < 200:
                        self.str_X = 'd'
                    elif self.int_MouseX < 250:
                        self.str_X = 'e'
                    elif self.int_MouseX < 300:
                        self.str_X = 'f'
                    elif self.int_MouseX < 350:
                        self.str_X = 'g'
                    elif self.int_MouseX < 400:
                        self.str_X = 'h'
                    self.int_Y = int(self.str_MouseY / 50) + 1
                    self.str_Name2 = self.str_X + str(self.int_Y)

                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    #
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    if not self.str_Name1 == self.str_Name2:
                        if self.bol_SafeMode:
                            self.bol_TEST = "Y" == raw_input("Move " + self.str_Name1 + " to " + self.str_Name2 +
                                                         " Are you sure(Y/N):").upper()
                        else:
                            self.bol_TEST = True
                        if self.bol_TEST:
                            Functions.move_(self.board_MainBoard, self.str_Name1, self.str_Name2)
                            print self.str_Turn + ':', self.str_Name1, ">", self.str_Name2
                            self.bol_Selected = False
                            for sq in self.board_MainBoard.array_square_Squares:
                                sq.bol_Selected = False
                            if self.str_Turn == 'w':
                                self.str_Turn = 'b'
                            else:
                                self.str_Turn = 'w'
                            continue

                    if self.str_Name1 == self.str_Name2:
                        self.bol_Selected = False
                        for sq in self.board_MainBoard.array_square_Squares:
                            sq.bol_Selected = False
                else:
                    self.int_MouseX, self.str_MouseY = event.pos
                    if self.int_MouseX < 50:
                        self.str_X = 'a'
                    elif self.int_MouseX < 100:
                        self.str_X = 'b'
                    elif self.int_MouseX < 150:
                        self.str_X = 'c'
                    elif self.int_MouseX < 200:
                        self.str_X = 'd'
                    elif self.int_MouseX < 250:
                        self.str_X = 'e'
                    elif self.int_MouseX < 300:
                        self.str_X = 'f'
                    elif self.int_MouseX < 350:
                        self.str_X = 'g'
                    elif self.int_MouseX < 400:
                        self.str_X = 'h'
                    self.int_Y = int(self.str_MouseY / 50) + 1
                    self.str_Name1 = self.str_X + str(self.int_Y)
                    for sq in self.board_MainBoard.array_square_Squares:
                        if sq.str_Name == self.str_Name1:
                            sq.bol_Selected = True
                    self.bol_Selected = True
                    continue
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #If exit was hit then stop
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            if event.type == pygame.QUIT:
                self.bol_True = True
                raise BreakError('Quit')
