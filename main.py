# -*- coding: utf-8 -*-

"""Main interpreter module which uses the Lexer class."""

import cli

from lexer.lexer import Lexer
from lexer.utils import get


def main() -> None:
	"""Main interpreter routine.

	Examples
	-------
	in: T -> F.
	out: False
	
	in: (T v F) -> (F ^ T).
	out: True
	
	in: (((T -> F) -> (T -> F)) ^ (F -> T)) -> F.
	out: False

	TODO:
	Make CLI friendly by parsing input directly through sys.argv
	Allow file input also through sys.argv
	"""
	#expression = cli.init()
	#print(expression)
	expression = "T -> F."
	tokens = get(expression)
	lexer = Lexer()
	lexer.lex = next(tokens) # Store the first token without passing generator into __init__
	valid = lexer.B(tokens)
	print(lexer.stack)
	if valid:
		print("Result:", lexer.stack.pop())
	else:
		print("Invalid expression.")


if __name__ == "__main__":
	main()