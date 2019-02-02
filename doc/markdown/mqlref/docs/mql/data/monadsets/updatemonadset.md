# UPDATE MONAD SET

## Purpose

## Grammar

```
update_monad_set_statement = "UPDATE"  "MONAD"  "SET"
                             monad_set_name  
                             (monad_set_operator | "REPLACE")
                             (monad_set_name | monad_set) ;

monad_set_name = IDENTIFIER ;  

monad_set_operator = "UNION"      
                   | "DIFFERENCE"
                   | "INTERSECT";  

monad_set = "{" monad_set_element_list "}" ;

monad_set_element_list = monad_set_element { "," monad_set_element } ;

monad_set_element = unsigned_integer
                  | unsigned_integer "-" unsigned_integer
                  | unsigned_integer "-" ;

unsigned_integer = digit { digit } ;

digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;

```

## Examples

```
```

## Explanation



## Return type



