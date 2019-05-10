# DROP ENUMERATION

## Purpose

## Grammar

```
drop_enumeration_statement = "DROP" ("ENUM" | "ENUMERATION") 
                             enumeration_name;

enumeration_name = IDENTIFIER ; 

```

## Examples

```
DROP ENUMERATION phrase_type_t
GO
```

## Explanation

This statement removes an enumeration altogether from the database,
including all its enumeration constants.

It is an error (and impossible) to drop an enumeration which is
currently in use by some object type.

## Return type

There is no return value.


