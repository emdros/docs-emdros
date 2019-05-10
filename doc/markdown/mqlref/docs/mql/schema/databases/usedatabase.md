# USE DATABASE

## Purpose

To connect to a given database.

## Grammar

```
use_database_statement = "USE" ["DATABASE"] database_name [with_key]; 

database_name = IDENTIFIER  |  STRING; 

with_key = "WITH" "KEY" STRING ;

```

## Examples

```
USE book_test
GO

// Equivalent to:
USE DATABASE book_test
GO

// SQLite3
USE DATABASE 'C:\Users\Frank\Documents\EmdrosDatabases\book_test.sqlite3'
GO

// With encryption (if enabled)
USE DATABASE 'C:\Users\Frank\Documents\EmdrosDatabases\encrypted_book_test.sqlite3'
WITH KEY '0xdeadbeef 0xcafebabe'
GO
```

## Explanation


Before you can start using a database you have CREATEd (see section
[\[CREATE\_DATABASE\]](/mql/schema/databases/createdatabase/)) or
INITIALIZEd (see section
[\[INITIALIZE\_DATABASE\]](/mql/schema/databases/initializedatabase/)),
you must connect to it using the USE DATABASE statement. The keyword
“DATABASE” is optional and can be left out.

If a transaction was in progress (see BEGIN TRANSACTION statement,
section [\[BEGIN TRANSACTION\]](/mql/meta/begintransaction/)), the
transaction is automatically committed before the USE DATABASE
statement is executed. Thus the user need not, cannot, and should not
commit it or abort it.

The database name can be either a T\_IDENTIFIER or a T\_STRING. For
MySQL and PostgreSQL, it must be a T\_IDENTIFIER. For SQLite3, it can
be a T\_STRING giving the filename (optionally including the full
path) of the file holding the database to be used. If no path is
given, the file must be in the current working directory.


## Return type

There is no return value.



