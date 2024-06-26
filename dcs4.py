# dcs4.py

from gsm_main import set_var, get_var
from asm_func import *
from save_com import *
from jbus import *





# MATRICE Functions

def MATRICE_CVTASC_TO_STRING():
    set_var('CVTASC_TO_STRING', str(get_var("CVTASC")))

def MATRICE_LOADED_BAGS():
    loaded_bags = ''.join([
        f'{get_var(f"B{i}"):0>2}' for i in range(22, 41)
    ])
    #  33050101010203030305020207070605050000
    #003305010101020303030502020707060505000000

    set_var('LOADED_BAGS', loaded_bags)
    #print(f"LOADED_BAGS: {get_var('LOADED_BAGS')}") 

# Main Functions

def GET_PLC_STATUS():
    EV('T1DATA1')
    TRANSFER('W21', 0, 'TMPHEX', 0, 2)

    CVHEXBCD('TMPHEX', 'CVTASC')
    
    MATRICE_CVTASC_TO_STRING()  # Call the MATRICE function before SORRAM
    SORRAM('CVTASC_TO_STRING', 'T1DATA1')

    SET_TRUE_SAVE()

def GET_PLC_ERROR():
    EV('T1DATA1')
    TRANSFER('W41', 0, 'TMPHEX', 0, 2)

    CVHEXBCD('TMPHEX', 'CVTASC')

    MATRICE_CVTASC_TO_STRING()  # Call the MATRICE function before SORRAM
    SORRAM('CVTASC_TO_STRING', 'T1DATA1')

    SET_TRUE_SAVE()

def GET_PLC_LOADED_VALUES():
    EV('T1DATA1')

    for i in range(22, 41):
        CVHEXBCD(f'W{i}', f'B{i}')
        #print(f"BBB: {str(get_var(f'B{i}'))}") 
        #print(f"WWW: {str(get_var(f'W{i}'))}") 
        

    MATRICE_LOADED_BAGS()  # Call the MATRICE function before SORRAM
    SORRAM('LOADED_BAGS', 'T1DATA1')

    SET_TRUE_SAVE()

def DCSCOMPLETE():
    # MAKE OUR STATUS COMPLETE
    FV('JBUSSTATUS', 'COMPLETE')
    TRANSFER('JBUSSTATUS', 0, 'W20', 0, 8)

    # CHECK DCS HAS GONE IDLE
    while True:
        TRANSFER('W40', 0, 'STRTEMP', 0, 20)
        if CMPRI('STRTEMP', 'IDLE'):
            RETTRUE1()
        elif CMPRI('STRTEMP', 'ERROR'):
            RETFALSE1()

def RETTRUE1():
    SET_TRUE_SAVE()
    DCSCOMPLETE_END()

def RETFALSE1():
    SET_FALSE_SAVE()

def DCSCOMPLETE_END():
    INITIA_2()

def INIT_A():
    INITIA_2()
    SET_TRUE_SAVE()

def DCSVOLUME():
    SET_TRUE_SAVE()

def DCSUNLOAD():
    SET_TRUE_SAVE()

def JNOCOMMSMSG():
    BV('JBUSACTIVE')
    MV('JBUSACTIVE', 'JBUSACTIVE1')
    DBV('JBUSACTIVE')
    
    
    if CMPRI('JBUSACTIVE1', 1):
        JNOCOMMSEXIT()
    else:
        CS3()
        EV('DISPLAY_LINE')
        FV('JBUSSTATUS', 'NO PLC COMMS')
        MV('JBUSSTATUS', 'DISPLAY_LINE')
        
        # SORVIS3_ 4,6,1,24
        # SORVAR3 5,6,1,JBUSACTIVATE
        JNOCOMMSMSG()

def JNOCOMMSEXIT():
    pass

