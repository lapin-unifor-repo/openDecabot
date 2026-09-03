# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import os, machine
#os.dupterm(None, 1) # disable REPL on UART(0)
import gc
#import webrepl
#webrepl.start()
gc.collect()
import tm1640
import time
from machine import Pin
#LEDmatrix
tm = tm1640.TM1640(clk=Pin(14), dio=Pin(13))
tm.write([0, 0, 66, 66, 66, 66, 66, 66])