from ursina import *
import json
from Data import *


app = Ursina()
window.color = color._20

gold = 0
has_gold_gen = False
gold_gens = 5
gold_gen_price = 10
context_menu = None
cheese_gen_price_2 = 5
rebirths = 0
datajson = "idlePy/Data/idleData.json"
rebirth_price = 100
gold_per_sec = 1 + rebirths
gold_per_click = 1
counter = Text(text=f'<gold>Cheese\n<white>--------\n<azure>{gold}', y=.25, z=-1, scale=2, origin=(0, 0), background=True)

button = Button(text='+', color=color.azure, scale=.125)
button.on_mouse_enter = Func(setattr, button, 'text', 'Fart')
button.on_mouse_exit = Func(setattr, button, 'text', '+')

def button_click():
    if held_keys['left mouse']:
        global gold
        gold += gold_per_click
        counter.text = f'<gold>Cheese\n<white>--------\n<azure>{gold}'
        print('button left clicked')
    elif held_keys['right mouse']:
        show_context_menu()
        print('Button right clicked')

button.on_click = button_click

button_2 = Button(text=f'{gold_gen_price}', cost=gold_gen_price, x=.2, scale=.125, color=color.dark_gray, disabled=True)
button_2.tooltip = Tooltip(f'<gold> cheese Generator 1\n<default>Earn 1 Cheese every second. \nCost {button_2.cost} * 2 per purchase.')

cheese_gen_2 = Button(text=f'{cheese_gen_price_2}', cost=cheese_gen_price_2, x=-.2, scale=.125, color=color.dark_gray, disabled= True)
cheese_gen_2.tooltip = Tooltip(f'<gold> Cheese Generator 2\n<default>Earn 2 Cheese every second. \nCost {cheese_gen_2.cost} * 2 per purchase.')

rebirth_button = Button(text=f'{rebirth_price}', cost=rebirth_price, x=.4, scale=.125, color=color.pink, disabled=True)
rebirth_button.tooltip = Tooltip(f'<blue> Reset\n<default>Rest your progress but gain perm stats. \n {rebirth_price}')

def buy_auto_gold():
    global gold
    global gold_gens
    global has_gold_gen

    if gold >= button_2.cost:
        gold -= button_2.cost
        has_gold_gen = True
        button_2.cost *= 2
        button_2.text = str(button_2.cost)
        counter.text = f'<gold>Cheese\n<white>--------\n<azure>{gold}'
        gold_gens += 1
        invoke(auto_generate_gold, 1, 1)

button_2.on_click = buy_auto_gold

def auto_buy_gold_2():
    global gold
    global gold_gens
    global has_gold_gen

    if gold_gens >= cheese_gen_2.cost:
        gold_gens -= cheese_gen_2.cost
        has_gold_gen = True
        cheese_gen_2.cost *= 2
        cheese_gen_2.text = str(cheese_gen_2.cost)
        counter.text = f'<gold>Cheese\n<white>--------\n<azure>{gold}'
        gold_gens += 1
        invoke(auto_generate_gold, 1, 1)

cheese_gen_2.on_click = auto_buy_gold_2

def buy_rebirth():
    global gold
    global gold_per_sec
    global has_gold_gen
    global rebirths
    global rebirth_price
    global gold_per_click

    if gold >= rebirth_price:
        gold = 0
        rebirths += 1
        button_2.cost = 10
        gold_per_sec = 1 + rebirths
        gold_per_click += 1
        has_gold_gen = False
        rebirth_price *= 2
        rebirth_button.cost = rebirth_price
        rebirths_counter.text = f'<azure>Rebirths <default>: <gold>{rebirths}<azure>\nClicks Per Click <default>: <gold>{gold_per_click}'
        rebirth_button.text = str(rebirth_price)
        counter.text = f'<gold>Cheese\n<white>--------\n<azure>{gold}'
        button_2.text = str(gold_gen_price)

rebirth_button.on_click = buy_rebirth

def auto_generate_gold(value=1, interval=1):
    global gold
    global gold_per_sec

    if has_gold_gen:
        gold += gold_per_sec
        counter.text = f'<gold>Cheese\n<white>--------\n<azure>{gold}'
        button_2.animate_scale(.125 * 1.1, duration=.1)
        button_2.animate_scale(.125, duration=.1, delay=.1)
        invoke(auto_generate_gold, value, delay=interval)

rebirths_counter = Text(text=f'<azure>Rebirths <default>: <gold>{rebirths}<azure>\nClicks Per Click <default>: <gold>{gold_per_click}', position=window.top_left)

def show_context_menu():
    global  context_menu
    if context_menu:
        destroy(context_menu)

    menu_options = ['Option 1', 'Option 2', 'Option 3']
    context_menu = Entity(parent=camera.ui, model='quad', scale=(0.2, 0.3), color=color.gray, position=mouse.position)

    for i, option in enumerate(menu_options):
        btn = Button(text=option, parent=context_menu, scale=(0.9, 0.2), position=(0, 0.3 - i * 0.2))
        btn.on_click = Func(on_menu_option_click, option)

def on_menu_option_click(option):
    print(f'Selected: {option}')
    destroy(context_menu)

def read_json(dataJson):
    with open(dataJson, 'r') as file:
        try:
            data = json.load(file)
            print(json.dumps(data, indent=4))
        except json.JSONDecodeError as e:
            print(f'Error Reading json file: ')

def update():
    global gold
    global rebirths
    global rebirth_price
    global has_gold_gen

    if mouse.right:
        show_context_menu()
        print('mouse right clicked')

    for b in (button_2, rebirth_button):
        if gold >= b.cost:
            b.disabled = False
            b.color = color.green
        else:
            b.disabled = True
            b.color = color.red

    for b in (cheese_gen_2, ):
        if gold_gens >= b.cost:
            b.disabled = False
            b.color = color.green
        else:
            b.disabled = True
            b.color = color.red
app.run()