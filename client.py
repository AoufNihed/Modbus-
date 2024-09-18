#create Modbus Client (Coil Write/Read)
from pymodbus.client import ModbusTcpClient
#create client!
client = ModbusTcpClient('127.0.0.1')
client.write_coil(1, True) #write coil
result = client.read_coils(1,1)#read
print(result.bits[0])
client.close()