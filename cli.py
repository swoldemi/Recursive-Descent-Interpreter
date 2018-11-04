# -*- coding: utf-8 -*-

"""Command-line interface config and tools."""

import sys

from typing import Union

from lexer.lexer import ExpressionError


header = """
  ____              _                    _____                              _             
 | __ )  ___   ___ | | ___  __ _ _ __   | ____|_  ___ __  _ __ ___  ___ ___(_) ___  _ __  
 |  _ \ / _ \ / _ \| |/ _ \/ _` | '_ \  |  _| \ \/ / '_ \| '__/ _ \/ __/ __| |/ _ \| '_ \ 
 | |_) | (_) | (_) | |  __/ (_| | | | | | |___ >  <| |_) | | |  __/\__ \__ \ | (_) | | | |
 |____/ \___/ \___/|_|\___|\__,_|_| |_| |_____/_/\_\ .__/|_|  \___||___/___/_|\___/|_| |_|
  ___       _                           _          |_|                                    
 |_ _|_ __ | |_ ___ _ __ _ __  _ __ ___| |_ ___ _ __                                      
  | || '_ \| __/ _ \ '__| '_ \| '__/ _ \ __/ _ \ '__|                                     
  | || | | | ||  __/ |  | |_) | | |  __/ ||  __/ |                                        
 |___|_| |_|\__\___|_|  | .__/|_|  \___|\__\___|_|                                        
\t\t\t|_|
by Simon Woldemichael for Dr. Richard Watson's CS 3361 - Concepts of Programming Languages                                                      
\r\n
"""


class InvalidSelectionError(Exception):
	def __init__(self):
		Exception.__init__(self, "\r\nInput must be 1, 2, or 3.")


def init() -> Union[str, Exception]:
	"""Initialize input selections.
	
	Returns
	-------
	Union[str, NoReturn]
		str: 
			Input expression to be lexed (either from a file or stdin).
		Exception: 
			If the user wanted to read from a file but the file is invalid.
			If the used typed a number other than 1, 2, or 3.
	"""
	sys.stdout.write(header)
	sys.stdout.write("[+] Your expression may only contain the following tokens: ->, (, ), v, ^, T, F, ~\r\n")
	sys.stdout.write("[+] v (lowercase letter V) denotes a disjunction (logical-or).\r\n")
	sys.stdout.write("[+] ^ (carat symbol) denotes a conjunction (logical-and).\r\n")
	sys.stdout.write("[+] Your expression must end with a period.\r\n")
	sys.stdout.write("\r\n")
	
	sys.stdout.write("[1] Quit.\r\n")
	sys.stdout.write("[2] Read expression from text file.\r\n")
	sys.stdout.write("[3] Read expression from console input.\r\n")
	
	try:
		selection = int(input("[*] Select an option [1, 2, or 3]: "))
	except ValueError:
		# Make sure input is number
		raise InvalidSelectionError()
	
	try:
		# Make sure input is either 1, 2, or 3
		if selection not in (1, 2, 3):
			raise InvalidSelectionError()
		elif selection == 1:
			# Selected Quit
			sys.stdout.write("[x] Quitting...\r\n")
			sys.exit(0)
		elif selection == 2:
			# Read input from file
			file_name = input("[*] Please type the name of the file: ")
			try:
				with open(file_name, "r+", encoding="utf-8") as source:
					expression = source.read()
			except OSError:
				sys.stderr.write(f"[x] Unable to open file: {file_name}\r\n")
				raise
		else:
			# Read input from stdin
			expression = input("[*] Please input your expression: ")
			if not expression:
				# Check empty
				raise ExpressionError("InputError. Expression is empty.")
	except Exception as e:
		sys.stderr.write(f"[x] Unexpected error: {e}\r\n") 
		raise
	return expression
