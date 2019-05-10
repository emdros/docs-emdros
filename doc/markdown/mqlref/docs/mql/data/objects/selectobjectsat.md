# SELECT OBJECTS AT

## Purpose

## Grammar

```
select_objects_at_statement =
               "SELECT" ["OBJECTS"] "AT" single_monad_specification
               "[" object_type_name "]" ;

single_monad_specification = "MONAD" "=" unsigned_integer;

unsigned_integer = digit { digit } ;

digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;

object_type_name = IDENTIFIER ;  

```

## Examples

```
SELECT OBJECTS
AT MONAD = 3406
[Clause]
GO
```

This example selects all those objects of type Clause which start at
monad 3406.

## Explanation

This statement returns a table containing the object id\_ds of all the
objects of the given type which start at the monad specified, i.e.,
whose first monad is the given monad.

The result is a table with one column, namely “id\_d”. Each row
represents one object, where the id\_d is its object id\_d.


## Return type

A table with the following schema:

| id\_d: id\_d |
| :----------: |

On failure, this table is empty. Note, however, that the table can also
be empty because there were no objects of the given type having the
given monad as their first monad. This is not an error.



