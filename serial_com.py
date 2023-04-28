import serial,csv, serial.tools.list_ports
from datetime import datetime

usb_port_list = serial.tools.list_ports.grep("usb")

usbports = sum(1 for i in usb_port_list)

def usbconn(portname):
    ser = serial.Serial(portname)

def listconn():

    port_list = serial.tools.list_ports.comports()

    for info in port_list:
        print(info)

    num = 1
    ports = sum(1 for i in port_list)

    if ports > 1:
        print("Choose device to connect to:")
        for info in port_list:
            print(num, end = '')
            print(info)
            num = num + 1
            print("")
        pnum = input("")
        #number inputer
    



if usbports ==0:
    usbconn(usb_port_list[0])
else:
    listconn()

# use exeption handlers

# once connection has been established

def reader():
    samples = 100
    line = 0
    while line <= samples:
        global datalist
        datalist = []
        dataline = ser.readline()
        print(dataline)
        datalist.append(dataline)
        line = line +1

now = datetime.now()

with open(now.strftime("%d/%m/%Y %H:%M:%S"), 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(datalist)

print("Data collection complete!")
