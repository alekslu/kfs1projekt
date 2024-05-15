from functions.jsonMain import *

import tkinter as tk 
import tkinter.scrolledtext as st 

checkbox_list_updated = list(filter(None, checkbox_list))
checked_checkboxes = []
translated_checked_checboxes = []

def create_checkboxes(values, parent_frame):
    for value in values:
        string_var = tk.StringVar()
        cb = tk.Checkbutton(parent_frame, text=value, variable=string_var, onvalue=value, offvalue='')
        cb.pack(anchor='w')
        checked_checkboxes.append(string_var)
        print("07052024-01",string_var)

def confirm():
    translated_checked_checboxes.clear()
    checked_frame.configure(state='normal')
    checked_frame.delete('1.0', tk.END)  # Clear existing content
    for string_var in checked_checkboxes:
        text = string_var.get()
        if text:
            translated_checked_checboxes.append(text)
    # Update the checked_frame with the values corresponding to the selected checkboxes
    for checkbox_value in translated_checked_checboxes:
        # Iterate over the JSON data
        for item in json_data:
            # Get the value of the checkbox recursively
            value = get_nested_values(item, checkbox_value)
            if value is not None:
                # If the value is found, insert it into the checked_frame
                if isinstance(value, list):
                    for val in value:
                        checked_frame.insert(tk.END, str(checkbox_value) + ' : ' + str(val) + '\n')
                else:
                    checked_frame.insert(tk.END, str(checkbox_value) + ' : ' + str(value) + '\n')
            else:
                checked_frame.insert(tk.END, str(checkbox_value) + ': //Väärtus puudub//')

    checked_frame.configure(state='disabled')

#
window = tk.Tk()
window.geometry("700x700")
window.title("Checkboxes for Values")

# Scrollable frame for checkboxes
#https://blog.teclado.com/tkinter-scrollable-frames/
checkbox_scrollable_frame = tk.Frame(window)
checkbox_scrollable_frame.pack(padx=10, pady=10, side='left', fill='both', expand=False)

canvas = tk.Canvas(checkbox_scrollable_frame)
scroll_bar = tk.Scrollbar(checkbox_scrollable_frame, orient="vertical", command=canvas.yview)
scrollable_checkbox_frame = tk.Frame(canvas)

scrollable_checkbox_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_checkbox_frame, anchor="w")
canvas.configure(yscrollcommand=scroll_bar.set)

scroll_bar.pack(side='right', fill='y')
canvas.pack(side='left', fill='both', expand=False)

# Create checkboxes inside the scrollable frame
create_checkboxes(checkbox_list_updated, scrollable_checkbox_frame)

# Text frame for checked values
checked_frame = tk.Text(window, height=5, width=30)
checked_frame.pack(fill='both', expand=True, padx=10, pady=10) 

# Confirm button
kinnitaBtn = tk.Button(window, text="Kinnita valik", command=confirm)
kinnitaBtn.pack(fill='both', padx=10, pady=10, expand=True)

# Scrolled text for displaying JSON
json_frame = st.ScrolledText(window, state='normal', height=50, width=70)
json_frame.pack(padx=10, pady=10, expand=True)
json_frame.insert('1.0', str(json_str))
json_frame.configure(state='disabled')  

window.mainloop()