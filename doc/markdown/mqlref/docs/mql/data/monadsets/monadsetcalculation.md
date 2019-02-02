# MONAD SET CALCULATION

## Purpose

## Grammar

```
monad_set_calculation_statement =
    "MONAD"  "SET"  "CALCULATION"
    monad_set_chain;

monad_set_chain = monad_set { monad_set_operator monad_set } ;

monad_set = "{" monad_set_element_list "}" ;

monad_set_element_list = monad_set_element { "," monad_set_element } ;

monad_set_element = unsigned_integer
                  | unsigned_integer "-" unsigned_integer
                  | unsigned_integer "-" ;

unsigned_integer = digit { digit } ;

digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;

monad_set_operator = "UNION"      
                   | "DIFFERENCE"
                   | "INTERSECT";  

```

## Examples

```
```

## Explanation



## Return type



