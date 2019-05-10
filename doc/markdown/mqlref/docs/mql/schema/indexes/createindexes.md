# CREATE INDEXES

## Purpose

To create indexes on the given object type(s).  Indexes can sometimes
be used to speed queries up.

## Grammar

```
create_indexes_statement = "CREATE" "INDEXES" on_object_type; 

on_object_type = "ON" "OBJECT" ("TYPE" | "TYPES")
                 "[" 
                    (object_type_name | "ALL")
                 "]" ;

object_type_name = IDENTIFIER ;  

```

## Examples
```
// All object types in the current database
CREATE INDEXES
ON OBJECT TYPES
[ALL]
GO   

// Only the Word object type in the current database
CREATE INDEXES
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

This statement creates indexes that have previously been dropped. It has
no effect if the indexes are there already. If “ALL” is specified as the
object type, then all object types in the current database will have
their indexes created (if not there already).

The manage\_indices program that comes with the Emdros distribution can
be used to achieve the same effect.

Note that the choice between “TYPE” and “TYPES” is just syntactic sugar.
It doesn’t matter which you use.

## Return type

There is no return value.