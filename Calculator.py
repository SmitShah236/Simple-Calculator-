import tkinter as tk
from tkinter import messagebox
import math

root = tk.Tk()
root.title("Simple Calculator")

# Defining colors and fonts
bg_color = "#000000"  
button_color = "#808080"  
entry_bg = "#333333"  
entry_border_color = "#ffffff"  
font_large = ('Arial', 24)
font_medium = ('Arial', 14)
font_title = ('Arial', 16, 'bold')  

root.configure(bg=bg_color)

# Calculator Frame
calculator_frame = tk.Frame(root, bg=bg_color, bd=5, relief="raised", highlightbackground="white", highlightthickness=2)
calculator_frame.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")
calculator_frame.update_idletasks()  

# Field to input Operations
entry_frame = tk.Frame(calculator_frame, bg=entry_bg, highlightbackground="white", highlightthickness=1)
entry_frame.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")

entry = tk.Entry(entry_frame, width=18, font=font_large, borderwidth=0, relief="flat", bg=entry_bg, fg="white", justify='right')
entry.grid(row=0, column=0, ipady=10, sticky="nsew") 

entry_frame.grid_columnconfigure(0, weight=1)
entry_frame.grid_rowconfigure(0, weight=1)

# Functionality of Operations
memory = {'value': 0} 

def button_click(value):
    current = entry.get()
    
    if value == 'C':
        entry.delete(0, tk.END)
    elif value == 'AC':
        entry.delete(0, tk.END)
        memory['value'] = 0
    elif value == 'OFF':
        root.destroy()
    elif value == '=':
        try:
            current = current.replace('%', '*0.01')
            current = current.replace('÷', '/')
            current = current.replace('×', '*')
            current = current.replace('−', '-')  
            current = evaluate_factorial(current)
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except Exception as e:
            messagebox.showerror("Error", f"Invalid Input: {e}")
    elif value == '√':
        try:
            value = float(current)
            result = math.sqrt(value)
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except ValueError:
            messagebox.showerror("Error", "Invalid Input")
        except:
            messagebox.showerror("Error", "Math Error")
    elif value == '^':
        entry.insert(tk.END, '**')
    elif value == '%':
        if current and current[-1].isdigit():
            entry.insert(tk.END, '%')
        else:
            entry.insert(tk.END, '0%')
    elif value == '(':
        entry.insert(tk.END, '(')
    elif value == ')':
        entry.insert(tk.END, ')')
    elif value == 'M+':
        try:
            memory['value'] += float(current)
            entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Invalid Input for Memory Addition")
    elif value == 'M-':
        try:
            memory['value'] -= float(current)
            entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Invalid Input for Memory Subtraction")
    elif value == 'MR':
        entry.insert(tk.END, memory['value'])
    elif value == 'MC':
        memory['value'] = 0
    elif value == '±':
        if current:
            if current[0] == '-':
                entry.delete(0)
            else:
                entry.insert(0, '-')
    elif value == '!':
        try:
            result = str(factorial(int(current)))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except ValueError:
            messagebox.showerror("Error", "Invalid Input for Factorial")
    else:
        entry.insert(tk.END, value)

def evaluate_factorial(expression):
    """Evaluate factorial (!) in the expression."""
    index = expression.find('!')
    while index != -1:
        start = index
        end = start + 1
        while start > 0 and expression[start - 1].isdigit():
            start -= 1
        num = int(expression[start:end - 1])
        result = factorial(num)
        expression = expression[:start] + str(result) + expression[end:]
        index = expression.find('!', end)
    return expression

def factorial(n):
    """Calculate factorial of n."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

buttons = [
    'OFF', 'MR', 'MC', 'M-', 'M+',
    '^', '!', '(', ')', '÷',
    '%', '7', '8', '9', '×',
    '√', '4', '5', '6', '−',
    'C', '1', '2', '3', '+',
    'AC', '0', '.', '±', '='
]

def create_button(text, row, col, width=3, height=1):
    font = font_medium
    if text == '−':
        font = ('Arial', 18)  
    return tk.Button(calculator_frame, text=text, padx=10, pady=10, width=width, height=height, font=font,
                     bg=button_color, fg="white", borderwidth=0, relief="flat", highlightthickness=0,
                     command=lambda: button_click(text))

for i, button_text in enumerate(buttons):
    row = i // 5 + 1
    col = i % 5
    button = create_button(button_text, row, col)
    button.grid(row=row, column=col, padx=3, pady=3, sticky="nsew")

for i in range(5):
    calculator_frame.grid_columnconfigure(i, weight=1)
for i in range((len(buttons) // 5) + 1):
    calculator_frame.grid_rowconfigure(i, weight=1)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.resizable(False, False) 

root.mainloop()
