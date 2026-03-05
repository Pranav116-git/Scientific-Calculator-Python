import tkinter as tk
from tkinter import ttk
import math
from scientific_calculator import ScientificCalculator

class ModernScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator Pro")
        self.root.geometry("500x700")
        self.root.resizable(False, False)
        
        # Initialize calculator
        self.calc = ScientificCalculator()
        
        # Theme and styles
        self.current_theme = 'dark'  # Start with dark theme for modern look
        self.setup_themes()
        
        # Variables
        self.history_visible = False
        
        # Setup UI
        self.apply_theme()
        self.setup_styles()
        self.create_widgets()
        self.bind_keyboard()
        
    def setup_themes(self):
        """Define color themes"""
        self.themes = {
            'dark': {
                'bg': '#1e1e1e',
                'display_bg': '#2d2d2d',
                'display_fg': '#00ff00',  # Matrix-style green
                'button_bg': '#333333',
                'button_fg': '#ffffff',
                'function_bg': '#4a4a4a',
                'scientific_bg': '#0a4a6e',
                'operator_bg': '#ff9500',
                'equal_bg': '#ff9500',
                'memory_bg': '#6a1b9a',
                'history_bg': '#2d2d2d',
                'history_fg': '#ffffff',
                'accent': '#00ff00'
            },
            'light': {
                'bg': '#f5f5f5',
                'display_bg': '#ffffff',
                'display_fg': '#000000',
                'button_bg': '#e0e0e0',
                'button_fg': '#000000',
                'function_bg': '#bdbdbd',
                'scientific_bg': '#2196f3',
                'operator_bg': '#ff9500',
                'equal_bg': '#ff9500',
                'memory_bg': '#9c27b0',
                'history_bg': '#ffffff',
                'history_fg': '#000000',
                'accent': '#2196f3'
            },
            'blue': {
                'bg': '#001f3f',
                'display_bg': '#003366',
                'display_fg': '#7fdbff',
                'button_bg': '#004080',
                'button_fg': '#ffffff',
                'function_bg': '#0066cc',
                'scientific_bg': '#0099ff',
                'operator_bg': '#ff851b',
                'equal_bg': '#ff851b',
                'memory_bg': '#b10dc9',
                'history_bg': '#003366',
                'history_fg': '#ffffff',
                'accent': '#7fdbff'
            }
        }
        
    def apply_theme(self):
        """Apply current theme"""
        theme = self.themes[self.current_theme]
        self.root.configure(bg=theme['bg'])
        
    def setup_styles(self):
        """Configure custom styles"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure custom button styles
        style.configure('Scientific.TButton', 
                       font=('Segoe UI', 10),
                       padding=5)
        
    def create_widgets(self):
        """Create all GUI widgets"""
        theme = self.themes[self.current_theme]
        
        # Top bar with theme toggle and mode indicator
        self.create_top_bar()
        
        # Display area
        self.create_display()
        
        # Memory indicators
        self.create_memory_indicator()
        
        # Angle mode indicator
        self.create_angle_indicator()
        
        # Scientific functions panel
        self.create_scientific_panel()
        
        # Main button panel
        self.create_button_panel()
        
        # History panel (initially hidden)
        self.create_history_panel()
        
    def create_top_bar(self):
        """Create top bar with controls"""
        theme = self.themes[self.current_theme]
        top_bar = tk.Frame(self.root, bg=theme['bg'])
        top_bar.pack(fill='x', padx=5, pady=5)
        
        # Theme selector
        themes = ['dark', 'light', 'blue']
        self.theme_var = tk.StringVar(value=self.current_theme)
        theme_menu = ttk.Combobox(top_bar, textvariable=self.theme_var, 
                                  values=themes, state='readonly', width=10)
        theme_menu.pack(side='left', padx=5)
        theme_menu.bind('<<ComboboxSelected>>', self.change_theme)
        
        # History toggle button
        self.history_btn = tk.Button(top_bar, text="📊 History", 
                                     command=self.toggle_history,
                                     bg=theme['function_bg'],
                                     fg='white', relief='flat')
        self.history_btn.pack(side='right', padx=5)
        
        # Help button
        help_btn = tk.Button(top_bar, text="?", 
                            command=self.show_help,
                            bg=theme['accent'],
                            fg='white', relief='flat', width=2)
        help_btn.pack(side='right', padx=5)
        
    def create_display(self):
        """Create main display and expression display"""
        theme = self.themes[self.current_theme]
        
        display_frame = tk.Frame(self.root, bg=theme['bg'])
        display_frame.pack(fill='x', padx=10, pady=(5, 0))
        
        # Expression display (smaller font)
        self.expression_display = tk.Label(
            display_frame,
            text='',
            font=('Consolas', 12),
            bg=theme['display_bg'],
            fg=theme['accent'],
            anchor='e',
            height=1,
            padx=10
        )
        self.expression_display.pack(fill='x', pady=(0, 2))
        
        # Main display (larger font)
        self.display = tk.Label(
            display_frame,
            text='0',
            font=('Arial', 48, 'bold'),
            bg=theme['display_bg'],
            fg=theme['display_fg'],
            anchor='e',
            height=2,
            padx=10
        )
        self.display.pack(fill='x')
        
    def create_memory_indicator(self):
        """Create memory indicator"""
        theme = self.themes[self.current_theme]
        
        memory_frame = tk.Frame(self.root, bg=theme['bg'])
        memory_frame.pack(fill='x', padx=10)
        
        self.memory_label = tk.Label(
            memory_frame,
            text='MEM: 0',
            font=('Segoe UI', 10),
            bg=theme['bg'],
            fg=theme['accent'],
            anchor='w'
        )
        self.memory_label.pack(side='left')
        
    def create_angle_indicator(self):
        """Create angle mode indicator"""
        theme = self.themes[self.current_theme]
        
        angle_frame = tk.Frame(self.root, bg=theme['bg'])
        angle_frame.pack(fill='x', padx=10)
        
        self.angle_label = tk.Label(
            angle_frame,
            text=f'Mode: {self.calc.angle_mode}',
            font=('Segoe UI', 10),
            bg=theme['bg'],
            fg=theme['accent'],
            anchor='e'
        )
        self.angle_label.pack(side='right')
        
        # Angle toggle button
        angle_btn = tk.Button(
            angle_frame,
            text="DEG/RAD/GRAD",
            command=self.toggle_angle_mode,
            bg=theme['function_bg'],
            fg='white',
            relief='flat',
            font=('Segoe UI', 9)
        )
        angle_btn.pack(side='right', padx=5)
        
    def create_scientific_panel(self):
        """Create scientific functions panel"""
        theme = self.themes[self.current_theme]
        
        sci_frame = tk.Frame(self.root, bg=theme['bg'])
        sci_frame.pack(fill='x', padx=10, pady=5)
        
        # Scientific functions organized in rows
        functions = [
            ['sin', 'cos', 'tan', 'log', 'ln'],
            ['√', '∛', 'x²', 'x³', '1/x'],
            ['|x|', 'exp', '10^x', 'π', 'e']
        ]
        
        for i, row in enumerate(functions):
            for j, func in enumerate(row):
                btn = tk.Button(
                    sci_frame,
                    text=func,
                    font=('Segoe UI', 10, 'bold'),
                    bg=theme['scientific_bg'],
                    fg='white',
                    relief='flat',
                    width=5,
                    height=1,
                    command=lambda f=func: self.scientific_function(f)
                )
                btn.grid(row=i, column=j, padx=2, pady=2, sticky='nsew')
                
        # Configure grid
        for i in range(3):
            sci_frame.grid_rowconfigure(i, weight=1)
        for j in range(5):
            sci_frame.grid_columnconfigure(j, weight=1)
            
    def create_button_panel(self):
        """Create main button panel"""
        theme = self.themes[self.current_theme]
        
        button_frame = tk.Frame(self.root, bg=theme['bg'])
        button_frame.pack(expand=True, fill='both', padx=10, pady=5)
        
        # Memory buttons row
        memory_buttons = ['MC', 'MR', 'M+', 'MS', 'M-']
        for i, text in enumerate(memory_buttons):
            btn = tk.Button(
                button_frame,
                text=text,
                font=('Segoe UI', 10, 'bold'),
                bg=theme['memory_bg'],
                fg='white',
                relief='flat',
                command=lambda x=text: self.memory_function(x)
            )
            btn.grid(row=0, column=i, padx=2, pady=2, sticky='nsew')
        
        # Main button layout
        buttons = [
            ['C', '⌫', '(', ')', '^'],
            ['7', '8', '9', '÷', '%'],
            ['4', '5', '6', '×', '!'],
            ['1', '2', '3', '-', ''],
            ['0', '00', '.', '+', '=']
        ]
        
        # Create main buttons
        for i, row in enumerate(buttons, start=1):  # Start from row 1 (after memory row)
            for j, text in enumerate(row):
                if not text:  # Skip empty cells
                    continue
                    
                # Determine button style
                if text == '=':
                    bg = theme['equal_bg']
                    fg = 'white'
                elif text in ['C', '⌫', '(', ')', '!', '^']:
                    bg = theme['function_bg']
                    fg = 'white'
                elif text in ['+', '-', '×', '÷', '%']:
                    bg = theme['operator_bg']
                    fg = 'white'
                else:
                    bg = theme['button_bg']
                    fg = theme['button_fg']
                
                # Map display operators to actual operators
                display_text = text
                if text == '×':
                    actual_op = '*'
                elif text == '÷':
                    actual_op = '/'
                else:
                    actual_op = text
                
                btn = tk.Button(
                    button_frame,
                    text=display_text,
                    font=('Segoe UI', 14, 'bold'),
                    bg=bg,
                    fg=fg,
                    relief='flat',
                    command=lambda x=actual_op: self.button_click(x)
                )
                
                # Special grid placement for zero button
                if text == '0' and j == 0 and i == 4:
                    btn.grid(row=i, column=j, columnspan=2, padx=2, pady=2, sticky='nsew')
                elif text == '=' and j == 4 and i == 4:
                    btn.grid(row=i, column=j, rowspan=2, padx=2, pady=2, sticky='nsew')
                else:
                    btn.grid(row=i, column=j, padx=2, pady=2, sticky='nsew')
        
        # Configure grid weights
        for i in range(6):  # 0-5 rows
            button_frame.grid_rowconfigure(i, weight=1)
        for j in range(5):
            button_frame.grid_columnconfigure(j, weight=1)
            
    def create_history_panel(self):
        """Create history panel (initially hidden)"""
        theme = self.themes[self.current_theme]
        
        self.history_frame = tk.Frame(self.root, bg=theme['history_bg'], height=150)
        
        # History title
        title = tk.Label(
            self.history_frame,
            text="Calculation History (Double-click to reuse)",
            font=('Segoe UI', 10, 'bold'),
            bg=theme['history_bg'],
            fg=theme['history_fg']
        )
        title.pack(pady=5)
        
        # History listbox with scrollbar
        list_frame = tk.Frame(self.history_frame, bg=theme['history_bg'])
        list_frame.pack(fill='both', expand=True, padx=5, pady=5)
        
        self.history_list = tk.Listbox(
            list_frame,
            font=('Consolas', 10),
            bg=theme['history_bg'],
            fg=theme['history_fg'],
            selectbackground=theme['accent'],
            height=5
        )
        self.history_list.pack(side='left', fill='both', expand=True)
        
        # Add double-click binding
        self.history_list.bind('<Double-Button-1>', self.on_history_click)
        
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side='right', fill='y')
        
        self.history_list.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.history_list.yview)
        
        # Button frame
        button_frame = tk.Frame(self.history_frame, bg=theme['history_bg'])
        button_frame.pack(fill='x', pady=5)
        
        # Clear history button
        clear_btn = tk.Button(
            button_frame,
            text="Clear History",
            command=self.clear_history,
            bg=theme['function_bg'],
            fg='white',
            relief='flat',
            width=12
        )
        clear_btn.pack(side='left', padx=5)
        
        # Close button
        close_btn = tk.Button(
            button_frame,
            text="Close",
            command=self.toggle_history,
            bg=theme['function_bg'],
            fg='white',
            relief='flat',
            width=8
        )
        close_btn.pack(side='right', padx=5)
        
    def toggle_history(self):
        """Toggle history panel visibility"""
        theme = self.themes[self.current_theme]
        
        if self.history_visible:
            self.history_frame.pack_forget()
            self.history_btn.config(text="📊 History")
            self.history_visible = False
            # Resize window to original size
            self.root.geometry("500x700")
        else:
            # Find the right place to insert history panel
            # Insert after the button panel (which is at index 5)
            self.history_frame.pack(fill='x', padx=10, pady=5)
            self.history_btn.config(text="📊 Hide History")
            self.history_visible = True
            self.update_history_display()
            # Expand window to accommodate history
            self.root.geometry("500x750")
            
    def update_history_display(self):
        """Update history listbox with calculations"""
        self.history_list.delete(0, tk.END)
        history_items = self.calc.get_history()
        if history_items:
            for item in history_items:
                self.history_list.insert(tk.END, item)
        else:
            self.history_list.insert(tk.END, "No calculations yet")
            
    def on_history_click(self, event):
        """Handle double-click on history item"""
        try:
            selection = self.history_list.curselection()
            if selection:
                item = self.history_list.get(selection[0])
                # Extract the expression part (before the = sign)
                if ' = ' in item:
                    expression = item.split(' = ')[0]
                    self.calc.input_processor.current_input = expression
                    self.display.config(text=expression)
                    self.expression_display.config(text=expression)
        except Exception as e:
            print(f"Error: {e}")
            
    def clear_history(self):
        """Clear calculation history"""
        self.calc.history = []
        self.update_history_display()
        
    def memory_function(self, func):
        """Handle memory functions"""
        if func == 'MC':
            self.calc.memory_clear()
        elif func == 'MR':
            result = self.calc.memory_recall()
            self.display.config(text=result)
        elif func == 'M+':
            self.calc.memory_add()
        elif func == 'MS':
            self.calc.memory_store()
        elif func == 'M-':
            # Subtract from memory
            try:
                current = float(self.calc.input_processor.get_current_input())
                self.calc.memory -= current
            except:
                pass
            
        self.memory_label.config(text=f'MEM: {self.calc.memory}')
        
    def scientific_function(self, func):
        """Handle scientific functions"""
        if func == 'π':
            self.calc.input_processor.current_input = str(math.pi)
            self.display.config(text=str(math.pi))
        elif func == 'e':
            self.calc.input_processor.current_input = str(math.e)
            self.display.config(text=str(math.e))
        elif func == '√':
            result = self.calc.apply_function('sqrt')
            self.display.config(text=result)
        elif func == '∛':
            result = self.calc.apply_function('cbrt')
            self.display.config(text=result)
        elif func == 'x²':
            result = self.calc.apply_function('x²')
            self.display.config(text=result)
        elif func == 'x³':
            result = self.calc.apply_function('x³')
            self.display.config(text=result)
        elif func == '1/x':
            result = self.calc.apply_function('1/x')
            self.display.config(text=result)
        elif func == '|x|':
            result = self.calc.apply_function('|x|')
            self.display.config(text=result)
        elif func == 'exp':
            result = self.calc.apply_function('exp')
            self.display.config(text=result)
        elif func == '10^x':
            result = self.calc.apply_function('10^x')
            self.display.config(text=result)
        else:
            # Trigonometric and logarithmic functions
            result = self.calc.apply_function(func)
            self.display.config(text=result)
            
    def toggle_angle_mode(self):
        """Toggle angle mode"""
        mode = self.calc.toggle_angle_mode()
        self.angle_label.config(text=f'Mode: {mode}')
        
    def change_theme(self, event=None):
        """Change calculator theme"""
        self.current_theme = self.theme_var.get()
        self.apply_theme()
        
        # Refresh UI with new theme
        for widget in self.root.winfo_children():
            widget.destroy()
            
        self.create_widgets()
        self.update_history_display()
        
    def button_click(self, value):
        """Handle button clicks"""
        if value == '=':
            result = self.calc.calculate()
            self.display.config(text=result)
            self.expression_display.config(text=self.calc.input_processor.get_current_input())
            self.update_history_display()
        elif value == 'C':
            self.calc.clear()
            self.display.config(text='0')
            self.expression_display.config(text='')
        elif value == '⌫':
            self.calc.process_input(value)
            self.display.config(text=self.calc.get_display_text())
        else:
            self.calc.process_input(value)
            self.display.config(text=self.calc.get_display_text())
            self.expression_display.config(text=self.calc.input_processor.get_current_input())
            
    def bind_keyboard(self):
        """Bind keyboard shortcuts"""
        # Numbers
        for i in range(10):
            self.root.bind(str(i), lambda e, x=str(i): self.button_click(x))
            
        # Operators
        self.root.bind('+', lambda e: self.button_click('+'))
        self.root.bind('-', lambda e: self.button_click('-'))
        self.root.bind('*', lambda e: self.button_click('*'))
        self.root.bind('/', lambda e: self.button_click('/'))
        self.root.bind('%', lambda e: self.button_click('%'))
        self.root.bind('^', lambda e: self.button_click('^'))
        
        # Special keys
        self.root.bind('<Return>', lambda e: self.button_click('='))
        self.root.bind('<BackSpace>', lambda e: self.button_click('⌫'))
        self.root.bind('<Escape>', lambda e: self.button_click('C'))
        self.root.bind('.', lambda e: self.button_click('.'))
        
        # Function keys for scientific functions
        self.root.bind('<Control-s>', lambda e: self.scientific_function('sin'))
        self.root.bind('<Control-c>', lambda e: self.scientific_function('cos'))
        self.root.bind('<Control-t>', lambda e: self.scientific_function('tan'))
        self.root.bind('<Control-l>', lambda e: self.scientific_function('log'))
        
    def show_help(self):
        """Show help dialog"""
        help_text = """
        Scientific Calculator Pro - Help
        
        Keyboard Shortcuts:
        • Numbers: 0-9
        • Operators: + - * / % ^
        • Enter: Calculate
        • Backspace: Delete last
        • Escape: Clear
        • Ctrl+S: sin
        • Ctrl+C: cos
        • Ctrl+T: tan
        • Ctrl+L: log
        
        Functions:
        • sin, cos, tan (with DEG/RAD/GRAD)
        • log (base 10), ln (natural)
        • √, ∛, x², x³
        • ! (factorial), |x| (absolute)
        • π, e constants
        • Memory: MC, MR, M+, MS
        
        History Panel:
        • Click "History" button to show/hide
        • Double-click any item to reuse
        • Clear button to erase history
        
        Features:
        • Multiple themes
        • Calculation history
        • Expression preview
        • Memory storage
        """
        
        help_window = tk.Toplevel(self.root)
        help_window.title("Help")
        help_window.geometry("450x550")
        
        # Add scrollbar
        frame = tk.Frame(help_window)
        frame.pack(fill='both', expand=True)
        
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side='right', fill='y')
        
        text_widget = tk.Text(frame, wrap='word', padx=10, pady=10,
                              yscrollcommand=scrollbar.set,
                              font=('Segoe UI', 10))
        text_widget.pack(side='left', fill='both', expand=True)
        
        scrollbar.config(command=text_widget.yview)
        
        text_widget.insert('1.0', help_text)
        text_widget.config(state='disabled')
        
        close_btn = tk.Button(help_window, text="Close", 
                             command=help_window.destroy,
                             bg=self.themes[self.current_theme]['function_bg'],
                             fg='white', relief='flat')
        close_btn.pack(pady=5)


def main():
    root = tk.Tk()
    
    # Set application icon (optional)
    try:
        root.iconbitmap('calculator.ico')
    except:
        pass
    
    app = ModernScientificCalculator(root)
    
    # Center window
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    root.mainloop()


if __name__ == "__main__":
    main()