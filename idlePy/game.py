from ursina import *

app = Ursina()
window.color = color._20

title = Text('<azure>Idle<gold>.py')
title.position = (0, 0.5)

button_container = Entity(model='quad', scale=(2, 4), color=color.dark_gray, position=(0.5,-1))

button1 = Button(text='<green>Start Game', scale=(0.5, 0.1), parent=button_container, position=(0, 0.2))
button2 = Button(text='<white>Settings', scale=(0.5, 0.1), parent=button_container, position=(0, 0))
button3 = Button(text='<red>Quit Game', scale=(0.5, 0.1), parent=button_container, position=(0, -0.2))

app.run()