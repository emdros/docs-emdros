# UPDATE OBJECT TYPE

## Grammar

```
update_object_type_statement = "UPDATE" ["OBJECT"] "TYPE"
                               "[" object_type_name
                                   feature_update_list
                               "]" ;

object_type_name = identifier;  

identifier = (alpha | "_") { (alpha | "_" | digit) } ;

alpha = "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i"
       | "j" | "k" | "l" | "m" | "n" | "o" | "p" | "q" | "r"
       | "s" | "t" | "u" | "v" | "w" | "x" | "y" | "z" 
       | "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I"
       | "J" | "K" | "L" | "M" | "N" | "O" | "P" | "Q" | "R"
       | "S" | "T" | "U" | "V" | "W" | "X" | "Y" | "Z" ;

digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;

feature_update_list = feature_update { feature_update } ;

feature_update = ["ADD"] feature_declaration
               | "REMOVE" feature_name ";"  ;

feature_declaration = feature_name ":" feature_type 
                      default_specification ["COMPUTED"] ";"
                    | feature_name ":" "LIST" "OF" 
                      list_feature_type ";" ; 

feature_name = identifier | "MONADS" ;

feature_type = "INTEGER" [with_index]
             | "STRING" [string_length] [from_set] [with_index]
             | "ASCII" [string_length] [from_set] [with_index]
             | "ID_D" [with_index]
             | identifier [with_index] /* For enumerations */
             | "SET" "OF" "MONADS" /* Same as MULTIPLE RANGE SET OF MONADS */
             | "SINGLE"   "MONAD"  "SET"  "OF"  "MONADS"
             | "SINGLE"   "RANGE"  "SET"  "OF"  "MONADS"
             | "MULTIPLE" "RANGE"  "SET"  "OF"  "MONADS" ;

with_index = "WITH"    "INDEX"
           | "WITHOUT" "INDEX"; 

string_length = "(" unsigned_integer ")" ;

unsigned_integer = digit { digit } ;

from_set = "FROM"  "SET";

default_specification = ["DEFAULT" expression ];

expression = signed_integer /* integer and id_d */
           | STRING
           | identifier /* enumeration constant */
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

list_of_identifier = identifier { "," identifier } ;

list_feature_type = "INTEGER" 
                  | "ID_D" ;

```

## Examples

```
```

## Explanation



## Return type



