# gsm_list_globalvars.py

from gsm_main import get_var

def print_system_variables():
    print("System Variables:")
    print(f"DAY: {get_var('DAY')}")
    print(f"MONTH: {get_var('MONTH')}")
    print(f"YEAR: {get_var('YEAR')}")
    print(f"HOUR: {get_var('HOUR')}")
    print(f"MINUTE: {get_var('MINUTE')}")
    print(f"SECOND: {get_var('SECOND')}")
    print(f"ANSWER: {get_var('ANSWER')}")
    print(f"VOIDIA: {get_var('VOIDIA')}")
    print(f"VOIIMP: {get_var('VOIIMP')}")
    print(f"VOICON: {get_var('VOICON')}")
    print(f"CLACON: {get_var('CLACON')}")
    print(f"LPLACE: {get_var('LPLACE')}")
    print(f"LANGUAGE: {get_var('LANGUAGE')}")
    print(f"LOCSERV: {get_var('LOCSERV')}")
    print(f"DEFSERV: {get_var('DEFSERV')}")

def print_global_variable_declarations():
    print("Global Variable Declarations:")
    variables = [
        "STATION", "DISPWT", "JBUSNO", "PFISTER", "REC_EXIST", "RES_DATA", 
        "MESSAGE", "TOPLINE", "MIDLINE", "BOTLINE", "HALF_LINE1", "HALF_LINE2", 
        "TMP_PRINT", "TMP_HALF", "TIMER", "RESULT", "COMMA", "TARGET_WEI", 
        "STAIMP", "PAPER_OUT", "SPOT_VER", "TIMER_STARTED", "INTERRUPT_FUNC", 
        "MCR_MOT_BADGE", "MACH", "NET_MSG_TOP_LINE", "NET_MSG_BOT_LINE", 
        "CARACTERE", "DATA_IN_BUF", "MAX_SAI", "PREFIXE", "TYPE_SAI", 
        "ETAT_SAI", "CPT", "OFFSET", "oWATCHDOG", "JBUSACTIVE1", "JBUSACTIVE", 
        "STAJBUS", "STALEC", "STAECR", "WATCHDOG"
    ]
    for var in variables:
        print(f"{var}: {get_var(var)}")

def print_jbus_record():
    print("JBUS Record:")
    variables = [f"W{i}" for i in range(1, 42)] + ["W50", "W60", "W70", "W71", "W72"]
    for var in variables:
        print(f"{var}: {get_var(var)}")

def print_pfister_record():
    print("Pfister Record:")
    variables = ["PF00", "PF01", "PF08", "PF09", "PF68", "PF69", "PF72", "PF73"]
    for var in variables:
        print(f"{var}: {get_var(var)}")

def print_stat_variables():
    print("Status Network Variables:")
    for i in range(1, 17):
        var = f"STAT_{i:02d}"
        print(f"{var}: {get_var(var)}")

def print_rslt_variables():
    print("Result String Network Variables:")
    for i in range(1, 17):
        var = f"RSLT_{i:02d}"
        print(f"{var}: {get_var(var)}")

def print_call_params():
    print("Call Parameters:")
    print(f"T1DATA1: {get_var('T1DATA1')}")
    print(f"T1DATA2: {get_var('T1DATA2')}")
    print(f"T1VALUE: {get_var('T1VALUE')}")

if __name__ == "__main__":
    print_system_variables()
    print()
    print_global_variable_declarations()
    print()
    print_jbus_record()
    print()
    print_pfister_record()
    print()
    print_stat_variables()
    print()
    print_rslt_variables()
    print()
    print_call_params()
