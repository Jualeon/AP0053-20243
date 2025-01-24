from machine import Pin
import utime

m1 = Pin(22, Pin.OUT)
m2 = Pin(23, Pin.OUT)

while True:
    m1.value(1)
    m2.value(0)
    utime.sleep(2)
    m1.value(0)
    m2.value(0)
    utime.sleep(1)
    m1.value(0)
    m2.value(1)
    utime.sleep(2)
    m1.value(0)
    m2.value(0)
    utime.sleep(1)
