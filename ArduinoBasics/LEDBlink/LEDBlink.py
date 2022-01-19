#Ahmad Osman
#2022-01-18
#Programs used to run code: Arduino 1.8.19, Python GUI (IDLE) 2.7.12
#Packages & toolkits may differ depending on python version 3.4+
#Refer @ https://www.python.org/downloads/ to ensure correct version is installed
"""
The following program is a simple arduino set up. The set up uses a standard python firmata import
to transfer the python language to the adruino code. The code used causes an LED attachment to blink
between consecutive sleep time intervels.
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
board = pyfirmata.Arduino('COM7') #port connection

it = pyfirmata.util.Iterator(board) #set an iterator to board
it.start() # start the iterator

board.digital[10].mode = pyfirmata.INPUT #sets up pin number 10 as the input port
#-----------------------------------------------------------------------------------------------------
"""
The loop below will access the board and read the import from port number 10. After reading the port 
value, it will check if sw is True, thus proceding to writing a specific value 1. 1 means the Led
is true and will turn on, where as 0 means otherwise.
"""
while True:
    sw = board.digital[10].read()
    if sw is True:
        board.digital[13].write(1)
    else:
        board.digital[13].write(0)
    time.sleep(0.0001) #sleep timer to produce consecutive interval blinking in LED

