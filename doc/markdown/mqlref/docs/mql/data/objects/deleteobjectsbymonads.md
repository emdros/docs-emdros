# DELETE OBJECTS BY MONADS

## Purpose

## Grammar

```
delete_objects_by_monads_statement =
     "DELETE" ("OBJECT" | "OBJECTS") "BY" monad_specification
     object_deletion_specification;

monad_specification = "MONADS" "=" monad_set; 

monad_set = "{" monad_set_element_list "}" ;

monad_set_element_list = monad_set_element { "," monad_set_element } ;

monad_set_element = unsigned_integer
                  | unsigned_integer "-" unsigned_integer
                  | unsigned_integer "-" ;

unsigned_integer = digit { digit } ;

digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;

object_deletion_specification = 
     "[" object_type_name_to_delete "]" ;

object_type_name_to_delete = object_type_name
                           | "ALL";

object_type_name = IDENTIFIER ;  

```

## Examples

```
```

## Explanation



## Return type



