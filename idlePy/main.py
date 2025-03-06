from ursina import *

app = Ursina()
window.color = color._20

gold = 0
has_gold_gen = False
gold_gens = 0
gold_gen_price = 10
rebirths = 0
rebirth_price = 100
gold_per_sec = 1 + rebirths
gold_per_click = 1
counter = Text(text=f'<gold>Cheese\n<white>--------\n<azure>{gold}', y=.25, z=-1, scale=2, origin=(0, 0), background=True)
button = Button(text='+', color=color.azure, scale=.125)


def button_click():
    global gold
    gold += gold_per_click
    counter.text = f'<gold>Cheese\n<white>--------\n<azure>{gold}'

button.on_click = button_click

button_2 = Button(text=f'{gold_gen_price}', cost=gold_gen_price, x=.2, scale=.125, color=color.dark_gray, disabled=True)
button_2.tooltip = Tooltip(
    f'<gold> Gold Generator\n<default>Earn 1 gold every second. \nCost {button_2.cost} * 2 per purchase.')

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



def update():
    global gold
    global rebirths
    global rebirth_price
    global has_gold_gen

    for b in (button_2, rebirth_button):
        if gold >= b.cost:
            b.disabled = False
            b.color = color.green
        else:
            b.disabled = True
            b.color = color.red

        if gold_gens == 5:
            rebirth_button.text = str(rebirth_price)
        else:
            rebirth_button.disabled = True
            rebirth_button.text = 'locked'

app.run()