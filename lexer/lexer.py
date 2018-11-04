# -*- coding: utf-8 -*-


from typing import Generator

import logme


@logme.log
class Lexer(object):
	"""Recursive descent functions required by the non-terminals
	presented in the project specification.


	Attributes
	----------
	stack : List[bool]
		Stack used for evaluation of valid expressions.
		The end of the list is the top of the stack.
	lex : str
		Current token being recursively verified in the instance.

	Notes
	------
	Recursive calls of instance methods do not need stack or lex to be 
	passed as they are accessed as instance attributes. 
	"""
	def __init__(self):
		self.stack = []
		self.lex = None
	

	def A(self, get: Generator[str, None, str]) -> bool:
		try:
			if self.lex == "T":
				self.stack.append(True)
				self.lex = next(get)
				return True
			elif self.lex == "F":
				self.stack.append(False)
				self.lex = next(get)
				return True
			elif self.lex == "(":
				# Parenthesis matching
				self.lex = next(get)
				if self.IT(get):
					if self.lex == ")":
						self.lex = next(get)
						return True
			return False
		except StopIteration:
			raise ExpressionError("SyntaxError. Expression must end with a period.")


	
	def L(self, get: Generator[str, None, str]) -> bool:
		if self.A(get):
			return True
		if self.lex == "~":
			self.lex = next(get)
			if self.L(get):
				# Perform NOT operation and add to stack
				self.stack.append((not self.stack.pop()))
				return True 
		return False


	def AT_TAIL(self, get: Generator[str, None, str]) -> bool:
		if self.lex == "^":
			self.lex = next(get)
			if self.L(get):
				# Perform AND operation and add to stack
				self.stack.append(
					self.stack.pop() and self.stack.pop()
				)
				if self.AT_TAIL(get):
					return True
			else: 
				return False
		return True
				

	def AT(self, get: Generator[str, None, str]) -> bool:
		if self.L(get):
			if self.AT_TAIL(get):
				return True
		return False
	

	def OT_TAIL(self, get: Generator[str, None, str]) -> bool:
		if self.lex == "v":
			self.lex = next(get)
			if self.AT(get):
				# Perform OR operation and add to stack
				q = self.stack.pop()
				p = self.stack.pop()
				self.stack.append(p or q)
				if self.OT_TAIL(get):
					return True
		return True


	def OT(self, get: Generator[str, None, str]) -> bool:
		if self.AT(get):
			if self.OT_TAIL(get):
				return True
		return False


	def IT_TAIL(self, get: Generator[str, None, str]) -> bool:
		if self.lex == "-":
			self.lex = next(get)
			if self.lex == ">":
				self.lex = next(get)
				if self.OT(get):
					if self.IT_TAIL(get):
						# Expression is valid
						# Evaluate implication and add to stack
						rhs = self.stack.pop()
						lhs = self.stack.pop()
						implication = ((not lhs) or (rhs))  # By truth table
						self.stack.append(implication)
						return True
		return True


	def IT(self, get: Generator[str, None, str]) -> bool:
		if self.OT(get):
			if self.IT_TAIL(get):
				return True
		return False


	def B(self, get: Generator[str, None, str]) -> bool:
		if self.IT(get):
			if self.lex == ".":
				return True
		return False


class ExpressionError(Exception):
	pass
