import time


def white_breath():
    yield x = 0
    while x == 0:
        for i in range(255):
            x = i
            # print(x)

    while x == 254:
        for i in range(255, 0, -1):
            x = i
            # print(x)

    yield x


while True:
    print(white_breath())
