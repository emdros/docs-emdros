# GET FEATURES

## Grammar

```
get_features_statement =
     "GET" ("FEATURE" | "FEATURES") feature_list
     "FROM" ("OBJECT" | "OBJECTS")
     "WITH" id_ds_specification
     "[" object_type_name "]" ;

feature_list = feature_list_member { "," feature_list_member } ;

feature_list_member = feature_name
                    | feature_name "(" identifier ")" 
                    | feature_name "(" "MONADS" ")" ;

feature_name = identifier | "MONADS" ;

identifier = (alpha | "_") { (alpha | "_" | digit) } ;

alpha = "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i"
       | "j" | "k" | "l" | "m" | "n" | "o" | "p" | "q" | "r"
       | "s" | "t" | "u" | "v" | "w" | "x" | "y" | "z" 
       | "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I"
       | "J" | "K" | "L" | "M" | "N" | "O" | "P" | "Q" | "R"
       | "S" | "T" | "U" | "V" | "W" | "X" | "Y" | "Z" ;

digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;

id_ds_specification = ("ID_D" | "ID_DS") "=" id_d_list;

id_d_list = id_d_const { "," id_d_const } ;

id_d_const = unsigned_integer | "NIL" ;

unsigned_integer = digit { digit } ;

object_type_name = identifier;  

```

## Examples

```
```

## Explanation



## Return type



