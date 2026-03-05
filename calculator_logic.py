import re
import math

class CalculatorError(Exception):
    """Custom exception for calculator errors"""
    pass

class InputProcessor:
    """Handles input processing and validation"""
    
    def __init__(self):
        self.current_input = ""
        self.last_result = None
        self.has_decimal = False
        
    def add_number(self, number):
        """Add a number to current input"""
        self.current_input += str(number)
        
    def add_decimal(self):
        """Add decimal point if valid"""
        if not self.has_decimal:
            # Check if we're starting a new number
            if not self.current_input or self.current_input[-1] in '+-*/%':
                self.current_input += "0."
            else:
                self.current_input += "."
            self.has_decimal = True
            
    def add_operator(self, operator):
        """Add an operator to current input"""
        # Prevent multiple operators in a row
        if self.current_input and self.current_input[-1] in '+-*/%':
            # Replace the last operator
            self.current_input = self.current_input[:-1] + operator
        else:
            self.current_input += operator
        self.has_decimal = False
        
    def backspace(self):
        """Remove last character"""
        if self.current_input:
            # Check if we're removing a decimal point
            if self.current_input[-1] == '.':
                self.has_decimal = False
            self.current_input = self.current_input[:-1]
            
    def clear(self):
        """Clear all input"""
        self.current_input = ""
        self.has_decimal = False
        self.last_result = None
        
    def get_current_input(self):
        """Get current input string"""
        return self.current_input if self.current_input else "0"


class ExpressionEvaluator:
    """Handles mathematical expression evaluation with operator precedence"""
    
    def __init__(self):
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2}
        
    def evaluate(self, expression):
        """Evaluate a mathematical expression"""
        if not expression:
            raise CalculatorError("Empty expression")
            
        # Tokenize the expression
        tokens = self.tokenize(expression)
        if not tokens:
            raise CalculatorError("Invalid expression")
            
        # Convert to postfix (RPN) using Shunting Yard algorithm
        postfix = self.infix_to_postfix(tokens)
        
        # Evaluate postfix expression
        result = self.evaluate_postfix(postfix)
        
        # Format result to remove unnecessary decimal places
        if result.is_integer():
            return int(result)
        return round(result, 10)  # Round to avoid floating point issues
        
    def tokenize(self, expression):
        """Convert expression string to list of tokens"""
        # Remove whitespace
        expression = expression.replace(' ', '')
        
        # Pattern to match numbers and operators
        pattern = r'(\d+\.?\d*|\.\d+|[+\-*/%])'
        tokens = re.findall(pattern, expression)
        
        # Validate tokens
        valid_operators = set('+-*/%')
        for token in tokens:
            if token not in valid_operators:
                try:
                    float(token)  # Try to convert to float
                except ValueError:
                    raise CalculatorError(f"Invalid token: {token}")
                    
        return tokens
        
    def infix_to_postfix(self, tokens):
        """Convert infix expression to postfix (RPN)"""
        output = []
        stack = []
        
        for token in tokens:
            if token.replace('.', '').replace('-', '').isdigit() or '.' in token:
                # Token is a number
                output.append(float(token))
            elif token in self.precedence:
                # Token is an operator
                while (stack and stack[-1] in self.precedence and 
                       self.precedence[stack[-1]] >= self.precedence[token]):
                    output.append(stack.pop())
                stack.append(token)
                
        # Pop remaining operators
        while stack:
            output.append(stack.pop())
            
        return output
        
    def evaluate_postfix(self, postfix):
        """Evaluate postfix expression"""
        stack = []
        
        for token in postfix:
            if isinstance(token, float):
                stack.append(token)
            else:
                # Operator
                if len(stack) < 2:
                    raise CalculatorError("Invalid expression")
                    
                b = stack.pop()
                a = stack.pop()
                
                if token == '+':
                    result = a + b
                elif token == '-':
                    result = a - b
                elif token == '*':
                    result = a * b
                elif token == '/':
                    if b == 0:
                        raise CalculatorError("Division by zero")
                    result = a / b
                elif token == '%':
                    result = a * (b / 100)
                    
                stack.append(result)
                
        if len(stack) != 1:
            raise CalculatorError("Invalid expression")
            
        return stack[0]


class ErrorHandler:
    """Handles error messages and validation"""
    
    @staticmethod
    def validate_expression(expression):
        """Validate expression before evaluation"""
        if not expression:
            return False, "Empty expression"
            
        # Check for consecutive operators
        operators = set('+-*/%')
        for i in range(len(expression) - 1):
            if expression[i] in operators and expression[i+1] in operators:
                return False, "Consecutive operators not allowed"
                
        # Check for division by zero
        if '/0' in expression and not any(c.isdigit() for c in expression.split('/0')[1]):
            return False, "Division by zero"
            
        return True, "Valid"
    
    @staticmethod
    def get_error_message(error):
        """Get user-friendly error message"""
        error_map = {
            "Division by zero": "Cannot divide by zero",
            "Empty expression": "Please enter an expression",
            "Invalid expression": "Invalid expression format",
            "Invalid token": "Invalid character entered"
        }
        
        for key, message in error_map.items():
            if key in str(error):
                return message
        return "Calculation error"


class Calculator:
    """Main calculator class that integrates all modules"""
    
    def __init__(self):
        self.input_processor = InputProcessor()
        self.evaluator = ExpressionEvaluator()
        self.error_handler = ErrorHandler()
        self.history = []
        
    def process_input(self, value):
        """Process button input"""
        if value in '0123456789':
            self.input_processor.add_number(value)
        elif value == '.':
            self.input_processor.add_decimal()
        elif value in '+-*/%':
            self.input_processor.add_operator(value)
        elif value == '⌫':
            self.input_processor.backspace()
        elif value == 'C':
            self.input_processor.clear()
            
    def calculate(self):
        """Evaluate current expression"""
        expression = self.input_processor.get_current_input()
        
        # Validate expression
        is_valid, message = self.error_handler.validate_expression(expression)
        if not is_valid:
            return message
            
        try:
            result = self.evaluator.evaluate(expression)
            # Add to history
            self.history.append(f"{expression} = {result}")
            if len(self.history) > 10:  # Keep last 10 calculations
                self.history.pop(0)
                
            # Store result for potential reuse
            self.input_processor.last_result = result
            self.input_processor.current_input = str(result)
            return str(result)
        except CalculatorError as e:
            return self.error_handler.get_error_message(e)
        except Exception as e:
            return f"Error: {str(e)}"
            
    def get_display_text(self):
        """Get text to display"""
        return self.input_processor.get_current_input()
        
    def clear(self):
        """Clear calculator"""
        self.input_processor.clear()
        
    def get_history(self):
        """Get calculation history"""
        return self.history