import machine
import time

# Set up the LED pin
led = machine.Pin(2, machine.Pin.OUT)

# Blink the LED on and off
while True:
    led.value(1)  # Turn LED on
    time.sleep(1) # Wait for 1 second
    led.value(0)  # Turn LED off
    time.sleep(1) # Wait for 1 second