## Recursive-Descent-Interpreter
### CS 3361 Concepts of Program Language Course Project

### Usage
1. Install Python 3.7+
2. `python -m pip install pipenv`
3. `pipenv run start`
4. Follow the help prompt. Expressions may be read from stdin or an input file.


### Examples
  - Note: 
    1. All expressions must end in a period
    2. The interpreter will stop parsing after it has came to the first period
    3. Whitespace, aside from whitespace between the tail and head of an implication (->), is ignored.
        - There cannot be a space between the tail and head of the implication

```
Input: (((T -> F) -> (T -> F)) ^ (F -> T)) -> F.
Output: False
```

```
Input: (((T -> F) -> (T -> F)) ^ (F -> T)) -> T.
Output: True
```

```
Input: ~~F -> ~~T.
Output: True
```

```
in: (T v F) -> (F ^ T).
Output: False
```

```
Input: T
Output: ExpressionError  # Does not end in a period
```

```
Input: T - > T.
Output: ExpressionError  # There is a space in the implication symbol
```

```
Input: T.T -> F.
Output: True  # Everything after the first period is ignored
```

### To do
1. Use argparse
2. Compile a binary