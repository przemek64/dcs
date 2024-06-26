import time
import os
from gsm_main import get_var, init_vars

# Initialize variables
init_vars()

# List of variables to monitor
variables_to_monitor1 = [
    # Group 1: W1 to W10
    ['W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8', 'W9', 'W10'],
    # Group 2: W11 to W20
    ['W11', 'W12', 'W13', 'W14', 'W15', 'W16', 'W17', 'W18', 'W19', 'W20'],
    # Group 3: W21 to W30
    ['W21', 'W22', 'W23', 'W24', 'W25', 'W26', 'W27', 'W28', 'W29', 'W30'],
    # Group 4: W31 to W40
    ['W31', 'W32', 'W33', 'W34', 'W35', 'W36', 'W37', 'W38', 'W39', 'W40'],
    # Group 5: Rest of Wx
    ['W41', 'W50', 'W60', 'W70', 'W71', 'W72'],
    # Group 6: PFx
    ['PF00', 'PF01', 'PF08', 'PF09', 'PF68', 'PF69', 'PF72', 'PF73'],
]

variables_to_monitor2 = [
    # Group 7: B22 to B31
    ['B22', 'B23', 'B24', 'B25', 'B26', 'B27', 'B28', 'B29', 'B30', 'B31'],
    # Group 8: B32 to B40
    ['B32', 'B33', 'B34', 'B35', 'B36', 'B37', 'B38', 'B39', 'B40'],
    # Group 9: Other variables
    ['CVTASC', 'CVTASC10', 'JBUSNO', 'JBUS', 'STRTEMP', 'JBUSLOOP', 'JBUSSTATUS', 'TMPPRODUCT', 'TMPHEX', 'TMPHEX1', 'TMPHEX8', 'JBUSACTIVATE', 'DISPLAY_LINE', 'LG_BUFFER', 'STAJBUS', 'STALEC', 'STAECR', 'VAR_EFF', 'PFISTER', 'T1DATA1', 'T1DATA2', 'T1VALUE', 'JBUS_ERROR_CODE']
]

def clear_screen():
    # Clear the screen based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

def print_variables(variables_to_monitor):
    max_length = max(len(group) for group in variables_to_monitor)
    for i in range(max_length):
        row_values = []
        for group in variables_to_monitor:
            if i < len(group):
                var = group[i]
                row_values.append(f"{var}: {get_var(var)}")
            else:
                row_values.append(" " * 20)  # Add spacing for alignment
        print(" | ".join(row_values))

def monitor_variables():
    while True:
        clear_screen()
        print("\nVariable Values - Part 1:\n")
        print_variables(variables_to_monitor1)
        
        print("\nVariable Values - Part 2:\n")
        print_variables(variables_to_monitor2)
        
        time.sleep(2)

if __name__ == "__main__":
    monitor_variables()
