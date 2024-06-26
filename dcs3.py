# dcs3.py

from gsm_main import set_var, get_var
from asm_func import *
from save_com import *
from jbus import *
from dcs4 import *

def SORVIS3():
    print(get_var('DISPLAY_LINE'))

# Main Functions

def DCSCHECKPROD():
    CS3()

    EV('DISPLAY_LINE')
    FV('DISPLAY_LINE', "COMMUNICATING")
    #SORVIS3_3_5_1_24()
    SORVIS3()
    EV('DISPLAY_LINE')
    FV('DISPLAY_LINE', "PLEASE WAIT")
    #SORVIS3_4_6_1_24()
    SORVIS3()

    INITIA_2()
    EV('JBUSLOOP')
    JNOCOMMSMSG()
    
    CVASCBCD('T1DATA2', 5, 'CVTASC')
    CVBCDHEX('CVTASC', 'W3')
    
    TRANSFER('T1DATA1', 25, 'JBUSSTATUS', 0, 1)
    CVASCBCD('JBUSSTATUS', 1, 'CVTASC')
    CVBCDHEX('CVTASC', 'W4')
    
    TRANSFER('T1DATA1', 0, 'W10', 0, 20)
    
    EV('JBUSSTATUS')
    if CMPRI('T1VALUE', 4):
        FV('JBUSSTATUS', 'ACTIVE_OFFLOAD')
        TRANSFER('JBUSSTATUS', 0, 'W20', 0, 14)
    else:
        FV('JBUSSTATUS', 'ACTIVE')
        TRANSFER('JBUSSTATUS', 0, 'W20', 0, 6)

def DCPLOOP():
    TEMPO(20)
    JNOCOMMSMSG()
    EV('JBUSSTATUS')
    TRANSFER('W40', 0, 'JBUSSTATUS', 0, 20)
    if CMPRI('JBUSSTATUS', 'TANKERIN'):
        DCPLOOP_3()
    elif CMPRI('JBUSSTATUS', 'OOS'):
        SETRET0()
    elif CMPRI('JBUSSTATUS', 'ERROR'):
        DCPERROR()
    else:
        DCPLOOP_5()

def DCPLOOP_3():
    JNOCOMMSMSG()
    EV('JBUSSTATUS')
    EV('TMPPRODUCT')
    TRANSFER('W30', 0, 'JBUSSTATUS', 0, 20)
    TRANSFER('W10', 0, 'TMPPRODUCT', 0, 20)
    if CMPR('JBUSSTATUS', 'TMPPRODUCT'):
        SETRET2()
    else:
        DCPLOOP_5()

def DCPLOOP_5():
    EV('JBUSSTATUS')
    JNOCOMMSMSG()
    TRANSFER('W72', 0, 'TMPHEX', 0, 2)
    CVHEXBCD('TMPHEX', 'CVTASC')
    if CMPRI('CVTASC', 0):
        if IFSUP():
            SETRET()
    else:
        IV('JBUSLOOP')
        if CMPRI('JBUSLOOP', 30):
            if IFINF():
                DCPLOOP()

def SETRET0():
    INITIA_2()
    SET_FALSE_SAVE()

def SETRET():
    TRANSFER('W72', 0, 'TMPHEX', 0, 2)
    CVHEXBCD('TMPHEX', 'CVTASC')
    if CMPRI('CVTASC', 1):
        PAUSE1()
    else:
        SETRET1()

def SETRET1():
    TRANSFER('W72', 0, 'TMPHEX', 0, 2)
    CVHEXBCD('TMPHEX', 'CVTASC')
    if CMPRI('CVTASC', 2):
        if SIFAUX():
            SETRETA()
    else:
        EV('DISPLAY_LINE')
        #SORVIS3_4_1_1_24()
        SORVIS3()
        FV('DISPLAY_LINE', "PLEASE WAIT")
        #SORVIS3_4_6_1_24()
        SORVIS3()
        DCPLOOP()

def SETRET2():
    SET_TRUE_SAVE()

def PAUSE1():
    JNOCOMMSMSG()
    FV('DISPLAY_LINE', 'WAITING FOR NEXT TANK')
    #SORVIS3_4_1_1_24()
    SORVIS3()
    DCPLOOP()

def DCPERROR():
    INITIA_2()
    SET_FALSE_SAVE()

def DCSLOAD():
    CS3()
    EV('JBUSLOOP')
    INITIA_3()
    EV('JBUSSTATUS')
    TRANSFER('W40', 0, 'JBUSSTATUS', 0, 20)
    if CMPRI('JBUSSTATUS', 'ERROR'):
        DCPERROR()

    JNOCOMMSMSG()
    FV('JBUSSTATUS', 'LOAD')
    TRANSFER('JBUSSTATUS', 0, 'W20', 0, 4)
    DCSLOAD_1()

def DCSLOAD_1():
    JNOCOMMSMSG()
    TEMPO(10)
    TRANSFER('W40', 0, 'JBUSSTATUS', 0, 20)
    if CMPRI('JBUSSTATUS', 'LOADING'):
        DCLLOOP()
    else:
        IV('JBUSLOOP')
        if CMPRI('JBUSLOOP', 30):
            if IFINF():
                DCSLOAD_1()
        INITIA_2()
        SET_FALSE_SAVE()

def DCLLOOP():
    FV('JBUSSTATUS', 'LOADING')
    TRANSFER('JBUSSTATUS', 0, 'W20', 0, 7)
    DISPSTATUS()

def DISPSTATUS():
    JNOCOMMSMSG()
    TRANSFER('W71', 0, 'TMPHEX', 0, 'WORD')
    CVHEXBCD('TMPHEX', 'CVTASC')
    SORVAR3_3_8_1_CVTASC()
    FV('DISPLAY_LINE', 'KG')
    #SORVIS3_3_15_1_2()
    SORVIS3()
    EV('JBUSSTATUS')
    TRANSFER('W40', 0, 'JBUSSTATUS', 0, 20)
    EV('DISPLAY_LINE')
    MV('JBUSSTATUS', 'DISPLAY_LINE')
    #SORVIS3_4_1_1_20()
    SORVIS3()
    EV('JBUSSTATUS')
    TRANSFER('W50', 0, 'JBUSSTATUS', 0, 20)
    EV('DISPLAY_LINE')
    MV('JBUSSTATUS', 'DISPLAY_LINE')
    #SORVIS3_5_1_1_20()
    SORVIS3()
    TRANSFER('W40', 0, 'STRTEMP', 0, 20)
    if CMPRI('STRTEMP', 'LOADED'):
        DCLRETTRUE()
    elif CMPRI('STRTEMP', 'PAUSE'):
        DCLPAUSE1()
    elif CMPRI('STRTEMP', 'LOADING'):
        DCLPAUSECLR()
    elif CMPRI('STRTEMP', 'ERROR'):
        DCLERROR()
    elif CMPRI('STRTEMP', 'IDLE'):
        DCLERROR()
    else:
        DISPSTATUS()

def DCLPAUSECLR():
    EV('DISPLAY_LINE')
    #SORVIS3_2_1_1_24()
    SORVIS3()
    DISPSTATUS()

def DCLRETTRUE():
    CS3()
    RETTRUE()

def RETTRUE():
    TRANSFER('W60', 0, 'T1DATA1', 0, 20)
    SET_TRUE_SAVE()

def DCLERROR():
    INITIA_2()
    FV('JBUSSTATUS', 'IDLE')
    TRANSFER('JBUSSTATUS', 0, 'W20', 0, 4)
    SET_FALSE_SAVE()

def DCLPAUSE1():
    CS3()
    EV('DISPLAY_LINE')
    FV('DISPLAY_LINE', "SEQUENCE HELD")
    DCLPAUSE()
