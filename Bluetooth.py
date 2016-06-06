import os
import bluetooth, time

#Time spent looking for local Bluetooth Devices
search_time = 10

# You can hardcode the desired device ID here as a string to skip the discovery stage
addr = None

print("Enable Bluetooth module with the follwing command: sudo bb-wl18xx-bluetooth")
print("Make sure your desired Bluetooth-capable device is turned on and discoverable.")

#If the address has not been hardcoded above then run the following script
if addr == None:
    try:
        input("When you are ready to begin, press the Enter key to continue...")
    except SyntaxError:
        pass

    os.system('clear')
# A simple menu to select from a stored text file or scan new devices
    ans  = input("Select your option from the menu: \n1. Scan for new Bluetooth Devices\n2. Select Bluetooth device from menu\n")
    if ans == 1:

        os.system('clear')
        print("Searching for Bluetooth devices...")

        nearby_devices = bluetooth.discover_devices(duration=search_time, flush_cache=True, lookup_names=True)
# If no devices have been found loop the scan to search again
        while len(nearby_devices) <= 0:
                input("No Devices Found, Make sure you Bluetooth Device is turned on \nPress Enter to Scan again....")
                os.system('clear')
                print("Scanning for Bluetooth Devices...")
                nearby_devices = bluetooth.discover_devices(duration=search_time, flush_cache=True, lookup_names=True)



        os.system('clear')
# If devices have been found run the follwing
        if len(nearby_devices) > 0:
            print("Found %d devices!" % len(nearby_devices))


            i = 0
        # Print out a list of all the discovered Bluetooth Devices
            for addr, name in nearby_devices:
                print("%s. %s - %s" % (i, addr, name))
                i =+ 1

            device_num = input("Please specify the number of the device you want to track: ")


            addr, name = nearby_devices[device_num][0], nearby_devices[device_num][1]
# Add the selected Bluetooth device to the next line in the text file
        f = open( 'file.txt', 'a' )
        f.write( addr + ',' + name + '\n' )
        f.close()


    if ans == 2:
        os.system('clear')
# Read the text file for a list of saved Bluetooth Devices
        f = open( 'file.txt', 'r')
        line = f.readline()

        z = 0
# Print the list using this loop, incrementing the value by line
        while line:
            z += 1
            print z , ". " , line
            line = f.readline()
        f.close()

# Prompt the user to enter the device number from the list
        f = open( 'file.txt', 'r')
        opt = input("")

        x = 0
# Read the line selected and extract the address of the device by splitting the line
        while x < opt:
            readit = f.readline().split(",")[0]
            x += 1
            addr = readit
        f.close()

os.system('clear')
print("Scanning for device %s." % (addr))
print("Initializing Scan...")



while True:

    state = bluetooth.lookup_name(addr, timeout=20)
    services = bluetooth.find_service(address=addr)

    if state == None and services == []:
        print("No device detected in range...")

    else:
        print("Device detected!")


    time.sleep(1)
    
