import tkinter as tk
from tkinter import ttk
from selection_boxes import selection_boxes

# TODO: create a class for this app

root = tk.Tk()
root.title("Code Generator")
root.geometry("1000x1000")

base_string_list = ["00" for i in range(11)]  # 11 pairs
main_code = tk.Label(root, text=str("".join(base_string_list)), font="Helvetica 15 bold")  # label with base
main_code.grid(row=0, column=2)


def create_drop_down_menu(parent, values, width, row, column, default_index=0, padx=5, pady=5):
    """This function is used inside other functions a lot so find usages using pycharm feature"""
    menu = ttk.Combobox(parent, values=values, width=width, state="readonly")
    menu.grid(row=row, column=column, padx=padx, pady=pady)
    menu.current(default_index)
    return menu


def event_select(event, list_name: list, pair_idx_to_change: int, add_one=True):
    """
    Changes the main code on top of the screen to reflect the choice made by the user - updates in a inf loop
    :param event: binding variable for widget object
    :param list_name: list to pull the indexes from to update the main code (top of the screen)
    :param pair_idx_to_change: index of the pairs which we swap everytime a choice is made. index = list index
    :param add_one: True if there is no N/A value in the list. N/A == 00 in terms of the pair to update
    :return: NOone
    """
    combobox = event.widget
    value = combobox.get()
    idx = str(list_name.index(value) + (1 if add_one else 0))
    base_string_list[pair_idx_to_change] = "0" + str(idx) if len(idx) == 1 else idx
    main_code.config(text="".join(base_string_list))  # this updates the string at the top as the selection is made


def add_element(list_to_append: list, widget_box: object):
    """
    Takes in the information from the entry box and adds it to the list_to_append list, updates the widget box"
    :param list_to_append: data that is pulled by the widget box for selection
    :param widget_box: to update the values inside the widget object
    :return: None
    """
    user_val = entry_widget.get()
    if user_val:
        list_to_append.append(user_val)
        widget_box['values'] = list_to_append
        entry_widget.delete(0, tk.END)


def delete_element(list_to_delete, widget_box):
    pass


# This is the entry widget which will take in the value that we need for the "Add x" button
entry_widget = tk.Entry(root)  # text box to enter elements and append it to the list - updates only when button is
# pressed
entry_widget.grid(row=9, column=2, padx=5, pady=5)

selection_boxes(root, create_drop_down_menu, event_select, add_element)  # different module with all elements

root.mainloop()
