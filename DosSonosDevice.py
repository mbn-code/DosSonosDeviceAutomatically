def script():
    try:
        import soco

        def start_dos():
            device = soco.discovery.any_soco()
            while len(str(device)) != 0:
                print("Currently dossing device::  ", device)
                device.stop()
            else:
                print("Check if the device is up and running on the network")

        device = soco.discovery.any_soco()
        if len(str(device)) != 0:
            print("Discovered device on network", device)
            Dos = input("Do you want to start the test [y/n]?: ")
            if Dos.lower() == "y":
                start_dos()
            elif Dos.lower() == "n":
                exit()  
        else: 
            print("No devices found on the network")
    except:
        if KeyboardInterrupt:
            exit_questionmark = input("Do you really want to exit [y/n]?: ")
            print("If you press Ctrl + C again after not exiting, the program will stop.")
            if exit_questionmark.lower() == "y":
                exit()
            elif exit_questionmark.lower() == "n":
                start_dos()

if __name__ == "__main__":
    script()