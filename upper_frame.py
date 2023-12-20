import tkinter as tk
from tkinter import ttk
from specs import certs_dict 

class UpperFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_all_widgets()
        self.base_string_list = ["00" for i in range(11)]
        self.create_main_widget()

    def create_main_widget(self):
        """Creates the Main Text Box at the top of the screen that can be copied and pasted anywhere"""
        self.text_widget = tk.Text(self, height=1, width=22, font="Helvetica 15 bold")
        self.text_widget.insert("1.0", "".join(self.base_string_list))
        self.text_widget.grid(row=0, column=3, padx=10, pady=10)

    def set_main_widget_value(self, updated_string):
        """base string widget modifier"""
        self.text_widget.config(state="normal")
        self.delete("1.0", tk.END)
        self.insert(updated_string)
        self.config(state="diabled")

    def make_selection_box(self, item_list, row, column, idx_change): # currently builds the box and places it on the grid 
        """item list -> list from specs list to pull data from for selection widget
            idx change -> which idx gets updated in the base string list shown at the very top of the screen"""
        combo_box = ttk.Combobox(self, values=item_list, width=30, state="readonly")
        combo_box.grid(row=row, column=column, padx=5, pady=5)
        combo_box.bind("<<ComboBoxSelected>>", lambda event : self.event_handler(event, item_list, idx_change))

    def event_handler(self, event, item_list, pair_idx_to_change):
        value = event.widget.get()
        idx = str(item_list.index(value))  # finding the idx in the list of the given combobox
        idx_replace = "0" + idx if len(idx) == 1 else idx  # idx becomes double digit string eg. "01", "10"
        self.base_string_list[pair_idx_to_change] = idx_replace  # replace the string in the main list
        self.set_main_widget_value("".join(self.base_string_list))  # update the widget value

    def create_all_widgets(self):
        pass        
