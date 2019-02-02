# SELECT ALL OBJECTS

## Grammar

```
select_all_objects_statement = select_clause
                  ( [in_clause] | "IN" monad_set_name )
                  with_max_range_clause
                  returning_clause
                  where_clause;

select_clause = "SELECT"
                ("FOCUS" | "ALL")
                ["OBJECTS"];

in_clause = "IN" in_specification ;

in_specification = monad_set
                 | "ALL" /* = all_m-1 */ ;

monad_set = "{" monad_set_element_list "}" ;

monad_set_element_list = monad_set_element { "," monad_set_element } ;

monad_set_element = unsigned_integer
                  | unsigned_integer "-" unsigned_integer
                  | unsigned_integer "-" ;

unsigned_integer = digit { digit } ;

digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;

monad_set_name = identifier;  

identifier = (alpha | "_") { (alpha | "_" | digit) } ;

alpha = "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i"
       | "j" | "k" | "l" | "m" | "n" | "o" | "p" | "q" | "r"
       | "s" | "t" | "u" | "v" | "w" | "x" | "y" | "z" 
       | "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I"
       | "J" | "K" | "L" | "M" | "N" | "O" | "P" | "Q" | "R"
       | "S" | "T" | "U" | "V" | "W" | "X" | "Y" | "Z" ;

with_max_range_clause =  /* empty : WITH MAX RANGE MAX_M MONADS */
                      | "WITH" "MAX" "RANGE" "MAX_M" "MONADS"
                      | "WITH" "MAX" "RANGE" unsigned_integer "MONADS" 
                      | "WITH" "MAX" "RANGE" "FEATURE" feature_name
                        "FROM" "[" object_type_name "]" ;

feature_name = identifier | "MONADS" ;

object_type_name = identifier;  

returning_clause = /* empty : return full sheaf */
                 | "RETURNING"  "FULL"  "SHEAF"
                 | "RETURNING"  "FLAT"  "SHEAF"
                 | "RETURNING"  "FLAT"  "SHEAF"
                   "ON" object_type_name_list;

object_type_name_list = object_type_name { "," object_type_name } ;

where_clause = "WHERE" mql_query; 

mql_query = topograph;

topograph = blocks;

blocks = using_range_clause  block_string
       | using_range_clause  unordered_group ;

using_range_clause = /* empty : return all */
                   | "RANGE"  "ALL" 
                   | "RANGE"  "(" unsigned_integer "," unsigned_integer ")" 
                   | "RANGE"  "(" unsigned_integer ")" ;

block_string = block_string2
             | block_string2 "OR" block_string ;

block_string2 = block_string1
              | block_string1  block_string2 ;

block_string1 = block_string0 
              | block_string0 "*" star_monad_set;

block_string0 = block
              | "[" block_string "]" ;

block = object_block
      | notexist_object_block
      | power
      | opt_gap_block
      | gap_block ;

object_block = "["  object_type_name
               marks_declaration
               object_reference_declaration
               retrieval
               firstlast
               monad_set_relation_clause
               feature_constraints
               feature_retrieval
               opt_blocks
               "]" ;

marks_declaration = [marks] ;

marks = mark { mark } ;

mark = "`" identifier ;

object_reference_declaration =
              /* empty: No object reference declaration */
            | "AS" object_reference ;

object_reference = identifier; 

retrieval =  /* empty */    
          | "NORETRIEVE"
          | "RETRIEVE"  
          | "FOCUS";      

firstlast =  /* empty */                  
          | "FIRST"                     
          | "LAST"                      
          | "FIRST"  "AND"  "LAST";  

monad_set_relation_clause =  /* empty */ 
          | monad_set_relation_operation
            "(" monad_set_name "," universe_or_substrate ")"
          | monad_set_relation_operation  "(" universe_or_substrate ")" ;  

monad_set_relation_operation = "PART_OF" 
                             | "STARTS_IN" 
                             | "OVERLAP" ;

universe_or_substrate = "UNIVERSE"
                      | "SUBSTRATE" ;

feature_constraints = /* empty */
                    | ffeatures;     

ffeatures = fterm | ffeatures "OR" fterm; 

fterm = ffactor | fterm "AND" ffactor;  

ffactor = "NOT"  ffactor
        | "("  ffeatures  ")"
        | feature_comparison;

feature_comparison = feature_name  comparison_operator  value
                   | computed_feature_name  comparison_operator  value
                   | feature_name "=" "(" ")"  /* equal to empty list */
                   | feature_name "=" "(" list_of_identifier ")"
                   | feature_name "=" "(" list_of_integer ")"
                   | feature_name "IN" "(" list_of_identifier ")"
                   | feature_name "IN" "(" list_of_integer ")"
                   | computed_feature_name "IN" "(" list_of_integer ")"
                   | feature_name "IN" object_reference_usage
                   | computed_feature_name "IN" object_reference_usage;

comparison_operator = "="  /* Equal to */
                    | "<"  /* Less than */
                    | ">"  /* Greater than */
                    | "<>" /* Not equal to */
                    | "<=" /* Less than or equal */
                    | ">=" /* Greater than or equal */
                    | "~"  /* Regular expression */
                    | "!~" /* Negated regular expression */
                    | "HAS"; 

value = enum_const
      | signed_integer
      | STRING
      | object_reference_usage ;

enum_const = identifier ; 

signed_integer = unsigned_integer | "-" unsigned_integer | "NIL" ; 

object_reference_usage = object_reference "." feature_name
                       | object_reference "." computed_feature_name;

computed_feature_name = feature_name  "("  feature_name  ")" ;

list_of_identifier = identifier { "," identifier } ;

list_of_integer = signed_integer { "," signed_integer } ;

feature_retrieval = /* empty */
                  | "GET"  feature_list ;

feature_list = feature_list_member { "," feature_list_member } ;

feature_list_member = feature_name
                    | feature_name "(" identifier ")" 
                    | feature_name "(" "MONADS" ")" ;

opt_blocks =  /* empty */ 
           | blocks ;

notexist_object_block =
               ("NOTEXIST" | "NOTEXISTS")
               "["  object_type_name
               marks_declaration
               object_reference_declaration
               retrieval
               firstlast
               monad_set_relation_clause
               feature_constraints
               feature_retrieval
               opt_blocks
               "]" ;

power = ".."
      | ".." restrictor
      | ".." "BETWEEN" limit "AND" limit;

restrictor = "<"  limit          
           | "<="  limit;   

limit = unsigned_integer  /* non-negative integer, may be 0. */ ;

opt_gap_block = "["  "GAP?"
                marks_declaration
                gap_retrieval
                opt_blocks
                "]" ;

gap_retrieval =  /* empty */   
              | "NORETRIEVE"
              | "RETRIEVE"  
              | "FOCUS";      

gap_block = "[" "GAP"
            marks_declaration
            gap_retrieval
            opt_blocks
            "]" ;

star_monad_set = /* empty */  
               | monad_set ; 

unordered_group = "[" "UNORDEREDGROUP"
                  object_block_string
                  "]" ;

object_block_string = object_block { object_block } ;

```

## Examples

```
```

## Explanation



## Return type



