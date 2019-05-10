# UPDATE OBJECT TYPE

## Purpose

To alter the schema of a given object type, either by adding or
removing features.

## Grammar

```
update_object_type_statement = "UPDATE" ["OBJECT"] "TYPE"
                               "[" object_type_name
                                   feature_update_list
                               "]" ;

object_type_name = IDENTIFIER ;  

feature_update_list = feature_update { feature_update } ;

feature_update = ["ADD"] feature_declaration
               | "REMOVE" feature_name ";"  ;

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
UPDATE OBJECT TYPE
[Word
    ADD no_of_morphemes : integer;
    REMOVE surface_without_accents;
]
GO
```
## Explanation

This statement *updates an object type*. It can either add a feature or
remove an already-existing feature. When adding a new feature, the ADD
keyword is optional. Other than that, it has exactly the same notation
as for feature declarations under the CREATE OBJECT TYPE statement.

Removing a feature requires the REMOVE keyword, the feature name, and a
semicolon.

Both additions and removals must be terminated with semicolon, even if
the `feature_update` is the only `feature_update` in the list of
`feature_update`s.

Note that the statement does not allow for *changing* the type of an
already existing feature, only for adding or removing features.


## Return type

There is no return value.

