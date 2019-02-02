# CREATE ENUMERATION

## Purpose

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
```

## Explanation



## Return type



