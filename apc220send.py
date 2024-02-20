import sys
import re
from datetime import datetime
import signal
import serial
import os

from time import sleep

from sys import platform
if platform == "linux" or platform == "linux2":
    print("Running on Linux")
elif platform == "darwin":
    print("Running on OSX")
elif platform == "win32":
    print("Wunning on Windows 32bit")
quit()

def usage(msg=None):
    if (msg):
	    print("ERROR: "+msg+"\n")
    print("""usage: python apc220send.py COMx SPEED 

"COMx" should be the COM port that the APC220 radio is connected to 
(typically COM2, but check this in Device Manager to be sure).

"SPEED" is the baud rate.  It is typically 9600 unless you have set your
APC220 radio to something different.  Only 2400, 4800 and 9600 are allowed.

The message to send is read from standard input
""")
    sys.exit(-1)


	
	
def signal_handler(signal, frame):
        print("Bye!")
        sys.exit(0)			


		
#############################################################################
#                                 Main Program                              #
#############################################################################

# Set up signal-handler so that the script can be exitted easily
signal.signal(signal.SIGINT, signal_handler)

# Check command-line arguments
if (len(sys.argv) != 3):
    usage()

comPort = sys.argv[1]
baudRate = sys.argv[2]

if (not os.name == 'nt'):
    print("Not Running on Windows")


#if (not re.match(r"^COM\d+$",comPort,re.IGNORECASE)):
#    usage("Invalid value for COM port")

if ((baudRate != "2400") and (baudRate != "4800") and (baudRate != "9600")):
    usage("invalid value for baud rate")

ser = serial.Serial(port=comPort,baudrate=baudRate)
ser.setRTS(False)

sleep(0.1)
#print(sys.stdin.read().encode(encoding="ascii", errors="replace"))
print(ser.write(sys.stdin.read().encode(encoding="ascii", errors="replace")))
ser.flush()
sleep(5)		# ser.flush() is supposed to wait until everything is sent, but it doesn't seem to :-(
ser.close()

