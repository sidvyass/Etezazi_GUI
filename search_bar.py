import pyodbc
import tkinter as tk
from tkinter import ttk

class SearchSQL(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x1000")
        self.title("Part Number Search")
        self.results_list = []
        self.bar_widget()
        self.display_widget()
        self.search_button()
        
    def bar_widget(self):
        self.combobox = ttk.Entry(self, width=50) 
        self.combobox.pack()
    
    def display_widget(self):
        frame = tk.Frame(self)
        frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        self.list_box = tk.Listbox(frame, width=100)
        self.scroll_bar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=self.list_box.yview)
        self.list_box.configure(yscrollcommand=self.scroll_bar.set)
        
        self.list_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)

    def search_button(self):
        self.s_button = tk.Button(self, text="Search", command=self.get_data)
        self.s_button.pack()
    
    def get_data(self):
        search_var = self.combobox.get()
        conn_string = "DRIVER={SQL Server};SERVER=ETZ-SQL;DATABASE=ETEZAZIMIETrakLive;Trusted_Connection=yes;"
        conn = pyodbc.connect(conn_string)
        cursor = conn.cursor()
        
        query2 = """SELECT PartNumber  
                    FROM item
                    WHERE PartNumber LIKE ? """
        params = [f'%{search_var}%'] 
        cursor.execute(query2, params)
        self.results_list = [row[0] for row in cursor.fetchall()]        

        self.list_box.delete(0, 'end')  # updating the listbox when the button is pressed
        for item in self.results_list:
            self.list_box.insert('end', item)
        
if __name__ == "__main__":
    bar = SearchSQL()
    bar.mainloop()
