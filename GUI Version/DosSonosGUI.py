
# File for GUI version code.

from tkinter import *
import soco


root = Tk()
root.title("Dos sonos GUI")
root.geometry("600x800")

device = soco.discovery.any_soco()

def start_dos():
    while len(str(device)) != 0:
        if device == None:
            print("No device found on network")
            print("Exiting test. .")
            import os
            os._exit()
    else:
        print("Currently dossing device: " + str(device) + " :")
    if len(str(device)) == 0:
        print("Check if the device is up and running on the network")

button_start = Button(root, text="start dos attack", height=1, width=20, bg="grey", command=start_dos()).pack()

button_exit = Button(root, text="EXIT ", height=1, width=20, bg="grey", command=exit).pack()

root.mainloop()