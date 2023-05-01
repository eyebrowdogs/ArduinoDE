import serial,csv, serial.tools.list_ports
from datetime import datetime
import pandas
import matplotlib.animation as animation
import time

def usbconn(portname):
    global ser
    try:
        ser = serial.Serial(portname,9600,parity="N")
        print("succesful connection at port " + portname)
        print(ser.is_open)
        return True
    except:
        ("Failed connection at at port " + portname)

port_list = serial.tools.list_ports.comports()


#fix waiter


def waiter():
    robert = True
    while robert == True:
        print("Waiting for cue...")
        cue = ser.readline()
        if cue == "begin":
            robert = False
            reader()
        ser.reset_input_buffer()
        time.sleep(3)
    

def reader():
    data = []
    line = ser.readline
    if line == "end":
        now = datetime.now()
        with open(now.strftime("%d/%m/%Y %H:%M:%S"), 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(data)
        return 
    else:
        data.append(line)
        
""" # use exeption handlers
for i in port_list:
    if usbconn(i.device) == True:
        waiter() """


usbconn("/dev/tty.usbmodem101")

waiter()

