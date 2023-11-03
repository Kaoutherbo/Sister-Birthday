from turtle import *
import colorsys
import random
import time

bgcolor('black')
tracer(600)


def draw():
    h = 0
    for i in range(60):
        # Calculate hues for deep purple (around 0.8) and yellow (around 0.16)
        purple_hue = 0.8
        yellow_hue = 0.16
        
        # Interpolate between deep purple and yellow
        hue = purple_hue + h * (yellow_hue - purple_hue)
        # Ensure the hue is within the valid range (0 to 1)
        hue = hue % 1.0
        
        c = colorsys.hsv_to_rgb(hue, 1, 1)
        h += 0.1
        
        up()
        goto(0, 0)
        down()
        color('black')
        fillcolor(c)
        begin_fill()
        rt(98)
        circle(i, 12)
        fd(100)
        fd(i)
        lt(29)
        for j in range(40):
            fd(i)
            circle(j, 290, steps=2)
        end_fill()

def draw_text(text, x, y, size=40):
    up()
    goto(x, y)
    down()
    color("white")
    write(text, font=("Arial", size, "bold"))
    
draw()
update()

emojis = ["🎈", "❤️", "🎁", "🍰", "🎉", "😄", "😊", "😍","🎈", "❤️", "🎁", "🍰", "🎉", "😄", "😊", "😍","🎈", "❤️", "🎁", "🍰", "🎉", "😄", "😊", "😍","🎈", "❤️", "🎁", "🍰", "🎉", "😄", "😊", "😍"]
emojis_positions = []

for _ in range(100):
    x = random.randint(-650, 600)
    y = random.randint(70, 400)
    emojis_positions.append((x, y))

for _ in range(80):
    clear()
    
    for i in range(len(emojis_positions)):
        x, y = emojis_positions[i]
        draw_text(random.choice(emojis), x, y, size=20)
        emojis_positions[i] = (x, y - 8)
    update()

    

delay_time = 2  # Delay time in seconds

# Delay before drawing "HAPPY BIRTHDAY"
draw_text("HAPPY BIRTHDAY🎂", -240, 40, size=40)
draw_text("Souad😘", -90, -80, size=40)
update()
time.sleep(delay_time)
clear()
draw()
update()
clear()
draw_text("Wish you all the best🎂", -250, 40, size=40)
draw_text("My lovely sister😘", -200, -80, size=40)
update()
time.sleep(delay_time)

done()
