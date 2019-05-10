# INITIALIZE DATABASE

## Purpose

To initialize a database that has already been created in an SQL
backend (such as PostgreSQL or MySQL) using that backend's tools, and
prepare the database for use with Emdros.

## Grammar

```
initialize_database_statement = 
    "INITIALIZE"  "DATABASE" database_name [with_key]; 

database_name = IDENTIFIER  |  STRING; 

with_key = "WITH" "KEY" STRING ;

```

## Examples

```
INITIALIZE DATABASE book_test
GO
```

## Explanation

The INITIALIZE DATABASE statement initializes a database without
creating it first. That is, the database must exist before issuing
this statement. It simply creates all the meta-data necessary for
having an Emdros database. This is useful on MySQL and PostgreSQL if
you don’t have privileges to create databases, but you do have
privileges to create tables in an already-provided database. On
SQLite3, it is also useful, if you want to add Emdros information to
an already-existing SQLite3 database. Other than not creating the
database, this statement accomplishes the same things as the CREATE
DATABASE statement (see Section
[\[CREATE\_DATABASE\]](/mql/schema/databases/createdatabase/)).

For the optional “WITH KEY” syntax, please see the CREATE DATABASE
statement.

There is no “WITH ENCODING” syntax for the INITIALIZE DATABASE
statement. This is because the encoding is only used when CREATEing
the database. However, the internal metadata of the database is set to
the default given under the explanation for CREATE DATABASE (see
Section [\[CREATE\_DATABASE\]](/mql/schema/databases/createdatabase/)).

## Return type

There is no return value.
