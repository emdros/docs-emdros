# UPDATE OBJECTS BY MONADS

## Grammar

```
update_objects_by_monads_statement =
     "UPDATE" ("OBJECT" | "OBJECTS") "BY" monad_specification 
     object_update_specification;

monad_specification = "MONADS" "=" monad_set; 

monad_set = "{" monad_set_element_list "}" ;

monad_set_element_list = monad_set_element { "," monad_set_element } ;

monad_set_element = unsigned_integer
                  | unsigned_integer "-" unsigned_integer
                  | unsigned_integer "-" ;

unsigned_integer = digit { digit } ;

digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;

object_update_specification = 
     "[" object_type_name   list_of_feature_assignments  "]" ;

object_type_name = identifier;  

identifier = (alpha | "_") { (alpha | "_" | digit) } ;

alpha = "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i"
       | "j" | "k" | "l" | "m" | "n" | "o" | "p" | "q" | "r"
       | "s" | "t" | "u" | "v" | "w" | "x" | "y" | "z" 
       | "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I"
       | "J" | "K" | "L" | "M" | "N" | "O" | "P" | "Q" | "R"
       | "S" | "T" | "U" | "V" | "W" | "X" | "Y" | "Z" ;

list_of_feature_assignments = feature_assignment { feature_assignment } ;

feature_assignment = feature_name ":=" expression ";" ;

feature_name = identifier | "MONADS" ;

expression = signed_integer /* integer and id_d */
           | STRING
           | identifier /* enumeration constant */
           | monad_set  /* set of monads */
           | "(" ")"    /* empty list */
           | "(" list_of_integer ")" 
           | "(" list_of_identifier ")" ;

signed_integer = unsigned_integer | "-" unsigned_integer | "NIL" ; 

list_of_integer = signed_integer { "," signed_integer } ;

list_of_identifier = identifier { "," identifier } ;

```

## Examples

```
```

## Explanation



## Return type



