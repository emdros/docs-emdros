# DROP INDEXES

## Purpose

To drop (delete) the index(es) associated with an object type, or all
object types, in a given database.  This affects query-speed, probably
negatively, but speeds up population of (insertion into) a database.

## Grammar

```
drop_indexes_statement = "DROP" "INDEXES" on_object_type; 

on_object_type = "ON" "OBJECT" ("TYPE" | "TYPES")
                 "[" 
                    (object_type_name | "ALL")
                 "]" ;

object_type_name = IDENTIFIER ;  

```

## Examples

```
// All object types in the current database.
DROP INDEXES
ON OBJECT TYPES
[ALL]
GO   

// Only the 'Word' object type.
DROP INDEXES
ON OBJECT TYPE
[Word]
GO
```

## Explanation

Emdros creates indexes on the tables associated with object types when
they are created. These indexes speed up retrieval, but slow down
insertion. Therefore, if you are going to insert a large amount of
objects, it is best to drop indexes on the object types you are going to
modify (possible all object types), then create the indexes again after
you have inserted all objects.

This statement drop indexes that have previously been create. It has no
effect if the indexes have been dropped already. If “ALL” is specified
as the object type, then all object types in the current database will
have their indexes dropped (if not dropped already).

The manage\_indices program that comes with the Emdros distribution can
be used to achieve the same effect.

Note that the choice between “TYPE” and “TYPES” is just syntactic sugar.
It doesn’t matter which you use.

If a feature has been declared WITH INDEX, this index is dropped.
However, the feature will have its index recreated upon a CREATE INDEXES
statement affecting that object type.


## Return type

There is no return value.

