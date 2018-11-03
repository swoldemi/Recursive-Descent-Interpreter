# -*- coding: utf-8 -*-

"""Main interpreter module which uses the Lexer class."""

from typing import Generator

import cli

from lexer.lexer import Lexer


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
		if token == " ":
			continue
		yield token


def main() -> None:
	"""Main interpreter routine.

	Example
	-------
	in: T -> F.
	out: False
	
	in: (T v F) -> (F ^ T).
	out: True
	
	in: (((T -> F) -> (T -> F)) ^ (F -> T)) -> F
	out: 
	TODO:
	Make CLI friendly by parsing input directly through sys.argv
	Allow file input also through sys.argv
	"""
	#expression = cli.init()
	#print(expression)
	expression = "T -> F"
	lex = Lexer(expression)
	valid = lex.B(get(expression))
	print(get)
	if valid:
		print(lex.result)
	else:
		print("Invalid expression.")
	

if __name__ == "__main__":
	main()