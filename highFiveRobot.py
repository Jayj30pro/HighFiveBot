from machine import Pin, PWM
import utime

servo = PWM(Pin(0))
servo.freq(50)

trigger = Pin(5, Pin.OUT)
echo = Pin(3, Pin.IN)

timepassed = 0 
distance = 0

def scan():
    global distance
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    distance = "{:.1f}".format(distance)
    
    print(distance + " cm")
    
def check():
    global distance
    if float(distance) < 30:  # Adjust the threshold as needed
        servo.duty_u16(1350)  # Move servo to 0-degree position
    elif float(distance) < 20:
        servo.duty_u16(8200)  # Move servo to 180-degree position
    else:
        servo.duty_u16(6000)  # Move servo to 90-degree position

while True:
    scan()
    check()
    utime.sleep(0.5)
