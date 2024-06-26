import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_tcp
import threading
import tkinter as tk
import pandas as pd
from tkinter import ttk

class ModbusSlaveGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Modbus TCP Slave")
        self.master.geometry("800x1000")  # Set window size to 800x800
        
        self.tree = ttk.Treeview(master, columns=('Offset', 'Wx', 'Description', 'Value'), show='headings')
        self.tree.heading('Offset', text='Offset')
        self.tree.heading('Wx', text='Wx')
        self.tree.heading('Description', text='Description')
        self.tree.heading('Value', text='Value')
        
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Adjust font size
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 8))
        style.configure("Treeview", font=("Arial", 8))

        self.descriptions = [
            "SET_BI300_STATUS", "Number of Bags", "Number of Stacks",
            "Requested Stack 1", "Requested Stack 2", "Requested Stack 3", "Requested Stack 4", "Requested Stack 5", "Requested Stack 6",
            "Requested Stack 7", "Requested Stack 8", "Requested Stack 9", "Requested Stack 10", "Requested Stack 11", "Requested Stack 12",
            "Requested Stack 13", "Requested Stack 14", "Requested Stack 15", "Requested Stack 16", "Requested Stack 17", 
            "PLC_STATUS", "Number of Bags", "Number of Stacks",
            "Loaded Stack 1", "Loaded Stack 2", "Loaded Stack 3", "Loaded Stack 4", "Loaded Stack 5", "Loaded Stack 6",
            "Loaded Stack 7", "Loaded Stack 8", "Loaded Stack 9", "Loaded Stack 10", "Loaded Stack 11", "Loaded Stack 12",
            "Loaded Stack 13", "Loaded Stack 14", "Loaded Stack 15", "Loaded Stack 16", "Loaded Stack 17", 
            "PLC_ERROR"
        ]
        
        self.offsets = list(range(1, 42))  # Start from W2 to W42
        self.df = pd.DataFrame(columns=['Offset', 'Wx', 'Description', 'Value'])
        self.df['Offset'] = self.offsets
        self.df['Wx'] = [f"W{offset}" for offset in self.offsets]
        self.df['Description'] = self.descriptions
        self.df['Value'] = [0] * 41
        
        for _, row in self.df.iterrows():
            self.tree.insert('', 'end', values=row.tolist())
        
        self.slave = None
        self.server_thread = threading.Thread(target=self.run_modbus_server)
        self.server_thread.daemon = True
        self.server_thread.start()
        
        self.master.after(1000, self.update_gui)

    def run_modbus_server(self):
        self.server = modbus_tcp.TcpServer(port=502)

        # Add a slave
        slave_id = 1
        self.slave = self.server.add_slave(slave_id)

        # Add holding registers (address 0 to 40 for 41 WORDs)
        self.slave.add_block('0', cst.HOLDING_REGISTERS, 0, 41)

        # Set initial values for the holding registers
        initial_values = [0] * 41
        self.slave.set_values('0', 0, initial_values)
        
        # Start the server
        self.server.start()
        
        print("Modbus TCP slave is running on 0.0.0.0:502...")
        
    def update_gui(self):
        if self.slave:
            current_values = self.slave.get_values('0', 0, 41)
            for i in range(20):
                if current_values[i] != self.df.at[i, 'Value']:
                    self.df.at[i, 'Value'] = current_values[i]
                    self.tree.item(self.tree.get_children()[i], values=self.df.iloc[i].tolist())
                    self.tree.item(self.tree.get_children()[i + 20], values=self.df.iloc[i + 20].tolist())
                    self.tree.tag_configure(f'changed{i}', background='yellow')
                    self.tree.item(self.tree.get_children()[i], tags=(f'changed{i}',))
                    self.tree.item(self.tree.get_children()[i + 20], tags=(f'changed{i + 20}',))
                    self.master.after(1000, self.remove_highlight, i)
                    self.master.after(1000, self.remove_highlight, i + 20)
                else:
                    self.df.at[i, 'Value'] = current_values[i]
                    self.tree.item(self.tree.get_children()[i], values=self.df.iloc[i].tolist())
                    self.tree.item(self.tree.get_children()[i + 20], values=self.df.iloc[i + 20].tolist())
        self.master.after(1000, self.update_gui)
        
    def remove_highlight(self, index):
        self.tree.tag_configure(f'changed{index}', background='')
        self.tree.item(self.tree.get_children()[index], tags=(''))

    def on_closing(self):
        print("Stopping the Modbus TCP slave...")
        if self.server:
            self.server.stop()
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ModbusSlaveGUI(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
