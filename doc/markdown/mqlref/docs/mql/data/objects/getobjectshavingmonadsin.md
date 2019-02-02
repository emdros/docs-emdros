# GET OBJECTS HAVING MONADS IN

## Purpose

## Grammar

```
get_objects_having_monads_in_statement =
        "GET" "OBJECTS" "HAVING" "MONADS" "IN"
        in_specification
        using_monad_feature
        "[" object_type_name
            ["GET" ("ALL" | feature_list)]
        "]" ;

in_specification = monad_set
                 | "ALL" /* = all_m-1 */ ;

monad_set = "{" monad_set_element_list "}" ;

monad_set_element_list = monad_set_element { "," monad_set_element } ;

monad_set_element = unsigned_integer
                  | unsigned_integer "-" unsigned_integer
                  | unsigned_integer "-" ;

unsigned_integer = digit { digit } ;

digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;

using_monad_feature = /* empty: Equivalent to
                         "USING" "MONAD" "FEATURE" "MONADS" */
                    | "USING" "MONAD" "FEATURE" IDENTIFIER
                    | "USING" "MONAD" "FEATURE" "MONADS"; 

object_type_name = IDENTIFIER ;  

feature_list = feature_list_member { "," feature_list_member } ;

feature_list_member = feature_name
                    | feature_name "(" IDENTIFIER ")" 
                    | feature_name "(" "MONADS" ")" ;

feature_name = IDENTIFIER | "MONADS" ;

```

## Examples

```
```

## Explanation



## Return type



