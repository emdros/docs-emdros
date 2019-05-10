# VACUUM DATABASE

## Purpose

To compactify and/or gather statistics about the data in a database,
in order use less space and speed up queries.

## Grammar

```
vacuum_database_statement = "VACUUM" ["DATABASE"] ["ANALYZE"];

```

## Examples

```
// Just vacuum, not analysis
VACUUM
GO

// ... equivalent to
VACUUM DATABASE
GO

// Also analyze
VACUUM ANALYZE
GO

// ... equivalent to
VACUUM DATABASE ANALYZE
GO
```

## Explanation

On PostgreSQL, this statement vacuums the database using the “VACUUM”
SQL statement. If the optional keyword “ANALYZE” is given, the statement
issues a “VACUUM ANALYZE” statement. See the PostgreSQL documentation
for what this does.

On MySQL, this statement issues OPTIMIZE TABLE queries for all object
types. If the ANALYZE keyword is given, ANALYZE TABLE queries are issued
as well.

On SQLite3, this statement first deletes all redundant sequence info
(compacting the sequence tables), then issues a VACUUM statement to
SQLite3.

The significance of this statement to Emdros development is that,
after populating a database, queries will speed up if you vacuum the
database before querying it, especially if you also do the ANALYZE
variant.

## Return type

There is no return value.



