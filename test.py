import time


def white_breath():
    x = 0
    interval_time = 0.007
    while x == 0:
        for i in range(255):
            x = i
            print(x)
            time.sleep(interval_time)

    while x == 254:
        for i in range(255, 0, -1):
            x = i
            print(x)
            time.sleep(interval_time)

    return x


while True:
    print(white_breath())
