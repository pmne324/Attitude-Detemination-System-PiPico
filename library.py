"""
MPU6050 Library for register on I2C bus
By : Porya M. Nilaore
"""
import os
from machine import I2C
from utime import sleep_ms

i2c_err_str = "Module could not communicate with module at address 0x{:02X}, check wiring"

'''class I2CBase:
    def writeto_mem(self, addr, memaddr, buf, *, addrsize=8):
        raise NotImplementedError("writeto_mem")

    def readfrom_mem(self, addr, memaddr, nbytes, *, addrsize=8):
        raise NotImplementedError("readfrom_mem")

    def write8(self, addr, buf, stop=True):
        raise NotImplementedError("write")

    def read16(self, addr, nbytes, stop=True):
        raise NotImplementedError("read")

    def __init__(self, bus=None, freq=None, sda=None, scl=None):
        raise NotImplementedError("__init__")
'''
class I2CUnifiedMachine:
    def __init__(self, bus=None, freq=None, sda=None, scl=None):
        '''if bus is None:
            bus = 0
        if freq is not None and sda is not None and scl is not None:
            print("Using supplied freq, sda and scl to create machine I2C")
            self.i2c = I2C(bus, freq=freq, sda=sda, scl=scl)
        else:'''
        self.i2c = I2C(bus)
        print(self.i2c)
        self.writeto_mem = self.i2c.writeto_mem
        self.readfrom_mem = self.i2c.readfrom_mem

    def write8(self, addr, reg, data):
        if reg is None:
            self.i2c.writeto(addr, data)
        else:
            self.i2c.writeto(addr, reg + data)
            
    def read16(self, addr, reg):
        self.i2c.writeto(addr, reg, False)
        return self.i2c.readfrom(addr, 2)

def create_unified_i2c(bus=None, freq=None, sda=None, scl=None):
    i2c = I2CUnifiedMachine(bus=bus, freq=freq, sda=sda, scl=scl)
    print(i2c)
    return i2c

