# testing the oTa code
print("Hiii huys")

import machine
import time

led_pin = machine.Pin(15, machine.Pin.OUT)

while True:
    
    led_pin.value(1)
    time.sleep(1)
    led_pin.value(0)
    time.sleep(1)
