################################################################################
# apc220test2.py
# MDeegan, 20240220
# python code to test the use of serial ports on Windows, Linux, Mac
################################################################################

import sys
import platform
import glob
import serial
from os import system, name


################################################################################
# start definition  of the serial_ports method
# Lists serial port names
#    :raises EnvironmentError:
#     On unsupported or unknown platforms
#    :returns:
#     A list of the serial ports available on the system
#

def serial_ports():
    
    # if we are running on Windows
    if sys.platform.startswith('win'):
        print("Running on Windows")
        print("And your serial ports are:...")
        # enumerate the ports based on COM1 .. COM256
        ports = ['COM%s' % (i + 1) for i in range(256)]

    # or, if we are running on Linux
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        print("Running on Linux")
        print("And your serial ports are:...")
        # enumerate the ports based on /dev/tty????
        ports = glob.glob('/dev/tty[A-Za-z]*')

    # or, if we are running on Mac
    elif sys.platform.startswith('darwin'):
    	# print some stats relating to the macOS etc.
        print("Running on Mac", platform.system(),platform.machine(), platform.platform())
        # platform.uname()
        # platform.version()
        # platform.mac_ver()
        print("And your serial ports are:...")
        # enumerate the ports based on /dev/tty.????
        ports = glob.glob('/dev/tty.*')
        
    # if we are not running on Windows, Linux or Mac then raise an exception
    else:
        raise EnvironmentError('Unsupported platform')

    # declare result as an array to be populated with valid ports
    result = []
    # for each port in the array of ports enumerated above
    for port in ports:
        try:
            s = serial.Serial(port)
            # if the attempt to create the port does not throw an exception
            # then close the port
            s.close()
            # and add the port to the result array
            result.append(port)
        except (OSError, serial.SerialException):
            # ignore the exception
            pass
    # return the array containing the ports that could be successfully created
    return result
# End definition of the serial_ports method
################################################################################

################################################################################
# start definition of clear() method
def clear():
 
    # for windows
    if name == 'nt':
        # use the system call 'cls'
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        # use the system call 'clear'
        _ = system('clear')
 
# end definition of clear() method
################################################################################


################################################################################
# start definition of the main method

# call the clear method that we defined above
clear()
print("Hello Mark")

# if this method is the main method
if __name__ == '__main__':
    # then print the result returned by calling the serial_ports() method
    print(serial_ports())

# and we're done
# end definition of the main method
################################################################################
