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

  
