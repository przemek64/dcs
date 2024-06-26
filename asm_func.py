# asm_func.py

import gsm_main
import os

import serial
import socket

import modbus_tk.defines as cst
from modbus_tk import modbus_rtu, modbus_tcp



def FV(var, value):
    gsm_main.set_var(var, value)
    
def BV(var):
    print(f"Variable {var} is locked for access.")

def DBV(var):
    print(f"Variable {var} is unlocked for access.")

def CMPRI(var, value):
    return gsm_main.get_var(var) == value

def MV(source, destination):
    value = gsm_main.get_var(source)
    gsm_main.set_var(destination, value)

def TRANSFER(source, src_offset, dest, dest_offset, length):
    src_value = gsm_main.get_var(source)
    #print(f"src_value {src_value}")
    dest_value = gsm_main.get_var(dest)
    #print(f"dest_value {dest_value}")
    if src_value is None or dest_value is None:
        raise ValueError(f"One of the variables {source} or {dest} does not exist.")

    if isinstance(src_value, str) and isinstance(dest_value, str):
        new_dest_value = (
            dest_value[:dest_offset] +
            src_value[src_offset:src_offset + length] +
            dest_value[dest_offset + length:]
        )
    else:
        new_dest_value = src_value  # For integers, simply assign the source value to the destination

    gsm_main.set_var(dest, new_dest_value)
    #print(f"new_dest_value {new_dest_value}")
    gsm_main.set_var(dest, new_dest_value)

def EV(var):
    var_value = gsm_main.get_var(var)
    if isinstance(var_value, str):
        gsm_main.set_var(var, " " * len(var_value))
    elif isinstance(var_value, int):
        gsm_main.set_var(var, 0)
    else:
        raise ValueError("Unsupported variable type for EV function.")

def ECRVAR(A, B):
    """
    Translated function ECRVAR from the original source.
    A : name of the variable
    B : server channel number
    """
    # For the purpose of this function, we'll just set the variable value directly
    gsm_main.set_var(A, gsm_main.get_var(A))
    print(f"Variable {A} set on server channel {B}")

def SIDEF(label):
    """
    Translated function SIDEF from the original source.
    label : Program jump label
    """
    # Placeholder for the server connection result, to simulate server request handling.
    server_connection_result = False

    if not server_connection_result:
        # Simulate the conditional jump to the given label
        print(f"Jump to label: {label}")

def SIFAUX(label):
    """
    Conditional jump if the function returns false.
    """
    function_result = False

    if not function_result:
        # Simulate the conditional jump to the given label
        print(f"Jump to label: {label}")

def SORRAM(matrix, variable=None):
    """
    Sends data described by a matrix to a buffer or variable.
    """
    data = gsm_main.get_var(matrix)
    if variable:
        gsm_main.set_var(variable, data)
    print(f"Data from {matrix} sent to {variable}")

def EFFLIG(x):
    """
    Deletes a record or a group of records based on data and filters in the file buffer key.
    """
    print(f"Delete record in file number: {x}")

def MFIN(label=None):
    """
    Delimits a matrix.
    """
    if label:
        print(f"End of matrix with label: {label}")
    else:
        print("End of matrix")

def UV(var):
    """
    Use a variable within a matrix.
    """
    value = gsm_main.get_var(var)
    if value is None:
        raise ValueError(f"Variable {var} does not exist.")
    print(f"Using variable {var} with value {value}")

def CVASCBCD(buffer, num_chars, variable):
    """
    Converts an ASCII buffer to a numeric variable with filtering.
    """
    value = gsm_main.get_var(buffer)
    if value is None:
        raise ValueError(f"Buffer {buffer} does not exist.")
    
    #print(f"buffer:value {value}")
    filtered_value = ''.join(filter(str.isdigit, value[:num_chars]))
    #print(f"filtered_value {filtered_value}")
    gsm_main.set_var(variable, int(filtered_value))
    print(f"Converted {value[:num_chars]} to {filtered_value} and stored in {variable}")

def CVBCDHEX(var_num, var_hex):
    """
    Converts a numeric variable to a HEX variable.
    """
    num_value = gsm_main.get_var(var_num)
    if num_value is None:
        raise ValueError(f"Variable {var_num} does not exist.")
    
    hex_value = format(num_value, 'X')
    gsm_main.set_var(var_hex, hex_value)
    print(f"Converted {num_value} to HEX {hex_value} and stored in {var_hex}")

def CVHEXBCD(A, B=None):
    """
    Translated function CVHEXBCD from the original source.
    A : Name of the binary variable to convert
    B : Name of the numeric variable receiving the result of the conversion (optional)
    """
    hex_value = gsm_main.get_var(A)
    if hex_value is None:
        raise ValueError(f"The variable {A} does not exist.")
    
    if isinstance(hex_value, int):
        bcd_value = int(str(hex_value), 16)
    else:
        raise ValueError("Unsupported variable type for CVHEXBCD function. Expected an integer.")

    if B is None:
        gsm_main.set_var('VARBCD', bcd_value)
    else:
        gsm_main.set_var(B, bcd_value)
        
        
def TEMPO(value):
    """
    Creates a delay for the specified duration.

    :param value: Duration of the delay in increments of 100 ms.
    """
    delay = value * 0.1  # Convert to seconds
    time.sleep(delay)
    
    
def IFEGAL(var1, var2, label):
    """
    Conditional jump if var1 equals var2.

    :param var1: First variable
    :param var2: Second variable
    :param label: Label to jump to if condition is true
    """
    if get_var(var1) == get_var(var2):
        print(f"Jump to label: {label}")


def IFDIF(var1, var2, label):
    """
    Conditional jump if var1 is different from var2.

    :param var1: First variable
    :param var2: Second variable
    :param label: Label to jump to if condition is true
    """
    if get_var(var1) != get_var(var2):
        print(f"Jump to label: {label}")

def IFSUP(var1, var2, label):
    """
    Conditional jump if var1 is greater than var2.

    :param var1: First variable
    :param var2: Second variable
    :param label: Label to jump to if condition is true
    """
    if get_var(var1) > get_var(var2):
        print(f"Jump to label: {label}")


def IFINF(var1, var2, label):
    """
    Conditional jump if var1 is less than var2.

    :param var1: First variable
    :param var2: Second variable
    :param label: Label to jump to if condition is true
    """
    if get_var(var1) < get_var(var2):
        print(f"Jump to label: {label}")
   
def CS3():
    os.system('cls')
    #print("Clear screen...")
    
    
    
    
def ALLOCP(voie):
    """
    Redirects the DIALOGUE channel to another serial channel.
    """
    print(f"Redirecting DIALOGUE channel to serial channel: {voie}")

def CLEARSIO(voie=None):
    """
    Clears a serial port in reception.
    """
    if voie:
        print(f"Clearing serial port: {voie}")
    else:
        print("Clearing standard DIALOGUE port")



def ECRMJBUS_mini(escl, adjbus, adbuffer, nbmots):
    """
    Write data to Modbus holding registers.

    :param escl: Slave address (or IP address for TCP)
    :param adjbus: Starting address of JBUS registers
    :param adbuffer: Starting address of buffer variables (e.g., 'W2')
    :param nbmots: Number of words to write
    """
    data_to_write = []

    # Read the data from the buffer variables
    for i in range(nbmots):
        buffer_var = f'{adbuffer[:-1]}{int(adbuffer[-1]) + i}'  # Adjust variable name to W2, W3, etc.
        value = gsm_main.get_var(buffer_var)
        if value is None:
            raise ValueError(f"Buffer variable {buffer_var} does not exist")
        data_to_write.append(int(value))


    client = minimalmodbus.Instrument('COM16', 1)  # Port name, slave address
    client.serial.baudrate = 9600
    client.serial.bytesize = 8
    client.serial.parity = serial.PARITY_NONE
    client.serial.stopbits = 1
    client.serial.timeout = 1  # seconds
    client.mode = minimalmodbus.MODE_RTU

    # Write data to holding registers
    try:
        client.write_registers(adjbus, data_to_write)
        print(f"JBUS Master Write Function\nSlave Number: {escl}\nJBUS Address: {adjbus}\nBuffer Address: {adbuffer}\nNumber of Words: {nbmots}")
    except IOError as e:
        print(f"Error writing to registers: {e}")



import serial
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu, modbus_tcp
import gsm_main  # Assuming this module provides `get_var` and `MODBUS_MODE`

import serial
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu, modbus_tcp
import gsm_main  # Assuming this module provides `get_var` and `MODBUS_MODE`

def ECRMJBUS(escl, adjbus, adbuffer, nbmots):
    """
    Write data to Modbus holding registers.

    :param escl: Slave address (or IP address for TCP)
    :param adjbus: Starting address of JBUS registers
    :param adbuffer: Starting address of buffer variables (e.g., 'W2')
    :param nbmots: Number of words to write
    """
    data_to_write = []

    # Extract the prefix (e.g., 'W') and numeric part of the variable name
    prefix = ''.join([char for char in adbuffer if char.isalpha()])
    start_index = int(''.join([char for char in adbuffer if char.isdigit()]))

    # Read the data from the buffer variables
    for i in range(nbmots):
        buffer_var = f'{prefix}{start_index + i}'  # Adjust variable name to W2, W3, etc.
        print(f"Buffer variable {buffer_var}")
        value = gsm_main.get_var(buffer_var)
        if value is None:
            raise ValueError(f"Buffer variable {buffer_var} does not exist")
        data_to_write.append(int(value))

    if gsm_main.MODBUS_MODE == 0:  # RTU
        # Initialize the Modbus RTU client with the same settings as the server
        try:
            serial_port = serial.Serial(
                port='COM' + str(escl),  # Ensure this matches the server port
                baudrate=9600,
                bytesize=8,
                parity=serial.PARITY_NONE,
                stopbits=1,
                timeout=1
            )
            client = modbus_rtu.RtuMaster(serial_port)
            client.set_timeout(1.0)
            client.set_verbose(True)
            
            # Write data to holding registers
            client.execute(escl, cst.WRITE_MULTIPLE_REGISTERS, adjbus, output_value=data_to_write)
            print(f"JBUS Master Write Function\nSlave Number: {escl}\nJBUS Address: {adjbus}\nBuffer Address: {adbuffer}\nNumber of Words: {nbmots}")

            # Flush and close the serial port
            serial_port.flush()
            serial_port.close()
            print("Serial port flushed and closed.")
            
        except Exception as e:
            print(f"Error writing to registers: {e}")

    elif gsm_main.MODBUS_MODE == 1:  # TCP
        # Initialize the Modbus TCP client
        try:
            client = modbus_tcp.TcpMaster(host=escl, port=502)
            client.set_timeout(1.0)
            client.set_verbose(True)
            
            # Write data to holding registers
            client.execute(1, cst.WRITE_MULTIPLE_REGISTERS, adjbus, output_value=data_to_write)  # Slave ID is usually 1 for TCP
            print(f"Modbus TCP Master Write Function\nIP Address: {escl}\nJBUS Address: {adjbus}\nBuffer Address: {adbuffer}\nNumber of Words: {nbmots}")
            
        except Exception as e:
            print(f"Error writing to registers: {e}")

    else:
        raise ValueError("Invalid MODBUS_MODE. Please set it to 0 for RTU or 1 for TCP.")




def LECMJBUS(escl, adjbus, adbuffer, nbmots):
    """
    Read data from Modbus holding registers.

    :param escl: Slave address (or IP address for TCP)
    :param adjbus: Starting address of JBUS registers
    :param adbuffer: Starting address of buffer variables (e.g., 'W2')
    :param nbmots: Number of words to read
    
     LECMJBUS(get_var('JBUSNO'), 1, 'W2', 2)
    """
    data_read = []

    # Extract the prefix (e.g., 'W') and numeric part of the variable name
    prefix = ''.join([char for char in adbuffer if char.isalpha()])
    start_index = int(''.join([char for char in adbuffer if char.isdigit()]))

    if gsm_main.MODBUS_MODE == 0:  # RTU
        # Initialize the Modbus RTU client with the same settings as the server
        try:
            serial_port = serial.Serial(
                port='COM' + str(escl),  # Ensure this matches the server port
                baudrate=9600,
                bytesize=8,
                parity=serial.PARITY_NONE,
                stopbits=1,
                timeout=1
            )
            client = modbus_rtu.RtuMaster(serial_port)
            client.set_timeout(1.0)
            client.set_verbose(True)
            
            # Read data from holding registers
            data_read = client.execute(escl, cst.READ_HOLDING_REGISTERS, adjbus, nbmots)
            print(f"JBUS Master Read Function\nSlave Number: {escl}\nJBUS Address: {adjbus}\nBuffer Address: {adbuffer}\nNumber of Words: {nbmots}")

            # Flush and close the serial port
            serial_port.flush()
            serial_port.close()
            print("Serial port flushed and closed.")
            
        except Exception as e:
            print(f"Error reading from registers: {e}")

    elif gsm_main.MODBUS_MODE == 1:  # TCP
        # Initialize the Modbus TCP client
        try:
            #print(f"client = modbus_tcp.TcpMaster {str(escl)}")
            client = modbus_tcp.TcpMaster(host=str(escl), port=502)
            #print("2")
            client.set_timeout(1.0)
            #print("3")
            client.set_verbose(True)
            #print("4")
            
            # Read data from holding registers
            data_read = client.execute(1, cst.READ_HOLDING_REGISTERS, adjbus, nbmots)  # Slave ID is usually 1 for TCP
            #client.execute(1, cst.READ_HOLDING_REGISTERS, adjbus, nbmots)  # Slave ID is usually 1 for TCP
            #client.execute(1, cst.READ_HOLDING_REGISTERS, 0, 10)
            #print("5")
            print(f"Modbus TCP Master Read Function\nIP Address: {escl}\nJBUS Address: {adjbus}\nBuffer Address: {adbuffer}\nNumber of Words: {nbmots}")
            
            
        except Exception as e:
            #print("!!!!!!!!")
            print(f"Error reading from registers: {e}")

    else:
        raise ValueError("Invalid MODBUS_MODE. Please set it to 0 for RTU or 1 for TCP.")

    #print("6666")
    # Write the read data to the buffer variables
    for i in range(nbmots):
        buffer_var = f'{prefix}{start_index + i}'  # Adjust variable name to W2, W3, etc.
        if i < len(data_read):
            value = data_read[i]
            #print(f"Updating buffer variable {buffer_var} with value {value}")
            gsm_main.set_var(buffer_var, value)
        else:
            raise ValueError(f"Read data is insufficient to update buffer variable {buffer_var}")


   
   
# Example of usage
# SORRAM('MATEX', 'VAR')
# CVASCBCD('BUFFER', 3, 'VARIABLE')
# CVBCDHEX('VAR1', 'VAR2')
# ALLOCP('INDIC3')
# CLEARSIO('COM1')
# ECRMJBUS(1, '1000H', '&VAR', 1)
# SIFAUX('LABEL')
