# SELECT OBJECTS AT

## Purpose

## Grammar

```
select_objects_at_statement =
               "SELECT" ["OBJECTS"] "AT" single_monad_specification
               "[" object_type_name "]" ;

single_monad_specification = "MONAD" "=" unsigned_integer;

unsigned_integer = digit { digit } ;

digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;

object_type_name = IDENTIFIER ;  

```

## Examples

```
```

## Explanation



## Return type



