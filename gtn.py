from random import randint

"""
draw number form range 1-100
"""


def draw_num():
    d_num = randint(1, 100)
    return d_num


"""
get guessing number from user -'lucky shot'

"""


def get__lucky_shot():
    try:
        shot = int(input("Your lucky shot: "))
    except ValueError:
        shot = "lucky should by number"
    return shot


"""
check if user shot is > < or == draw number
if to small print "to small" and return "0"
if to big print  "to big: an return "0"
if  equal   print "you WIN" 
"""


def check_d_num(d_num, shot):
    if d_num > shot:
        print("To small \n")
        return False
    elif d_num < shot:
        print("To big \n")
        return False
    else:
        print("You Win!")
        return True


"""
take draw parameter and compare whit user shot's
"""


def play():
    d_n = draw_num()
    shot = get__lucky_shot()
    while not check_d_num(d_n, shot):
        shot = get__lucky_shot()


play()
