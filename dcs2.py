# dcs2.py

from gsm_main import set_var, get_var
from asm_func import *
from save_com import *

# MATRICE Functions

def MATRICE_CVTASC10_TO_STRING():
    set_var('CVTASC10_TO_STRING', str(get_var("CVTASC10")))

def MATRICE_PF00_TO_STRING():
    set_var('PF00_TO_STRING', str(get_var("PF00")) + str(get_var("PF01")))
    
def MATRICE_PF09_TO_STRING():
    set_var('PF09_TO_STRING', str(get_var("PF09")))

def MATRICE_JBUS_ERROR_TO_STRING():
    set_var('JBUS_ERROR_TO_STRING', str(get_var("JBUS_ERROR_CODE")))

# Main Functions

def GET_PFISTER_STATUS():
    EV('T1DATA1')

    # Call the MATRICE function before SORRAM
    MATRICE_PF00_TO_STRING()
    SORRAM('PF00_TO_STRING', 'T1DATA1')

    SET_TRUE_SAVE()
   

def SET_PFISTER_COMMAND():
    # Set I/O
    # Registers 68..69
    # E140 - high = BI300 controls set point and start signal
    # E140 - lo = RLT panel controls set point and start

    # E141 - high - lo = start load signal from BI300
    # E142 - high - lo = stop loading sequence from BI300

    EV('PF68')
    CVASCBCD('T1DATA1', 5, 'CVTASC')
    CVBCDHEX('CVTASC', 'PF69')

    ALLOCP('JBUS')
    CLEARSIO('JBUS')

    ECRMJBUS(get_var('JBUSNO'), 68, 'PF68', 2)

    if not get_var('server_connection_result'):  # Assuming SIFAUX is used for server connection result
        JBUS_ERROR()

    SET_TRUE_SAVE()
   
    
def GET_PFISTER_DELIVERED_QUANTITY():
    EV('T1DATA1')

    # Call the MATRICE function before SORRAM
    MATRICE_PF09_TO_STRING()
    SORRAM('PF09_TO_STRING', 'T1DATA1')

    SET_TRUE_SAVE()

def SET_PFISTER_REQUIRED_WEIGHT():
    EV('PF72')
    CVASCBCD('T1DATA1', 5, 'CVTASC')
    CVBCDHEX('CVTASC', 'PF73')

    ALLOCP('JBUS')
    CLEARSIO('JBUS')

    ECRMJBUS(get_var('JBUSNO'), 72, 'PF72', 2)

    if not get_var('server_connection_result'):  # Assuming SIFAUX is used for server connection result
        JBUS_ERROR()

    SET_TRUE_SAVE()

def JBUS_ERROR():
    MATRICE_JBUS_ERROR_TO_STRING()
    SORRAM('JBUS_ERROR_TO_STRING', 'T1DATA1')

    SET_FALSE_SAVE()

def SET_REQUESTED_VALUES():
    # Number of bags
    CVASCBCD('T1DATA1', 4, 'CVTASC')
    CVBCDHEX('CVTASC', 'W2')

    # Number of stacks
    EV('T1DATA2')
    TRANSFER('T1DATA1', 4, 'T1DATA2', 0, 2)
    CVASCBCD('T1DATA2', 2, 'CVTASC')
    CVBCDHEX('CVTASC', 'W3')

    for i in range(1, 18):
        EV('T1DATA2')
        TRANSFER('T1DATA1', 4 + 2*i, 'T1DATA2', 0, 2)
        CVASCBCD('T1DATA2', 2, 'CVTASC')
        CVBCDHEX('CVTASC', f'W{4+i-1}')

    ALLOCP('JBUS')
    CLEARSIO('JBUS')

    ECRMJBUS(get_var('JBUSNO'), 1, 'W2', 19)

    if not get_var('server_connection_result'):  # Assuming SIFAUX is used for server connection result
        JBUS_ERROR()

    SET_TRUE_SAVE()

def SET_LOADED_VALUES():
    # Number of bags
    CVASCBCD('T1DATA1', 4, 'CVTASC')
    CVBCDHEX('CVTASC', 'W22')

    # Number of stacks
    EV('T1DATA2')
    TRANSFER('T1DATA1', 4, 'T1DATA2', 0, 2)
    CVASCBCD('T1DATA2', 2, 'CVTASC')
    CVBCDHEX('CVTASC', 'W23')

    for i in range(1, 18):
        EV('T1DATA2')
        TRANSFER('T1DATA1', 4 + 2*i, 'T1DATA2', 0, 2)
        CVASCBCD('T1DATA2', 2, 'CVTASC')
        CVBCDHEX('CVTASC', f'W{24+i-1}')

    ALLOCP('JBUS')
    CLEARSIO('JBUS')

    ECRMJBUS(get_var('JBUSNO'), 21, 'W22', 19)

    if not get_var('server_connection_result'):  # Assuming SIFAUX is used for server connection result
        JBUS_ERROR()

    SET_TRUE_SAVE()

def SET_BI300_STATUS():
    # Status in T1DATA1
    CVASCBCD('T1DATA1', 1, 'CVTASC')
    CVBCDHEX('CVTASC', 'W1')

    ALLOCP('JBUS')
    CLEARSIO('JBUS')

    ECRMJBUS(get_var('JBUSNO'), 0, 'W1', 1)

    if not get_var('server_connection_result'):  # Assuming SIFAUX is used for server connection result
        JBUS_ERROR()

    SET_TRUE_SAVE()


def CLEAR_REGISTRY():
    for i in range(1, 42):
        EV(f'W{i}')
    
    FV('W21', 999)  # 0-4 are valid statuses, initialize variable using value 999

    ALLOCP('JBUS')
    CLEARSIO('JBUS')

    ECRMJBUS(get_var('JBUSNO'), 0, 'W1', 41)

    if not get_var('server_connection_result'):  # Assuming SIFAUX is used for server connection result
        JBUS_ERROR()

    SET_TRUE_SAVE()
