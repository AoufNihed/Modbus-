# Industrial Communication Systems & Modbus TCP Protocols

## Overview
After my internship at **Sonelgaz Distribution Oran**, I delved deeper into **industrial communication systems** and **Modbus TCP protocols**. This project involved developing a Modbus server and client using Python and exploring legacy systems like **RS-232**, **RS-485**, and **Remote Terminal Units (RTUs)**.

## Project Highlights
- **Modbus TCP Server & Client**: Created a Modbus server that runs on TCP/IP, and a client to interact with the server for reading and writing data.
- **Legacy System Exploration**: Investigated industrial communication systems such as:
  - **RS-232**: Used in point-to-point communication with distances <15 meters and speeds up to 20kbps.
  - **RS-485**: Widely used today with half-duplex communication, up to 1200 meters, and speeds <100kbps.
  - **RTUs (Remote Terminal Units)**: Legacy control systems still in operation, observed during my internship.
  
## Technical Implementation
- Utilized **Python's pymodbus library** to create:
  - A **Modbus server** with multiple data blocks (coils, discrete inputs, holding registers, and input registers).
  - A **Modbus client** for writing and reading coils and registers.
