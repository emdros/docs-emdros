# CREATE MONAD SET

## Purpose

## Grammar

```
create_monad_set_statement = "CREATE"  "MONAD"  "SET"
                             monad_set_name
                             "WITH"  monad_specification;

monad_set_name = IDENTIFIER ;  

monad_specification = "MONADS" "=" monad_set; 

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



