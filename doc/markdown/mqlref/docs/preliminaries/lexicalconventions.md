# Lexical conventions

The lexical conventions for MQL are as follows:

## Comments
There are two kinds of comments:
    
1.  Enclosed in `/\*` (opening) and `\*/` (closing). This kind of
    comment can span multiple lines. This is the same as C-style
    comments.

2.  Starting with `//` and ending at the end of the line. This is the
    style used in C++.

## Keywords are case-insensitive

All keywords (such as `CREATE`, `SELECT`, `<=`, etc.) are
case-*in*sensitive insofar as they are made up of letters.  (Some
keywords are symbols not containing letters, such as `=`, `<>`, `<=`,
`>=`, etc.)

## Identifiers are the same as in C

 A T\_IDENTIFIER begins with any letter (a-z,A-Z) or an underscore
(\_), followed by zero or more letters (a-z,A-Z), numbers (0-9), or
underscores (\_). For example, “Word”, “\_delimiter”, “i18n”, and
“phrase\_type\_t” are all identifiers. However, “8bf” is not an
identifier because it does not start with a letter or an underscore.
Neither is bf@foo.com an identifier, because it does not consist
solely of letters, underscores, and numbers.
    
Whether a T\_IDENTIFIER is case-sensitive depends on what it stands
for (i.e., what its “referent” is). See the following table for a
description.

| T\_IDENTIFIER referent    | Case-sensitivity |
| :------------------------ | :--------------- |
| Database name             | insensitive      |
| Object type name          | insensitive      |
| Enumeration name          | insensitive      |
| Enumeration constant name | sensitive        |

## Integers

A T\_INTEGER is any sequence of one or more digits (0-9). For example,
“0”, “42”, and “747” are all integers.

## Strings

A T\_STRING is one of two kinds:
    
1.  A T\_STRING can start with a single quote (`'`), followed by zero
    or more characters which are not single quotes, and ending with
    another single quote (`'`). Such a string can contain newlines,
    but it cannot contain escape sequences.  This makes it better
    suited to being used in regular expressions than the next kind of
    string.

2.  A T\_STRING can also start with a double quote (`"`), followed by
    zero or more characters, escape-sequences (see the following
    table), or newlines, and ending with a double quote (`"`).

| Escape sequences | Meaning                                 |
| :--------------: | :-------------------------------------- |
|       \\n        | newline (ASCII 10)                      |
|       \\t        | horizontal tab (ASCII 9)                |
|       \\v        | vertical tab (ASCII 11)                 |
|       \\b        | backspace (ASCII 8)                     |
|       \\a        | bell (ASCII 7)                          |
|       \\r        | carriage-return (ASCII 13)              |
|       \\f        | form-feed (ASCII 12)                    |
|       \\\\       | slash (\\) (ASCII 92)                   |
|       \\?        | question-mark (?) (ASCII 63)            |
|       \\’        | single quote (’) (ASCII 39)             |
|        \\        | double quote () (ASCII 34)              |
|      \\ooo       | Octal number (e.g., \\377 is 255)       |
|      \\xXX       | Hexadecimal number (e.g., \\xFF is 255) |

## Marks

A T\_MARKS is a sequence of one or more identifiers, each prefixed by
a backping (‘). For example, the following are all T\_MARKS:

- ‘yellow
- ‘red‘context
- ‘marks‘are‘useful
- ‘Flash\_Gordon‘was‘a‘Hero

More precisely, a T\_MARKS conforms to the regular expression:

```
(`[a-zA-Z_][a-zA-Z_0-9]*)+
```

## Whitespace

White-space (spaces, newlines, and tabs) is ignored except in
T\_STRINGs.



# Name-spaces

A name-space, in computer-terminology, is a language-domain with fixed
borders within which names must be unique. *Within* a name-space, two
different entities *cannot* be called by the same name without causing a
name-clash. In other words, within a name-space, names must be unique.
However, if two name-spaces are *orthogonal* to each other, then a name
from one name-space *can* be the same as a name from the other
name-space *without* causing a name-clash.

In MQL, the following name-spaces exist. They are all orthogonal to each
other:

  - Each object type forms a name-space with respect to its features.
    That is, a single object type cannot have two features with the same
    name, but different object types can have features with the same
    name. The two features with the same name need not even have the
    same feature type. This is because all name-spaces are orthogonal to
    each other.

  - Each enumeration forms a name-space with respect to its constants.
    That is, a single enumeration cannot have two enumeration constants
    with the same name, but different enumerations can have enumeration
    constants with the same name. Since all name-spaces are orthogonal
    to each other, the two enumeration constants with the same name need
    not have the same integer value.

  - Each database forms a global name-space with respect to object type
    names. That is, object type names must be globally unique within a
    database. However, since all name-spaces are orthogonal to each
    other, you can have features or enumeration constants which have the
    same name as an object type.

# Top-level constraints on MQL syntax

The MQL engine can receive any number (greater than or equal to 1) of
MQL statements. The only requirement is that each statement must end
with the keyword `GO`. This keyword acts as a delimiter between each
statement. The last statement may also be terminated with `GO`, but
need not be. Single statements on their own need not be terminated with
`GO` either.

If you connect to the MQL engine in daemon-mode, you must append the
meta-level statement “QUIT” after the “GO” of the last statement.
