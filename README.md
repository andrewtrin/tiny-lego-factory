# 🤖 Python Factory FSM Controller

![Python](https://img.shields.io/badge/Python-3.x-blue)
![MicroPython](https://img.shields.io/badge/MicroPython-Pico%20W-purple)
![Architecture](https://img.shields.io/badge/Architecture-Host--Client-green)

This project is a hardware simulation of a factory work cell, built to demonstrate a professional, multi-layered software architecture. The system uses a host-client model where a "Factory PC" (a Python script) runs the high-level logic and sends commands to a "Pico Controller" (a MicroPython device) over a serial connection.

The core of this project is to showcase three key software engineering principles from industrial automation:
1.  **Hardware Abstraction:** The "brain" doesn't know *how* a motor works, only how to send a command.
2.  **Encapsulation:** Hardware-specific code is bundled into clean, reusable classes.
3.  **Finite State Machines (FSMs):** The main factory logic is managed by a robust, state-driven process.

<img width="480" height="480" alt="image" src="https://github.com/user-attachments/assets/093bccb8-39a1-4273-b0f8-97103a23f61c" />

---

## 🏗️ System Architecture

This project is split into two main parts, mirroring a real-world industrial setup:

### 1. The "Factory PC" (The Brain)
* **Device:** Your computer (e.g., a laptop).
* **File:** `factory_pc.py`
* **Language:** Standard Python 3.
* **Role:** Runs the high-level logic. It contains the **Finite State Machine (FSM)** that defines the factory's process (e.g., `IDLE` $\rightarrow$ `HOMING` $\rightarrow$ `RUNNING_CONVEYOR`). It acts as the "chef" using a "recipe book."

### 2. The "Controller" (The Hands)
* **Device:** Raspberry Pi Pico W.
* **File:** `main.py`
* **Language:** MicroPython.
* **Role:** Acts as a "dumb" controller or "IO-Link." Its only job is to listen for simple, one-word commands from the PC (like `"HOME"` or `"PICK"`) and execute the corresponding hardware function.



---

## ⚙️ Hardware

* **Host PC:** A computer capable of running Python 3.
* **Controller:** Raspberry Pi Pico W.
* **Picker Arm:** 2x SG90 Servos on a LEGO chassis.
* **Conveyor Belt:** 1x 28BYJ-48 Stepper Motor with ULN2003 Driver.
* **Connection:** USB Cable (acting as a serial network).

---

## 🚀 How to Run

### 1. Pico Setup (The "Controller")
1.  Connect all your hardware (servos, stepper motor) to your Pico's pins as defined in the `main.py` script.
2.  Flash your completed `main.py` script (which includes the `Servo` class and `move_conveyor` function) onto your Raspberry Pi Pico.
3.  **Find your Pico's COM Port:** Use Thonny's interpreter settings to find the port your Pico is connected to (e.g., `COM7` on Windows or `/dev/ttyACM0` on Mac/Linux).
4.  **Close Thonny** (or any other program using the port).

### 2. PC Setup (The "Brain")
1.  **Install PySerial:** Open your computer's terminal (not Thonny) and run:
    ```bash
    pip install pyserial
    ```
2.  **Configure Port:** Open `factory_pc.py` and change the port in this line to match your Pico's port:
    ```python
    station = StationInterface(port="YOUR_PORT_HERE")
    ```
3.  **Run:** From your terminal, navigate to the project folder and run the script:
    ```bash
    python factory_pc.py
    ```

You will see the status messages from the FSM printed in your terminal, and your physical LEGO station will execute the automated sequence.
