##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Move Class for Chess
# created by Vigil
# started: jan 2015
##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import func
import Functions
import Board
import Square

def remover(move):
    moves_ = filter(kingtest, move.moves)
    map(move.moves.remove, moves_)

def kingtest(j):
    return j.min_ == -1000

class Move():
    ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #Function for Initalizing Move
    ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #@profile
    def __init__(self, loc, target, board, color, movestring = ''):
        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #MAking Inital Atributes
        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if movestring == '':
            #print ":("
            self.loc = loc
            self.tar = target
            self.color = color
        else:
            #print ":)"
            string = movestring.split('|')
            self.color = string[0]
            self.loc = [int(y) for y in string[1].split(',')]
            self.tar = [int(y) for y in string[2].split(',')]
            board = Board.Board('pictures/chess2.jpg', [0, 0], 'b1')
            board.FromString(string[3])
            #print self.loc, self.tar
        self.score = 0
        self.moves = []
        self.s_avg = 0
        self.s_min = 0
        self.s_max = 0
        self.s_total = 0
        self.av = 0
        self.av_ = 0
        self.tarsq = 0
        self.locsq = 0
        self.min = 0
        self.max = 0
        self.min_ = 0
        self.max_ = 0
        self.int_Rule_Num = 0
        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Making Squares Of origanal Location
        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        b2 = Functions.create_b(board)
        #print self.tar, self.loc
        map(self.sort, b2.array_square_Squares)
        # for sq in b2.array_square_Squares:
        #     #print "~", sq.loc
        #     if sq.coordinate_location == self.tar:
        #         self.tarsq = sq
        #     if sq.coordinate_location == self.loc:
        #         self.locsq = sq
        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Setting Atributes
        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if not self.tarsq == 0:
            ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Sets self.rule num to the rule num of
            #the rarget Square so it can be used later
            ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            self.int_Rule_Num = self.tarsq.int_Rule_Num
            ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #sets Move's Score
            ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            self.score = Functions.rulenum_to_score(self.tarsq.int_Rule_Num)
            #print self.score
        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Moves the move
        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #print self.locsq
        Functions.move_(b2, self.locsq.str_Name, self.tarsq.str_Name)
        map(Square.Square.check, b2.array_square_Squares, [b2] * len(b2.array_square_Squares))
        #b2.check() #testing
        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Useless Junk?
        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        ##            king=False
        ##            for sq in b2.array_square_Squares:
        ##                if sq.loc==target:
        ##                    for i in sq.p_m:
        ##                        for square in b2.array_square_Squares:
        ##                            if square.loc==i:
        ##                                if square.int_Rule_Num==6:
        ##                                    king=True
        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Modifies The biult in sting funtion so it instead prints Where the move goes
        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    def sort(self, sq):
        if sq.coordinate_location == self.tar:
            self.tarsq = sq
        if sq.coordinate_location == self.loc:
            self.locsq = sq

    def __str__(self):
        return "{Move " + Functions.rulenum_to_piece(
            self.tarsq.int_Rule_Num) + " From " + self.locsq.str_Name + " to " + self.tarsq.str_Name + \
               " which contained " + Functions.rulenum_to_piece(self.int_Rule_Num) + "}"

    ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #Self destruct
    ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # def delet(self, List):
    #     List.remove(self)

    ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #Make a string from a move
    ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def toString(self, Board):
        return '|'.join([self.color, str(self.loc).strip('[').strip(']'),
                         str(self.tar).strip('[').strip(']'), Board.ToString()])

    ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #Prints stats like Score,Average,Min,and Max along with the Move itself
    ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def PrintStats(self):
        print self, "Score:", self.score, "Average:", self.av, "Minimum:", self.min, "Minimum_:", self.min_, "Maximum:", self.max, "Maximum_:", self.max_

    ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #recurion function for finding the score, Fast mode
    ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def __check__(self, b2, b1, num, c2, LIST):#, fast
        num = num - 1
        color = 0
        b2 = Functions.create_b(b2)
        Functions.move_(b2, self.locsq.str_Name, self.tarsq.str_Name)
        if self.color == 'b':
            color = 'w'
        if self.color == 'w':
            color = 'b'
        II = False
        print ":["
        if not self.color == c2:
            if self.score == 1000:
                for t in LIST[0]:
                    if t == LIST[1]:
                        LIST.remove(t)  # .delet(LIST)
                        II = True
                        break
        if not num == 0 and not color == 0 and not II:
            self.moves = Functions.__check__(b2, b1, color, num, c2, [0, 0])#, fast
        #print num
        if num == 0:
            self.max = self.score
            self.min = self.score
            self.av = self.score
        else:
            #print ':>'
            av = 0
            for move in self.moves:
                av += move.av
            self.av_ = av = float(av) / func.length(self.moves) + 1
            self.av = self.score - av
            #print self.av

            #------------------------------------------
            test = 0
            t2 = 0
            for move in self.moves:
                if move.max > test:
                    test = move.max
                if move.score > t2:
                    t2 = move.score
            self.min = self.score - test
            self.min_ = -t2
            #------------------------------------------
            test = 0
            t2 = 0
            for move in self.moves:
                if move.min < test:
                    test = move.min
                if move.score < t2:
                    t2 = move.score
            self.max = self.score - test
            #print self.max
            self.max_ = -t2
            #------------------------------------------
            if self.color == c2:
                for move in self.moves:
                    for j in move.moves:
                        if j.min_ == -1000:
                            move.moves.remove(j)
            if not self.color == c2:
                for j in self.moves:
                    if j.min_ == -1000:
                        self.moves.remove(j)
                        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                        #The Up to Date Recursion function for finding the Average, Min and Max
                        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #@profile
    def check(self, b2, b1, num, c2, LIST, level, screen):#fast_, fast
        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #This is likely the most inportant function in this game.
        #Because it is the scource of the AI. Tagicaly I am
        #commenting this years after it was written, or mabey just
        #a year, anyways, beacuase i can not remeber what everything does
        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #prepares variables
        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        num = num - 1
        color = 0
        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Creates New Board, deleting the old on in the process(prevents Mem Leak)
        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        b2 = Functions.create_b(b2)

        Functions.move_(b2, self.locsq.str_Name, self.tarsq.str_Name)

        map(Square.Square.check, b2.array_square_Squares, [b2] * len(b2.array_square_Squares))
        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Sets color?
        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if self.color == 'b':
            color = 'w'
        elif self.color == 'w':
            color = 'b'
        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Check! :
        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        II = False
        ##        print type(LIST), LIST[0]
        # delet = self.delet

        def test(t):
            return t == LIST[1]
        # delet = Move.delet

        if not self.color == c2 and self.score == 1000:
            stuff = filter(test, LIST[0])
            II = not len(stuff) == []
            map(LIST.remove, stuff)

        # if not self.color == c2:
        #     if self.score == 1000:
        #         for t in LIST[0]:
        #             if t == LIST[1]:
        #                 LIST.remove(t)  # , LIST)
        #                 II = True
        #                 break
        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Continues recursivly, unless the end is reaced, or the king is checked,
        #or ?the color failed to be set?, I don't know why that is there.
        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if not num == 0 and not color == 0 and not II:
            self.moves = Functions.check(b2, b1, color, num, c2, LIST, level, screen,)#fast, fast_)
        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #If the end is reach sets the Min, Max and Average to The score
        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if num == 0:
            self.min = self.max = self.av = self.score
        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Otherwise it calulates them
        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        else:
            ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Calculating Average
            ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            if not self.moves == []:
                av = 0
                test = self.moves[0].max
                t2 = self.moves[0].score
                test2 = self.moves[0].min
                t3 = self.moves[0].score
            else:
                av = 0
                test = 0
                t2 = 0
                test2 = 0
                t3 = 0
            if color == c2:  # means not AI turn
                for move in self.moves:
                    av += move.av
                    if move.max > test:
                        test = move.max
                    if move.score > t2:
                        t2 = move.score
                    # if move.min < test2:
                    #     test2 = move.min
                    if move.score < t3:
                        t3 = move.score
                self.min = self.score - test
                self.min_ = -t2
                self.av_ = av = float(av) / func.length(self.moves) + 1
                self.av = self.score - av
                self.max = self.score - test
                self.max_ = -t3
            else:
                for move in self.moves:
                    av += move.av
                    if move.max > test:
                        test = move.max
                    if move.score > t2:
                        t2 = move.score
                    if move.min < test2:
                        test2 = move.min
                    if move.score < t3:
                        t3 = move.score
                self.min = self.score - test
                self.min_ = -t2
                self.av_ = av = float(av) / func.length(self.moves) + 1
                self.av = self.score - av
                self.max = self.score - test2
                self.max_ = -t3


            #print self.av
            ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Calculating Minimum
            ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Calculating Maximum
            ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Prevents king from moving into check
            ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            #remove = list.remove
            if self.color == c2:


                map(remover, self.moves)

                # for move in self.moves:
                #     for j in move.moves:
                #         if j.min_ == -1000:
                #             remove(move.moves, j)
            else:
                # moves_ = self.moves
                moves_ = filter(kingtest, self.moves)
                map(self.moves.remove, moves_)

                # for j in self.moves:
                #     if j.min_ == -1000:
                #         remove(moves_, j)

    def remote_check(self, b2, num, c2, LIST, level):
        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #This is likely the most inportant function in this game.
        #Because it is the scource of the AI. Tragicly I am
        #commenting this years after it was written, or mabey just
        #a year, anyways, beacuase i can not remeber what everything does
        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #prepares variables
        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        num -= 1
        color = 0
        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Creates New Board, deleting the old on in the process(prevents Mem Leak)
        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #print b2.PrintString()
        b2 = Functions.create_b(b2)

        #print b2.PrintString()
        Functions.move_(b2, self.locsq.str_Name, self.tarsq.str_Name)
        map(Square.Square.check, b2.array_square_Squares, [b2] * len(b2.array_square_Squares))
        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Sets color?
        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if self.color == 'b':
            color = 'w'
        if self.color == 'w':
            color = 'b'
        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Check! :)
        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        II = False
        ##        print type(LIST), LIST[0]
        def test(t):
            return t == LIST[1]
        # delet = Move.delet
        if not self.color == c2 and self.score == 1000:
            stuff = filter(test, LIST[0])
            II = not len(stuff) == []
            map(LIST.remove, stuff)  # , [LIST] * len(stuff)
            # for t in LIST[0]:
            #     if t == LIST[1]:
            #         delet(t, LIST)
            #         II = True
            #         break
        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Continues recursivly, unless the end is reaced, or the king is checked,
        #or ?the color failed to be set?, I don't know why that is there.
        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if not num == 0 and not color == 0 and not II:
            self.moves = Functions.remote_check(b2, color, num, c2, LIST, level)
        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #If the end is reach sets the Min, Max and Average to The score
        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if num == 0:
            self.min = self.max = self.av = self.score
        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Otherwise it calulates them
        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        else:
            ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Calculating Average
            ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            av = 0
            test = 0
            test2 = 0
            t2 = 0
            t2_ = 0
            for move in self.moves:
                av += move.av
                if move.max > test:
                    test = move.max
                if move.score > t2:
                    t2 = move.score
                if move.min < test:
                    test2 = move.min
                if move.score < t2:
                    t2_ = move.score
            self.av_ = av = float(av) / func.length(self.moves) + 1
            self.av = self.score - av
            self.min = self.score - test
            self.min_ = -t2
            self.max = self.score - test2
            self.max_ = -t2_
            #print self.av
            ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Calculating Minimum
            ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            # test = 0
            # t2 = 0
            # for move in self.moves:
            #     if move.max > test:
            #         test = move.max
            #     if move.score > t2:
            #         t2 = move.score
            # self.min = self.score - test
            # self.min_ = -t2
            ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Calculating Maximum
            ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            # test = 0
            # t2 = 0
            # for move in self.moves:
            #     if move.min < test:
            #         test = move.min
            #     if move.score < t2:
            #         t2 = move.score
            # self.max = self.score - test
            # self.max_ = -t2
            ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #Prevents king from moving into check
            ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            remove = list.remove
            if self.color == c2:
                for move in self.moves:
                    for j in move.moves:
                        if j.min_ == -1000:
                            #print ";)"
                            remove(move.moves, remove(j))
            if not self.color == c2:
                for j in self.moves:
                    if j.min_ == -1000:
                        #print ":)"
                        remove(self.moves, remove(j))

    ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #Moves the Move
    ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def MOVE(self, board):
        Functions.move_(board, self.locsq.str_Name, self.tarsq.str_Name)
        #print self.color + ':', self.locsq.str_Name, ">", self.tarsq.str_Name

##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#End of Document
##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        
