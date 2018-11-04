# -*- coding: utf-8 -*-

from sys import version_info
from typing import Any, Tuple, NewType, TypeVar, Union

is_python37 = (version_info.major == 3) and (version_info.minor == 7)


class Syntax(object):
	"""Defines the syntax used by the Lexer; only used for informal annotations.
	Sequences of TypeVar definitions that contain TypeVar are referring to the 
	TypeVar being defined on the same line, to the left of the equals sign (recursive reference).

	Notes
	-----
	In comparison to their order on the project specification, these non-terminal definitions are reversed.
	EpsilionEmpty is simply the empty case of a non-terminal.
	Terminator is the period expected at the end of the expression.

	Warnings
	--------
	This requires Python 3.7+
	"""
	if is_python37:
		Intersection = Union # Remap for simplicity since typing.Intersection still doesn't exist
		EpsilonEmpty = TypeVar("EpsilonEmpty", str, None)
		
		Atom = TypeVar("Atom", bool, str)
		Literal = TypeVar("Literal", Atom, None)
		AndTail = TypeVar("AndTail", Union[Intersection[str, Literal, TypeVar], EpsilonEmpty], None)
		AndTerm = TypeVar("AndTerm", Intersection[Literal, AndTail], None)
		OrTail = TypeVar("OrTail", Union[Intersection[str, AndTerm, TypeVar], EpsilonEmpty], None)
		OrTerm = TypeVar("OrTerm", Intersection[AndTerm, OrTail], None)
		ImplyTail = TypeVar("ImplyTail", Union[Intersection[str, OrTerm, TypeVar], EpsilonEmpty], None)
		ImplyTerm = TypeVar("ImplyTerm", Intersection[OrTerm, ImplyTail], None)
		Terminator = TypeVar("Terminator", str, None)
		BooleanStatement = TypeVar("BooleanStatement", Intersection[ImplyTerm, Terminator], None)
	else:
		raise RuntimeError("Please use Python 3.7.")
