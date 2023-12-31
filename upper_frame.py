import pyodbc
import tkinter as tk
from tkinter import ttk
from main_specs import certs_dict 
from tkinter import simpledialog
from tkinter import messagebox

class UpperFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.base_string_list = ["00" for i in range(11)]
        self.submit_list = []
        self.combobox_list = []

        self.create_main_widget()  # all other widgets change the value of this one
        self.create_all_widgets()
        
        self.focus_force()  # brings the window into focus of the user without needing to click
        
    def create_all_widgets(self):
        """Creates a Label and calls the make selection box. Label has the same name as the List that Combobox pulls data from"""
        # TODO: we need to change this and add a parameter to make another app
        for idx, key in enumerate(certs_dict.keys()):
            tk.Label(self, text=f"Select {key.upper()}").grid(row=idx+1, column=1)  # Column 1 = all the headings (labels)
            self.combobox_list.append(self.make_selection_box(certs_dict[key], idx+1, 2, idx))  # Column 2 = selection box (combo box)
        self.submitted_vals_list_box()

    def create_main_widget(self):
        """Creates the Main Text Box at the top of the screen that can be copied and pasted anywhere"""
        self.text_widget = tk.Text(self, height=1, width=22, font="Helvetica 15 bold", state="disabled")
        self.text_widget.insert("1.0", "".join(self.base_string_list))
        self.text_widget.grid(row=0, column=2, padx=20, pady=10)

    def set_main_widget(self, updated_string):
        """base string widget modifier"""
        self.text_widget.config(state="normal")
        self.text_widget.delete("1.0", tk.END)
        self.text_widget.insert("1.0", updated_string)
        self.text_widget.config(state="disabled")

    def make_selection_box(self, item_list, row, column, idx_change): # currently builds the box and places it on the grid 
        """item list -> list from specs list to pull data from for selection widget
            idx change -> which idx gets updated in the base string list shown at the very top of the screen"""
        combo_box = ttk.Combobox(self, values=item_list, width=30, state="readonly")
        combo_box.grid(row=row, column=column, padx=5, pady=5)
        combo_box.bind("<<ComboboxSelected>>", lambda event : self.event_handler(event, item_list, idx_change))
        return combo_box

    def event_handler(self, event, item_list, pair_idx_to_change):
        """Updates the string value as the user makes selection"""
        value = event.widget.get()
        idx = str(item_list.index(value))  # finding the idx in the list of the given combobox
        idx_replace = "0" + idx if len(idx) == 1 else idx  # idx becomes double digit string eg. "01", "10"
        self.base_string_list[pair_idx_to_change] = idx_replace  # replace the string in the main list
        self.set_main_widget("".join(self.base_string_list))  # update the widget value

    def get_code_update_box(self):
        """Updates the Finish Code according the user selection, displays error message if invalid selection"""
        code = self.text_widget.get("1.0", tk.END)
        try:
            if code[1] == "0":
                messagebox.showerror("Empty Code", message="Code is Null")
            elif code in self.submit_list:
                messagebox.showerror("Code already submitted")
            else:
                self.submit_list.append(code)
            self.update_list_box()  # updates the submitted vals list box
        except IndexError:
            messagebox.showerror("No Input", message="The field is empty")

    def submitted_vals_list_box(self):
        self.box = tk.Listbox(self, font="helvetica 12 bold", height=20, width=22)
        self.box.grid(row=1, column=4, padx=20, rowspan=10, columnspan=1)
        tk.Button(self, text="submit", command=self.get_code_update_box).grid(row=11, column=2)
            
    def update_list_box(self):
        """Updates the submitted values list box - on the left side of the screen"""
        self.box.delete(0, tk.END)
        for i in self.submit_list:
           self.box.insert(tk.END, i)  # deletes everything and updates the box 
           # clear the top box 

    def search_data_mie_trak(search_value):
        """Searches Mie Trak and prints the results to the terminal"""
        connection_string = "DRIVER={SQL Server};SERVER=ETZ-SQL;DATABASE=ETEZAZIMIETrakLive;Trusted_Connection=yes;"
        conn = pyodbc.connect(connection_string)
        if conn:
            print("connected")
        cursor = conn.cursor()
        query = f"""SELECT *
                    FROM ItemClass
                    WHERE ItemClassPk IN (
                        SELECT ItemClassFK
                        FROM item
                        WHERE PartNumber LIKE ? 
                    );"""
        params = [f'%{search_value}%']
        cursor.execute(query, params)
        rows = cursor.fetchall()
        conn.close()
        return rows

    def update_selection_box(self, combobox_index_num, value_to_append, list_name):
        certs_dict[list_name].append(value_to_append)
        self.combobox_list[combobox_index_num]['values'] = certs_dict[list_name]
    