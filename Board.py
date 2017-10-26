##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Board Class for Chess
# created by Vigil
#started: jan 2015
##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import pygame
import Square
import Functions
import func


class Board(pygame.sprite.Sprite):
    ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #Function for Initalizing Board
    ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def __init__(self, image, location, name, image_=None):
        #pygame.sprite.Sprite.__init__(self)
        if image_ is None:
            self.surface_Image = pygame.image.load(image)  # was image
        else:
            self.surface_Image = image_
        #self.rect = self.image.get_rect()
        self.coordinates_Location = self.int_Top, self.int_Left = location
        self.str_Name = name
        self.array_square_Squares = []  # was sq
        self.array_square_BlackSquares = []  # was black
        self.array_square_WhiteSquares = []  # was white
        self.multiarray_square_Board = [[0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0]]

    ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #Prints Board and it's Squares onto Screen
    ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def show(self, screen):
        screen.blit(self.surface_Image, self.coordinates_Location)
        map(Square.Square.show, self.array_square_Squares, [screen] * len(self.array_square_Squares))
        pygame.display.flip()

    ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #Sorts Squares, then has them Check
    ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def check(self):
        self.array_square_BlackSquares = []
        self.array_square_WhiteSquares = []
        temp_array_square_Squares = self.array_square_Squares
        temp_function_WhiteAppend = self.array_square_WhiteSquares.append
        temp_function_BlackAppend = self.array_square_BlackSquares.append
        def SortSquares(square):
            if square.str_color == 'w':
                temp_function_WhiteAppend(square)
            else:
                temp_function_BlackAppend(square)
        map(SortSquares, temp_array_square_Squares)
        map(Square.Square.check, temp_array_square_Squares, [self] * len(temp_array_square_Squares))
        # for square in self.sq:
        #     if square.str_color == 'w':
        #         self.white.append(square)
        #     elif square.str_color == 'b':
        #         self.black.append(square)
        #     square.check(self)

    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #Load from string
    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def FromString(self, str_arg_string):
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Clears the List of Squares
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.array_square_Squares = []
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Creates new Squares
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        int_counter = 0
        for str_letter in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'):
            for int_iterator in range(0, 8):
                location = [int_counter, int_iterator]
                temp_square_storage = Square.Square(0, location, str_letter + str(int_iterator+1))
                self.array_square_Squares.append(temp_square_storage)
                self.multiarray_square_Board[int_counter][int_iterator] = temp_square_storage
            int_counter += 1
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Sets Squares Their Values
        ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        str_arg_string = str_arg_string.split(",")
        array_str_string2 = []
        int_counter = 0
        #print len(self.sq)
        for str_iterator_string1 in str_arg_string:
            #print '1'
            str_iterator_string1 = func.strip(str_iterator_string1, [' '])
            str_iterator_string1 = func.strip(str_iterator_string1, ['\n'])
            array_str_string2.append(str_iterator_string1)
            #print string1
        str_arg_string = array_str_string2

        for square_iterator_Square in self.array_square_Squares:
            str_arg_string[int_counter] = str_arg_string[int_counter].split("^")
            square_iterator_Square.int_Rule_Num = int(str_arg_string[int_counter][1])
            square_iterator_Square.str_Image_Location = str_arg_string[int_counter][0]
            ##                    print sq.str_Image_Location , type(sq.str_Image_Location)
            if square_iterator_Square.str_Image_Location == "0":
                square_iterator_Square.str_Image_Location = 0
                square_iterator_Square.surface_Image = 0
            else:
                square_iterator_Square.surface_Image = pygame.image.load(square_iterator_Square.str_Image_Location)
            square_iterator_Square.str_color = str_arg_string[int_counter][2]
            if square_iterator_Square.str_color == "0":
                square_iterator_Square.str_color = 0
            int_counter += 1
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #MAkes a string representing the Board
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#cleanup stopped here
    def ToString(self):
        SquareString = []
        for sq in self.array_square_Squares:
            SquareString.append(str(sq.str_Image_Location) + "^" + str(sq.int_Rule_Num) + "^" + str(sq.str_color))
        return ",".join(SquareString)

    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #Return a peice with the give name
    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def Peice(self, name):
        for square in self.array_square_Squares:
            if square.name == name:
                return square
        return []

    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #Return a row with the give name
    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def Row(self, name):
        squares = []
        for square in self.array_square_Squares:
            if square.name.__contains__(name):
                squares.append(square)
        return squares

    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #Makes a string representing the Board
    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def PrintString(self):
        String = '______ ______ ______ ______ ______ ______ ______ ______\n'
        Strings = []
        for row in range(1, 9):
            squares = self.Row(str(row))
            string1 = ''
            if row % 2 == 0:
                string1 += '|XXXXXX|        |XXXXXX|        |XXXXXX|        |XXXXXX|        |\n'
                string1 += '|X'
                strings1 = []
                for col in range(0, 8, 2):
                    if squares[col].str_color == 0:
                        x = "XXXX"
                    else:
                        x = ' ' + (squares[col].str_color).upper() + (
                            Functions.rulenum_to_leter(squares[col].int_Rule_Num)) + ' '
                    if squares[col + 1].str_color == 0:
                        xX = "     "
                    else:
                        xX = ' ' + (squares[col + 1].str_color).upper() + (
                            Functions.rulenum_to_leter(squares[col + 1].int_Rule_Num)) + ' '
                    strings1.append(x + 'X| ' + xX)
                string1 += ' |X'.join(strings1)
                string1 += ' |\n'
                string1 += '|XXXXXX|        |XXXXXX|        |XXXXXX|        |XXXXXX|        |\n'
                Strings.append(string1)
            else:
                string1 += '|        |XXXXXX|        |XXXXXX|        |XXXXXX|        |XXXXXX|\n'
                string1 += '| '
                strings1 = []
                for col in range(0, 8, 2):
                    if squares[col].str_color == 0:
                        x = "   "
                    else:
                        x = ' ' + (squares[col].str_color).upper() + (
                            Functions.rulenum_to_leter(squares[col].int_Rule_Num)) + ' '
                    if squares[col + 1].str_color == 0:
                        xX = "XXXX"
                    else:
                        xX = ' ' + (squares[col + 1].str_color).upper() + (
                            Functions.rulenum_to_leter(squares[col + 1].int_Rule_Num)) + ' '
                    strings1.append(x + ' |X' + xX)
                string1 += 'X| '.join(strings1)
                string1 += 'X|\n'
                string1 += '|        |XXXXXX|        |XXXXXX|        |XXXXXX|        |XXXXXX|\n'
                Strings.append(string1)
        String += ' ====== ====== ====== ====== ====== ====== ====== ======\n'.join(Strings)
        String += ' ------ ------ ------ ------ ------ ------ ------ ------\n'
        return String

##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#End of Document
##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
