# main.py

from machine import Pin, PWM
from time import sleep, sleep_ms
import sys # Read from USB serial
import _thread

class Servo:
    def __init__ (self, pin_number):
        self.pwm_object = PWM(Pin(pin_number))
        self.pwm_object.freq(50)
        
    def move_to_angle(self, angle):
        duty = int(1640 + (angle / 180) * 6550)
        self.pwm_object.duty_u16(duty)

# Defined list of the 4 output pins
motor_pins = [
    Pin(10, Pin.OUT),
    Pin(11, Pin.OUT),
    Pin(12, Pin.OUT),
    Pin(13, Pin.OUT)
]

# Half-stepping 8-step sequence
step_sequence = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1]
]

def move_conveyor(steps):
    for _ in range(steps):
        for step in step_sequence:
            for i in range(4):
                motor_pins[i].value(step[i])
            sleep_ms(1)
            
pan_servo = Servo(14)
tilt_servo = Servo(15)

# Main loop
while True:
    command = sys.stdin.readline().strip()
    #command = input("Enter command: ")
    if command == "HOME":
        pan_servo.move_to_angle(90)
        tilt_servo.move_to_angle(90)
        
    elif command == "PICK":
        pan_servo.move_to_angle(0)
        sleep(2)
        tilt_servo.move_to_angle(0)
        sleep(1)
        tilt_servo.move_to_angle(90)
        sleep(1)
        
    elif command == "CONVEYOR_ON":
        move_conveyor(200)
        
    elif command == "conveyor_sweep":
        move_conveyor(2000)
    
    elif command == "demo":
        _thread.start_new_thread(move_conveyor, (2000,))
        
        pan_servo.move_to_angle(0)
        sleep(2)
        tilt_servo.move_to_angle(0)
        sleep(1)
        tilt_servo.move_to_angle(90)
        sleep(2)
        pan_servo.move_to_angle(90)
        sleep(2)
        tilt_servo.move_to_angle(0)
        sleep(1)
        tilt_servo.move_to_angle(90)
        
    elif command == "shannon":
        pan_servo.move_to_angle(0)
        tilt_servo.move_to_angle(0)
        sleep(1)
        pan_servo.move_to_angle(180)
        sleep(1)
        tilt_servo.move_to_angle(90)