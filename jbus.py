# jbus.py

from asm_func import *
from gsm_main import get_var, set_var, init_vars, init_consts
import time

def echo_message():
    print("--------JBUS.SRC------------")
    print("JBUS TABLE SIZE        =  ", get_var('LG_BUFFER'))
    print("--------JBUS.SRC------------")
    

def JBUSESC():
    # PILE functionality placeholder
    pass

def TEMPO(duration):
    time.sleep(duration / 100.0)  # Convert 100ms units to seconds

def JBUSESC2():
       
    while get_var('JBUSACTIVATE') == 2:
        TEMPO(50)
    while get_var('JBUSACTIVATE') != 0:
        TEMPO(50)
    JBUSESC3()

def JBUSESC3():
    print(f'JBUSESC3', get_var('JBUSACTIVATE'))
    print(f'DISPLAY_LINE', get_var('DISPLAY_LINE'))
    
    TEMPO(50)
    CS3()
    
    ALLOCP('JBUS')
    CLEARSIO('JBUS')

    EV('STAJBUS')
    EV('STALEC')
    EV('STAECR')
    EV('VAR_EFF')
    
    JBUSESC4()  #!!!!!!!!!!!!!!!!!
    return      ##PH: dont use phister for now  

    if CMPRI('PFISTER', 1):
        JBUSESC4()
    else:
        try:
            LECMJBUS(get_var('JBUSNO'), 0, 'PF00', 2)
            LECMJBUS(get_var('JBUSNO'), 8, 'PF08', 2)
        except Exception as e:
            print(f"Error reading from registers: {e}")
        #JBUSESC3()  #PH: stack overflow                          

def JBUSESC4():
    print(f'JBUSESC4', get_var('JBUSACTIVATE'))
    try:
        LECMJBUS(get_var('JBUSNO'), 0, 'W1', 41)
    except Exception as e:
        print(f"Error reading from registers: {e}")
    #JBUSESC3()    #PH: stack overflow                                 

def INITIA():
    for i in range(1, 30):
        EV(f'W{i}')
    
    FV('JBUSSTATUS', 'IDLE')
    TRANSFER('JBUSSTATUS', 0, 'W20', 0, 4)
    return
    
def INITIA_2():
    for i in range(2, 30):
        EV(f'W{i}')

    FV('JBUSSTATUS', 'IDLE')
    TRANSFER('JBUSSTATUS', 0, 'W20', 0, 4)

def INITIA_3():
    for i in range(2, 30):
        EV(f'W{i}')
    
    return

if __name__ == "__main__":
    echo_message()
    
    init_consts()    
    init_vars() 
    
    INITIA_2()
    
    if gsm_main.MODBUS_MODE == 0:     #Com port
        set_var('JBUSNO', '1') #Slave No
    else:                   #Tcp
        set_var('JBUSNO', '192.168.16.139') #Slave IP
    #
    set_var('JBUSACTIVATE', 0)
    set_var('PFISTER', 1)
    
    print(f'JBUSACTIVATE', get_var('JBUSACTIVATE'))
    while True:   
        JBUSESC3()
        

        
