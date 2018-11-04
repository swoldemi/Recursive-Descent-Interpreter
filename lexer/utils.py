# -*- coding: utf-8 -*-

"""Utility functions used in lexical analysis."""

from typing import Generator

from .lexer import ExpressionError

def get(expression: str) -> Generator[str, None, str]:
	"""Generator which will yeild the next token in an expression.
	
	Parameters
	-----------
	expression: str
		The expression input from the user.
	Returns
	--------
	Generator[YieldType=str, SendType=None, ReturnType=str]

	Notes
	-----
	This is not an instance method of Lexer to match 
	the patterns disscussed during class.
	"""
	saw_implication_tail = False
	for token in expression:
		if saw_implication_tail and token != ">":
			raise ExpressionError("Cannot have space between implication symbol (->)")
		elif saw_implication_tail and token == ">":
			saw_implication_tail = False
		if token == "-":
			saw_implication_tail = True
		if token == " ":
			continue
		yield token
