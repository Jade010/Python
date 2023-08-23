import math

class Calculator(object):
	"""docstring for Calculator"""
	# _Part 1: Implement this constructor_

	# Create a new Calculator with maxSize slots in the stack
	# @param maxSize - number of spaces in the stack
	def __init__(self, maxSize):
		self.maxSize = maxSize # max size of stack
		self.stack = [] # the stack
		self.variables = {"x": None, "y": None, "z": None} # the variables

	# _Part 2: Implement this method_

	# Push the specified double onto the stack
	# @param d - the value to push
	# Return False if the stack too large
	def push(self, value):
		# check if stack is full
		if len(self.stack) >= self.maxSize: 
			return False
		else: # if not full then append value to stack
			self.stack.append(value)
			return True

	# _Part 3: Implement this method_

	# Pop the top value off the stack
	# Return None if the stack is currently empty.
	def pop(self):
		# if stack is empty return none
		if len(self.stack) == 0:
			return None
		else: # if not empty then remove and return
			return self.stack.pop()

	# _Part 4: Implement this method_

	# Calculate the value from a String of operations.

	# Basic operations:
	# "+" - adds the top two entries on the stack
	# "*" - multiplies the top two entries on the stack
	# "-" - subtracts the top entry in the stack from the 2nd entry in the stack
	# "/" - divides the 2nd entry in the stack by the top entry in the stack
	# "^" - raises the 2nd entry in the stack to the power indicated by the top entry in the stack
	# "lg" - takes the lg (log base 2) of the top entry in the stack

	# Variables
	# expand the use of the calculator by supporting the use of
	# three variables 'x', 'y', and 'z' in expressions. Specifically
	# for each variable, there should be a way to set its value 
	# the tokens 'setx', 'sety', and 'setz' respectively, and a way to 
	# read its value -- the tokens: 'x', 'y', and 'z' respectively.
	# With these new operators we should be able to evaluate
	# expressions such as:
	# "10 4 + setx" (set the 'x' variable to 14)
	# "42 x /"      (divide 42 by the value stored for 'x' -- currently 14)
	# "x x -"       (subtract 14 from 14)

	# @param inputString - the string representing a mathematic expression
	# Return None if a specified operator is unknown.

	def calculate(self, inputString):
		tokens = inputString.split() # split input string into a list of tokens
		# looping through tokens
		for token in tokens:
			# if the token is a number convert to a float and push in stack
			if token.isnumeric():
				self.push(float(token))
			# if the token is an operator then use required formulas
			elif token in ['+', '-', '*', '/', '^']:
				if len(self.stack) < 2:
					return None
				a = self.pop()
				b = self.pop()

				if token == '+':
					self.push(b + a)
				elif token == '-':
					self.push(b - a)
				elif token == '*':
					self.push(b * a)
				elif token == '/':
					if a == 0: # prevent divide by 0 error
						return None
					self.push(b / a)
				elif token == '^':
					self.push(b ** a)
			elif token == 'lg':
				if len(self.stack) < 1: 
					return None
				self.push(math.log2(self.pop()))
			# If the token is a variable setter then set value of variable in it has at least one value
			elif token in ['setx', 'sety', 'setz']:
				if len(self.stack) < 1:
					return None
				self.variables[token[-1]] = self.pop()
			# if token is a variable
			elif token in ['x', 'y', 'z']:
				# if not set a value then return none
				if self.variables[token] is None:
					return None
				self.push(self.variables[token]) # push value of variable on stack
			else:
				return None
		return self.pop() # pop value from stack and return it as the result

	def getVariable(self, var):
		return self.variables.get(var)


#Some sample tests for you to run to make sure your code works.
if __name__ == '__main__':
	c = Calculator(5)
	print(c.calculate("10 4 +"), " should equal 14")
	print(c.calculate("4 2 /"), " should equal 2")
	print(c.calculate("10 4 + 3 * 2 /"), " should equal 21")
	print(c.calculate("16 lg"), " should equal 4")
	print(c.calculate("16 4 -"), " should equal 12")
	print(c.calculate("5 16 4 + -"), " should equal -15")
	print(c.calculate("5 20 -"), " should equal -15")
	print(c.calculate("5"), " should equal 5")
	print(c.calculate("10 4 + 3 * 2 /"), " should equal 21")
	print(c.calculate("10 4 + setx"), " should equal None")
	print(c.calculate("42 x /"), " should equal 3")
	print(c.calculate("x x -"), " should equal 0")





















