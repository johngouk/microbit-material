# Thanks to @ScienceOxford for the initial code
from microbit import *
import neopixel

# The maximum NP LED setting
maxValue = 200

# Colours derived by proportional values, against maxValue
red = (maxValue, 0, 0)
orange = (maxValue, int(maxValue*0.5), 0)
yellow = (int(maxValue*0.8), maxValue, 0)
chartreuse = (int(maxValue*0.4), maxValue, 0)
green = (0, maxValue, 0)
teal = (0, maxValue, maxValue)
blue = (0, 0, maxValue)
indigo = (maxValue, 0, int(maxValue*0.5))
violet = (maxValue, 0, maxValue)
white = (maxValue, maxValue, maxValue)

colours = [red, orange, yellow, chartreuse, green, teal, blue, indigo, violet, white]
allRed = [red,red,red,red,red,red,red,red,red,red]
allBlue = [blue,blue,blue,blue,blue,blue,blue,blue,blue,blue]
allOrange = [orange,orange,orange,orange,orange,orange,orange,orange,orange,orange]
allTeal = [teal,teal,teal,teal,teal,teal,teal,teal,teal,teal]
allViolet = [violet,violet,violet,violet,violet,violet,violet,violet,violet,violet]
flashColours = [allRed,allBlue,allOrange,allTeal,allViolet]

# Turns on NPs one at a time, using colourList, low to high
def stepOn(colourList):
    for pixel in range(0, len(lights)):
        lights[pixel] = colourList[pixel]
        lights.show()
        sleep(200)

# Turns off NPs one at a time, high to low
def stepOff():
    for pixel in reversed(range(0,len(lights))):
        lights[pixel] = (0,0,0)
        lights.show()
        sleep(200)

# Flashes all NPs, using provided colourList
def flashOn(colourList):
    lights.clear()
    for pixel in range(0, len(lights)):
        lights[pixel] = colourList[pixel]
    lights.show()
    sleep(200)
    lights.clear()
    lights.show()
    sleep(200)

# flashAlt - flashes alternate NPs using colourList, either odd or even - oddEven is 0 or 1
def flashAlt(colourList,oddEven):
    lights.clear()
    for pixel in range(oddEven, len(lights),2):
        lights[pixel] = colourList[pixel]
    lights.show()
    sleep(200)
    lights.clear()
    lights.show()
    sleep(200)

def fade(rate):
    stepSize = rate
    steps = maxValue / stepSize
    for steps in range (0,steps):
        for pixel in range(0, len(lights)):
            # Have to use list() and tuple() to access/rewrite lights tuple entries
            vals = list(lights[pixel])
            for ind in range (0,len(vals)):
                vals[ind] = max(vals[ind]-stepSize,0)
            lights[pixel] = tuple(vals)
        lights.show()
        sleep(50)

lights = neopixel.NeoPixel(pin0, 10)
while True:
    stepOn(colours)
    stepOff()
    for steps in range (0,5):
        flashOn(flashColours[steps])
    for steps in range (0,5):
        flashAlt(flashColours[steps],steps%2)
    for steps in range (0,5):
        flashAlt(colours,steps%2)
    stepOn(colours)
    fade(5)
    sleep(200)
