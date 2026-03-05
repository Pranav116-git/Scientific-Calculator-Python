# Scientific Calculator Pro 🧮

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
[![GitHub stars](https://img.shields.io/github/stars/Pranav116-git/Scientific-Calculator-Python)](https://github.com/Pranav116-git/Scientific-Calculator-Python/stargazers)

A fully featured scientific calculator with a modern GUI built using Python and tkinter.

## 📸 Screenshots

<img width="1920" height="1080" alt="Screenshot (453)" src="https://github.com/user-attachments/assets/0112a174-3135-441d-92bc-55e237c66f0c" />


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
   git clone https://github.com/Pranav116-git/Scientific-Calculator-Python.git
2.Navigate to the project folder:
bash
cd Scientific-Calculator-Python

3.Run the calculator:
bash
python scientific_calculator_gui.py

### Method 2: Download EXE
Download the latest release from the Releases page.

## 📋 Requirements

- Python 3.6 or higher
- No external packages required! (uses only Python standard library)

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

📁 Project Structure
text
Scientific-Calculator-Python/
├── scientific_calculator.py      # Scientific calculation logic
├── scientific_calculator_gui.py   # Main GUI application
├── calculator_logic.py            # Basic calculator logic
├── calculator.ico                  # Application icon
├── screenshot.png                  # App screenshot
├── requirements.txt                # Dependencies
└── README.md                       # This file
🤝 Contributing
Contributions are welcome! Feel free to:

Report bugs

Suggest new features

Submit pull requests

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

👨‍💻 Author
Pranav

GitHub: @Pranav116-git

Project Link: https://github.com/Pranav116-git/Scientific-Calculator-Python
