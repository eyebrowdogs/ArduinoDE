# ArduinoDE

- Serial comm-based python script and Arduino code. 
- Button controlled data collection triggering. Press once to start, green LED will light up and data will be sent. Press again to stop, red LED will light up signaling no data is being sent.
- Python script saves a csv file after data RX is complete. Look in the script's "CSVs" directory for timestamped files.
- docs folder contains a SolidWorks assembly of the pictured enclosure, STLs and .sldprt files.


PASCO capstone-like DIY spring plotter made for **PhD. Pablo Enrique Moreira** 
by **Paul Navarro Amezcua**
at *Universidad Ánahuac Querétaro.* 
    Métodos Cuantitativos Dept.


![](https://raw.githubusercontent.com/eyebrowdogs/ArduinoDE/main/docs/ensamble%203.PNG)

(Enclosure, status LEDs etc are optional, a sensor of any type can be used paired to the Arduino board in any wiring configuration. Modify the Arduino code accordingly)

| Components  | Notes |
| ------------- | ------------- |
| Arduino UNO  | (avr board) |
| Red 5mm LED  | 220 Ohm resitor in series  |
| Green 5mm LED | 220 Ohm resitor in series  |
| 2/4 pin 6mm Push Button | 10k Ohm pull-down resitor in series  |
| Mini 170 Breadboard | (Or solder averything together)  |
| 7 M3x10mm Screws  | (I used wood screws) |
