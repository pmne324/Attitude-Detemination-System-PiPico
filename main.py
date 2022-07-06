from imu import IMU
from library import sleep_ms # Cross-platform compatible sleep function
from gps import GPS
import uart
from machine import UART,Pin
from packet import encoding2bin as enc

TX = Pin(4)
RX = Pin(5)
BR = 9600
BUS = 1
gps_port = UART(BUS, baudrate=BR, tx=TX, rx=RX)

lat = 35.69980007202098
long = 51.33802050209452
alt = 1280
satNo = 0
gpsTime = 0
err = 0

Ax = 0
Ay = 0
Az = 0
Wx = 0
Wy = 0
Wz = 0
T = 0

start = bin(324)
end = bin(325)

while True:
    # Thread GPS
    try:
        gps = GPS(gps_port)
        
        lat = gps[0]
        long = gps[1]
        alt = gps[2]
        satNo = gps[3]
        gpsTime = gps[4]
        err = gps[5]
        if err == False:
            err = 0
        else:
            err = 1
    except:
        lat = lat
        long = long
        alt = alt
        satNo = satNo
        gpsTime = gpsTime
        err = 1
        
    # Thread MPU6050
    try:
        motion = IMU()

        accel = motion.read_accel_data() # read the accelerometer [ms^-2]
        Ax = accel["x"]
        Ay = accel["y"]
        Az = accel["z"]

        gyro = motion.read_gyro_data()   # read the gyro [deg/s]
        Wx = gyro["x"]
        Wy = gyro["y"]
        Wz = gyro["z"]

        T = motion.read_temperature()
        
    except:
        Ax = Ax
        Ay = Ay
        Az = Az
        Wx = Wx
        Wy = Wy
        Wz = Wz
        T = T

    # Packet Creation
    view = ("S"+ "," + "G" + "," + str(lat) + "," + str(long) + "," + str(alt) + "," + str(satNo) + "," + str(err) + "," + "I"+ "," +str(Ax) + "," + str(Ay) + "," + str(Az) + "," + str(Wx) + "," + str(Wy) + "," + str(Wz) + "," + str(T) + "," + "E")
    print(view)
    '''latb = enc(lat)
    longb = enc(long)
    altb = enc(alt)
    gpsTimeb = enc(gpsTime)
    errb = enc(err)
    Axb = enc(Ax)
    Ayb = enc(Ay)
    Azb = enc(Az)
    Wxb = enc(Wx)
    Wyb = enc(Wy)
    Wzb = enc(Wz)
    Tb = enc(T)'''
    
    
    #packet = (start+latb+longb,altb,gpsTimeb,errb,Axb,Ayb,Azb,Wxb,Wyb,Wzb,Tb,end)
    uart.send(view)

