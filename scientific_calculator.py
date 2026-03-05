import math
import re
from calculator_logic import Calculator, CalculatorError, ExpressionEvaluator

class ScientificExpressionEvaluator(ExpressionEvaluator):
    """Extended evaluator with scientific functions"""
    
    def __init__(self):
        super().__init__()
        # Add scientific operators with higher precedence
        self.precedence.update({
            '^': 3,  # Power
            'sin': 4, 'cos': 4, 'tan': 4,
            'log': 4, 'ln': 4,
            'sqrt': 4, 'cbrt': 4,
            '!': 4,  # Factorial
            'π': 4, 'e': 4  # Constants
        })
        
    def tokenize(self, expression):
        """Enhanced tokenizer for scientific functions"""
        expression = expression.replace(' ', '').lower()
        
        # Pattern for scientific notation and functions
        pattern = r'(\d+\.?\d*|\.\d+|[+\-*/%^()!]|sin|cos|tan|log|ln|sqrt|cbrt|π|e)'
        tokens = re.findall(pattern, expression)
        
        # Handle negative numbers
        processed_tokens = []
        i = 0
        while i < len(tokens):
            if tokens[i] == '-' and (i == 0 or tokens[i-1] in '+-*/%^('):
                # Unary minus
                i += 1
                if i < len(tokens) and (tokens[i].replace('.', '').isdigit() or tokens[i] in ['π', 'e']):
                    processed_tokens.append('-' + tokens[i])
                    i += 1
                else:
                    processed_tokens.append('-')
            else:
                processed_tokens.append(tokens[i])
                i += 1
                
        return processed_tokens
    
    def evaluate_postfix(self, postfix):
        """Enhanced evaluation for scientific functions"""
        stack = []
        
        for token in postfix:
            if isinstance(token, (int, float)):
                stack.append(token)
            elif token == 'π':
                stack.append(math.pi)
            elif token == 'e':
                stack.append(math.e)
            elif token == 'sin':
                val = stack.pop()
                stack.append(math.sin(math.radians(val)))
            elif token == 'cos':
                val = stack.pop()
                stack.append(math.cos(math.radians(val)))
            elif token == 'tan':
                val = stack.pop()
                stack.append(math.tan(math.radians(val)))
            elif token == 'log':
                val = stack.pop()
                stack.append(math.log10(val))
            elif token == 'ln':
                val = stack.pop()
                stack.append(math.log(val))
            elif token == 'sqrt':
                val = stack.pop()
                if val < 0:
                    raise CalculatorError("Cannot calculate square root of negative number")
                stack.append(math.sqrt(val))
            elif token == 'cbrt':
                val = stack.pop()
                stack.append(val ** (1/3) if val >= 0 else -((-val) ** (1/3)))
            elif token == '!':
                val = int(stack.pop())
                if val < 0:
                    raise CalculatorError("Factorial of negative number undefined")
                stack.append(math.factorial(val))
            elif token == '^':
                b = stack.pop()
                a = stack.pop()
                stack.append(a ** b)
            else:
                # Handle basic operators
                if len(stack) < 2:
                    raise CalculatorError("Invalid expression")
                b = stack.pop()
                a = stack.pop()
                
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    if b == 0:
                        raise CalculatorError("Division by zero")
                    stack.append(a / b)
                elif token == '%':
                    stack.append(a * (b / 100))
                    
        if len(stack) != 1:
            raise CalculatorError("Invalid expression")
            
        return stack[0]


class ScientificCalculator(Calculator):
    """Extended calculator with scientific functions"""
    
    def __init__(self):
        super().__init__()
        self.evaluator = ScientificExpressionEvaluator()
        self.memory = 0
        self.angle_mode = 'DEG'  # DEG, RAD, GRAD
        self.constants = {
            'π': math.pi,
            'e': math.e
        }
        
    def memory_store(self):
        """Store current value to memory"""
        try:
            self.memory = float(self.input_processor.get_current_input())
            return True
        except ValueError:
            return False
            
    def memory_recall(self):
        """Recall value from memory"""
        self.input_processor.current_input = str(self.memory)
        return str(self.memory)
        
    def memory_clear(self):
        """Clear memory"""
        self.memory = 0
        
    def memory_add(self):
        """Add to memory"""
        try:
            self.memory += float(self.input_processor.get_current_input())
            return True
        except ValueError:
            return False
            
    def toggle_angle_mode(self):
        """Toggle between DEG, RAD, GRAD"""
        modes = ['DEG', 'RAD', 'GRAD']
        current_index = modes.index(self.angle_mode)
        self.angle_mode = modes[(current_index + 1) % 3]
        return self.angle_mode
        
    def apply_function(self, func_name):
        """Apply scientific function to current input"""
        try:
            current = float(self.input_processor.get_current_input()) if self.input_processor.current_input else 0
            
            if func_name == 'sin':
                if self.angle_mode == 'DEG':
                    result = math.sin(math.radians(current))
                elif self.angle_mode == 'GRAD':
                    result = math.sin(current * math.pi / 200)
                else:  # RAD
                    result = math.sin(current)
            elif func_name == 'cos':
                if self.angle_mode == 'DEG':
                    result = math.cos(math.radians(current))
                elif self.angle_mode == 'GRAD':
                    result = math.cos(current * math.pi / 200)
                else:  # RAD
                    result = math.cos(current)
            elif func_name == 'tan':
                if self.angle_mode == 'DEG':
                    result = math.tan(math.radians(current))
                elif self.angle_mode == 'GRAD':
                    result = math.tan(current * math.pi / 200)
                else:  # RAD
                    result = math.tan(current)
            elif func_name == 'log':
                result = math.log10(current)
            elif func_name == 'ln':
                result = math.log(current)
            elif func_name == 'sqrt':
                result = math.sqrt(current)
            elif func_name == 'x²':
                result = current ** 2
            elif func_name == 'x³':
                result = current ** 3
            elif func_name == '1/x':
                result = 1 / current
            elif func_name == '|x|':
                result = abs(current)
            elif func_name == 'exp':
                result = math.exp(current)
            elif func_name == '10^x':
                result = 10 ** current
                
            self.input_processor.current_input = str(result)
            return str(result)
            
        except Exception as e:
            return f"Error: {str(e)}"