def script():    
    try:
        import soco
        def start_dos():
            device = soco.discovery.any_soco()
            while len(str(device)) != 0:
                print("Currently dossing device::  ", device)
                device.stop()
            if len(str(device)) == 0:
                print("Check if the device is up and running on the network")

        device = soco.discovery.any_soco()
        if len(str(device)) != 0:
            print("Discovered device on network", device)
            Dos = input("Do you want to start the test [y/n]?: ")
            if Dos.lower() == "y":
                start_dos()
            elif Dos.lower() == "n":
                exit()  
        if len(str(device)) == 0: 
            print("No devices found on the network, make sure the device is up and running")
    except:
        # I am checking if ctrl + c is being pressed so the script 
        # Can be stopped immediately when you want it to. 
        if KeyboardInterrupt:
            exit_questionmark = input("Do you really want to exit [y/n]?: ")
            print("If you press Ctrl + C again after not exiting, the program will stop.")
            if exit_questionmark.lower() == "y":
                exit()
            elif exit_questionmark.lower() == "n":
                start_dos()

if __name__ == "__main__":
    script()