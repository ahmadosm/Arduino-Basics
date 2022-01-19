#Ahmad Osman
#2022-01-18
#Programs used to run code: Arduino 1.8.19, Python GUI (IDLE) 2.7.12
#Packages & toolkits may differ depending on python version 3.4+
#Refer @ https://www.python.org/downloads/ to ensure correct version is installed
"""
The following program allows the user to adjust the frequency of the LED blinking
using a potentiometer ranging from 0-1 value.
The code calculates the delay as the analog_value + 0.01 to avoid having delay equal to zero. 
Otherwise,  it is common to get an analog_value of None during the first few iterations. 
To avoid getting an  error when running the program, you use a conditional in line 13 to test whether 
analog_value is None. Then you control the period of the blinking LED.
"""
#-----------------------------------------------------------------------------------------------------
"""
The following code implements all utilities and toolkits needed for the code.
The program under 'try' check if the toolkits are installed and if so continues.
Otherwise in 'except', the toolkits will be installed and the process will continue
"""

try:
    import pyfirmata, time
    from pyfirmata import Arduino, util
   # from tkinter import messagebox
except:
    import pip
    pip.main(['install','pyfirmata'])
    import pyfirmata, time
    from pyfirmata import Arduino, util
#-----------------------------------------------------------------------------------------------------
"""
The code below is a simple setup to access the arduino board. This consists of connecting the board
to the respective port which is set up on the desktop hardware.
"""

board = pyfirmata.Arduino('COM7')
it = pyfirmata.util.Iterator(board)
it.start()

analog_input = board.get_pin('a:0:i') # set up an analog input to specified pin range
led = board.get_pin('d:13:o') # access the pin to which the LED is connected
#-----------------------------------------------------------------------------------------------------


while True:
    analog_value = analog_input.read() #read the current state of the analog pin range values
    if analog_value is not None: #Check if any values are assigned to analog input

        delay = analog_value + 0.01 #If no values, increase delay by interval

        led.write(1) #set Led light to true thus turning on
        time.sleep(delay)

        led.write(0) #Turn LED off
        time.sleep(delay)
    else:
        time.sleep(0.1) #If analog input DNE, sleep program.
