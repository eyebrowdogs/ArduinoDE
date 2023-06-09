import serial,csv, serial.tools.list_ports
from datetime import datetime
#import pandas
#import matplotlib.animation as animation
import time
import os
import re
import sys


def usbconn(portname):
    global ser
    try:
        ser = serial.Serial(portname,9600,parity="N",stopbits=1)
        ser.reset_input_buffer()
        print("✅ Succesful connection at port " + portname)
        print("Is port " + portname + " open?: " + str(ser.is_open))
        print("Looking for Arduino DE...")
        ser.reset_input_buffer()
        ser.reset_output_buffer()
        for i in range(4):
            ser.write('a'.encode('utf-8'))
            time.sleep(1)
            response = ser.readline()
            dresponse = response.decode('utf-8')
            if dresponse == 'a\r\n':
                print("✅ ArduinoDE found")
                ser.reset_input_buffer()
                ser.reset_output_buffer()
                return True
            ser.reset_output_buffer()
            ser.reset_input_buffer()       
            
        print("❌ Device not running ArduinoDE, upbload .ino file to board an try again")    
        return False
        
    except Exception as ex:
        print(str(ex))
        print("❌ Failed connection at at port " + portname)
        return False

    

def waiter2():
    print("Waiting...")
    try:

        buff = ser.readline()
        #print(buff)
        dbuff = buff.decode('utf-8')

        if dbuff == "begin\r\n":
            print("✅ Calling reader from waiter...")
            reader()

        ser.reset_input_buffer()
    except Exception:
        print("Device disconnected")
        sys.exit()


 

def reader():
    data = []
    print("Beginning reader") 
    reading = True
    start = time.monotonic() 
    while reading == True:
         
        line = ser.readline()
        #print(line)
        dline = line.decode('utf-8')
        print(dline)
        if dline == "end\r\n":
            end = time.monotonic()
            print("Ended reader")
            print(f"Elapsed time:  {end - start:0.8f} ")
            #print(data) 
            # path = os.path.abspath(os.curdir)
            # now = datetime.now()

            # name = os.path.join(path,"CSVs",str(now.strftime("%d-%m-%Y-%H:%M:%S")))+".csv"
            # #name.replace(" ","")
            # #name = "csv.csv"
            # with open(name, "w",newline="\n",) as f:
            #     print("Writing csv..")
            #     writer = csv.writer(f)
            #     writer.writerows(data)
            #     print('✅ csv written successfully')
            csvwriter(data)
            reading  = False
                # data = []
            return data #later use for plotting
        else:
            noends = dline[0:][:-2]
            dupes = noends.split(",")
            data.append(dupes)
            reading = True

def csvwriter(data):
        path = os.path.abspath(os.curdir)
        now = datetime.now()
        name = os.path.join(path,"CSVs",str(now.strftime("%d-%m-%Y-%H:%M:%S")))+".csv"
        with open(name, "w",newline="\n",) as f:
            print("Writing csv..")
            writer = csv.writer(f)
            writer.writerows(data)
            print('✅ csv written successfully')
            #reading  = False
            data = []

def eachwriter(data):
    #save csv on each data point, append each point dont rewrite whole array into file
    pass      
        
def manualconnector(port):

    obj = usbconn(port)

    if obj is True:
        while True:
            waiter2()
    else:
        print("Failed to wait")


def autoconnect(port_list):

    for name in port_list:
        try:
            usb = re.search("usb", str(name))
        except Exception:
            print("❌ No USB device found at " + str(name))
        if usb:
            print("✅ USB device found at " + str(name) + " attempting connection...")
            print("calling usbconn")
            obj = usbconn(name[0])
            if obj is True:
                while True:
                    waiter2()
            else:
                print("❌ Failed to wait")
        elif usb == None:
            print("❌ No USB device found at " + str(name))



port_list = serial.tools.list_ports.comports()

autoconnect(port_list)

#uncomment to manually connect to the port

#manualconnector("port to be used") 




