from functions.jsonMain import *

import tkinter as tk 
import tkinter.scrolledtext as st 

checkbox_list_updated = list(filter(None, checkbox_list))
checked_checkboxes = []
#translated_checked_checboxes = []
translated_checked_checboxes = ['batters.batter.id', 'batters.batter.type', 'batters']

def create_checkboxes(values, parent_frame):
    for value in values:
        string_var = tk.StringVar()
        cb = tk.Checkbutton(parent_frame, text=value, variable=string_var, onvalue=value, offvalue='')
        cb.pack(anchor='w')
        checked_checkboxes.append(string_var)
        print(string_var)

def confirm():
    translated_checked_checboxes.clear()
    checked_frame.configure(state='normal')
    checked_frame.delete('1.0', tk.END)  # Clear existing content
    for string_var in checked_checkboxes:
        text = string_var.get()
        if text:
            translated_checked_checboxes.append(text)
    # Update the checked_frame with the updated list of checked checkboxes
    for item in translated_checked_checboxes:
        checked_frame.insert(tk.END, item + '\n')
    print("translated_checked_checboxes", translated_checked_checboxes)
    checked_frame.configure(state='disabled')

#
window = tk.Tk()
window.geometry("700x700")
window.title("Checkboxes for Values")

#
checkbox_frame = tk.Listbox(window)
checkbox_frame.pack(padx=10, pady=10, side='left', fill='both')
create_checkboxes(checkbox_list_updated, checkbox_frame)

#
checked_frame = tk.Text(window, height=5, width=30)
checked_frame.pack(fill='both', expand=True, padx=10, pady=10) 

#
kinnitaBtn = tk.Button(window, text="Kinnita valik", command=confirm)
kinnitaBtn.pack(fill='both', padx=10, pady=10)

#
json_frame = st.ScrolledText(window, state='normal', height=50, width=70)
json_frame.pack(padx = 10, pady = 10)
json_frame.insert('1.0', str(json_str))
json_frame.configure(state ='disabled')  

window.mainloop() 

