import keyboard

# def print_pressed_keys(e):
#     print(e, e.event_type, e.name)

# keyboard.hook(print_pressed_keys)
# keyboard.wait()


translate = {
     'down':' нажал на клавишу ',
     'up':' отпустил клавишу '
 }


def print_pressed_keys(e):
    print(
        'Пользователь {}{}'.format(translate[e.event_type], e.name)
        )


keyboard.hook(print_pressed_keys)
keyboard.wait()