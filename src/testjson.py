import json
import os

path = os.path.abspath(os.curdir)
name = os.path.join(path,"src/config.json")

with open (name, 'r') as f:
    configD = json.load(f)
    print (configD)

try:
    filesPathj = configD['filesPath'] # full path 
    prefixj = configD['prefix']
    sufixj = configD['sufix']
    timestampFj = configD['timestampF']
    baudratej = configD['baudrate']
    portj = configD['port']
    continuousApppendj = configD['continuousApppend']
    livePlotsj = configD['livePlots']

except Exception:
    print('missing keys for config.json')