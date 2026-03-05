# Scientific Calculator Pro 🧮

A fully featured scientific calculator with a modern GUI built using Python and tkinter.

## ✨ Features

### Basic Operations
- Addition (+), Subtraction (-), Multiplication (*), Division (/)
- Percentage calculations (%)
- Decimal number support
- Backspace and Clear functions

### Scientific Functions
- **Trigonometry**: sin, cos, tan (with DEG/RAD/GRAD modes)
- **Logarithms**: log (base 10), ln (natural log)
- **Powers**: x², x³, x^y, √, ∛
- **Constants**: π, e
- **Other**: factorial (!), absolute value (|x|), 1/x, exp, 10^x

### GUI Features
- 🎨 **Multiple themes**: Dark, Light, Blue
- 📊 **History panel** with double-click to reuse calculations
- 💾 **Memory functions**: MC, MR, M+, MS, M-
- ⌨️ **Full keyboard support**
- ❓ **Built-in help system**

## 🚀 Installation

### Method 1: Run from Source
1. Clone this repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Scientific-Calculator-Python.git

2. cd Scientific-Calculator-Python

3. python scientific_calculator_gui.py

## Method 2: Download EXE
Download the latest release from the Releases page.

📖 How to Use
Basic Usage
Click buttons or use keyboard to enter expressions

Press = or Enter to calculate

Use C to clear, ⌫ to delete last character

Scientific Functions
Type a number

Click function button (sin, cos, log, etc.)

Result appears instantly

History Panel
Click "History" button to show/hide calculation history

Double-click any item to reuse that calculation

Themes
Use dropdown menu at top to switch between Dark/Light/Blue themes

Press Ctrl+T to toggle quickly

⌨️ Keyboard Shortcuts
Key	Function
0-9	Number input
+ - * /	Basic operators
^	Power
Enter	Calculate (=)
Backspace	Delete last character
Escape	Clear (C)
Ctrl+S	sin
Ctrl+C	cos
Ctrl+T	tan
Ctrl+L	log

📦 Building EXE
To create a standalone executable:

bash
pip install pyinstaller
pyinstaller --onefile --windowed --icon=calculator.ico --name="ScientificCalculator" scientific_calculator_gui.py
The EXE will be in the dist folder.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
[![GitHub stars](https://img.shields.io/github/stars/YOUR_USERNAME/Scientific-Calculator-Python)](https://github.com/YOUR_USERNAME/Scientific-Calculator-Python/stargazers)
