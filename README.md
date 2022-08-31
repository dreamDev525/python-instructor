# Python Instructor

- An article to complete the Python course.
- **Notice:** Wherever you see the word **[*Optional*]**, it means that it is not a part of your introductory class, but you can check and study as you wish.
- **Disclaimer:** _The content of this repository is only for testing and training and is provided at the discretion of the author; So it may not be suitable for production or other conditions._

## How to _install_ and _run_ python?

- Check this [link](/lessons/python/installation/README.md) ([farsi](/lessons/python/installation/README-FARSI.md)) to install and run Python.

## Homework

- Check [this link](/README-PYTHON-HOMEWORKS.md)

## Examples <sub>[Optional]</sub>

- Check [this link](/README-PYTHON-EXAMPLES.md)

## Roadmaps

- [Python](/README-PYTHON-ROADMAP.md)
- [Web](/README-WEB.md)
- [Network <sub>Basic Concepts</sub>](/README-NETWORK.md)
- [More](/README-MORE.md)

## Headings

1. Introduction
1. Syntax
   - `pep8, naming, comments, indentation, ...`
1. Variables
1. [Strings](/lessons/python/concepts/string)
   - [`encode, decode`](/lessons/python/concepts/string/encode-string.py)
   - [`strip, lstrip, rstrip`](/lessons/python/concepts/string/trim-string.py)
   - [`join, concatenation`](/lessons/python/concepts/string/concat-string.py)
   - [`endswith, startswith, find, rfind, index, rindex`](/lessons/python/concepts/string/search-string.py)
   - [`translate, maketrans, format, format_map`](/lessons/python/concepts/string/format-string.py)
   - [`partition, rpartition, splitlines, split, slice`](/lessons/python/concepts/string/split-string.py)
   - [`(title, capitalize), (lower, upper, swapcase, casefold), (center, ljust, rjust)`](/lessons/python/concepts/string/audit-string.py)
   - [`in, (istitle, islower, isupper), isspace, isprintable, isidentifier, (isascii, isalpha), (isalnum, isnumeric, isdecimal, isdigit)`](/lessons/python/concepts/string/check-string.py)
   - [`zfill, count, replace, len, expandtabs, multi-line, loop-over-characters, reverse`](/lessons/python/concepts/string/other-string-functions.py)
   - [Scape Chars `\t \f \" \n \r \b \oct \hex`](/lessons/python/concepts/string/scape-chars.py)
1. [Boolean](/lessons/python/concepts/boolean/boolean-concept.py)
1. [Random](/lessons/python/concepts/random/general-random-functions.py)
   - `random(), randint(), shuffle(), choice()`
1. [Operators](/lessons/python/concepts/operators)
   1. [Arithmetic](/lessons/python/concepts/operators/arithmetic-operators.py) `+ -` ,...
   2. [Assignment](/lessons/python/concepts/operators/assignment-operators.py) `= += -=` ,...
   3. [Comparison](/lessons/python/concepts/operators/comparison-operators.py) `== != >=` ,...
   4. [Logical](/lessons/python/concepts/operators/logical-operators.py) `and, or, not`
   5. [Identity](/lessons/python/concepts/operators/identity-operators.py) `is, is not`
   6. [Membership](/lessons/python/concepts/operators/membership-operators.py) `in, not in`
   7. [Bitwise](/lessons/python/concepts/operators/bitwise-operators.py) `& | ^ ~ << >>`
1. Debugging (break point)
1. List
   - Ordered, Changeable, Indexed, Allow Duplicate
   - [`access, assign, iterate, list(), .append(), .insert(), .remove(), del, .pop(), .copy(), .extend(), .clear(), len(), .count(), slice, join, unpack, in, .index(), .reverse(), .sort()`](/lessons/python/concepts/collections/list-access.py)
1. Tuple
   - Ordered, Unchangeable, Indexed, Allow Duplicate
   - Tuples are **unchangeable**, or **immutable** so you cannot add or remove items from it
   - [`access, tuple with one item, tuple(), iterate, del completely, len(), .count(), slice, join, unpack, in, .index()`](/lessons/python/concepts/collections/tuple-access.py)
1. Set, FrozenSet
   - Unordered, Unchangeable (By index, But you can add/remove), Unindexed, No Duplicate
   - [`access, len(), set(), in, .add(), .update(), (.remove(), .discard(), .pop(), del), .copy(), .clear(), (.union(), intersection, difference, symmetric_difference), (disjoint, subset, superset)`](/lessons/python/concepts/collections/set-access.py)
   - [`frozenset()`](/lessons/python/concepts/collections/set-frozen.py)
1. Dictionary
   - Ordered, Changeable, Key Value, No Duplicate
   - [`access, assign, .update(), dict(), .keys(), .values(), .items(), zip(), len(), .pop(), .popitem(), del, .clear(), .copy(), .fromkeys(), .setdefault())`](/lessons/python/concepts/collections/dict-access.py)
1. DataTypes
   - Numbers: [`Integer, Float, Complex`](/lessons/python/concepts/data-types/data-type-number.py)
   - Sequence: [`String`](/lessons/python/concepts/data-types/data-type-string.py), [`Range`](/lessons/python/concepts/data-types/data-type-range.py), [`List`](/lessons/python/concepts/collections/list-access.py), [`Tuple`](/lessons/python/concepts/collections/tuple-access.py.py), `Bytes`, `ByteArray`
   - Set: [`Set`](/lessons/python/concepts/collections/set-access.py), [`FrozenSet`](/lessons/python/concepts/collections/set-frozen.py)
   - Map: [`Dictionary`](/lessons/python/concepts/collections/dict-access.py)
   - Nothing: `None`
   - Boolean: [`Boolean`](/lessons/python/concepts/boolean/boolean-concept.py)
   - Binary: [`Bytes, ByteArray, MemoryView`](/lessons/python/concepts/data-types/data-type-bytes.py)
     - `bytes` is immutable; however `bytearray` is mutable
1. Module
1. Conversion, TypeCasting
1. Input
1. Keywords
   - if, elif, else
   - for
   - while, continue, break
   - try, except, finally
   - and, or, not, in, is
   - [import, from, as](/lessons/python/concepts/keywords/keywords-import.py)
   - class, def, lambda, pass, return, del
   - [global, nonlocal](/lessons/python/concepts/keywords/keywords-scope.py)
   - assert<sub>[Optonal]</sub>, raise<sub>[Optonal]</sub>
   - with <sub>[Optonal]</sub>
   - [yield](/lessons/python/concepts/keywords/keywords-yield.py) <sub>[Optonal]</sub>
1. [Function, Method, Lambda](/lessons/python/concepts/object-oriented/types-of-methods.py)
1. Comperhension
1. Scope, Globals, Locals
   - `locals(), globals()`
1. Read File, Write File, Pickle
1. Math
1. Date
1. OOP Concepts

### Optional

1. VENV
1. \_\_name\_\_
1. PIP
   - [`install, list, uninstall, freeze`, ...](/lessons/python/installation/README-PIP.md)
1. Arguments
   - [`*argv`, `**kwargs`](/lessons/python/concepts/advanced/argv-kwargs.py)
1. [Eval, Exec](/lessons/python/concepts/advanced/eval-exec.py)
1. [Operator Overload](/lessons/python/concepts/operators/operator-overload.py)
1. Exception, Custom Exception, Types of Errors
1. [Assertion](/lessons/python/concepts/advanced/simple-assertion.py)
1. [Decorator](/lessons/python/concepts/advanced/simple-decorator.py)
1. MetaClasses, MetaProgramming
1. [Generator](/lessons/python/concepts/advanced/simple-generator.py)
1. Iterator
   - [Iterator, Iterable](/lessons/python/concepts/advanced/simple-iterator.py)
   - [Custom Iterator](/lessons/python/concepts/advanced/custom-iterator.py)
1. Closure
1. [Descriptor](/lessons/python/concepts/advanced/simple-descriptor.py)
1. [Reflection](/lessons/python/concepts/advanced/simple-reflection.py)
1. Regular Expression
1. Socket [`client`](/lessons/python/examples/simple-socket-client.py), [`server`](/lessons/python/examples/simple-socket-server.py)
1. Web Service, Web Socket
1. SQL (MariaDB, Sqlite, ...)
1. NoSQL (MongoDB, Redis, ...)
1. ORM
1. Serialization, Deserialization
1. JSON, CSV, XML
1. Mutable vs Immutable in practice

### Modules, Libs, SDKs, ... <sub>[Advance]</sub>

- Tkinter
- NumPy
- PyGame
- OpenCV
- Django
- Flask
- Kivy
- Pillow
- PyAutoGUI
- PyTorch
- TF
- Chain
- ...
