# SELECT OBJECTS HAVING MONADS IN

## Purpose

## Grammar

```
select_objects_having_monads_in_statement =
               "SELECT" "OBJECTS"  "HAVING" "MONADS" "IN"
               monad_set
               "[" (object_type_name | "ALL") "]" ;

monad_set = "{" monad_set_element_list "}" ;

monad_set_element_list = monad_set_element { "," monad_set_element } ;

monad_set_element = unsigned_integer
                  | unsigned_integer "-" unsigned_integer
                  | unsigned_integer "-" ;

unsigned_integer = digit { digit } ;

digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;

object_type_name = IDENTIFIER ;  

```

## Examples

```
SELECT OBJECTS
HAVING MONADS IN { 23-45, 68, 70, 87-93 }
[Clause]
GO   
   
SELECT OBJECTS
HAVING MONADS IN { 1, 5-7, 103-109 }
[ALL]
GO   
   
SELECT OBJECTS
HAVING MONADS IN { 23 }
[Word]
GO
```

## Explanation

This statement returns the object types and object id\_ds of the objects
that have at least one monad in the monad set specified. If “ALL” is
specified as the object type, then this is done for all object types in
the database. If a specific object type is specified, then that object
type is used.

The returned table has one row for each object. Each object is
represented only once. The monad in each row is guaranteed to be from
the set of monads specified, and is guaranteed to be from the object in
the row.

This statement is useful in much the same way that the SELECT OBJECTS AT
statement is useful. It can be used, e.g., for getting id\_ds of objects
that must be displayed as part of the results of a query, but which are
not in the query results. This statement can also be used like the
SELECT OBJECTS AT statement by simply making the monad set a singleton
set with only one monad. Note, however, that this statement does
something a different from SELECT OBJECTS AT. Whereas SELECT OBJECTS AT
will only retrieve an object if that object *starts on* the given monad,
this present statement will retrieve the object if only the object *has
at least one monad* from the monad set given. This statement also has
the advantage that one can ask for all object types. This enables one to
access objects which one knows might be there, but of which one does not
know the object types. It also has the advantage of being much faster
than a series of SELECT OBJECTS AT statements if one is looking for
objects in more than one monad.

This statement was typically used in a series of SELECT OBJECTS HAVING
MONADS IN, GET MONADS, and GET FEATURES statements, in order to obtain
all information necessary for display of data. This sequence has been
wrapped neatly into the GET OBJECTS HAVING MONADS IN statement, which is
now the preferred method of doing this sequence.

Note to programmers: If you want to get objects not from all object
types but from only a subset of all object types, the easiest thing is
to issue the required number of copies of the statement with GO in
between, varying only the object type. That way, if you are using the
mql program as a proxy for the MQL engine, you don’t incur the overhead
of starting and stopping the mql program.

## Return type

| object\_type\_name : string | monad : monad\_m | id\_d : id\_d |
| :-------------------------: | :--------------: | :-----------: |

On failure, this table is empty. Note, however, that the table can also
be empty if the command were successful, if there were no objects that
had at least one monad in the monad set
specified.



