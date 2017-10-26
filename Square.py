##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Square Class for Chess
# created by Vigil
# started: jan 2015
##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import pygame
import Images
import func
##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Functions that are used later
##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def mapperQ(List, square, x, y, b, color):  # Combines items for filter, Used in the Queen move calculator
    if not (square.int_X - x) == 0:
        xnum = (square.int_X - x) / abs(square.int_X - x)
    else:
        xnum = 0
    if not (square.int_Y - y) == 0:
        ynum = (square.int_Y - y) / abs(square.int_Y - y)
    else:
        ynum = 0
    list.append(List, [square, x, y, xnum, ynum, b, color])


def append_Bishup(List, Item, b):  # Used in the Bishop move calculator
    j, h, number, x, y = Item
    list.append(List, b[x + j * number][y + h * number])


def appendKing(List, Item):   # Used in the Bishop move calculator
    list.append(List, [Item[0] + Item[3], Item[1] + Item[4]])


def KingFilter(Item):   # Used in the Bishop move calculator
    x, y, b, i, j, color = Item
    return ((not j == 0 or not i == 0) and 0 <= (x + i) <= 7 and 0 <= (y + j) <= 7) and \
           (b[x + i][y + j].surface_Image == 0 or not b[x + i][y + j].str_color == color)


def test5(List):   # Used in the bishop move calculator
    j, h, number, x, y = List
    return not number == 0 and 0 <= (x + j * number) <= 7 and 0 <= (y + h * number) <= 7


def filterer(List_):   # Used in the knight move calculator
    b, x, y, x1, y1, color = List_
    if 0 <= (x + x1) <= 7 and 0 <= (y + y1) <= 7:
        return not b[x + x1][y + y1].str_color == color
    else:
        return 0


def append_SQ(List, Item):  # Modified append function
    list.append(List, Item.coordinate_location)


##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Square class, represents the squares on a chess board
##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class Square(pygame.sprite.Sprite):
    ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Funtion for initiating a square
    ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def __init__(self, image, location, name, square=None):
        # pygame.sprite.Sprite.__init__(self)
        if square is None:
            self.str_Image_Location = image  # Was image_loc
            if image == 0:
                self.surface_Image = 0  # Was image
            else:
                self.surface_Image = pygame.image.load(image)
            if not self.surface_Image == 0:
                self.rect_Rectangle = self.surface_Image.get_rect()  # stopped cleanup here
            location = [location[0], location[1]]  # Why is this Here??
            self.int_X, self.int_Y = self.coordinate_location = location  # Was x,y,location#= self.top, self.left
            self.str_Name = name  # Was name
            self.int_Rule_Num = 0
            self.array_coordinate_Possible_Moves = []
            self.str_color = 0  # Was color
            self.bol_Selected = 0
        else:
            self.str_Image_Location = square.str_Image_Location
            self.surface_Image = square.surface_Image
            self.int_X, self.int_Y = self.coordinate_location = square.coordinate_location  # = self.top, self.left
            self.str_Name = square.str_Name
            self.int_Rule_Num = square.int_Rule_Num
            self.array_coordinate_Possible_Moves = []
            self.str_color = square.str_color


    ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Shows posible moves, not used
    ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def self_create(self, board):
        for loc in self.array_coordinate_Possible_Moves:
            for sq in board.sq:
                if sq.coordinate_location == loc:
                    sq.surface_Image = self.surface_Image
                    sq.int_Rule_Num = self.int_Rule_Num
                    sq.str_color = self.str_color
                    ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    # Calculates posible moves
                    ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    #@profile
    def check(self, board):

        # if self.int_Rule_Num == 0:
        # pass
        #==================================================================================
        #For pawn
        #==================================================================================
        if self.int_Rule_Num == 1:
            append = list.append
            p_m = []
            x = self.int_X
            y = self.int_Y
            b = board.multiarray_square_Board
            color = self.str_color
##            if color == 'w':
##                i = 1
##            else:
##                i = -1
            if color == 'w':
                test = 1
                if not x == 7:
                    sq = b[(x + 1)][y]
                    if sq.surface_Image == 0:
                        append(p_m, [x + 1, y])
                    else:
                        test = 0
                    if not y == 7:
                        sq = b[x + 1][y + 1]
                        if not sq.surface_Image == 0 and not sq.str_color == color:
                            append(p_m, [x + 1, y + 1])
                    if not y == 0:
                        sq = b[x + 1][y - 1]
                        if not sq.surface_Image == 0 and not sq.str_color == color:
                            append(p_m, ([x + 1, y - 1]))

                if x == 1:
                    sq = b[x + 2][y]
                    if not sq.surface_Image == 0:
                        test = 0
                else:
                    test = 0

                if test:
                    append(p_m, ([x + 2, y]))
                if x == 7:
                    self.surface_Image = Images.White.queen
                    self.str_Image_Location = 'pictures/queen.png'
                    self.int_Rule_Num = 5
            elif color == 'b':
                test = 1
                if not x == 0:
                    sq = b[x - 1][y]
                    if sq.surface_Image == 0:
                        append(p_m, ([x - 1, y]))
                    else:
                        test = 0

                    if not y == 7:
                        sq = b[x - 1][y + 1]
                        if not sq.surface_Image == 0 and not sq.str_color == color:
                            append(p_m, ([x - 1, y + 1]))

                    if not y == 0:
                        sq = b[x - 1][y - 1]
                        if not sq.surface_Image == 0 and not sq.str_color == color:
                            append(p_m, ([x - 1, y - 1]))

                if x == 6:
                    sq = b[x - 2][y]
                    if not sq.surface_Image == 0:
                        test = 0
                else:
                    test = 0
                if test:
                    append(p_m, ([x - 2, y]))
                if x == 0:
                    self.surface_Image = Images.Black.queen
                    self.str_Image_Location = 'pictures/bqueen.png'
                    self.int_Rule_Num = 5
            self.array_coordinate_Possible_Moves = p_m
        #==================================================================================
        #For rook
        #==================================================================================
        elif self.int_Rule_Num == 2:
            p_m = []
            x = self.int_X
            y = self.int_Y
            b = board.multiarray_square_Board
            color = self.str_color

            def append_2_x(self, item):
                list.append(self, [x, item])

            def append_2_y(self, item):
                list.append(self, [item, y])

            def test4(number):
                test = 1
                for square in b[x]:
                    if (y > square.int_Y > number or y < square.int_Y < number) and not square.surface_Image == 0:
                        test = 0
                        break
                return test and (b[x][number].surface_Image == 0 or not b[x][number].str_color == color)

            def test3(number):
                test = 1
                for row in b:
                    if (x > row[y].int_X > number or x < row[y].int_X < number) and not row[y].surface_Image == 0:
                        test = 0
                        break
                return test and (b[number][y].surface_Image == 0 or not b[number][y].str_color == color)

            numbers = filter(test4, [1, 2, 3, 4, 5, 6, 7])
            map(append_2_x, [p_m] * len(numbers), numbers)

            numbers = filter(test3, [1, 2, 3, 4, 5, 6, 7])
            map(append_2_y, [p_m] * len(numbers), numbers)
            self.array_coordinate_Possible_Moves = p_m

        #==================================================================================
        #For Knight
        #==================================================================================
        elif self.int_Rule_Num == 3:
            p_m = []
            x = self.int_X
            y = self.int_Y
            b = board.multiarray_square_Board
            color = self.str_color
            List_ = []

            map(func.append_6, [List_] * 8, [b] * 8, [x] * 8, [y] * 8, [2, 2, -2, -2, 1, 1, -1, -1],
                [1, -1, 1, -1, 2, -2, 2, -2], [color] * 8)
            numbers = filter(filterer, List_)
            map(func.append_2by2, [p_m] * len(numbers), numbers)

            self.array_coordinate_Possible_Moves = p_m
        #==================================================================================
        #For Bishup
        #==================================================================================
        elif self.int_Rule_Num == 4:
            p_m = []
            x = self.int_X
            y = self.int_Y
            b = board.multiarray_square_Board
            color = self.str_color
            List = []
            List_ = []
            map(func.append_5, [List_] * 28,
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                [1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1],
                [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7], [x] * 28,
                [y] * 28)

            numbers = filter(test5, List_)
            num = len(numbers)
            map(append_Bishup, [List] * num, numbers, [b] * num)
            #@profile
            def test6(square):
                # xnum = (square.int_X - x) / abs(square.int_X - x)
                # ynum = (square.int_Y - y) / abs(square.int_Y - y)
                test = 1
                if not abs(square.int_X - x) == 0:
                    for number in xrange(1, abs(square.int_X - x)):
                        if not b[x + (square.int_X - x) / abs(square.int_X - x) * number][
                                    y + (square.int_Y - y) / abs(square.int_Y - y) * number].surface_Image == 0:
                            test = 0
                            break
                else:
                    for number in xrange(1, abs(square.int_Y - y)):
                        if not b[x + (square.int_X - x) / abs(square.int_X - x) * number][
                                    y + (square.int_Y - y) / abs(square.int_Y - y) * number].surface_Image == 0:
                            test = 0
                            break

                return test and not square == 0 and (square.surface_Image == 0 or not square.str_color == color)

            numbers = filter(test6, List)

            map(append_SQ, [p_m] * len(numbers), numbers)

            self.array_coordinate_Possible_Moves = p_m
        #==================================================================================
        #For Queen
        #==================================================================================
        elif self.int_Rule_Num == 5:
            #append = list.append
            p_m = []
            x = self.int_X
            y = self.int_Y
            b = board.multiarray_square_Board
            color = self.str_color
            List = []
            List_ = []
            map(func.append_5, [List_] * 56,
                [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [-1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1,
                 -1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
                [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1,
                 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7], [x] * 56, [y] * 56)

            numbers = filter(test5, List_)
            num = len(numbers)
            map(append_Bishup, [List] * num, numbers, [b] * num)
            #@profile
            def test6(square):
                test = 1

                if not (square.int_X - x) == 0:
                    if not (square.int_Y - y) == 0:
                        for number in xrange(1, abs(square.int_X - x)):
                            if not b[x + (square.int_X - x) / abs(square.int_X - x) * number][
                                        y + (square.int_Y - y) / abs(square.int_Y - y) * number].surface_Image == 0:
                                test = 0
                                break
                    else:
                        for number in xrange(1, abs(square.int_X - x)):
                            if not b[x + (square.int_X - x) / abs(square.int_X - x) * number][y].surface_Image == 0:
                                test = 0
                                break

                else:
                    for number in xrange(1, abs(square.int_Y - y)):
                        if not b[x][y + (square.int_Y - y) / abs(square.int_Y - y) * number].surface_Image == 0:
                            test = 0
                            break
                return test and not square == 0 and (square.surface_Image == 0 or not square.str_color == color)

            numbers = filter(test6, List)

            map(append_SQ, [p_m] * len(numbers), numbers)

            self.array_coordinate_Possible_Moves = p_m

        #==================================================================================
        #For King
        #==================================================================================
        elif self.int_Rule_Num == 6:
            p_m = []
            x = self.int_X
            y = self.int_Y
            b = board.multiarray_square_Board
            color = self.str_color
            #[-1, -1, -1, 0, 0, 1, 1, 1]
            #[-1, 0, 1, -1, 1, -1, 0, 1]

            List = []

            map(func.append_6, [List] * 8, [x] * 8, [y] * 8, [b] * 8,
                [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1], [color] * 8)

            numbers = filter(KingFilter, List)

            map(appendKing, [p_m] * len(numbers), numbers)

            self.array_coordinate_Possible_Moves = p_m

    def drawsquare(self, coordinate_loc, screen):
        pygame.draw.rect(screen, pygame.color.Color("Green"),
                         pygame.rect.Rect(coordinate_loc[0] * 50, coordinate_loc[1] * 50, 50, 50), 5)

    ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # prints square on screen
    ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def show(self, screen):
        if not self.surface_Image == 0:
            if self.bol_Selected:
                map(Square.drawsquare, [self] * len(self.array_coordinate_Possible_Moves),
                    self.array_coordinate_Possible_Moves, [screen] * len(self.array_coordinate_Possible_Moves))
                pygame.draw.rect(screen, pygame.color.Color("Yellow"),
                                 pygame.rect.Rect(self.int_X * 50, self.int_Y * 50, 50, 50), 3)
            screen.blit(self.surface_Image, [self.coordinate_location[0] * 50, self.coordinate_location[1] * 50])

            # print x * 50, y * 50

##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# End of Document
##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
