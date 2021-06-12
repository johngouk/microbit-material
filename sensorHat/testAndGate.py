from microbit import *

display.show(Image.HEART)
pin1.write_digital(0)
pin2.write_digital(0)
# Allow experimenter to see the "I'm working!" HEART
sleep(500)
display.clear()
a_on = False
b_on = False
while True:
    # Flip A&B states if buttons have been pressed
    if button_a.was_pressed():
        a_on = not a_on
    if button_b.was_pressed():
        b_on = not b_on
    # If a state is on, turn on the port and
    # a helpful display pixel :-)
    # The AND gate does the summing in hardware
    if a_on:
        display.set_pixel(0, 0, 9)
        pin1.write_digital(1)
    else:
        display.set_pixel(0, 0, 0)
        pin1.write_digital(0)
    if b_on:
        display.set_pixel(4, 0, 9)
        pin2.write_digital(1)
    else:
        display.set_pixel(4, 0, 0)
        pin2.write_digital(0)
    # Let's give it a rest
    sleep(500)
