import os
import bluetooth, time

search_time = 10

# You can hardcode the desired device ID here as a string to skip the discovery stage
addr = None
print("Enable Bluetooth module with the follwing command: sudo bb-wl18xx-bluetooth")
print("Make sure your desired Bluetooth-capable device is turned on and discoverable.")

if addr == None:
    try:
        input("When you are ready to begin, press the Enter key to continue...")
    except SyntaxError:
        pass

    os.system('clear')
    ans  = input("Select your option from the menu: \n1. Scan for new Bluetooth Devices\n2. Select Bluetooth device from menu\n")
    if ans == 1:

        os.system('clear')
        print("Searching for Bluetooth devices...")

        nearby_devices = bluetooth.discover_devices(duration=search_time, flush_cache=True, lookup_names=True)

        while len(nearby_devices) <= 0:
                input("No Devices Found, Make sure you Bluetooth Device is turned on \nPress Enter to Scan again....")
                os.system('clear')
                print("Scanning for Bluetooth Devices...")
                nearby_devices = bluetooth.discover_devices(duration=search_time, flush_cache=True, lookup_names=True)



        os.system('clear')
        if len(nearby_devices) > 0:
            print("Found %d devices!" % len(nearby_devices))


        i = 0 # Just an incrementer for labeling the list entries
        # Print out a list of all the discovered Bluetooth Devices
        for addr, name in nearby_devices:
            print("%s. %s - %s" % (i, addr, name))
            i =+ 1

        device_num = input("Please specify the number of the device you want to track: ")

        # extract out the useful info on the desired device for use later
        addr, name = nearby_devices[device_num][0], nearby_devices[device_num][1]

        f = open( 'file.txt', 'a' )
        f.write( addr + ',' + name + '\n' )
        f.close()


    if ans == 2:
        os.system('clear')

        f = open( 'file.txt', 'r')
        line = f.readline()

        z = 0

        while line:
            z += 1
            print z , ". " , line
            line = f.readline()
        f.close()

        f = open( 'file.txt', 'r')
        opt = input("")

        x = 0

        while x < opt:
         readit = f.readline().split(",")[0]
         x += 1
        addr = readit
        f.close()

os.system('clear')
print("Scanning for device %s." % (addr))
print("Initializing Scan...")


while True:
    # Try to gather information from the desired device.
    # We're using two different metrics (readable name and data services)
    # to reduce false negatives.
    state = bluetooth.lookup_name(addr, timeout=20)
    services = bluetooth.find_service(address=addr)

    if state == None and services == []:
        print("No device detected in range...")

    else:
        print("Device detected!")

    # Arbitrary wait time
    time.sleep(1)
