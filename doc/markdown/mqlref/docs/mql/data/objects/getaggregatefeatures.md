# GET AGGREGATE FEATURES

## Grammar

```
get_aggregate_features_statement =
        "GET" "AGGREGATE" "FEATURES"
        aggregate_feature_list
        "FROM" "OBJECTS"
        [in_clause] /* empty = 'all_m-1' */
        using_monad_feature
        "["
          object_type_name
          feature_constraints
        "]" ;

aggregate_feature_list = aggregate_feature { "," aggregate_feature } ;

aggregate_feature = "MIN"  "(" feature_name ")" 
                  | "MAX"  "(" feature_name ")" 
                  | "SUM"  "(" feature_name ")" 
                  | "COUNT"  "(" "*" ")" 
                  | "COUNT"  "(" aggregate_feature_comparison  ")" ;

feature_name = identifier | "MONADS" ;

identifier = (alpha | "_") { (alpha | "_" | digit) } ;

alpha = "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i"
       | "j" | "k" | "l" | "m" | "n" | "o" | "p" | "q" | "r"
       | "s" | "t" | "u" | "v" | "w" | "x" | "y" | "z" 
       | "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I"
       | "J" | "K" | "L" | "M" | "N" | "O" | "P" | "Q" | "R"
       | "S" | "T" | "U" | "V" | "W" | "X" | "Y" | "Z" ;

digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;

aggregate_feature_comparison = feature_name
                               comparison_operator
                               value
                             | feature_name
                               comparison_operator
                               "(" list_of_identifier ")" 
                             | feature_name
                               comparison_operator
                               "(" list_of_integer ")" ;

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

unsigned_integer = digit { digit } ;

object_reference_usage = object_reference "." feature_name
                       | object_reference "." computed_feature_name;

object_reference = identifier; 

computed_feature_name = feature_name  "("  feature_name  ")" ;

list_of_identifier = identifier { "," identifier } ;

list_of_integer = signed_integer { "," signed_integer } ;

in_clause = "IN" in_specification ;

in_specification = monad_set
                 | "ALL" /* = all_m-1 */ ;

monad_set = "{" monad_set_element_list "}" ;

monad_set_element_list = monad_set_element { "," monad_set_element } ;

monad_set_element = unsigned_integer
                  | unsigned_integer "-" unsigned_integer
                  | unsigned_integer "-" ;

using_monad_feature = /* empty: Equivalent to
                         "USING" "MONAD" "FEATURE" "MONADS" */
                    | "USING" "MONAD" "FEATURE" identifier
                    | "USING" "MONAD" "FEATURE" "MONADS"; 

object_type_name = identifier;  

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

```

## Examples

```
```

## Explanation



## Return type



