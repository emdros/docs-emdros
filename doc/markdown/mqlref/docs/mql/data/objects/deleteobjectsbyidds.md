# DELETE OBJECTS BY ID DS

## Purpose

## Grammar

```
delete_objects_by_id_ds_statement =
     "DELETE" ("OBJECT" | "OBJECTS") "BY" id_ds_specification
     object_deletion_specification;

id_ds_specification = ("ID_D" | "ID_DS") "=" id_d_list;

id_d_list = id_d_const { "," id_d_const } ;

id_d_const = unsigned_integer | "NIL" ;

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



