# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel


# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 30

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False,
                           pixel_order=ORDER)


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos*2)
        g = int(255 - pos*2)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos*2)
        g = 0
        b = int(pos*2)
    else:
        pos -= 170
        r = 0
        g = int(pos*2)
        b = int(255 - pos*2)
    return (255, 155, b) if ORDER == neopixel.RGB or ORDER == neopixel.GRB else (r, g, b, 0)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)


def white_breath():
    x = 0
    interval_time = 0.007
    time.sleep(1)
    while x == 0:
        for i in range(255):
            x = i
            pixels.fill((x, x, x))
            pixels.show()
            time.sleep(interval_time)

    while x == 254:
        for i in range(255, 0, -1):
            x = i
            pixels.fill((i, i, i))
            pixels.show()
            time.sleep(interval_time)


def repeat_fun(times, f, *args):
    for i in range(times):
        f(*args)


try:
    while True:
        print("light start")
        repeat_fun(5, white_breath)
        # rainbow cycle with 1ms delay per step
        repeat_fun(3, rainbow_cycle, 0.01)
        # white_breath()

        # for i in range(num_pixels):
        #     for r in range(255):
        #         pixels[i] = (r, 0, 0)
        #         pixels.show()
        #         time.sleep(0.001)
        #     j = i - 1
        #     for y in range(255):
        #         pixels[j] = (y, y, y)
        #         pixels.show()
        #         time.sleep(0.001)
        #     time.sleep(0.01)

except KeyboardInterrupt:
    print("KeyboardInterrupt has been caught.")
