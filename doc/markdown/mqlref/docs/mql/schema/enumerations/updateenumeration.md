# UPDATE ENUMERATION

## Purpose

## Grammar

```
update_enumeration_statement =
          "UPDATE" ("ENUM" | "ENUMERATION")
          enumeration_name "="  
          "{" ec_update_list "}" ;

enumeration_name = identifier; 

identifier = (alpha | "_") { (alpha | "_" | digit) } ;

alpha = "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i"
       | "j" | "k" | "l" | "m" | "n" | "o" | "p" | "q" | "r"
       | "s" | "t" | "u" | "v" | "w" | "x" | "y" | "z" 
       | "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I"
       | "J" | "K" | "L" | "M" | "N" | "O" | "P" | "Q" | "R"
       | "S" | "T" | "U" | "V" | "W" | "X" | "Y" | "Z" ;

digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;

ec_update_list = ec_update { "," ec_update } ;

ec_update = ["ADD"] ["DEFAULT"] ec_name ec_initialization
          | "UPDATE" ["DEFAULT"] ec_name ec_initialization
          | "REMOVE" ec_name;

ec_name = identifier; 

ec_initialization = "=" signed_integer; 

signed_integer = unsigned_integer | "-" unsigned_integer | "NIL" ; 

unsigned_integer = digit { digit } ;

```

## Examples

```
```

## Explanation



## Return type



