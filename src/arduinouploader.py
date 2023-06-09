import subprocess
import os

def upload_arduino_code(sketch_file, board_type, port):
    avrdude_cmd = f'avrdude -v -patmega328p -carduino -P{port} -b115200 -D -Uflash:w:{sketch_file}:i'
    subprocess.call(avrdude_cmd, shell=True)

# Usage example
path = os.path.abspath(os.curdir)
sketch_file = os.path.join(path,"src/ArduinoDE.ino.hex")
board_type = 'arduino:avr:uno'  # Modify this according to your board
port = '/dev/tty.usbmodem1101'  # Modify this according to your system

upload_arduino_code(sketch_file, board_type, port)
