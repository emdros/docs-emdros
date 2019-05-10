# GET OBJECTS HAVING MONADS IN

## Purpose

This statement retrieves objects of a given object type.  The objects
are chosen based on whether or not a specified monad set has at least
one monad in common with the monads in a specified monad set feature
on the object.  The statement makes it possible also to retrieve
feature values of features on the objects.

This statement, together with the [\[SELECT ALL
OBJECTS\]](/mql/data/objects/selectallobjects/) statement, is one of
the two most useful statements in the MQL language.

## Grammar

```
get_objects_having_monads_in_statement =
        "GET" "OBJECTS" "HAVING" "MONADS" "IN"
        in_specification
        using_monad_feature
        "[" object_type_name
            ["GET" ("ALL" | feature_list)]
        "]" ;

in_specification = monad_set
                 | "ALL" /* = all_m-1 */ ;

monad_set = "{" monad_set_element_list "}" ;

monad_set_element_list = monad_set_element { "," monad_set_element } ;

monad_set_element = unsigned_integer
                  | unsigned_integer "-" unsigned_integer
                  | unsigned_integer "-" ;

unsigned_integer = digit { digit } ;

digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;

using_monad_feature = /* empty: Equivalent to
                         "USING" "MONAD" "FEATURE" "MONADS" */
                    | "USING" "MONAD" "FEATURE" IDENTIFIER
                    | "USING" "MONAD" "FEATURE" "MONADS"; 

object_type_name = IDENTIFIER ;  

feature_list = feature_list_member { "," feature_list_member } ;

feature_list_member = feature_name
                    | feature_name "(" IDENTIFIER ")" 
                    | feature_name "(" "MONADS" ")" ;

feature_name = IDENTIFIER | "MONADS" ;

```

## Examples

```
GET OBJECTS
HAVING MONADS IN { 23-45, 68, 70, 87-93 }
[Clause]
GO   
   
GET OBJECTS
HAVING MONADS IN { 1, 5-7, 103-109 }
USING MONAD FEATURE parallel_monads
[Phrase GET phrase_type, function]
GO   
   
GET OBJECTS
HAVING MONADS IN { 23 }
[Word GET ALL]
GO
```

## Explanation

This statement returns the objects of the given object type that have at
least one monad in the monad set specified. A flat sheaf is returned
with one straw containing all the objects to be retrieved.

The monad set to use is the object’s monad set by default. If the
“using\_monad\_set\_feature” variant is used, the monad sets used are
the ones stored in this feature. The feature must be a set of monads.

This statement is useful in much the same way that the SELECT OBJECTS AT
statement is useful. It can be used, e.g., for getting id\_ds of objects
that must be displayed as part of the results of a query, but which are
not in the query results.

This statement is the preferred method for getting objects from the
engine, rather than a sequence of SELECT OBJECTS HAVING MONADS IN, GET
MONADS, and GET FEATURES. It is much faster than the combination of
the three.



## Return type

A flat sheaf is returned which contains the objects in question as
MatchedObjects. See Section [\[Flat
sheaf\]](/mql/topographic/preliminaries/flatsheaf/) for more
information.

