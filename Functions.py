##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Misalanious Functions fo Chess
# created by Vigil
# started: jan 2015
##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import pygame

import Square
import Board
import Move



##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Check Funtion, for checking moves, uses recursion
##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#@profile
def check(board, b1, color, num, c2, list_, level, screen):#, fastfast,_
    ##    print ":)", LIST[1]
    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #Display The board
    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #b1.show(screen)
    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #Makes a new board
    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # b2 = create_b(board)
    # map(Square.Square.check, b2.array_square_Squares, [b2] * len(b2.array_square_Squares))

    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #Makes the Moves
    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    moves = []
    def test(sq):
        return sq.str_color == color and not sq.array_coordinate_Possible_Moves == []

    def checkextend(sq):
        moves.extend(map(Move.Move, [sq.coordinate_location] * len(sq.array_coordinate_Possible_Moves),
                         sq.array_coordinate_Possible_Moves, [board] * len(sq.array_coordinate_Possible_Moves),
                         [color] * len(sq.array_coordinate_Possible_Moves)))
    # extend = list.extend
    # for sq in board.array_square_Squares:
    #     if sq.str_color == color:
    #         if not sq.array_coordinate_Possible_Moves == []:
    #             # for loc in sq.array_coordinate_Possible_Moves:
    #             #     moves.append(Move.Move(sq.loc, loc, board, color))
    #             length = len(sq.array_coordinate_Possible_Moves)
    #             extend(moves, map(Move.Move, [sq.coordinate_location] * length, sq.array_coordinate_Possible_Moves,
    #  [board] * length, [color] * length))

    array_square_SQ = filter(test, board.array_square_Squares)
    map(checkextend, array_square_SQ)
    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #For fast Mode(non functional)
    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # if fast_:
    #     pass
    # if num == level:
    #     del_list = []
    #     for move in moves:
    #         move.__check__(b2, b1, c2, screen)
    #         if move.min == 1000:
    #             del_list.append(move)
    #     for move in del_list:
    #         moves.remove(move)
    # nmoves = []
    # _moves = moves
    # for i in xrange(0, 2):
    #     __best__ = _moves[0]
    #     for move in _moves:
    #         if move.score > __best__.score:
    #             __best__ = move
    #     nmoves.append(__best__)
    #     _moves.remove(__best__)
    # moves = nmoves
    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #Has the moves Check
    #Add Web Check Here
    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # elif not fast_:
    #check = Move.Move.check
    #num_ = len(moves)
    map(Move.Move.check, moves, [board] * len(moves), [b1] * len(moves), [num] * len(moves),
        [c2] * len(moves), [[list_[1], moves]] * len(moves),
        [level] * len(moves), [screen] * len(moves))  # [fast] * len(moves),, [fast_] * len(moves)
        # for move in moves:
        #     check(move, board, b1, num, c2, [list_[1], moves], fast, level, screen, fast_)
    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #returns the moves it has made. 
    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    return moves


##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Check Funtion, for checking moves, uses recursion
##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#@profile
def remote_check(board, color, num, c2, list_, level):
    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #Makes a new board
    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # b2 = create_b(board)
    # for sq in b2.array_square_Squares:
    #     sq.check()
    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #Makes the Moves
    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    moves = []

    #extend = list.extend
    def test(sq):
        return sq.str_color == color and not sq.array_coordinate_Possible_Moves == []

    def checkextend(sq):
        list.extend(moves, map(Move.Move, [sq.coordinate_location] * len(sq.array_coordinate_Possible_Moves),
                          sq.array_coordinate_Possible_Moves, [board] * len(sq.array_coordinate_Possible_Moves),
                          [color] * len(sq.array_coordinate_Possible_Moves)))
    array_square_SQ = filter(test, board.array_square_Squares)
    map(checkextend, array_square_SQ)

    #     extend(moves, map(Move.Move, [sq.coordinate_location] * len(sq.array_coordinate_Possible_Moves),
    #                               sq.array_coordinate_Possible_Moves, [board] * len(sq.array_coordinate_Possible_Moves),
    #                               [color] * len(sq.array_coordinate_Possible_Moves)))
    #
    # for sq in board.array_square_Squares:
    #     if sq.str_color == color and not sq.array_coordinate_Possible_Moves == []:
    #             # for loc in sq.array_coordinate_Possible_Moves:
    #             #     moves.append(Move.Move(sq.loc, loc, board, color))
    #             # len(sq.array_coordinate_Possible_Moves) = len(sq.array_coordinate_Possible_Moves)
    #             extend(moves, map(Move.Move, [sq.coordinate_location] * len(sq.array_coordinate_Possible_Moves),
    #                               sq.array_coordinate_Possible_Moves, [board] * len(sq.array_coordinate_Possible_Moves),
    #                               [color] * len(sq.array_coordinate_Possible_Moves)))
    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #Has the moves Check
    #Add Web Check Here
    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    Remote_check = Move.Move.remote_check
    map(Remote_check, moves, [board] * len(moves), [num] * len(moves), [c2] * len(moves),
        [[list_[1], moves]] * len(moves), [level] * len(moves))
    # for move in moves:
    #     Remote_check(move, board, num, c2, [list_[1], moves], level)
    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #returns the moves it has made.
    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    return moves


##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Check Funtion, for checking moves, uses recursion
##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def generate_moves(board, color):
    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #Makes a new board
    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # b2 = create_b(board)
    # b2.check()
    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #Makes the Moves
    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    moves = []
    extend = list.extend
    for sq in board.array_square_Squares:
        if sq.str_color == color:
            if not sq.array_coordinate_Possible_Moves == []:
                # for loc in sq.array_coordinate_Possible_Moves:
                #     moves.append(Move.Move(sq.loc, loc, board, color))
                length = len(sq.array_coordinate_Possible_Moves)
                extend(moves, map(Move.Move, [sq.coordinate_location] * length, sq.array_coordinate_Possible_Moves, [board] * length, [color] * length))
    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #returns the moves it has made.
    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    return moves


##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##Converts Rule Number To Score
##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def rulenum_to_score(num):
    if num == 1:
        return 1
    elif num == 2:
        return 10
    elif num == 3:
        return 10
    elif num == 4:
        return 10
    elif num == 5:
        return 100
    elif num == 6:
        return 1000
    else:
        return 0


##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##Converts Rule Number To Name of Piece
##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def rulenum_to_piece(num):
    if num == 1:
        return "Pawn"
    elif num == 2:
        return "Rook"
    elif num == 3:
        return "Knight"
    elif num == 4:
        return "Bishop"
    elif num == 5:
        return "Queen"
    elif num == 6:
        return "King"
    else:
        return "Nothing"


##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##Converts Rule Number To firstLeter of Piece
##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def rulenum_to_leter(num):
    if num == 1:
        return "P"
    elif num == 2:
        return "R"
    elif num == 3:
        return "K"
    elif num == 4:
        return "B"
    elif num == 5:
        return "Q"
    elif num == 6:
        return "K"
    else:
        return "0"


##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##Duplicate of Check function, For Fast mode(Which does not worK)
##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def __check__(board, b1, color, screen):
    b1.show(screen)
    b2 = create_b(board)
    b2.check()
    moves = []
    if color == 'w':
        for sq in b2.array_square_WhiteSquares:
            if not sq.array_coordinate_Possible_Moves == []:
                for loc in sq.array_coordinate_Possible_Moves:
                    moves.append(Move.Move(sq.coordinate_location, loc, b2, 'w'))
    if color == 'b':
        for sq in board.black:
            if not sq.array_coordinate_Possible_Moves == []:
                for loc in sq.array_coordinate_Possible_Moves:
                    moves.append(Move.Move(sq.coordinate_location, loc, b2, 'b'))
    return moves


##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##not used, was for recursive Average calulation
##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def get_av(list_):
    for move in list_:
        move.get_av()


##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##Move a piece on the board
##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def move_(board, from_, to):
    block1 = 0
    block2 = 0
    for block in board.array_square_Squares:
        if block.str_Name == from_:
            block1 = block
        if block.str_Name == to:
            block2 = block
    if block1 == 0 or block1 == 0:
        print 'nonexistent square'
    else:
        block2.str_Image_Location = block1.str_Image_Location
        block2.surface_Image = block1.surface_Image
        block2.int_Rule_Num = block1.int_Rule_Num
        block2.str_color = block1.str_color
        block1.str_Image_Location = 0
        block1.surface_Image = 0
        block1.int_Rule_Num = 0
        block1.str_color = 0


##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##Creates a peice
##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def create(board, square, color, type_, num):
    for sq in board.array_square_Squares:
        if sq.str_Name == square:
            if color == 'black' or color == 'b':
                sq.str_color = bl = 'b'
            else:
                sq.str_color = 'w'
                bl = ''
            piece = bl + type_
            sq.surface_Image = pygame.image.load('pictures/' + piece + '.png')
            sq.str_Image_Location = 'pictures/' + piece + '.png'
            sq.int_Rule_Num = num


##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##Creates a board
##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def create_b(board):
    b2 = Board.Board('pictures/chess2.jpg', [0, 0], 'b2', image_=board.surface_Image)
    append = b2.array_square_Squares.append
    SQ = Square.Square

    def test(i, ii):
        square = board.multiarray_square_Board[i][ii]
        sq = SQ(0, 0, 0, square=square)
        b2.multiarray_square_Board[i][ii] = sq
        append(sq)

    #for sq in board.array_square_Squares:
    #   print sq.loc
    map(test, [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4,
               4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7],
        [0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3, 4,
         5, 6, 7, 0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3, 4, 5, 6, 7])
    #for sq in b2.array_square_Squares:
    #   print "~", sq.loc
    return b2


##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##Runs a File
##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def RunFile(Path):
    import os, subprocess, sys

    try:
        os.startfile(Path)
    except AttributeError:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, Path])

##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##End of Document
##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
