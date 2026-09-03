import machine
import time
buzzer_pin = machine.Pin(3, machine.Pin.OUT)
buzzer = machine.PWM(buzzer_pin)
buzzer.freq(440)
buzzer.duty_u16(32768)
time.sleep(1)
buzzer.freq(494)
time.sleep(1)
buzzer.freq(523)
time.sleep(1)
buzzer.duty(0)
buzzer.deinit()