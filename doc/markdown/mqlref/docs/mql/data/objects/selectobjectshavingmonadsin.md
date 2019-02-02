# SELECT OBJECTS HAVING MONADS IN

## Purpose

## Grammar

```
select_objects_having_monads_in_statement =
               "SELECT" "OBJECTS"  "HAVING" "MONADS" "IN"
               monad_set
               "[" (object_type_name | "ALL") "]" ;

monad_set = "{" monad_set_element_list "}" ;

monad_set_element_list = monad_set_element { "," monad_set_element } ;

monad_set_element = unsigned_integer
                  | unsigned_integer "-" unsigned_integer
                  | unsigned_integer "-" ;

unsigned_integer = digit { digit } ;

digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;

object_type_name = IDENTIFIER ;  

```

## Examples

```
```

## Explanation



## Return type



