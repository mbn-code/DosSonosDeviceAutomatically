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
            if device == None:
                print("No device found on the network")
                print("Exiting the test . .")
                import os
                os._exit()
            else:
                print("Discovered device on network", device)
                Dos = input("Do you want to start the test [y/n]?: ")
                if Dos.lower() == "y":
                    start_dos()
                elif Dos.lower() == "n":
                    print("exiting now. .")
                    exit()
    except:
        # I am checking if ctrl + c is being pressed so the script 
        # Can be stopped immediately when you want it to. 
        if KeyboardInterrupt:
            exit()

if __name__ == "__main__":
    script()