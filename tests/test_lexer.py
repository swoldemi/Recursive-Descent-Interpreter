# -*- coding: utf-8 -*-

import os
import sys
import unittest

sys.path.append(os.path.dirname(os.getcwd()))

from lexer.lexer import Lexer, ExpressionError
from lexer.utils import get


class TestLexer(unittest.TestCase):

	cases = {
		"(((T -> F) -> (T -> F)) ^ (F -> T)) -> T.": [True, True],
		"(((T -> F) -> (T -> F)) ^ (F -> T)) -> F.": [False, True],
		"T                                       .": [True, True],
		"F                                       .": [False, True],
		"T ^ T                                   .": [True, True],
		"T ^ F                                   .": [False, True],
		"F ^ F                                   .": [False, True],
		"F v F                                   .": [False, True],
		"T v F                                   .": [True, True],
		"T -> F                                  .": [False, True],
		"F -> F                                  .": [True, True],
		"T -> T                                  .": [True, True],
		"~T v F                                  .": [False, True],
		"~T v ~        F                         .": [True, True],
		"~~F -> ~~T                              .": [True, True],
		"This is not valid                        ": [None, False],
		"(((T -> F) -> (T -> F)) ^ (F -> T)) -> F ": [None, False],
	}

	def test_results(self) -> None:
		"""For every key in cases, assert that the result of
		the expression `key` is equal to cases[key][0]
		and the Lexer instance returns cases[key][1].


		Notes
		-----
		If the entire expression is valid, but it does not end with a period
		an ExpressionError is raised. Else, the interpreter will fail fast.
		"""
		for case, result in zip(self.cases.keys(), self.cases.values()):
			token = get(case)
			lexer = Lexer()
			lexer.lex = next(token)
			
			try:
				valid = lexer.B(token)
			except ExpressionError as e:
				pass
			
			if valid:
				self.assertEqual(lexer.stack.pop(), result[0])
			self.assertEqual(valid, result[1])


if __name__ == "__main__":
	unittest.main()
