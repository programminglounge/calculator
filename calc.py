import tkinter as tk
import random
import math
import re

def enterdot():
  w.insert("end", ".")

def enterdelete():
  w.delete("end-2c")

def enterac():
  w.delete("1.0", "end")
  
def enter0():
  w.insert("end", "0")
  
def enter1():
  w.insert("end", "1")
  
def enter2():
  w.insert("end", "2")
  
def enter3():
  w.insert("end", "3")
  
def enter4():
  w.insert("end", "4")
  
def enter5():
  w.insert("end", "5")
  
def enter6():
  w.insert("end", "6")
  
def enter7():
  w.insert("end", "7")
  
def enter8():
  w.insert("end", "8")
  
def enter9():
  w.insert("end", "9")
  
def enterplus():
  w.insert("end", "+")
  
def enternegative():
  w.insert("end", "-")
  
def entermultiply():
  w.insert("end", "*")
  
def enterpercent():
  w.insert("end", "%")
  
def enterdivide():
  w.insert("end", "/")
  
def enterequal():
  content = w.get("1.0", "end")
  operands = re.split('\*|\/|\+|\-|\n|\%', content)
  operators = []
  for i in content:
    if not i.isdigit() and i!='.':
      operators.append(i)
  operands.pop()
  operators.pop()
  if (len(operands) != len(operators)+1):
    enterac()
    w.insert("end", "error: Please check the list of operators and operands")
  else:
    result = 0;
    while (len(operators) != 0):
      if ('/' in operators and '*' in operators and '%' in operators):
        if (operators.index('/') < operators.index('*') and operators.index('/') < operators.index('%')):
          result = result + float (operands[operators.index('/')])/ float (operands[operators.index('/')+1])
          operands.pop(operators.index('/'))
          operands.pop(operators.index('/'))
          operands.insert(operators.index('/'), result)
          result = 0
          operators.pop(operators.index('/'), result)
        elif (operators.index('*') < operators.index('/') and operators.index('*') < operators.index('%')):
          result = result + float (operands[operators.index('*')])* float (operands[operators.index('*')+1])
          operands.pop(operators.index('*'))
          operands.pop(operators.index('*'))
          operands.insert(operators.index('*'), result)
          result = 0
          operators.pop(operators.index('*'), result)
        elif (operators.index('%') < operators.index('/') and operators.index('%') < operators.index('*')):
          result = result + float (operands[operators.index('%')])% float (operands[operators.index('%')+1])
          operands.pop(operators.index('%'))
          operands.pop(operators.index('%'))
          operands.insert(operators.index('%'), result)
          result = 0
          operators.pop(operators.index('%'), result)
      elif ('/' in operators and '*' in operators):
        if(operators.index('/') < operators.index('*')):
          result = result + float (operands[operators.index('/')])/ float (operands[operators.index('/')+1])
          operands.pop(operators.index('/'))
          operands.pop(operators.index('/'))
          operands.insert(operators.index('/'), result)
          result = 0
          operators.pop(operators.index('/'), result)
        else:
          result = result + float (operands[operators.index('*')])* float (operands[operators.index('*')+1])
          operands.pop(operators.index('*'))
          operands.pop(operators.index('*'))
          operands.insert(operators.index('*'), result)
          result = 0
          operators.pop(operators.index('*'), result)
            
      elif ('/' in operators and '%' in operators):
        if(operators.index('/') < operators.index('%')):
          result = result + float (operands[operators.index('/')])/ float (operands[operators.index('/')+1])
          operands.pop(operators.index('/'))
          operands.pop(operators.index('/'))
          operands.insert(operators.index('/'), result)
          result = 0
          operators.pop(operators.index('/'), result)
        else:
          result = result + float (operands[operators.index('%')])% float (operands[operators.index('%')+1])
          operands.pop(operators.index('%'))
          operands.pop(operators.index('%'))
          operands.insert(operators.index('%'), result)
          result = 0
          operators.pop(operators.index('%'), result) 
       
      elif ('*' in operators and '%' in operators):
        if(operators.index('*') < operators.index('%')):
          result = result + float (operands[operators.index('*')])* float (operands[operators.index('*')+1])
          operands.pop(operators.index('*'))
          operands.pop(operators.index('*'))
          operands.insert(operators.index('*'), result)
          result = 0
          operators.pop(operators.index('*'), result)
        else:
          result = result + float (operands[operators.index('%')])% float (operands[operators.index('%')+1])
          operands.pop(operators.index('%'))
          operands.pop(operators.index('%'))
          operands.insert(operators.index('%'), result)
          result = 0
          operators.pop(operators.index('%'), result) 
          
      elif ('%' in operators):
        result = result + float (operands[operators.index('%')])% float (operands[operators.index('%')+1])
        operands.pop(operators.index('%'))
        operands.pop(operators.index('%'))
        operands.insert(operators.index('%'), result)
        result = 0
        operators.pop(operators.index('%'), result)
        
      elif ('/' in operators):
        result = result + float (operands[operators.index('/')])/ float (operands[operators.index('/')+1])
        operands.pop(operators.index('/'))
        operands.pop(operators.index('/'))
        operands.insert(operators.index('/'), result)
        result = 0
        operators.pop(operators.index('/'), result)
        
      elif ('*' in operators):
        result = result + float (operands[operators.index('*')])* float (operands[operators.index('*')+1])
        operands.pop(operators.index('*'))
        operands.pop(operators.index('*'))
        operands.insert(operators.index('*'), result)
        result = 0
        operators.pop(operators.index('*'), result)
        
      elif ('+' in operators):
        result = result + float (operands[operators.index('+')])+ float (operands[operators.index('+')+1])
        operands.pop(operators.index('+'))
        operands.pop(operators.index('+'))
        operands.insert(operators.index('+'), result)
        result = 0
        operators.pop(operators.index('+'), result)
        
      
      elif ('-' in operators):
        result = result + float (operands[operators.index('-')])- float (operands[operators.index('-')+1])
        operands.pop(operators.index('-'))
        operands.pop(operators.index('-'))
        operands.insert(operators.index('-'), result)
        result = 0
        operators.pop(operators.index('-'), result)
     
  result = float(operands[0])
  enterac()
  w.insert("end", result)
  
def enterequal():
  content = w.get("1.0", "end")
  operands = re.split('\*|\/|\+|\-|\n|\%', content)
  operators = []
  for i in content:
    if not i.isdigit() and i!='.':
      operators.append(i)
  operands.pop()
  operators.pop()
  if (len(operands) != len(operators)+1):
    enterac()
    w.insert("end", "error: Please check the list of operators and operands")
  else:
    result = 0;
    while (len(operators) != 0):
      if ('/' in operators and '*' in operators and '%' in operators):
        if (operators.index('/') < operators.index('*') and operators.index('/') < operators.index('%')):
          result = result + float (operands[operators.index('/')])/ float (operands[operators.index('/')+1])
          operands.pop(operators.index('/'))
          operands.pop(operators.index('/'))
          operands.insert(operators.index('/'), result)
          result = 0
          operators.pop(operators.index('/'), result)
        elif (operators.index('*') < operators.index('/') and operators.index('*') < operators.index('%')):
          result = result + float (operands[operators.index('*')])* float (operands[operators.index('*')+1])
          operands.pop(operators.index('*'))
          operands.pop(operators.index('*'))
          operands.insert(operators.index('*'), result)
          result = 0
          operators.pop(operators.index('*'), result)
        elif (operators.index('%') < operators.index('/') and operators.index('%') < operators.index('*')):
          result = result + float (operands[operators.index('%')])% float (operands[operators.index('%')+1])
          operands.pop(operators.index('%'))
          operands.pop(operators.index('%'))
          operands.insert(operators.index('%'), result)
          result = 0
          operators.pop(operators.index('%'), result)
      elif ('/' in operators and '*' in operators):
        if(operators.index('/') < operators.index('*')):
          result = result + float (operands[operators.index('/')])/ float (operands[operators.index('/')+1])
          operands.pop(operators.index('/'))
          operands.pop(operators.index('/'))
          operands.insert(operators.index('/'), result)
          result = 0
          operators.pop(operators.index('/'), result)
        else:
          result = result + float (operands[operators.index('*')])* float (operands[operators.index('*')+1])
          operands.pop(operators.index('*'))
          operands.pop(operators.index('*'))
          operands.insert(operators.index('*'), result)
          result = 0
          operators.pop(operators.index('*'), result)
            
      elif ('/' in operators and '%' in operators):
        if(operators.index('/') < operators.index('%')):
          result = result + float (operands[operators.index('/')])/ float (operands[operators.index('/')+1])
          operands.pop(operators.index('/'))
          operands.pop(operators.index('/'))
          operands.insert(operators.index('/'), result)
          result = 0
          operators.pop(operators.index('/'), result)
        else:
          result = result + float (operands[operators.index('%')])% float (operands[operators.index('%')+1])
          operands.pop(operators.index('%'))
          operands.pop(operators.index('%'))
          operands.insert(operators.index('%'), result)
          result = 0
          operators.pop(operators.index('%'), result) 
       
      elif ('*' in operators and '%' in operators):
        if(operators.index('*') < operators.index('%')):
          result = result + float (operands[operators.index('*')])* float (operands[operators.index('*')+1])
          operands.pop(operators.index('*'))
          operands.pop(operators.index('*'))
          operands.insert(operators.index('*'), result)
          result = 0
          operators.pop(operators.index('*'), result)
        else:
          result = result + float (operands[operators.index('%')])% float (operands[operators.index('%')+1])
          operands.pop(operators.index('%'))
          operands.pop(operators.index('%'))
          operands.insert(operators.index('%'), result)
          result = 0
          operators.pop(operators.index('%'), result) 
          
      elif ('%' in operators):
        result = result + float (operands[operators.index('%')])% float (operands[operators.index('%')+1])
        operands.pop(operators.index('%'))
        operands.pop(operators.index('%'))
        operands.insert(operators.index('%'), result)
        result = 0
        operators.pop(operators.index('%'), result)
        
      elif ('/' in operators):
        result = result + float (operands[operators.index('/')])/ float (operands[operators.index('/')+1])
        operands.pop(operators.index('/'))
        operands.pop(operators.index('/'))
        operands.insert(operators.index('/'), result)
        result = 0
        operators.pop(operators.index('/'), result)
        
      elif ('*' in operators):
        result = result + float (operands[operators.index('*')])* float (operands[operators.index('*')+1])
        operands.pop(operators.index('*'))
        operands.pop(operators.index('*'))
        operands.insert(operators.index('*'), result)
        result = 0
        operators.pop(operators.index('*'), result)
        
      elif ('+' in operators):
        result = result + float (operands[operators.index('+')])+ float (operands[operators.index('+')+1])
        operands.pop(operators.index('+'))
        operands.pop(operators.index('+'))
        operands.insert(operators.index('+'), result)
        result = 0
        operators.pop(operators.index('+'), result)
        
      
      elif ('-' in operators):
        result = result + float (operands[operators.index('-')])- float (operands[operators.index('-')+1])
        operands.pop(operators.index('-'))
        operands.pop(operators.index('-'))
        operands.insert(operators.index('-'), result)
        result = 0
        operators.pop(operators.index('-'), result)
  if (operands[0] >=0):   
    result = float(operands[0])
    sqrtresult = math.sqrt(result)
    enterac()
    w.insert("end", sqrtresult)
  
  else:
    enterac()
    w.insert("end", "underneath square root can not be negative")
    
root = tk.Tk()
root.geometry('600*600')
w = tk.Text(root, height = '10', width = '50')
pane = tk.Frame(root)
pane.grid (row = 1, column = 0)

button_0 = tk.Button(pane, text = "0", command = enter0, width = 8)
button_0.grid(row = 5, column = 0)
button_dot = tk.Button(pane, text= ".", command = enterdot, width = 8)
button_dot.grid (row = 5, column = 1)
button_back = tk.Button(pane, text= "back", command = enterdelete, width = 8)
button_back.grid (row = 5, column = 2)
button_equal = tk.Button(pane, text= "=", command = enterequal, width = 8)
button_equal.grid (row = 5, column = 3)

button_1 = tk.Button(pane, text = "1", command = enter1, width = 8)
button_1.grid(row = 4, column = 0)
button_2 = tk.Button(pane, text= "2", command = enter2, width = 8)
button_2.grid (row = 4, column = 1)
button_3 = tk.Button(pane, text= "3", command = enter3, width = 8)
button_3.grid (row = 4, column = 2)
button_plus = tk.Button(pane, text= "+", command = enterplus, width = 8)
button_plus.grid (row = 4, column = 3)

button_4 = tk.Button(pane, text = "4", command = enter4, width = 8)
button_4.grid(row = 3, column = 0)
button_5 = tk.Button(pane, text= "5", command = enter5, width = 8)
button_5.grid (row = 3, column = 1)
button_6 = tk.Button(pane, text= "6", command = enter6, width = 8)
button_6.grid (row = 3, column = 2)
button_minus = tk.Button(pane, text= "-", command = enternegative, width = 8)
button_minus.grid (row = 3, column = 3)

button_7 = tk.Button(pane, text = "7", command = enter7, width = 8)
button_7.grid(row = 2, column = 0)
button_8 = tk.Button(pane, text= "8", command = enter8, width = 8)
button_8.grid (row = 2, column = 1)
button_9 = tk.Button(pane, text= "9", command = enter9, width = 8)
button_9.grid (row = 2, column = 2)
button_multiply = tk.Button(pane, text= "*", command = entermultiply, width = 8)
button_multiply.grid (row = 2, column = 3)

button_AC = tk.Button(pane, text = "AC", command = enterac, width = 8)
button_AC.grid(row = 1, column = 0)
button_par = tk.Button(pane, text= "sqrt", command = entersqrt, width = 8)
button_par.grid (row = 1, column = 1)
button_percent = tk.Button(pane, text= "%", command = enterpercent, width = 8)
button_percent.grid (row = 1, column = 2)
button_divide = tk.Button(pane, text= "/", command = enterdivide, width = 8)
button_divide.grid (row = 1, column = 3)

root.mainloop()
