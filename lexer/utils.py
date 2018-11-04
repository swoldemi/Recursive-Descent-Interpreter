# -*- coding: utf-8 -*-

"""Utility functions used in lexical analysis."""

from typing import Generator


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
	for token in expression:
		print(f"TOKEN IS '{token}'")
		if token == " ":
			continue
		yield token
