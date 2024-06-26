import os
import json
import time
import threading

MEMORY_DIR = 'MEMORY'

# Ensure MEMORY_DIR exists
if not os.path.exists(MEMORY_DIR):
    os.makedirs(MEMORY_DIR)

def read_memory(var_name):
    file_path = os.path.join(MEMORY_DIR, f'{var_name}.json')
    while True:
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return None
        except IOError:
            time.sleep(0.01)  # Wait and retry if the file is being written to

def write_memory(var_name, value):
    file_path = os.path.join(MEMORY_DIR, f'{var_name}.json')
    with open(file_path, 'w') as f:
        json.dump(value, f, indent=4)

def get_var(var_name):
    return read_memory(var_name)

def set_var(var_name, value):
    write_memory(var_name, value)

def init_consts():
    # Global variable definitions
    global T1REQUEST, T2SPOOLER
    T1REQUEST = 2
    T2SPOOLER = 20

    # Serial Channel Assignment
    global CONSOLE, BI300, GSM_NET, JBUS, DL3, MONITOR, INDICATOR
    CONSOLE = 1
    BI300 = 2  # LCD Cabinet Display
    # TP2000 = 2  # WEIGHT INDICATOR
    GSM_NET = 3  # Tally Line Printer
    JBUS = 4
    DL3 = 4  # WYSE TERMINAL
    MONITOR = 5  # WYSE TERMINAL
    INDICATOR = 6

    # Input I/O Assignment
    global INPUT0, INPUT1, INPUT2, INPUT3, INPUT4, INPUT5, INPUT6, INPUT7
    INPUT0 = 0
    INPUT1 = 1
    INPUT2 = 2
    INPUT3 = 3
    INPUT4 = 4
    INPUT5 = 5
    INPUT6 = 6
    INPUT7 = 7

    # Output I/O Assignment
    global OUTPUT0, OUTPUT1, OUTPUT2, OUTPUT3, OUTPUT4, OUTPUT5, OUTPUT6, OUTPUT7
    OUTPUT0 = 8
    OUTPUT1 = 9
    OUTPUT2 = 10
    OUTPUT3 = 11
    OUTPUT4 = 12
    OUTPUT5 = 13
    OUTPUT6 = 14
    OUTPUT7 = 15

    global FORCEWORD, FORCEBYTE
    FORCEWORD = 0x80
    FORCEBYTE = 0x40
    
    global MODBUS_MODE
    #MODBUS_MODE = 0 # JBUS
    #JBUS = 16 #Com port
    
    MODBUS_MODE = 1 # TCP
    #JBUS = network 
   

def init_vars():
    # System Variables
    set_var('DAY', 0)
    set_var('MONTH', 0)
    set_var('YEAR', 0)
    set_var('HOUR', 0)
    set_var('MINUTE', 0)
    set_var('SECOND', 0)

    set_var('ANSWER', "")
    set_var('VOIDIA', 0)
    set_var('VOIIMP', 0)
    set_var('VOICON', 0)
    set_var('CLACON', "")
    set_var('LPLACE', 0)
    set_var('LANGUAGE', "")

    set_var('LOCSERV', "")
    set_var('DEFSERV', 0)

    # Global Variable Declarations
    set_var('STATION', 0)
    set_var('DISPWT', 0)
    set_var('JBUSNO', 0)
    set_var('PFISTER', 0)
    set_var('REC_EXIST', 0)

    set_var('RES_DATA', " " * 80)
    set_var('MESSAGE', " " * 80)
    set_var('TOPLINE', " " * 25)
    set_var('MIDLINE', " " * 25)
    set_var('BOTLINE', " " * 25)

    set_var('HALF_LINE1', " " * 20)
    set_var('HALF_LINE2', " " * 20)
    set_var('TMP_PRINT', " " * 69)
    set_var('TMP_HALF', " " * 34)

    set_var('TIMER', 0)
    set_var('RESULT', "")
    set_var('COMMA', "")
    set_var('TARGET_WEI', 0)
    set_var('STAIMP', 0)
    set_var('PAPER_OUT', "")
    set_var('SPOT_VER', " " * 5)

    set_var('TIMER_STARTED', 0)
    set_var('INTERRUPT_FUNC', 0)
    set_var('MCR_MOT_BADGE', 0)
    set_var('MACH', 0)

    set_var('NET_MSG_TOP_LINE', " " * 38)
    set_var('NET_MSG_BOT_LINE', " " * 38)
    set_var('CARACTERE', "")
    set_var('DATA_IN_BUF', " " * 38)

    set_var('MAX_SAI', 0)
    set_var('PREFIXE', 0)
    set_var('TYPE_SAI', 0)
    set_var('ETAT_SAI', "")
    set_var('CPT', 0)
    set_var('OFFSET', 0)
    set_var('oWATCHDOG', 0)

    set_var('JBUSACTIVE1', 0)
    set_var('JBUSACTIVE', 0)
    set_var('STAJBUS', "")
    set_var('STALEC', "")
    set_var('STAECR', "")
    set_var('WATCHDOG', 0)

    # Status Network Variables
    for i in range(1, 17):
        set_var(f'STAT_{i:02d}', "")

    # Result String Network Variables
    for i in range(1, 17):
        set_var(f'RSLT_{i:02d}', " " * 80)

    # JBUS RECORD
    for i in range(1, 42):
        set_var(f'W{i}', 0)
    set_var('W50', 0)
    set_var('W60', 0)
    set_var('W70', 0)
    set_var('W71', 0)
    set_var('W72', 0)

    # Pfister record
    set_var('PF00', 0)
    set_var('PF01', 0)
    set_var('PF08', 0)
    set_var('PF09', 0)
    set_var('PF68', 0)
    set_var('PF69', 0)
    set_var('PF72', 0)
    set_var('PF73', 0)

    set_var('AFILLER', [""] * 50)

    set_var('CVTASC', 0)
    set_var('CVTASC1', 0)
    set_var('CVTASC10', 0)
    set_var('STRTEMP', " " * 20)
    set_var('JBUSLOOP', 0)
    set_var('JBUSSTATUS', " " * 20)
    set_var('TMPPRODUCT', " " * 20)
    set_var('TMPHEX', "")
    set_var('TMPHEX1', "")
    set_var('TMPHEX8', "")
    set_var('VAR_EFF', "")
    
    set_var('JBUSACTIVATE', 0)
    
    # CALL PARAMS
    set_var('T1DATA1', "")
    set_var('T1DATA2', "")
    set_var('T1VALUE', 0)
    
    set_var('DISPLAY_LINE', " " * 20)
