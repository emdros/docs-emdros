# SELECT OBJECT TYPES USING ENUM

## Purpose

## Grammar

```
select_object_types_using_enum_statement =
           "SELECT"  ["OBJECT"] "TYPES"
           "USING"   ("ENUM" | "ENUMERATION")  enumeration_name;

enumeration_name = identifier; 

identifier = (alpha | "_") { (alpha | "_" | digit) } ;

alpha = "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i"
       | "j" | "k" | "l" | "m" | "n" | "o" | "p" | "q" | "r"
       | "s" | "t" | "u" | "v" | "w" | "x" | "y" | "z" 
       | "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I"
       | "J" | "K" | "L" | "M" | "N" | "O" | "P" | "Q" | "R"
       | "S" | "T" | "U" | "V" | "W" | "X" | "Y" | "Z" ;

digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;

```

## Examples

```
```

## Explanation



## Return type


