##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Square Class for Chess
# created by Vigil
# started: jan 2015
##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import pygame


class Square(pygame.sprite.Sprite):
    ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #Funtion for initiating a square
    ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def __init__(self, image, location, name):
        pygame.sprite.Sprite.__init__(self)
        self.image_loc = image
        if image == 0:
            self.image = 0
        else:
            self.image = pygame.image.load(image)
        if not self.image == 0:
            self.rect = self.image.get_rect()
        self.x, self.y = self.loc = self.location = location #= self.top, self.left
        self.name = name
        self.rule_num = 0
        self.p_m = []
        self.color = 0
        self.selected = False

    ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #Shows posible moves, not used
    ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def self_create(self, board):
        for loc in self.p_m:
            for sq in board.sq:
                if sq.location == loc:
                    sq.image = self.image
                    sq.rule_num = self.rule_num
                    sq.color = self.color
                    ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    #Calculates posible moves
                    ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    def check(self, board):
        self.p_m = []
        if self.rule_num == 0:
            pass
        #==================================================================================
        #For pawn
        #==================================================================================
        elif self.rule_num == 1:
            if self.color == 'w':
                test = True
                sq = board.b[(self.x/50 + 1)][ self.y/50]
                if sq.image == 0:
                    self.p_m.append([self.x + 50, self.y])
                else:
                    test = False

                sq = board.b[(self.x / 50) + 1][(self.y / 50) + 1]
                    if not sq.image == 0 and not sq.color == self.color:
                        self.p_m.append([self.x + 50, self.y + 50])
                elif sq.location == [self.x + 50, self.y - 50]:
                    if not sq.image == 0 and not sq.color == self.color:
                        self.p_m.append([self.x + 50, self.y - 50])
                elif self.x == 50:
                    if sq.location == [self.x + 100, self.y]:
                        if not sq.image == 0:
                            test = False
                elif not self.x == 50:
                    test = False
                if test:
                    self.p_m.append([self.x + 100, self.y])
                if self.x == 350:
                    self.image = pygame.image.load('pictures/queen.png')
                    self.image_loc = 'pictures/queen.png'
                    self.rule_num = 5
                    self.color = 'w'
            if self.color == 'b':
                test = True
                for sq in board.sq:
                    if sq.location == [self.x - 50, self.y]:
                        if sq.image == 0:
                            self.p_m.append([self.x - 50, self.y])
                        else:
                            test = False
                    elif sq.location == [self.x - 50, self.y + 50]:
                        if not sq.image == 0 and not sq.color == self.color:
                            self.p_m.append([self.x - 50, self.y + 50])
                    elif sq.location == [self.x - 50, self.y - 50]:
                        if not sq.image == 0 and not sq.color == self.color:
                            self.p_m.append([self.x - 50, self.y - 50])
                    elif self.x == 300:
                        if sq.location == [self.x - 100, self.y]:
                            if not sq.image == 0:
                                test = False
                    elif not self.x == 300:
                        test = False
                if test:
                    self.p_m.append([self.x - 100, self.y])
                if self.x == 0:
                    self.image = pygame.image.load('pictures/bqueen.png')
                    self.image_loc = 'pictures/bqueen.png'
                    self.rule_num = 5
                    self.color = 'b'
                    #==================================================================================
                    #For rook
                    #==================================================================================
        elif self.rule_num == 2:
            for number in range(0, 8):
                test = True
                for square in board.sq:
                    if square.location[0] == self.x:
                        if square.location == [self.x, number * 50]:
                            SQ = square
                        if self.y > number * 50:
                            if self.y > square.y > number * 50:
                                if not square.image == 0:
                                    test = False
                        if self.y < number * 50:
                            if self.y < square.y < number * 50:
                                if not square.image == 0:
                                    test = False
                if test:
                    if SQ.image == 0:
                        self.p_m.append([self.x, number * 50])
                    elif not SQ.color == self.color:
                        self.p_m.append([self.x, number * 50])
                test = True
                for square in board.sq:
                    if square.location[1] == self.y:
                        if square.location == [number * 50, self.y]:
                            SQ = square
                        if self.x > number * 50:
                            if self.x > square.x > number * 50:
                                if not square.image == 0:
                                    test = False
                        if self.x < number * 50:
                            if self.x < square.x < number * 50:
                                if not square.image == 0:
                                    test = False
                if test:
                    if SQ.image == 0:
                        self.p_m.append([number * 50, self.y])
                    elif not SQ.color == self.color:
                        self.p_m.append([number * 50, self.y])
                        #==================================================================================
                        #For Knight
                        #==================================================================================
        elif self.rule_num == 3:
            for square in board.sq:
                for i in [100, -100]:
                    for j in [50, -50]:
                        if square.location == [self.x + i, self.y + j] and not square.color == self.color:
                            self.p_m.append([self.x + i, self.y + j])
                        if square.location == [self.x + j, self.y + i] and not square.color == self.color:
                            self.p_m.append([self.x + j, self.y + i])
                            #==================================================================================
                            #For Bishup
                            #==================================================================================
        elif self.rule_num == 4:
            List = []
            for j in [1, -1]:
                for h in [1, -1]:
                    for number in range(-8, 8):
                        for square in board.sq:
                            if square.location == [self.x + j * number * 50, self.y + h * number * 50]:
                                List.append(square)
            for square in List:  ##getting target
                test = True
                for sq in List:
                    if square.x < self.x:
                        if square.y < self.y:
                            if self.x > sq.x > square.x and self.y > sq.y > square.y:
                                if not sq.image == 0:
                                    test = False
                        if square.y > self.y:
                            if self.x > sq.x > square.x and self.y < sq.y < square.y:
                                if not sq.image == 0:
                                    test = False
                    if square.x > self.x:
                        if square.y < self.y:
                            if self.x < sq.x < square.x and self.y > sq.y > square.y:
                                if not sq.image == 0:
                                    test = False
                        if square.y > self.y:
                            if self.x < sq.x < square.x and self.y < sq.y < square.y:
                                if not sq.image == 0:
                                    test = False
                if test:
                    if not square == 0:
                        if square.image == 0:
                            self.p_m.append(square.location)
                        elif not square.color == self.color:
                            self.p_m.append(square.location)
                            #==================================================================================
                            #For Queen
                            #==================================================================================
        elif self.rule_num == 5:
            for number in range(0, 8):
                test = True
                for square in board.sq:
                    if square.location[0] == self.x:
                        if square.location == [self.x, number * 50]:
                            SQ = square
                        if self.y > number * 50:
                            if self.y > square.y > number * 50:
                                if not square.image == 0:
                                    test = False
                        if self.y < number * 50:
                            if self.y < square.y < number * 50:
                                if not square.image == 0:
                                    test = False
                if test:
                    if SQ.image == 0:
                        self.p_m.append([self.x, number * 50])
                    elif not SQ.color == self.color:
                        self.p_m.append([self.x, number * 50])
                test = True
                for square in board.sq:
                    if square.location[1] == self.y:
                        if square.location == [number * 50, self.y]:
                            SQ = square
                        if self.x > number * 50:
                            if self.x > square.x > number * 50:
                                if not square.image == 0:
                                    test = False
                        if self.x < number * 50:
                            if self.x < square.x < number * 50:
                                if not square.image == 0:
                                    test = False
                if test:
                    if SQ.image == 0:
                        self.p_m.append([number * 50, self.y])
                    elif not SQ.color == self.color:
                        self.p_m.append([number * 50, self.y])
            List = []
            for j in [1, -1]:
                for h in [1, -1]:
                    for number in range(-8, 8):
                        for square in board.sq:
                            if square.location == [self.x + j * number * 50, self.y + h * number * 50]:
                                List.append(square)
            for square in List:  #getting target
                test = True
                for sq in List:
                    if square.x < self.x:
                        if square.y < self.y:
                            if self.x > sq.x > square.x and self.y > sq.y > square.y:
                                if not sq.image == 0:
                                    test = False
                        if square.y > self.y:
                            if self.x > sq.x > square.x and self.y < sq.y < square.y:
                                if not sq.image == 0:
                                    test = False
                    if square.x > self.x:
                        if square.y < self.y:
                            if self.x < sq.x < square.x and self.y > sq.y > square.y:
                                if not sq.image == 0:
                                    test = False
                        if square.y > self.y:
                            if self.x < sq.x < square.x and self.y < sq.y < square.y:
                                if not sq.image == 0:
                                    test = False
                if test:
                    if not square == 0:
                        if square.image == 0:
                            self.p_m.append(square.location)
                        elif not square.color == self.color:
                            self.p_m.append(square.location)
                            #==================================================================================
                            #For King
                            #==================================================================================
        elif self.rule_num == 1000:
            for i in [1, -1, 0, 0]:
                for j in [1, -1, 0, 0]:
                    if not j == 0 or not i == 0:
                        for sq in board.sq:
                            if sq.location == [self.x + i * 50, self.y + j * 50]:
                                if sq.image == 0:
                                    self.p_m.append(sq.location)
                                elif not sq.color == self.color:
                                    self.p_m.append(sq.location)
                                    ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    #prints square on screen
                                    ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    def show(self, screen):
        if not self.image == 0:
            if self.selected:
                pygame.draw.rect(screen, pygame.color.Color("Yellow"), pygame.rect.Rect(self.x * 50, self.y * 50, 50, 50), 1)
            screen.blit(self.image, self.location)

##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#End of Document
##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
