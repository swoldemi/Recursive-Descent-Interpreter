# -*- coding: utf-8 -*-

from typing import Generator


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
	

	def B(self, get: Generator[str, None, str]) -> bool:
		lex = next(get)
		print(lex)
		"""
		if self.IT():
			if 
		"""
		return True
