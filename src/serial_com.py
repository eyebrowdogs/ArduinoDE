import serial,csv, serial.tools.list_ports
from datetime import datetime
import time
import os
import re
import sys
from arduinouploader import *
import logging
import json



class NoUsbConnectedError(Exception):
    "No USB devices found in ports"
    pass

if len(sys.argv)>=2:
    configPath = str(sys.argv[1])
else:   configPath = "src/config.json"

pathj = os.path.abspath(os.curdir)
namej = os.path.join(pathj,configPath)

try:
    with open (namej, 'r') as f:
        configD = json.load(f)
        print(configD)
except Exception:
    print("❌ Failed to read configuration file, check for config.json or provide a valid configuration file")
    print("Eg: serial_com.py myconfig.json")


# default config
    filesPathj = None
    prefixj = None
    sufixj = None
    timestampFj = "%d-%m-%Y-%H:%M:%S"
    baudratej = None
    portj = None
    CAj = False
    livePlotsj = False

try:
    filesPathj = configD['filesPath'] # full path 
    prefixj = configD['prefix']
    sufixj = configD['sufix']
    timestampFj = configD['timestampF']
    print(timestampFj)
    baudratej = configD['baudRate']
    portj = configD['port']
    print(portj)
    CAj = configD['CA']
    livePlotsj = configD['livePlots']
    #print(configD)

except Exception as e:
    print(str(e))
    print('❌missing keys for config.json')


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
        for _ in range(4):
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
            
        print("❌ Device not running ArduinoDE, upload .ino file to board an try again")
        print("Run arduinouploader.py to upload")    
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
            if CAj is not False:
                CAreader()
                return
            else:
                reader()
                return

        ser.reset_input_buffer()
    except Exception as e:
        print(str(e))
        print("❌ Device disconnected")
        sys.exit()

if CAj is not False:
    def CAreader(): 
        name = namer()
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
                reading  = False
            else:
                noends = dline[0:][:-2]
                dupes = noends.split(",")
                try:
                    with open(name, "a",newline="\n",) as f:
                        #print("Writing csv..")
                        f.write(dupes)
                        #print('✅ csv written successfully')
                        #reading  = False
                except Exception:
                    print("❌ Failed to open file, check path:")
                    print(str(name))
                reading = True

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
            csvwriter(data)
            reading  = False
                # data = []
            #return data #later use for plotting
        else:
            noends = dline[0:][:-2]
            dupes = noends.split(",")
            data.append(dupes)
            reading = True

def namer():
    #global timestampFj
    # if timestampFj is None:
    #     timestampFj = "%d-%m-%Y-%H:%M:%S"
    if filesPathj is None: #writes on current path
        path = os.path.abspath(os.curdir)
        now = datetime.now()
        name = os.path.join(path,"CSVs",str(now.strftime(timestampFj)))+".csv"
        return name
    else: # writes on config key path
        name = os.path.join(filesPathj,str(now.strftime(timestampFj)))+".csv"
        return name

def csvwriter(data):
        name = namer()
        try:
            with open(name, "w",newline="\n",) as f:
                print("Writing csv..")
                writer = csv.writer(f)
                writer.writerows(data)
                print('✅ csv written successfully')
                #reading  = False
                data = []
        except Exception:
            print("❌ Failed to open file, check path:")
            print(str(name))
   
        
def manualconnector(port):

    obj = usbconn(port)

    if obj is True:
        while True:
            waiter2()
    else:
        print("❌ Invalid port")


def autoconnect(port_list):

    for name in port_list:
        try:
            usb = re.search("usb", str(name))
        except Exception:
            pass
        if usb:
            print("✅ USB device found at " + str(name) + " attempting connection...")
            print("calling usbconn")
            print(name[0])
            return name[0]
            # obj = usbconn(name[0])
            # if obj is True:
            #     while True:
            #         waiter2()
            # else:
            #     print("❌ Failed to wait")
        elif usb == None:
            print("❌ No USB device found at " + str(name))
            #maybe raise exeception?
    raise NoUsbConnectedError

def connector(usbDev):

    if usbconn(usbDev):
        while True:
            waiter2()
    else: 
        print("flashing Arduino")
        upload_arduino_code(usbDev)
        connector()


port_list = serial.tools.list_ports.comports()

#usbDev = autoconnect(port_list)
if portj is None:
    try:
        usbDev = autoconnect(port_list)
        connector(usbDev)
    except Exception as e:
        print("❌ No usb device is detected in port list")
        #print(type(e))
else:
    manualconnector(portj) 

