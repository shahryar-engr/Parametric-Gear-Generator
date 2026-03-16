import win32com.client
import tkinter as tk
from tkinter import simpledialog
import os

# Function to ask all three variables at once
def ask_gear_parameters(gear_number):
    popup = tk.Toplevel()
    popup.title(f"Gear {gear_number} Parameters")
    
    tk.Label(popup, text="Module:").grid(row=0, column=0)
    module_entry = tk.Entry(popup)
    module_entry.grid(row=0, column=1)
    
    tk.Label(popup, text="Number of Teeth:").grid(row=1, column=0)
    teeth_entry = tk.Entry(popup)
    teeth_entry.grid(row=1, column=1)
    
    tk.Label(popup, text="Pressure Angle:").grid(row=2, column=0)
    angle_entry = tk.Entry(popup)
    angle_entry.grid(row=2, column=1)
    
    values = {}
    
    def submit():
        values['Module'] = float(module_entry.get())
        values['No_of_teeth'] = int(teeth_entry.get())
        values['Pressure_angle'] = float(angle_entry.get())
        popup.destroy()
    
    tk.Button(popup, text="Submit", command=submit).grid(row=3, columnspan=2)
    
    popup.grab_set()
    popup.wait_window()
    
    return values['Module'], values['No_of_teeth'], values['Pressure_angle']

# Main window (hidden)
root = tk.Tk()
root.withdraw()

# Ask how many gears
num_gears = simpledialog.askinteger("Input", "How many gears do you want to generate?")

gear_list = []

# Get parameters for each gear
for i in range(num_gears):
    Module, No_of_teeth, Pressure_angle = ask_gear_parameters(i+1)
    gear_list.append((Module, No_of_teeth, Pressure_angle))

# Connect to SolidWorks
swApp = win32com.client.Dispatch("SldWorks.Application")
swApp.Visible = True

# Path of the base gear
file_path = r"C:\Users\mreng\Desktop\Test\Gear\SpurGear_30T.SLDPRT"
swModel = swApp.OpenDoc(file_path, 1)
eqMgr = swModel.GetEquationMgr
folder = os.path.dirname(file_path)

# Update and save each gear
for Module, No_of_teeth, Pressure_angle in gear_list:
    eqMgr.Equation(0, f'"Module" = {Module}')
    eqMgr.Equation(1, f'"No_of_teeth" = {No_of_teeth}')
    eqMgr.Equation(2, f'"Pressure_angle" = {Pressure_angle}')
    
    swModel.EditRebuild()
    
    step_path = os.path.join(folder, f"SpurGear_{No_of_teeth}T.step")
    swModel.SaveAs(step_path)
    print(f"Gear with {No_of_teeth} teeth saved as STEP: {step_path}")

print("All gears generated successfully!")