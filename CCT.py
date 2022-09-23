# Import tkinter & PhotoImage.
import tkinter as tk
from tkinter import PhotoImage

# Configure tkinter, window name, size, colour.
root = tk.Tk()
root.title("CCT")
root.resizable(False, False)
root.attributes("-alpha", 0.95)
root.config(bg = "#F5F5F5")

# Set titlebar image.
photo = PhotoImage(file='C:/Users/ryan/Desktop/stuff/Scripts/CCT/v1.0/CCT_icon.png')
root.iconphoto(False, photo)

# Label for top of window.
label_info = tk.Label(root, text="Coordinate Conversion Tool", pady = 5, bg = "#e8e8e8", padx=20)
label_info.grid(row=0, column=0, columnspan=4, sticky = tk.W+tk.E, pady=(0,10))

# Label and entry for degree.
label_d = tk.Label(text="Degree ->", bg = "#F5F5F5")
label_d.grid(row=1, column=0, columnspan=2, sticky = tk.W, padx=(10,0))
entry_d = tk.Entry(root, width=10, bg = "#e8e8e8")
entry_d.grid(row=1, column=2, columnspan=2, sticky = tk.E, padx=(0,10))

# Label and entry for minute.
label_m = tk.Label(text="Minute ->", bg = "#F5F5F5")
label_m.grid(row=2, column=0, columnspan=2, sticky = tk.W, padx=(10,0))
entry_m = tk.Entry(root, width=10, bg = "#e8e8e8")
entry_m.grid(row=2, column=2, columnspan=2, sticky = tk.E, padx=(0,10))

# Label and entry for second.
label_s = tk.Label(text="Second ->", bg = "#F5F5F5")
label_s.grid(row=3, column=0, columnspan=2, sticky = tk.W, padx=(10,0))
entry_s = tk.Entry(root, width=10, bg = "#e8e8e8")
entry_s.grid(row=3, column=2, columnspan=2, sticky = tk.E, padx=(0,10))

# Function to retrieve radiobutton quadrant selection.
def retrieve_quadrant():
    print("Quadrant: " + quadrant_var.get())

# Quadrant radiobutton default value & variable.
quadrant_var = tk.StringVar(value = "N")

# Radiobuttons for quadrant selection.    
quad_button_n = tk.Radiobutton(root, text = "N", variable = quadrant_var, value = "N", command = retrieve_quadrant, bg="#F5F5F5")
quad_button_n.grid(row=4, column=0)
    
quad_button_e = tk.Radiobutton(root, text = "E", variable = quadrant_var, value = "E", command = retrieve_quadrant, bg="#F5F5F5")
quad_button_e.grid(row=4, column=1)

quad_button_s = tk.Radiobutton(root, text = "S", variable = quadrant_var, value = "S", command = retrieve_quadrant, bg="#F5F5F5")
quad_button_s.grid(row=4, column=2)

quad_button_w = tk.Radiobutton(root, text = "W", variable = quadrant_var, value = "W", command = retrieve_quadrant, bg="#F5F5F5")
quad_button_w.grid(row=4, column=3)

##attempt to retrieve degree value on calculate button press.

# Default Degree Minute Second variables.
degree_var = tk.IntVar()
degree_var.set(0)

minute_var = tk.IntVar()
minute_var.set(0)

second_var = tk.IntVar()
second_var.set(0)

print("Default DMS: " + str(degree_var.get()) + " " + str(minute_var.get()) + " " + str(second_var.get()))

# Function to retrieve degree entry value.
def retrieve_DMS():
   
    #set DMS variables from user input.
    if entry_d.get() == "":
        degree_var.set(0)
    else:
        degree_var.set(entry_d.get())
    
    if entry_m.get() == "":
        minute_var.set(0)
    else:
        minute_var.set(entry_m.get())

    if entry_s.get() == "":
        second_var.set(0)
    else:
        second_var.set(entry_s.get())

    print("Input DMS: " + str(degree_var.get()) + " " + str(minute_var.get()) + " " + str(second_var.get()))
    
    #define DMS as current user inputs.
    degree = degree_var.get()
    minute = minute_var.get()
    second = second_var.get()
    
    # Raw calculated output for DMS to DD.
    calculated_dd = (float(degree) + (float(minute)/60) + (float(second)/3600))
    print("Calculated DD Raw: " + str(calculated_dd))
    
    # Rounded DD output.
    rounded_dd = round(calculated_dd,8)
    print("Calculated DD Rounded: " + str(rounded_dd))

    # Fetch components for final output
    rounded_dd_str = str(rounded_dd)
    selected_quadrant = quadrant_var.get()
    final_output = "output"

    # If statement to assign correct quadrant value to output
    if selected_quadrant == "W":
        final_output = "- " + rounded_dd_str + " " + selected_quadrant
    elif selected_quadrant == "S":
        final_output = "- " + rounded_dd_str + " " + selected_quadrant
    else:
        final_output = rounded_dd_str + " " + selected_quadrant

    # Catch DMS values outside of allowed limits.
    if float(degree) > 180:
        final_output = "DMS exceeds range"
    elif float(degree) < -0:
        final_output = "DMS exceeds range"
    elif float(minute) > 59:
        final_output = "DMS exceeds range"
    elif float(minute) < -0:
        final_output = "DMS exceeds range"
    elif float(second) > 59:
        final_output = "DMS exceeds range"
    elif float(second) < -0:
        final_output = "DMS exceeds range"
    elif calculated_dd > 90 and selected_quadrant == "N":
        final_output = "DMS exceeds range"
    elif calculated_dd > 90 and selected_quadrant == "S":
        final_output = "DMS exceeds range"
    elif calculated_dd > 180 and selected_quadrant == "E":
        final_output = "DMS exceeds range"
    elif calculated_dd > 180 and selected_quadrant == "W":
        final_output = "DMS exceeds range"
    elif final_output == "0.0 N" or final_output == "- 0.0 S" or final_output == "0.0 E" or final_output == "- 0.0 W":
        final_output = "please enter DMS"
    else:
        print("Final Output: " + final_output)

    # Label for final output
    label_output = tk.Label(text=final_output, borderwidth=2, relief="groove", font=("Arial", 12))
    label_output.grid(row=7, column=0, columnspan=4, sticky = tk.W+tk.E, padx=10)

# Button for calculating the conversion.
calculate = tk.Button(text="Calculate", command=retrieve_DMS)
calculate.grid(row=5, column=0, columnspan=2, sticky = tk.E+tk.W, padx=10, pady=10)

# Function to reset DMS to default values and clear the output box.
def reset_DMS():
    degree_var.set(0)
    minute_var.set(0)
    second_var.set(0)
    entry_d.delete(0,tk.END)
    entry_m.delete(0,tk.END)
    entry_s.delete(0,tk.END)
    print("Reset DMS: " + str(degree_var.get()) + " " + str(minute_var.get()) + " " + str(second_var.get()))
    label_output = tk.Label(text="", borderwidth=2, relief="groove", font=("Arial", 12))
    label_output.grid(row=7, column=0, columnspan=4, sticky = tk.W+tk.E, padx=10)

# Button to reset DMS values.
calculate = tk.Button(text="Reset", command=reset_DMS)
calculate.grid(row=5, column=2, columnspan=2, sticky = tk.E+tk.W, padx=10, pady=10)

# Label with placeholder output text.
label_output = tk.Label(text="", borderwidth=2, relief="groove", font=("Arial", 12))
label_output.grid(row=7, column=0, columnspan=4, sticky = tk.W+tk.E, padx=10)

# Label at the bottom of the application.
label_foot = tk.Label(text="RSGEO", bg = "#F5F5F5", fg = "#7a7a7a", pady = 1)
label_foot.grid(row=8, column=0, columnspan=4, sticky = tk.W+tk.E)

# Holds python while tkinter root window is open.
root.mainloop()