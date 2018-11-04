# -*- coding: utf-8 -*-

"""Main interpreter module which uses the Lexer class."""

import cli

from lexer.lexer import Lexer
from lexer.utils import get


def main() -> None:
	"""Main interpreter routine."""
	expression = cli.init()
	tokens = get(expression)
	lexer = Lexer()
	lexer.lex = next(tokens)  # Store the first token without passing generator into __init__
	valid = lexer.B(tokens)
	if valid:
		print("Result:", lexer.stack.pop())
	else:
		print("Invalid expression.")


if __name__ == "__main__":
	main()