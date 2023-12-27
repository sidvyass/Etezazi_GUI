import tkinter as tk
from tkinter import ttk
from upper_frame import UpperFrame
import pyodbc
from main_specs import certs_dict

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x1000")
        self.title("Code Generator")
        self.create_widgets()
            
    def create_widgets(self):
        # here we add another frame which will ask the user which kind of app it wants to open
        # heat treat or op finsih
        self.upper_frame = UpperFrame(self)
        self.upper_frame.pack(side="top", fill="both", expand=True)
        
    def update_upper_frame_combobox(self, value_to_append, combobox_index_num):
        enumerated_dict = list(certs_dict.keys())
        certs_dict[enumerated_dict[combobox_index_num]].append(value_to_append)
        self.upper_frame.combobox_list[combobox_index_num]['values'] = certs_dict[enumerated_dict[combobox_index_num]]

    @staticmethod
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
        if len(rows) > 0:
            for row in rows:
                print(row)
        else:
            print("No elements found")
        conn.close()

if __name__ == "__main__":
    app = MainApplication()
    app.update_upper_frame_combobox("sid", 0)
    app.mainloop()