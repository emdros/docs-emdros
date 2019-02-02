# GET AGGREGATE FEATURES

## Purpose

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

feature_name = IDENTIFIER | "MONADS" ;

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

enum_const = IDENTIFIER ; 

signed_integer = unsigned_integer | "-" unsigned_integer | "NIL" ; 

unsigned_integer = digit { digit } ;

digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;

object_reference_usage = object_reference "." feature_name
                       | object_reference "." computed_feature_name;

object_reference = IDENTIFIER ; 

computed_feature_name = feature_name  "("  feature_name  ")" ;

list_of_identifier = IDENTIFIER { "," IDENTIFIER } ;

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
                    | "USING" "MONAD" "FEATURE" IDENTIFIER
                    | "USING" "MONAD" "FEATURE" "MONADS"; 

object_type_name = IDENTIFIER ;  

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



