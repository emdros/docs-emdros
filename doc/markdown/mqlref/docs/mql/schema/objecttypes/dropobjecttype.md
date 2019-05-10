# DROP OBJECT TYPE

## Purpose

To remove an object type from the schema, along with all of the
objects it contains.

## Grammar

```
drop_object_type_statement =
             "DROP"  ["OBJECT"] "TYPE"
             "["  object_type_name  "]" ;

object_type_name = IDENTIFIER ;  

```

## Examples

```
DROP OBJECT TYPE
[Sploinks]
GO

```

## Explanation

This statement drops an object type entirely from the database. This
deletes not only the object type, but also all the objects of that
object type, as well as the object type’s features. Enumerations which
are used as a feature type are not dropped, however.



## Return type

There is no return value.