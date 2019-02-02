# UPDATE OBJECTS BY ID DS

## Purpose

## Grammar

```
update_objects_by_id_ds_statement = 
     "UPDATE" ("OBJECT" | "OBJECTS") "BY" id_ds_specification
     object_update_specification;

id_ds_specification = ("ID_D" | "ID_DS") "=" id_d_list;

id_d_list = id_d_const { "," id_d_const } ;

id_d_const = unsigned_integer | "NIL" ;

unsigned_integer = digit { digit } ;

digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;

object_update_specification = 
     "[" object_type_name   list_of_feature_assignments  "]" ;

object_type_name = IDENTIFIER ;  

list_of_feature_assignments = feature_assignment { feature_assignment } ;

feature_assignment = feature_name ":=" expression ";" ;

feature_name = IDENTIFIER | "MONADS" ;

expression = signed_integer /* integer and id_d */
           | STRING
           | IDENTIFIER /* enumeration constant */
           | monad_set  /* set of monads */
           | "(" ")"    /* empty list */
           | "(" list_of_integer ")" 
           | "(" list_of_identifier ")" ;

signed_integer = unsigned_integer | "-" unsigned_integer | "NIL" ; 

monad_set = "{" monad_set_element_list "}" ;

monad_set_element_list = monad_set_element { "," monad_set_element } ;

monad_set_element = unsigned_integer
                  | unsigned_integer "-" unsigned_integer
                  | unsigned_integer "-" ;

list_of_integer = signed_integer { "," signed_integer } ;

list_of_identifier = IDENTIFIER { "," IDENTIFIER } ;

```

## Examples

```
```

## Explanation



## Return type



