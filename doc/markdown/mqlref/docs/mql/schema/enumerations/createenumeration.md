# CREATE ENUMERATION

## Purpose

To create an enumeration and its constant values.

## Grammar

```
create_enumeration_statement = "CREATE" ("ENUM" | "ENUMERATION")
                               enumeration_name "=" 
                               "{" ec_declaration_list "}" ;

enumeration_name = IDENTIFIER ; 

ec_declaration_list = ec_declaration { "," ec_declaration } ;

ec_declaration = ["DEFAULT"]  ec_name  [ec_initialization] ;

ec_name = IDENTIFIER ; 

ec_initialization = "=" signed_integer; 

signed_integer = unsigned_integer | "-" unsigned_integer | "NIL" ; 

unsigned_integer = digit { digit } ;

digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;

```

## Examples

```
CREATE ENUMERATION
phrase_type_t = {
   VP = 1,
   NP,
   AP, 
   PP,
   DEFAULT NotApplicable = -1
}
GO
```

This particular statement creates an enumeration called
“phrase\_type\_t” with the following constants and values:

| Name          | Value | Default |
| :------------ | :---: | :-----: |
| NotApplicable |  \-1  |   Yes   |
| VP            |   1   |   No    |
| NP            |   2   |   No    |
| AP            |   3   |   No    |
| PP            |   4   |   No    |


## Explanation

This statement creates a new enumeration and populates it with
enumeration constants.

If there is no declaration that has the “default” keyword, then the
first one in the list becomes the default.

If the first declaration does not have an initialization, its value
becomes 1. This is different from C and C++ `enum`s, which get 0 as the
first value by default.

If a declaration does not have an initialization, its values becomes
that of the previous declaration, plus 1. This mimics C and C++ `enum`s.

Label names must be unique within the enumeration. That is, you cannot
have two constants with the same name in the same enumeration.

Values must also be unique within the enumeration. That is, you cannot
have two different labels with the same value in the same enumeration.
This is different from C/C++ `enum`s, where two labels may have the same
value.

## Return type

There is no return value.


