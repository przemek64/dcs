# dcs.py

import sys
from gsm_main import *
from asm_func import *
from save_com import *

from dcs import set_params
from dcs2 import *
from dcs3 import *
from dcs4 import *

# Define constants with function indexes
F_DCSCHECKPROD_1 = 1
F_DCSLOAD = 2
F_INIT_A = 3
F_DCSCHECKPROD_4 = 4
F_DCSCOMPLETE = 5
F_CLEAR_REGISTRY = 6
F_SET_REQUESTED_VALUES = 7
F_GET_PLC_STATUS = 8
F_GET_PLC_ERROR = 9
F_GET_PLC_LOADED_VALUES = 10
F_SET_BI300_STATUS = 11
F_SET_LOADED_VALUES = 12
F_GET_PFISTER_STATUS = 13
F_GET_PFISTER_DELIVERED_QUANTITY = 14
F_SET_PFISTER_REQUIRED_WEIGHT = 15
F_SET_PFISTER_COMMAND = 16


# Function definitions
def dcs_dcscheckprod(_T1DATA1, _T1DATA2):
    set_params(_T1DATA1, _T1DATA2, F_DCSCHECKPROD_1)
    print(f"dcs_dcscheckprod called with params: {_T1DATA1}, {_T1DATA2}")
    DCSCHECKPROD()

def dcs_dcsload(_T1DATA1, _T1DATA2):
    set_params(_T1DATA1, _T1DATA2, F_DCSLOAD)
    print(f"dcs_dcsload called with params: {_T1DATA1}, {_T1DATA2}")
    DCSLOAD()

def dcs_init_a(_T1DATA1, _T1DATA2):
    set_params(_T1DATA1, _T1DATA2, F_INIT_A)
    print(f"dcs_init_a called with params: {_T1DATA1}, {_T1DATA2}")
    INIT_A()

def dcs_dcscheckprod_4(_T1DATA1, _T1DATA2):
    set_params(_T1DATA1, _T1DATA2, F_DCSCHECKPROD_4)
    print(f"dcs_dcscheckprod_4 called with params: {_T1DATA1}, {_T1DATA2}")
    DCSCHECKPROD()

def dcs_dcscomplete(_T1DATA1, _T1DATA2):
    set_params(_T1DATA1, _T1DATA2, F_DCSCOMPLETE)
    print(f"dcs_dcscomplete called with params: {_T1DATA1}, {_T1DATA2}")
    DCSCOMPLETE()

def dcs_clear_registry(_T1DATA1, _T1DATA2):
    set_params(_T1DATA1, _T1DATA2, F_CLEAR_REGISTRY)
    print(f"dcs_clear_registry called with params: {_T1DATA1}, {_T1DATA2}")
    CLEAR_REGISTRY()

def dcs_set_requested_values(_T1DATA1, _T1DATA2):
    set_params(_T1DATA1, _T1DATA2, F_SET_REQUESTED_VALUES)
    print(f"dcs_set_requested_values called with params: {_T1DATA1}, {_T1DATA2}")
    SET_REQUESTED_VALUES()

def dcs_get_plc_status(_T1DATA1, _T1DATA2):
    set_params(_T1DATA1, _T1DATA2, F_GET_PLC_STATUS)
    print(f"dcs_get_plc_status called with params: {_T1DATA1}, {_T1DATA2}")
    GET_PLC_STATUS()

def dcs_get_plc_error(_T1DATA1, _T1DATA2):
    set_params(_T1DATA1, _T1DATA2, F_GET_PLC_ERROR)
    print(f"dcs_get_plc_error called with params: {_T1DATA1}, {_T1DATA2}")
    GET_PLC_ERROR()

def dcs_get_plc_loaded_values(_T1DATA1, _T1DATA2):
    set_params(_T1DATA1, _T1DATA2, F_GET_PLC_LOADED_VALUES)
    print(f"dcs_get_plc_loaded_values called with params: {_T1DATA1}, {_T1DATA2}")
    GET_PLC_LOADED_VALUES()

def dcs_set_bi300_status(_T1DATA1, _T1DATA2):
    set_params(_T1DATA1, _T1DATA2, F_SET_BI300_STATUS)
    print(f"dcs_set_bi300_status called with params: {_T1DATA1}, {_T1DATA2}")
    SET_BI300_STATUS()

def dcs_set_loaded_values(_T1DATA1, _T1DATA2):
    set_params(_T1DATA1, _T1DATA2, F_SET_LOADED_VALUES)
    print(f"dcs_set_loaded_values called with params: {_T1DATA1}, {_T1DATA2}")
    SET_LOADED_VALUES()

def dcs_get_pfister_status(_T1DATA1, _T1DATA2):
    set_params(_T1DATA1, _T1DATA2, F_GET_PFISTER_STATUS)
    print(f"dcs_get_pfister_status called with params: {_T1DATA1}, {_T1DATA2}")
    GET_PFISTER_STATUS()

def dcs_get_pfister_delivered_quantity(_T1DATA1, _T1DATA2):
    set_params(_T1DATA1, _T1DATA2, F_GET_PFISTER_DELIVERED_QUANTITY)
    print(f"dcs_get_pfister_delivered_quantity called with params: {_T1DATA1}, {_T1DATA2}")
    GET_PFISTER_DELIVERED_QUANTITY()

def dcs_set_pfister_required_weight(_T1DATA1, _T1DATA2):
    set_params(_T1DATA1, _T1DATA2, F_SET_PFISTER_REQUIRED_WEIGHT)
    print(f"dcs_set_pfister_required_weight called with params: {_T1DATA1}, {_T1DATA2}")
    SET_PFISTER_REQUIRED_WEIGHT()

def dcs_set_pfister_command(_T1DATA1, _T1DATA2):
    set_params(_T1DATA1, _T1DATA2, F_SET_PFISTER_COMMAND)
    print(f"dcs_set_pfister_command called with params: {_T1DATA1}, {_T1DATA2}")
    SET_PFISTER_COMMAND()


if __name__ == "__main__":

    init_consts()    
    init_vars() 

    if gsm_main.MODBUS_MODE == 0:     #Com port
        set_var('JBUSNO', '1') #Slave No
    else:                   #Tcp
        set_var('JBUSNO', '192.168.16.139') #Slave IP

    ### MATRIX
    #dcs_init_a("","")
    #time.sleep(3)  ## 
    
    dcs_clear_registry("","")
    time.sleep(3)  ##
    
    dcs_set_requested_values("009902020304000103060502020707060505000000", "11")   
    time.sleep(3)  ##   
    
    dcs_set_loaded_values("003305010101020303030502020707060505000000", "11")  
    time.sleep(3)  ##
    
    dcs_get_plc_status("","")
    print(f"Result: {get_var('T1DATA1')}")
    time.sleep(3)  ##
    
    dcs_get_plc_error("","")
    print(f"Result: {get_var('T1DATA1')}")
    time.sleep(3)  ##
    
    dcs_set_bi300_status("1","")
    print(f"Result: {get_var('T1DATA1')}")
    time.sleep(3)  ##
    
    dcs_get_plc_loaded_values("","")
    print(f"Result: {get_var('T1DATA1')}")    
    time.sleep(3)  ##
    
    dcs_clear_registry("","")
     
    ###MATIRX
        
    
        

