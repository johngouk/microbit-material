from microbit import *

def setPin(pin_no: int, pinOn: bool):
    pin_no = pin_no % 8  # Make sure we haven't been slipped a dud
    col = pin_no % 4
    row = pin_no // 4
    cols[col].write_digital(1 if pinOn else 0)
    rows[row].write_digital(1 if pinOn else 0)
    display.set_pixel(col, row, 9 if pinOn else 0)

cols = [pin0, pin1, pin2, pin8]
rows = [pin12, pin16]
display.show(Image.HEART)
for i in range(0, len(cols)-1):
    cols[i].write_digital(0)
for j in range(0, len(rows)-1):
    rows[j].write_digital(0)

# Allow experimenter to see the "I'm working!" HEART
sleep(500)
display.clear()

a_on = False
b_on = False
count = -1
while True:
    # Flip A&B states if buttons have been pressed
    if button_a.was_pressed():
        a_on = not a_on
    if button_b.was_pressed():
        b_on = not b_on
    # If a state is on, turn on the port and
    # a helpful display pixel :-)
    # The AND gate does the summing in hardware
    display.clear()
    if a_on:
        count = count+1
        if count > 7:
            count = 0
        setPin(count, True)
        sleep(1000)
        setPin(count, False)
    # Let's give it a rest
    sleep(500)
