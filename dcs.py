# dcs.py

import sys
from gsm_main import *
from asm_func import *
from save_com import *

from dcs2 import *
from dcs3 import *
from dcs4 import *


def set_params(vT1DATA1, vT1DATA2, vT1VALUE):

    set_var('T1DATA1', vT1DATA1)
    set_var('T1DATA2', vT1DATA2)
    set_var('T1VALUE', vT1VALUE)
    
def DCS_COMMS():

    # Initialize variables
    set_var('JBUS_ERROR_CODE', 0)
    
    for i in range(22, 41):
        set_var(f'B{i}', 0)
        
    # CALL INITIA (Placeholder for the actual function call)
    # CALL JNOCOMMSMSG (Placeholder for the actual function call)

    # DISPLAY MESSAGE (Placeholder for the actual function call)
    # CALL DISPLAY_DATA2

    set_var('JBUSACTIVATE', 1)
    
    T1VALUE = get_var('T1VALUE')
    
    if T1VALUE == 1:
        DCSCHECKPROD()  #python dcs.py "" "" 1    ####### ??????????
    elif T1VALUE == 2:
        DCSLOAD()      #python dcs.py "" "" 2    ####### ??????????
    elif T1VALUE == 3:
        INIT_A()       #python dcs.py "" "" 3    #######OK
    elif T1VALUE == 4:
        # DCSUNLOAD() (Placeholder for the actual function call)
        DCSCHECKPROD()       #!!!!!!!!!
    elif T1VALUE == 5:
        DCSCOMPLETE()       #!!!!!!!!!
    elif 6 <= T1VALUE <= 12:
        if T1VALUE == 6:
            CLEAR_REGISTRY()       #python dcs.py "" "" 6    #######OK
        elif T1VALUE == 7:
            SET_REQUESTED_VALUES()     #python dcs.py "0601020304050203040502020000000000000000" "11" 7    #######OK
        elif T1VALUE == 8:
            GET_PLC_STATUS()     #python dcs.py "" "" 8
        elif T1VALUE == 9:
            GET_PLC_ERROR()      #python dcs.py "" "" 9
        elif T1VALUE == 10:
            GET_PLC_LOADED_VALUES()  #python dcs.py "" "" 10 
        elif T1VALUE == 11:
            SET_BI300_STATUS()     #python dcs.py "8" "" 11    #######OK
        elif T1VALUE == 12:
            SET_LOADED_VALUES()    #python dcs.py "0601020304050203040502020000000000000000" "11" 12   #######OK
    elif 13 <= T1VALUE <= 16:
        if T1VALUE == 13:
            GET_PFISTER_STATUS()  #python dcs.py "1" "" 13
        elif T1VALUE == 14:
            GET_PFISTER_DELIVERED_QUANTITY()    #python dcs.py "1" "" 13
        elif T1VALUE == 15:
            SET_PFISTER_REQUIRED_WEIGHT()   #python dcs.py "1" "" 15
        elif T1VALUE == 16:
            SET_PFISTER_COMMAND()      #python dcs.py "1" "" 15
    else:
        SET_FALSE()
        SAVE_COMMAND()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python dcs.py <T1DATA1> <T1DATA2> <T1VALUE>")
        sys.exit(1)
        
    init_consts()    
    init_vars() 
    #set_var('JBUSNO', 1)    

    vT1DATA1 = sys.argv[1]
    vT1DATA2 = sys.argv[2]
    try:
        vT1VALUE = int(sys.argv[3])
    except ValueError:
        print("T1VALUE must be an integer.")
        sys.exit(1)

    set_params(vT1DATA1, vT1DATA2, vT1VALUE) 
    if gsm_main.MODBUS_MODE == 0:     #Com port
        set_var('JBUSNO', '1') #Slave No
    else:                   #Tcp
        set_var('JBUSNO', '192.168.16.139') #Slave IP
        
    DCS_COMMS()
    
    vT1DATA1 = get_var('T1DATA1')
    print(f"T1DATA1: {vT1DATA1}")
    vT1DATA2 = get_var('T1DATA2')
    print(f"T1DATA2: {vT1DATA2}")
    vT1VALUE = get_var('T1VALUE')    
    print(f"T1VALUE: {vT1VALUE}")


        

