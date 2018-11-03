# -*- coding: utf-8 -*-

from typing import Generator


class Lexer(object):
	"""Recursive descent functions required by the non-terminals
	presented in the project specification.


	Attributes
	----------
	expression : str
		Expression to be checked for syntatic correctness and evaluated
	stack : list
		Stack used for evaluation of valid expressions.
		The end of the list is the top of the stack.
	result : bool
		Result of the expression, if the expression is valid

	Notes
	------
	Recursive calls of instance methods do not need stack or lex to be 
	passed as they are accessed as instance attributes. 
	"""
	def __init__(self, expression: str):
		self.expression = expression
		self.stack = []
		self.result = None
		

	def B(self, get: Generator[str, None, str]) -> bool:
		lex = next(get)
		print(lex)
		"""
		if self.IT():
			if 
		"""
		return True
