# Parametric Spur Gear Generator for SolidWorks

## Overview

This project demonstrates **automation of parametric CAD modeling in SolidWorks using Python**.
The script allows users to generate multiple spur gears by specifying key design parameters through a simple pop-up interface.

The program updates **SolidWorks global variables** (Module, Number of Teeth, and Pressure Angle), rebuilds the model automatically, and exports each generated gear as a **STEP file**.

This approach helps automate repetitive CAD tasks and quickly generate multiple gear variants for design exploration, simulation, or manufacturing.

---

## Demo

Watch the project demo here:

[![Watch the demo](https://img.youtube.com/vi/VIDEO_ID/0.jpg)](https://youtu.be/VIDEO_ID)

---

## Features

* Generate **multiple gears in one run**
* Simple **pop-up interface for user inputs**
* Update **SolidWorks Global Variables automatically**
* Automatic **model rebuild inside SolidWorks**
* Export generated gears as **STEP files**
* STEP files named based on the number of teeth (e.g., `SpurGear_40T.step`)

---

## How It Works

1. The script asks how many gears you want to generate.
2. For each gear, the user enters:

   * Module
   * Number of Teeth
   * Pressure Angle
3. Python connects to SolidWorks using the **COM API**.
4. The script updates the **Equation Manager global variables**.
5. SolidWorks rebuilds the gear automatically.
6. The updated gear is exported as a **STEP file**.

---

## Requirements

* Python 3.x
* SolidWorks installed
* Python package:

```
pip install pywin32
```

---

## Usage

1. Open the script file.
2. Update the path to the base SolidWorks gear file:

```
file_path = r"C:\Users\yourname\path\SpurGear_30T.SLDPRT"
```

3. Run the script:

```
python GearGenerator.py
```

4. Enter gear parameters in the pop-up windows.

Generated STEP files will be saved in the **same folder as the SolidWorks part**.

---

## Example Output

Example generated files:

```
SpurGear_20T.step
SpurGear_30T.step
SpurGear_40T.step
```

---

## Skills Demonstrated

* Python scripting
* SolidWorks API automation
* Parametric CAD modeling
* Design automation workflows
* STEP file generation

---

## Potential Applications

* Rapid generation of gear variants
* Parametric design exploration
* Automated CAD workflows
* Manufacturing preparation

---

## Author

Shahryar
Mechanical Engineer | CAD & Design Automation
