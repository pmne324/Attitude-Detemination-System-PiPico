import os
import utime
from machine import UART

uart = UART(0, baudrate = 9600)
utime.sleep(3)
    
def send(data):
    uart.write(data)
    

