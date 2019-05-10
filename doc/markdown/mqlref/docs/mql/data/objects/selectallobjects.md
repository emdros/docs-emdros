# SELECT ALL OBJECTS

## Purpose

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

monad_set_name = IDENTIFIER ;  

with_max_range_clause =  /* empty : WITH MAX RANGE MAX_M MONADS */
                      | "WITH" "MAX" "RANGE" "MAX_M" "MONADS"
                      | "WITH" "MAX" "RANGE" unsigned_integer "MONADS" 
                      | "WITH" "MAX" "RANGE" "FEATURE" feature_name
                        "FROM" "[" object_type_name "]" ;

feature_name = IDENTIFIER | "MONADS" ;

object_type_name = IDENTIFIER ;  

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

mark = "`" IDENTIFIER ;

object_reference_declaration =
              /* empty: No object reference declaration */
            | "AS" object_reference ;

object_reference = IDENTIFIER ; 

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

enum_const = IDENTIFIER ; 

signed_integer = unsigned_integer | "-" unsigned_integer | "NIL" ; 

object_reference_usage = object_reference "." feature_name
                       | object_reference "." computed_feature_name;

computed_feature_name = feature_name  "("  feature_name  ")" ;

list_of_identifier = IDENTIFIER { "," IDENTIFIER } ;

list_of_integer = signed_integer { "," signed_integer } ;

feature_retrieval = /* empty */
                  | "GET"  feature_list ;

feature_list = feature_list_member { "," feature_list_member } ;

feature_list_member = feature_name
                    | feature_name "(" IDENTIFIER ")" 
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
SELECT ALL OBJECTS
IN { 1-4, 5, 7-9 }
WITH MAX RANGE 5 MONADS
RETURNING FULL SHEAF
WHERE
[Word lexeme = ">RY/"]
GO
```

## Explanation

This statement is a front-end to the MQL Query-subset (see chapter 4
starting on page ).

The parameters to an MQL query are:

1.  A universe U,

2.  A substrate Su, and

3.  A topograph.

The universe U is a contiguous stretch of monads. The search is
restricted only to include objects which are wholly contained within
this universe (i.e., which are part\_of\[4\] the universe).

The substrate is used to further restrict the search. For there is the
additional requirement that all objects found must be wholly contained
within (i.e., part\_of) the substrate as well. The substrate must be
part\_of the universe. Mathematically speaking, the substrate is the set
intersection of whatever was in the IN clause and all\_m-1 (i.e., the
set of all monads in the database).

The topograph is what is specified as `mql_query` in the above grammar.

The IN-specification tells the query-engine what the substrate Su should
be. There are three choices:

1.  Specify an explicit monad set like “{ 1-3000,
    7000-10000 }”

2.  Specify a named arbitrary monad set (see section
    [\[Arbitrary-monad-sets\]](#Arbitrary-monad-sets)).

3.  Leave it blank. This means that the substrate is calculated as
    all\_m-1 (i.e., all of the monads in the database; see  or  or page
    in this Programmer’s Guide.)

The universe U is then calculated as all the monads between the first
and last monads of the substrate.

The “max range” specifies the maximum number of monads to take as a
context for any power block at the outermost level. The significance of
this is that it helps users not to get query results which are correct
but useless because the query returns too many straws in the sheaf. This
is done by putting an upper limit on the number of monads a power block
may extend over. This limit can be “MAX\_M” monads, meaning that there
is in practice no limit to the stretch of monads which can be matched by
a power block. It can also be empty, which is the same as “MAX\_M”
monads, i.e., no limit. It can also be an explicit number of monads,
say, 5 or 100. The max range can also be taken as the length of the
largest object of any object type. The set of monads to use can be
either the privileged “monads” feature, or any feature whose type is SET
OF MONADS. Note that the limit is NOT taken as the length of any actual
object of the given object type which happens to be part\_of the current
stretch of monads under investigation. Rather, the cap is set before
query execution time by inspecting the largest length of any monad set
of the given monad set feature in the object type.

The difference between the RETURNING FULL SHEAF and the RETURNING FLAT
SHEAF clause is that the latter applies the “flatten” operator to the
sheaf before returning it, whereas the former does not. If the
returning\_clause clause is empty, it means the same thing as RETURNING
FULL SHEAF. If the RETURNING FLAT SHEAF has an ON appendix with a list
of object type names, then the two-argument flatten operator is applied
using this list of object type names. See section
[\[Flat-sheaf\]](/mql/topographic/preliminaries/flatsheaf/) for an explanation of flat
sheaves and the “flatten” operator.

### Monad set

The explicit monad set in the IN clause, if given, must consist of a
comma-separated list of monad-set-elements enclosed in curly braces. A
monad-set-element is either a single integer (referring to a single
monad) or a range consisting of two integers (referring to a range of
monads). The monad-set-elements need not occur in any specific order,
and are allowed to overlap. The result is calculated by adding all the
monads together into one big set. The ranges of monads must, however, be
monotonic, i.e., the second integer must be greater than or equal to the
first.



## Return type

A sheaf, either full or flat: All retrieved objects are included, but
those objects that had the `focus` modifier in the query are flagged
as such. Please see [\[sheaf\]](/mql/topographic/preliminaries/sheaf/)
for an explanation of the sheaf.  The section on the [\[Console sheaf
grammar\]](#Appendix:Console-sheaf-grammar) gives the grammar for the
console-sheaf. Please see section
[\[Flat-sheaf\]](/mql/topographic/preliminaries/flatsheaf/) for an
explanation of the flat sheaf.
