import serial,csv, serial.tools.list_ports
from datetime import datetime
import pandas
import matplotlib.animation as animation
import time
import os



def usbconn(portname):
    global ser
    try:
        ser = serial.Serial(portname,9600,parity="N",stopbits=1)
        ser.reset_input_buffer()
        print("succesful connection at port " + portname)
        print(ser.is_open)
        return True
    except Exception:
        print("Failed connection at at port " + portname)
        return False

port_list = serial.tools.list_ports.comports()
data = []

#fix waiter


""" def waiter():
    robert = True
    while robert == True:
        print("Waiting for cue...")
        cue = ser.readline()
        if cue == "begin":
            robert = False
            reader()
        ser.reset_input_buffer()
        time.sleep(3) """
    

def waiter2():
    print("Waiting...")
    buff = ser.read_until()
    print(buff)
    dbuff = buff.decode('utf-8')

    if dbuff == "begin\r\n":
        print("calling reader from begin...")
        reader()

    ser.reset_input_buffer()
    ser.flush()
    time.sleep(3)        
    



def reader():
    print("begin reader") 
    reading = True
    while reading == True:  
        line = ser.read_until()
        print(line)
        dline = line.decode('utf-8')
        print(dline)
        if dline == "end\r\n":
            print("ended reader")
            #path = os.path.abspath(os.curdir)
            #now = datetime.now()

            #name = os.path.join(path,str(now.strftime("%d/%m/%Y %H:%M:%S")))+".csv"
            #name.replace(" ","")
            name = "csv.csv"
            with open(name, "w",newline="") as f:
                print("writing csv..")
                writer = csv.writer(f)
                writer.writerows(data)
                print('csv written successfully')
                reading  = False
                data = []
            return 
        else:
            data.append(dline)
            reading = True
        
""" # use exeption handlers
for i in port_list:
    if usbconn(i.device) == True:
        waiter() """


obj = usbconn("/dev/tty.usbmodem1101")

if obj is True:
    while True:
        waiter2()
else:
    print("Failed to wait")
