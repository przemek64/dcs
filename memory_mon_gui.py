import tkinter as tk
from tkinter import ttk
from gsm_main import get_var, init_vars
import threading
import time

# Initialize variables
init_vars()

# Updated list of variables to monitor with shorter descriptions
variables_to_monitor1 = [
    # Group 1: W1 to W10
    ['(W1) SET_BI300_STATUS', 'W1'],
    ['(W2) No. of Bags', 'W2'],
    ['(W3) No. of Stacks', 'W3'],
    ['(W4) Req. Stack 1', 'W4'],
    ['(W5) Req. Stack 2', 'W5'],
    ['(W6) Req. Stack 3', 'W6'],
    ['(W7) Req. Stack 4', 'W7'],
    ['(W8) Req. Stack 5', 'W8'],
    ['(W9) Req. Stack 6', 'W9'],
    ['(W10) Req. Stack 7', 'W10'],
    ['(W11) Req. Stack 8', 'W11'],
    ['(W12) Req. Stack 9', 'W12'],
    ['(W13) Req. Stack 10', 'W13'],
    ['(W14) Req. Stack 11', 'W14'],
    ['(W15) Req. Stack 12', 'W15'],
    ['(W16) Req. Stack 13', 'W16'],
    ['(W17) Req. Stack 14', 'W17'],
    ['(W18) Req. Stack 15', 'W18'],
    ['(W19) Req. Stack 16', 'W19'],
    ['(W20) Req. Stack 17', 'W20'],
    # Group 3: W21 to W30
    ['(W21) PLC_STATUS', 'W21'],
    ['(W22) No. of Bags', 'W22'],
    ['(W23) No. of Stacks', 'W23'],
    ['(W24) Ldd. Stack 1', 'W24'],
    ['(W25) Ldd. Stack 2', 'W25'],
    ['(W26) Ldd. Stack 3', 'W26'],
    ['(W27) Ldd. Stack 4', 'W27'],
    ['(W28) Ldd. Stack 5', 'W28'],
    ['(W29) Ldd. Stack 6', 'W29'],
    ['(W30) Ldd. Stack 7', 'W30'],
    # Group 4: W31 to W40
    ['(W31) Ldd. Stack 8', 'W31'],
    ['(W32) Ldd. Stack 9', 'W32'],
    ['(W33) Ldd. Stack 10', 'W33'],
    ['(W34) Ldd. Stack 11', 'W34'],
    ['(W35) Ldd. Stack 12', 'W35'],
    ['(W36) Ldd. Stack 13', 'W36'],
    ['(W37) Ldd. Stack 14', 'W37'],
    ['(W38) Ldd. Stack 15', 'W38'],
    ['(W39) Ldd. Stack 16', 'W39'],
    ['(W40) Ldd. Stack 17', 'W40'],
    # Group 5: Rest of Wx
    ['(W41) PLC_ERROR', 'W41'],
    ['(W50)', 'W50'],
    ['(W60)', 'W60'],
    ['(W70)', 'W70'],
    ['(W71)', 'W71'],
    ['(W72)', 'W72'],
    # Group 6: PFx
    ['(PF00)', 'PF00'],
    ['(PF01)', 'PF01'],
    ['(PF08)', 'PF08'],
    ['(PF09)', 'PF09'],
    ['(PF68)', 'PF68'],
    ['(PF69)', 'PF69'],
    ['(PF72)', 'PF72'],
    ['(PF73)', 'PF73']
]

variables_to_monitor2 = [
    # Group 7: B22 to B31
    ['B22', 'B22'], ['B23', 'B23'], ['B24', 'B24'], ['B25', 'B25'], ['B26', 'B26'], ['B27', 'B27'], ['B28', 'B28'], ['B29', 'B29'], ['B30', 'B30'], ['B31', 'B31'],
    # Group 8: B32 to B40
    ['B32', 'B32'], ['B33', 'B33'], ['B34', 'B34'], ['B35', 'B35'], ['B36', 'B36'], ['B37', 'B37'], ['B38', 'B38'], ['B39', 'B39'], ['B40', 'B40'],
    # Group 9: Other variables
    ['CVTASC', 'CVTASC'], ['CVTASC10', 'CVTASC10'], ['JBUSNO', 'JBUSNO'], ['JBUS', 'JBUS'], ['STRTEMP', 'STRTEMP'], ['JBUSLOOP', 'JBUSLOOP'], ['JBUSSTATUS', 'JBUSSTATUS'], ['TMPPRODUCT', 'TMPPRODUCT'], 
    # ----
    ['TMPHEX', 'TMPHEX'], ['TMPHEX1', 'TMPHEX1'], ['TMPHEX8', 'TMPHEX8'], ['JBUSACTIVATE', 'JBUSACTIVATE'], ['LG_BUFFER', 'LG_BUFFER'], ['STAJBUS', 'STAJBUS'], ['STALEC', 'STALEC'],
    # ----
    ['STAECR', 'STAECR'], ['VAR_EFF', 'VAR_EFF'], ['PFISTER', 'PFISTER'], ['T1DATA1', 'T1DATA1'], ['T1DATA2', 'T1DATA2'], ['T1VALUE', 'T1VALUE'], ['JBUS_ERROR_CODE', 'JBUS_ERROR_CODE']
]

previous_values = {}

def update_labels(labels, variables_to_monitor):
    for i in range(len(variables_to_monitor)):
        description, var_name = variables_to_monitor[i]
        current_value = get_var(var_name)
        previous_value = previous_values.get(var_name)
        
        if current_value != previous_value:
            labels[i].config(text=f"{description}: {current_value}", background="yellow")
            previous_values[var_name] = current_value
            labels[i].after(1000, lambda lbl=labels[i]: lbl.config(background="white"))
        else:
            labels[i].config(text=f"{description}: {current_value}")

def refresh_labels(display_text, labels1, labels2):
    while True:
        display_line = get_var('DISPLAY_LINE')
        
        display_text.config(state=tk.NORMAL)
        display_text.delete(1.0, tk.END)
        display_text.insert(tk.END, display_line)
        display_text.config(state=tk.DISABLED)
        
        update_labels(labels1, variables_to_monitor1)
        update_labels(labels2, variables_to_monitor2)
        time.sleep(2)

def create_grid(frame, variables_to_monitor):
    labels = []
    for i in range(len(variables_to_monitor)):
        lbl = ttk.Label(frame, text="", width=50)
        lbl.grid(row=i % 15, column=i // 15, padx=5, pady=2)
        labels.append(lbl)
    return labels

def main():
    root = tk.Tk()
    root.title("Variable Monitor")

    display_frame = ttk.Frame(root)
    display_frame.grid(row=0, column=0, padx=10, pady=10)
    
    frame0 = ttk.LabelFrame(root, text="DISPLAY_MESSAGE")
    frame0.grid(row=1, column=0, padx=10, pady=10)
    
    display_text = tk.Text(frame0, height=4, width=120, state=tk.DISABLED)
    display_text.pack()
    
    frame1 = ttk.LabelFrame(root, text="Part 1")
    frame1.grid(row=2, column=0, padx=10, pady=10)
    labels1 = create_grid(frame1, variables_to_monitor1)
    
    frame2 = ttk.LabelFrame(root, text="Part 2")
    frame2.grid(row=3, column=0, padx=10, pady=10)
    labels2 = create_grid(frame2, variables_to_monitor2)
    
    threading.Thread(target=refresh_labels, args=(display_text, labels1, labels2), daemon=True).start()
    
    root.mainloop()

if __name__ == "__main__":
    main()
