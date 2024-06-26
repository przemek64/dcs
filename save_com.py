# Import necessary functions from asm_func and gsm_list_globalvars
from asm_func import *
from gsm_list_globalvars import *

def SAVE_INT_COMMAND():
    EV('REC_EXIST')
    SET_NET_STATUS_INTERUPT()
    SET_NET_RESULT_DATA()
    SAVE_COMM_NET()

def SAVE_COMMAND():
    EV('REC_EXIST')
    SET_NET_STATUS_COMPLETE()
    SET_NET_RESULT_DATA()

def SAVE_COMM_NET():
    if CMPRI('REC_EXIST', 3):
        FV('REC_EXIST', 4)
        SORVIS('NO_SEND')
    
    IV('REC_EXIST')
    SEND_NET_VAR()
    
    if not SIFAUX():
        SAVE_COMM_NET()
    
    EFFLIG(1)

def E_SAVE_COMMAND():
    EV('REC_EXIST')
    SET_NET_STATUS_ERROR()
    SET_NET_RESULT_DATA()

def E_SAVE_COMM_NET():
    if CMPRI('REC_EXIST', 3):
        FV('REC_EXIST', 4)
        SORVIS('NO_SEND')
    
    IV('REC_EXIST')
    SEND_NET_VAR()
    
    if not SIFAUX():
        E_SAVE_COMM_NET()
    
    EFFLIG(1)

def SET_NET_STATUS_INTERUPT():
    SET_NET_STATUS('I')

def SET_NET_STATUS_COMPLETE():
    SET_NET_STATUS('C')

def SET_NET_STATUS_ERROR():
    SET_NET_STATUS('E')

def SET_NET_STATUS(status):
    station = gsm_main.get_var('STATION')
    
    if station == 1:
        FV('STAT_01', status)
    elif station == 2:
        FV('STAT_02', status)
    elif station == 3:
        FV('STAT_03', status)
    elif station == 4:
        FV('STAT_04', status)
    elif station == 5:
        FV('STAT_05', status)
    elif station == 6:
        FV('STAT_06', status)
    elif station == 7:
        FV('STAT_07', status)
    elif station == 8:
        FV('STAT_08', status)
    elif station == 9:
        FV('STAT_09', status)
    elif station == 10:
        FV('STAT_10', status)
    elif station == 11:
        FV('STAT_11', status)
    elif station == 12:
        FV('STAT_12', status)
    elif station == 13:
        FV('STAT_13', status)
    elif station == 14:
        FV('STAT_14', status)
    elif station == 15:
        FV('STAT_15', status)
    elif station == 16:
        FV('STAT_16', status)

def SET_NET_RESULT_DATA():
    EV('RES_DATA')
    TRANSFER('RESULT', 0, 'RES_DATA', 0, 1)
    TRANSFER('COMMA', 0, 'RES_DATA', 1, 1)
    TRANSFER('T1DATA1', 0, 'RES_DATA', 2, 60)
    
    station = gsm_main.get_var('STATION')
    
    if station == 1:
        MV('RES_DATA', 'RSLT_01')
    elif station == 2:
        MV('RES_DATA', 'RSLT_02')
    elif station == 3:
        MV('RES_DATA', 'RSLT_03')
    elif station == 4:
        MV('RES_DATA', 'RSLT_04')
    elif station == 5:
        MV('RES_DATA', 'RSLT_05')
    elif station == 6:
        MV('RES_DATA', 'RSLT_06')
    elif station == 7:
        MV('RES_DATA', 'RSLT_07')
    elif station == 8:
        MV('RES_DATA', 'RSLT_08')
    elif station == 9:
        MV('RES_DATA', 'RSLT_09')
    elif station == 10:
        MV('RES_DATA', 'RSLT_10')
    elif station == 11:
        MV('RES_DATA', 'RSLT_11')
    elif station == 12:
        MV('RES_DATA', 'RSLT_12')
    elif station == 13:
        MV('RES_DATA', 'RSLT_13')
    elif station == 14:
        MV('RES_DATA', 'RSLT_14')
    elif station == 15:
        MV('RES_DATA', 'RSLT_15')
    elif station == 16:
        MV('RES_DATA', 'RSLT_16')

def SET_NET_RESULT_EMPTY():
    station = gsm_main.get_var('STATION')
    
    if station == 1:
        EV('RSLT_01')
    elif station == 2:
        EV('RSLT_02')
    elif station == 3:
        EV('RSLT_03')
    elif station == 4:
        EV('RSLT_04')
    elif station == 5:
        EV('RSLT_05')
    elif station == 6:
        EV('RSLT_06')
    elif station == 7:
        EV('RSLT_07')
    elif station == 8:
        EV('RSLT_08')
    elif station == 9:
        EV('RSLT_09')
    elif station == 10:
        EV('RSLT_10')
    elif station == 11:
        EV('RSLT_11')
    elif station == 12:
        EV('RSLT_12')
    elif station == 13:
        EV('RSLT_13')
    elif station == 14:
        EV('RSLT_14')
    elif station == 15:
        EV('RSLT_15')
    elif station == 16:
        EV('RSLT_16')

def SEND_NET_VAR():
    station = gsm_main.get_var('STATION')
    
    if station == 1:
        ECRVAR('RSLT_01', 'GSM_NET')
        FAUXRET()
        ECRVAR('STAT_01', 'GSM_NET')
        FAUXRET()
    elif station == 2:
        ECRVAR('RSLT_02', 'GSM_NET')
        FAUXRET()
        ECRVAR('STAT_02', 'GSM_NET')
        FAUXRET()
    elif station == 3:
        ECRVAR('RSLT_03', 'GSM_NET')
        FAUXRET()
        ECRVAR('STAT_03', 'GSM_NET')
        FAUXRET()
    elif station == 4:
        ECRVAR('RSLT_04', 'GSM_NET')
        FAUXRET()
        ECRVAR('STAT_04', 'GSM_NET')
        FAUXRET()
    elif station == 5:
        ECRVAR('RSLT_05', 'GSM_NET')
        FAUXRET()
        ECRVAR('STAT_05', 'GSM_NET')
        FAUXRET()
    elif station == 6:
        ECRVAR('RSLT_06', 'GSM_NET')
        FAUXRET()
        ECRVAR('STAT_06', 'GSM_NET')
        FAUXRET()
    elif station == 7:
        ECRVAR('RSLT_07', 'GSM_NET')
        FAUXRET()
        ECRVAR('STAT_07', 'GSM_NET')
        FAUXRET()
    elif station == 8:
        ECRVAR('RSLT_08', 'GSM_NET')
        FAUXRET()
        ECRVAR('STAT_08', 'GSM_NET')
        FAUXRET()
    elif station == 9:
        ECRVAR('RSLT_09', 'GSM_NET')
        FAUXRET()
        ECRVAR('STAT_09', 'GSM_NET')
        FAUXRET()
    elif station == 10:
        ECRVAR('RSLT_10', 'GSM_NET')
        FAUXRET()
        ECRVAR('STAT_10', 'GSM_NET')
        FAUXRET()
    elif station == 11:
        ECRVAR('RSLT_11', 'GSM_NET')
        FAUXRET()
        ECRVAR('STAT_11', 'GSM_NET')
        FAUXRET()
    elif station == 12:
        ECRVAR('RSLT_12', 'GSM_NET')
        FAUXRET()
        ECRVAR('STAT_12', 'GSM_NET')
        FAUXRET()
    elif station == 13:
        ECRVAR('RSLT_13', 'GSM_NET')
        FAUXRET()
        ECRVAR('STAT_13', 'GSM_NET')
        FAUXRET()
    elif station == 14:
        ECRVAR('RSLT_14', 'GSM_NET')
        FAUXRET()
        ECRVAR('STAT_14', 'GSM_NET')
        FAUXRET()
    elif station == 15:
        ECRVAR('RSLT_15', 'GSM_NET')
        FAUXRET()
        ECRVAR('STAT_15', 'GSM_NET')
        FAUXRET()
    elif station == 16:
        ECRVAR('RSLT_16', 'GSM_NET')
        FAUXRET()
        ECRVAR('STAT_16', 'GSM_NET')
        FAUXRET()

def SET_TRUE():
    FV('RESULT', 'Y')

def SET_FALSE():
    FV('RESULT', 'N')

def SET_TRUE_SAVE():
    FV('RESULT', 'Y')
    SAVE_COMMAND()

def SET_FALSE_SAVE():
    FV('RESULT', 'N')
    SAVE_COMMAND()

def SET_INTERUPT_SAVE():
    FV('RESULT', 'I')
    SAVE_INT_COMMAND()

def E_SET_FALSE_SAVE():
    FV('RESULT', 'N')
    E_SAVE_COMMAND()

if __name__ == "__main__":
    # Test the functions and print the global variables
    gsm_main.init_consts()
    gsm_main.init_vars()

    FV("STATION", 1)
    SET_NET_STATUS_COMPLETE()
    FV("STAT_01", "TEST")
    # CMPRI("STAT_01", "TEST")



    print()
    SET_NET_RESULT_DATA()
    print_rslt_variables()
    print()
    
    # Test ECRVAR function
    ECRVAR('STAT_01', 'GSM_NET')
    print()
    print_stat_variables()
    print()
    print_call_params()
    
    # Test SEND_NET_VAR function
    SEND_NET_VAR()
    print_stat_variables()
    print_rslt_variables()
