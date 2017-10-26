# +++++++++++++++++++++++
#this modual contains all of the random functions i use
#created by savagewil
#started: 11/13/12, finished: never
#++++++++++++++++++++++++++++++


def strip(string, remove):
    for item in remove:
        string = ''.join(string.split(item))
    return string


def _split(string):
    splist = []
    for let in string:
        splist.append(let)
    return splist


def l_split(List, string):
    x = [string]
    y = []
    for i in List:
        for j in x:
            y.extend(j.split(i))
        x = y
        y = []
    return x

def append_2(self, x, item):
    list.append(self, [x, item])

def append_2_x(self, x, item):
    list.append(self, [x, item[0]])

def append_2_y(self, x, item):
    list.append(self, [x[0], item])

def append_5(List_, w, e, r, t, y):
    list.append(List_, [w, e, r, t, y])

def append_6(List_, w, e, r, t, y, j):
    list.append(List_, [w, e, r, t, y, j])

def append_2by2(List_, item):
    list.append(List_, [item[1] + item[3], item[2] + item[4]])

def length(List):
    length = 0
    for lkjh in List:
        length += 1
    return length - 1


def let_num(let):
    num = ''
    if let == 'a':
        num = 0
    if let == 'b':
        num = 1
    if let == 'c':
        num = 2
    if let == 'd':
        num = 3
    if let == 'e':
        num = 4
    if let == 'f':
        num = 5
    if let == 'g':
        num = 6
    if let == 'h':
        num = 7
    if let == 'i':
        num = 8
    if let == 'j':
        num = 9
    if let == 'k':
        num = 10
    if let == 'l':
        num = 11
    if let == 'm':
        num = 12
    if let == 'n':
        num = 13
    if let == 'o':
        num = 14
    if let == 'p':
        num = 15
    if let == 'q':
        num = 16
    if let == 'r':
        num = 17
    if let == 's':
        num = 18
    if let == 't':
        num = 19
    if let == 'u':
        num = 20
    if let == 'v':
        num = 21
    if let == 'w':
        num = 22
    if let == 'x':
        num = 23
    if let == 'y':
        num = 24
    if let == 'z':
        num = 25
    if let == ' ':
        num = ' '
    if let == '.':
        num = '.'
    if let == '!':
        num = '!'
    if let == ',':
        num = ','
    if let == '"':
        num = '"'
    if let == "'":
        num = "'"
    return num


def print_abc():
    print 'a'
    print 'b'
    print 'c'
    print 'd'
    print 'e'
    print 'f'
    print 'g'
    print 'i'
    print 'j'
    print 'k'
    print 'l'
    print 'm'
    print 'n'
    print 'o'
    print 'p'
    print 'q'
    print 'r'
    print 's'
    print 't'
    print 'u'
    print 'v'
    print 'w'
    print 's'
    print 'x'
    print 'y'
    print 'z'
