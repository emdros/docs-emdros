# UPDATE ENUMERATION

## Purpose

## Grammar

```
update_enumeration_statement =
          "UPDATE" ("ENUM" | "ENUMERATION")
          enumeration_name "="  
          "{" ec_update_list "}" ;

enumeration_name = IDENTIFIER ; 

ec_update_list = ec_update { "," ec_update } ;

ec_update = ["ADD"] ["DEFAULT"] ec_name ec_initialization
          | "UPDATE" ["DEFAULT"] ec_name ec_initialization
          | "REMOVE" ec_name;

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



