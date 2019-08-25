import time


def white_breath():
    x = 0
    while x == 0:
        for i in range(255):
            x = i

    while x == 254:
        for i in range(255, 0, -1):
            x = i

    yield x


while True:

    print(white_breath())
