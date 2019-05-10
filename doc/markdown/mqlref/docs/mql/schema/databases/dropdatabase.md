# DROP DATABASE

## Purpose

To remove a database from the system.

## Grammar

```
drop_database_statement = "DROP" "DATABASE" database_name; 

database_name = IDENTIFIER  |  STRING; 

```

## Examples

```
DROP DATABASE book_test
GO

// For SQLite3
DROP DATABASE 'C:\Users\Frank\Documents\EmdrosDatabases\book_test.sqlite3'
GO

```

## Explanation

A previously CREATEd database (see section
[\[CREATE\_DATABASE\]](/mql/schema/databases/createdatabase/)) can be
completely removed from the system using this statement. All data in
the database is irretrievably lost, including all objects, all object
types, and all enumerations.

If a transaction was in progress (see BEGIN TRANSACTION statement,
section [\[BEGIN TRANSACTION\]](/mql/meta/begintransaction/)), the
transaction is automatically committed before the DROP DATABASE
statement is executed. Thus the user need not, cannot, and should not
commit it or abort it.

The database name can be either a T\_IDENTIFIER or a T\_STRING. For
MySQL and PostgreSQL, it must be a T\_IDENTIFIER. For SQLite, it can
be a T\_STRING giving the filename (optionally including the full
path) of the file holding the database to be dropped. If no path is
given, the file must be in the current working directory.

## Return type

There is no return value.



