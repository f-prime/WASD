#!/usr/bin/env python
#WASD Interpreter
#Version 1.1
import sys
def wasd(code):
  array = [0] * 1000000
  pointer = 0
  x = 0
  while True: 
     if x >= len(code)-1: break
     if pointer < 0 or array[pointer] < 0:
	pointer = 0
	array[pointer] = 0
	continue
     if code[x] == "a": pointer -= 1
     elif code[x] == "d": pointer += 1
     elif code[x] == "s": array[pointer] -= 1
     elif code[x] == "w": array[pointer] += 1
     elif code[x] == "e": print(chr(array[pointer]))
     elif code[x] == "q": 
	try: array[pointer] = input("Input: ")
	except: print "Input must be an integer"
     elif code[x] == "(":
	while code[x] != ")":x += 1
     elif code[x] == "1":
	if array[pointer] == 0:
	  while True:
	     if code[x] == "a": pointer -= 1
	     elif code[x] == "d": pointer += 1
    	     elif code[x] == "s": array[pointer] -= 1
     	     elif code[x] == "w": array[pointer] += 1
     	     elif code[x] == "e": 
		try:print(chr(array[pointer]))
		except:break
	     elif code[x] == "(":
		while code[x] != ")":x += 1	
     	     elif code[x] == "q":
	              try: array[pointer] = input("Input: ")
        	      except: print "Input must be an integer"
	     x += 1
	     if code[x] == "2":
	      while True:
		x -= 1
		if code[x] == "1":break
     x += 1   
try:
  if ".wasd" not in sys.argv[1]:
    print("Not a valid WASD file")
  with open(sys.argv[1], 'r') as code: 
	try:wasd(code.read())
	except:pass
except:
    print "Useage: python wasd.py <file.wasd>"
