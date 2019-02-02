# GET FEATURES

## Purpose

## Grammar

```
get_features_statement =
     "GET" ("FEATURE" | "FEATURES") feature_list
     "FROM" ("OBJECT" | "OBJECTS")
     "WITH" id_ds_specification
     "[" object_type_name "]" ;

feature_list = feature_list_member { "," feature_list_member } ;

feature_list_member = feature_name
                    | feature_name "(" IDENTIFIER ")" 
                    | feature_name "(" "MONADS" ")" ;

feature_name = IDENTIFIER | "MONADS" ;

id_ds_specification = ("ID_D" | "ID_DS") "=" id_d_list;

id_d_list = id_d_const { "," id_d_const } ;

id_d_const = unsigned_integer | "NIL" ;

unsigned_integer = digit { digit } ;

digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;

object_type_name = IDENTIFIER ;  

```

## Examples

```
```

## Explanation



## Return type



