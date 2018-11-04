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
		self.logger.info(f"Inside of [A]. Lex is {self.lex}")
		if self.lex == "T":
			self.logger.info("[A] adding True to stack.")
			self.stack.append(True)
			self.lex = next(get)
			return True
		elif self.lex == "F":
			self.logger.info("[A] adding False to stack.")
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
		self.logger.info(f"[A] is returning False. Lex is {self.lex}.")
		return False

	
	def L(self, get: Generator[str, None, str]) -> bool:
		self.logger.debug("Inside of [L]")
		if self.A(get):
			self.logger.info(f"[L] is returning True[0]. Lex is {self.lex}")		
			return True
		if self.lex == "~":
			self.lex = next(get)
			if self.L(get):
				# Perform NOT operation and add to stack
				self.stack.append((not self.stack.pop()))
				self.logger.info(f"[L] is returning True[1]. Lex is {self.lex}")		
				return True 
		self.logger.info(f"[L] is returning False. Lex is {self.lex}")		
		return False


	def AT_TAIL(self, get: Generator[str, None, str]) -> bool:
		self.logger.debug("Inside of [AT_TAIL]")
		if self.lex == "^":
			self.lex = next(get)
			if self.L(get):
				# Perform AND operation and add to stack
				self.stack.append(
					self.stack.pop() and self.stack.pop()
				)
				if self.AT_TAIL(get):
					self.logger.info(f"[AT_TAIL] is returning True[0]. Lex is {self.lex}")		
					return True
			else: 
				self.logger.info(f"[AT_TAIL] is returning False. Lex is {self.lex}")		
				return False
		self.logger.info(f"[AT_TAIL] is returning True[1]. Lex is {self.lex}")		
		return True
				

	def AT(self, get: Generator[str, None, str]) -> bool:
		self.logger.debug("Inside of [AT].")
		if self.L(get):
			if self.AT_TAIL(get):
				self.logger.info(f"[AT] is returning True. Lex is {self.lex}")		
				return True
		self.logger.info(f"[AT] is returning False. Lex is {self.lex}")		
		return False
	

	
	def OT_TAIL(self, get: Generator[str, None, str]) -> bool:
		self.logger.debug("Inside of [OT_TAIL].")
		if self.lex == "v":
			self.lex = next(get)
			if self.AT(get):
				# Perform OR operation and add to stack
				q = self.stack.pop()
				p = self.stack.pop()
				self.stack.append(p and q)
				if OT_TAIL(get):
					self.logger.info(f"[OT_TAIL] is returning True[0]. Lex is {self.lex}")		
					return True
		self.logger.info(f"[OT_TAIL] is returning True[1]. Lex is {self.lex}")		
		return True


	def OT(self, get: Generator[str, None, str]) -> bool:
		self.logger.debug("Inside of [OT].")
		if self.AT(get):
			if self.OT_TAIL(get):
				self.logger.info(f"[OT] is returning True. Lex is {self.lex}")		
				return True
		self.logger.info(f"[OT] is returning False. Lex is {self.lex}")		
		return False


	def IT_TAIL(self, get: Generator[str, None, str]) -> bool:
		self.logger.debug("Inside of [IT_TAIL].")
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
						implication = ((not lhs) or (rhs)) # By truth table
						self.stack.append(implication)
						self.logger.info(f"[IT_TAIL] is returning True. Lex is {self.lex}")		
						return True
		self.logger.info(f"[IT_TAIL] is returning False. Lex is {self.lex}")		
		return False


	def IT(self, get: Generator[str, None, str]) -> bool:
		self.logger.debug("Inside of [IT].")
		if self.OT(get):
			if self.IT_TAIL(get):
				self.logger.info(f"[IT] is returning True. Lex is {self.lex}")				
				return True
		self.logger.info(f"[IT] is returning False. Lex is {self.lex}")		
		return False


	def B(self, get: Generator[str, None, str]) -> bool:
		self.logger.debug("Inside of [B].")
		if self.IT(get):
			if self.lex == ".":
				self.logger.info(f"[B] is returning True. Lex is {self.lex}")		
				return True
		self.logger.info(f"[B] is returning False. Lex is {self.lex}")		
		return False
