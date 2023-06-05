import serial,csv, serial.tools.list_ports
from datetime import datetime
import pandas
import matplotlib.animation as animation
import time
import os
import re 


path = os.path.abspath(os.curdir)
now = datetime.now()
name = os.path.join(path,str(now.strftime("%d-%m-%Y-%H:%M:%S")))+".csv"
print(name)