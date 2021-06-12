from microbit import *

# points = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE',
#           'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
slots = [
    11.25,
    33.75,
    56.25,
    78.75,
    101.25,
    123.75,
    146.25,
    168.75,
    191.25,
    213.75,
    236.25,
    258.75,
    281.25,
    303.75,
    326.25,
    348.75,
]
ports = [
    pin0,
    pin1,
    pin2,
    pin3,
    pin4,
    pin6,
    pin6,
    pin7,
    pin8,
    pin9,
    pin10,
    pin11,
    pin12,
    pin13,
    pin14,
    pin15,
]

def getBearing(heading: int):
    for i in range(0, len(slots) - 1):
        if heading < slots[i]:
            return i
    return 0

def on_forever():
    bearing = compass.heading()
    pinIndex = getBearing(bearing)
    ports[pinIndex].write_digital(1)
    sleep(200)
    ports[pinIndex].write_digital(0)
    #       led.toggle(2, 2)
    sleep(200)

compass.calibrate()

while True:
    display.off()
    on_forever()
