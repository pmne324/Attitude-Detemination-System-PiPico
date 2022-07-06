from machine import UART, Pin
import utime
import time

TX = Pin(4)
RX = Pin(5)
BR = 9600
BUS = 1

gps_port = UART(BUS, baudrate=BR, tx=TX, rx=RX)
print(gps_port)


TIMEOUT = False
FIX_STATUS = False

latitude = ""
longitude = ""
altitude = ""
satellites = ""
GPStime = ""

def getGPS(gpsModule):
    global FIX_STATUS, TIMEOUT, latitude, longitude, altitude, satellites, GPStime
    
    timeout = time.time() + 8 
    while True:
        gpsModule.readline()
        buff = str(gpsModule.readline())
        parts = buff.split(',')
    
        if (parts[0] == "b'$GPGGA" and len(parts) == 15):
            if(parts[1] and parts[2] and parts[3] and parts[4] and parts[5] and parts[6] and parts[7]):
                print(buff)
                
                latitude = convertToDegree(parts[2])
                if (parts[3] == 'S'):
                    latitude = -latitude
                longitude = convertToDegree(parts[4])
                if (parts[5] == 'W'):
                    longitude = -longitude
                satellites = parts[7]
                GPStime = parts[1][0:2] + ":" + parts[1][2:4] + ":" + parts[1][4:6]
                altitude = parts[9] + parts[10]
                FIX_STATUS = True
                break
            
        if (time.time() > timeout):
            TIMEOUT = True
            break
        utime.sleep_ms(500)
        

def convertToDegree(RawDegrees):

    RawAsFloat = float(RawDegrees)
    firstdigits = int(RawAsFloat/100) 
    nexttwodigits = RawAsFloat - float(firstdigits*100) 
    
    Converted = float(firstdigits + nexttwodigits/60.0)
    Converted = '{0:.6f}'.format(Converted) 
    return str(Converted)
'''
while True:
    
    getGPS(gps_port)

    if(FIX_STATUS == True):
        print("Printing GPS data...")
        print(" ")
        print("Latitude: "+latitude)
        print("Longitude: "+longitude)
        print("Altitude: "+altitude)
        print("Satellites: " +satellites)
        print("Time: "+GPStime)
        print("----------------------")
        
        FIX_STATUS = False
        
    if(TIMEOUT == True):
        print("No GPS data is found.")
        TIMEOUT = False
'''        
def GPS():
    global FIX_STATUS, TIMEOUT, latitude, longitude, altitude, satellites, GPStime

    getGPS(gps_port)

    if(FIX_STATUS == True):
        lat = latitude
        long = longitude
        alt = altitude
        satNo = satellites
        gpsTime = GPStime
        error = False
        FIX_STATUS = False
        
    if(TIMEOUT == True):
        lat = latitude
        long = longitude
        alt = altitude
        satNo = satellites
        gpsTime = GPStime        
        error = True
        TIMEOUT = False
        
    return lat, long, alt, satNo, gpsTime, error
        
    
