from functions.jsonMain import *

import tkinter as tk 
import tkinter.scrolledtext as st 

checkbox_list_updated = list(filter(None, checkbox_list))
checked_checkboxes = []
translated_checked_checboxes = []

# name of the file that is saved
printfile = "output.txt"

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
                        checked_frame.insert(tk.END, str(checkbox_value) + ' : ' + str(val) + '\n'+ '\n')
                else:
                    checked_frame.insert(tk.END, str(checkbox_value) + ' : ' + str(value) + '\n'+ '\n')
            else:
                checked_frame.insert(tk.END, str(checkbox_value) + ': //Väärtus puudub//'+ '\n')

    checked_frame.configure(state='disabled')
    
#  clear funktsioon on lingitud Puhasta kõik nupuga ja puhastab valitud checkboxid    
def clear():
    translated_checked_checboxes.clear()
    checked_frame.configure(state='normal')
    checked_frame.delete('1.0', tk.END)  # Clear existing content
    for i in checked_checkboxes:
        i.set('')


# Function to get values from the checked_frame (the values from JSON that are requested)
# and save the in a txt file 
def retrieve_input():
    input = checked_frame.get("1.0",'end-1c')
    print(input)
    
    with open(printfile, 'w', encoding='utf-8') as file:
        file.write(input)
 
 
# For mousescroll support
# https://stackoverflow.com/questions/17355902/tkinter-binding-mousewheel-to-scrollbar
def on_mouse_wheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

window = tk.Tk()
window.geometry("1280x720")
window.title("JSON konverter")

# change this to change checkbox_scrollable_frame and canvas width (x-axis)
checbox_controller_x = 235

checkbox_scrollable_frame = tk.Frame(window, width=checbox_controller_x)
checkbox_scrollable_frame.pack(padx=0, pady=10, side='left', fill='y', expand=False)

canvas = tk.Canvas(checkbox_scrollable_frame, width=checbox_controller_x)
scroll_bar = tk.Scrollbar(checkbox_scrollable_frame, orient="vertical", command=canvas.yview)
scrollable_checkbox_frame = tk.Frame(canvas)

#https://blog.teclado.com/tkinter-scrollable-frames/
scrollable_checkbox_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_checkbox_frame, anchor="nw")
canvas.configure(yscrollcommand=scroll_bar.set)

scroll_bar.pack(side='right', fill='y')
canvas.pack(padx=0, pady=10, side='left', fill='y', expand=False)

# Bind mouse wheel event to the canvas
checkbox_scrollable_frame.bind("<Enter>", lambda e: canvas.bind_all("<MouseWheel>", on_mouse_wheel))
checkbox_scrollable_frame.bind("<Leave>", lambda e: canvas.unbind_all("<MouseWheel>"))


# Create checkboxes inside the scrollable frame
create_checkboxes(checkbox_list_updated, scrollable_checkbox_frame)

# Text frame for checked values
checked_frame = tk.Text(window, height=25, width=90)
checked_frame.pack(fill='both', expand=True, padx=10, pady=10)


# Added a frame to manage the location of buttons
button_frame = tk.Frame(window, height = 30)
button_frame.pack(padx=10, pady=10, side='right', fill='x', expand=False)

# Confirm button
kinnitaBtn = tk.Button(button_frame, text="Kinnita valik", command=confirm)
kinnitaBtn.pack(fill='both', padx=5, pady=5, expand=True, side='top')

# Clear button
puhastaBtn = tk.Button(button_frame, bg='red', text="Puhasta valik", command=clear)
puhastaBtn.pack(fill='both', padx=5, pady=5, expand=True, side='left')

# Print button
printBtn = tk.Button(button_frame, bg='yellow', text="Prindi", command=retrieve_input)
printBtn.pack(fill='both', padx=5, pady=5, expand=True, side='right')

# Scrolled text for displaying JSON
json_frame = st.ScrolledText(window, state='normal', height=80, width=140)
json_frame.pack(padx=10, pady=10, expand=True, side='bottom')
json_frame.insert('1.0', str(json_str))
json_frame.configure(state='disabled')  

window.mainloop()
