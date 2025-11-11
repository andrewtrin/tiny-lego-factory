import serial
import time

class StationInterface:
    def __init__(self, port):
        print(f"Attempting to connect to port: {port}")
        self.pico = serial.Serial(port=port, baudrate=115200, timeout=1)
        print("Pico connection successful.")
        
        time.sleep(2)

    def send_command(self, command):
        print(f"Sending command: {command}")
        self.pico.write(f"{command}\n".encode())            

def run_factory_fsm():
    print("Initializing station interface...")
    station = StationInterface(port="COM7")
    current_state = "IDLE"

    while True:
        if current_state == "IDLE":
            print("State is IDLE. Moving to HOMING.")
            current_state = "HOMING"
        elif current_state == "HOMING":
            print("Homing station...")
            station.send_command("HOME")
            current_state = "RUNNING_CONVEYOR"
            time.sleep(2)
        elif current_state == "RUNNING_CONVEYOR":
            print("Starting conveyor...")
            station.send_command("CONVEYOR_ON")
            current_state = "PICKING_PART"
            time.sleep(5)
        elif current_state == "PICKING_PART":
            print("Picking part...")
            station.send_command("PICK")
            current_state = "IDLE"
            time.sleep(2)

if __name__ == "__main__":
    run_factory_fsm()