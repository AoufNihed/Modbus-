from pymodbus.client import ModbusTcpClient

def write_registers():
    # 1.Connect to Modbus server
    client = ModbusTcpClient('127.0.0.1', port=502)  
    client.connect()  # Connect to the server

    # 2.List of 10 integers to write
    values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    # 3.Write the values 
    client.write_registers(1, values)

    # 3.Read back the 10 registers to check 
    result = client.read_holding_registers(1, 10)
    print(result.registers)

    client.close() 

if __name__ == "__main__":
    write_registers()
