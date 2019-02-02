# CREATE OBJECT TYPE

## Purpose

## Grammar

```
create_object_type_statement = "CREATE" ["OBJECT"] "TYPE"
                               [if_not_exists]
                               [range_type]
                               [monad_uniqueness_type]
                               "[" object_type_name
                                  [feature_declaration_list]
                               "]"; 

if_not_exists = "IF"  "NOT"  "EXISTS" ;

range_type = "WITH"  "MULTIPLE"  "RANGE"  "OBJECTS"
           | "WITH"  "SINGLE"    "RANGE"  "OBJECTS"
           | "WITH"  "SINGLE"    "MONAD"  "OBJECTS" ;

monad_uniqueness_type = "HAVING"  "UNIQUE"  "FIRST"  "MONADS"
                      | "HAVING"  "UNIQUE"
                        "FIRST"   "AND"     "LAST"   "MONADS"
                      | "WITHOUT" "UNIQUE"  "MONADS" ;

object_type_name = IDENTIFIER ;  

feature_declaration_list = feature_declaration { feature_declaration } ;

feature_declaration = feature_name ":" feature_type 
                      default_specification ["COMPUTED"] ";"
                    | feature_name ":" "LIST" "OF" 
                      list_feature_type ";" ; 

feature_name = IDENTIFIER | "MONADS" ;

feature_type = "INTEGER" [with_index]
             | "STRING" [string_length] [from_set] [with_index]
             | "ASCII" [string_length] [from_set] [with_index]
             | "ID_D" [with_index]
             | IDENTIFIER [with_index] /* For enumerations */
             | "SET" "OF" "MONADS" /* Same as MULTIPLE RANGE SET OF MONADS */
             | "SINGLE"   "MONAD"  "SET"  "OF"  "MONADS"
             | "SINGLE"   "RANGE"  "SET"  "OF"  "MONADS"
             | "MULTIPLE" "RANGE"  "SET"  "OF"  "MONADS" ;

with_index = "WITH"    "INDEX"
           | "WITHOUT" "INDEX"; 

string_length = "(" unsigned_integer ")" ;

unsigned_integer = digit { digit } ;

digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;

from_set = "FROM"  "SET";

default_specification = ["DEFAULT" expression ];

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

list_feature_type = "INTEGER" 
                  | "ID_D" ;

```

## Examples

```
```

## Explanation



## Return type



