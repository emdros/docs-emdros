# CREATE DATABASE

## Purpose

To create and initialize an Emdros database, preparing it to receive
EMdF data.

## Grammar

```
create_database_statement = 
    "CREATE"  "DATABASE" database_name [with_key]
    ["USING" "ENCODING" STRING] ;

database_name = IDENTIFIER  |  STRING; 

with_key = "WITH" "KEY" STRING ;

```

## Examples

```
CREATE DATABASE book_test
GO

CREATE DATABASE 'C:\Users\Frank\Document\EMdrosDatabase\book_test.sqlite3'
GO

CREATE DATABASE book_test_utf8
USING ENCODING ’utf-8’
GO

CREATE DATABASE book_test_latin1
USING ENCODING ’iso-8859-1’
GO

```

## Explanation

The CREATE DATABASE statement creates and initializes a database. No
text data is put into the database, and no object types are created, but
the structures necessary for the EMdF engine to function are set in
place. The user need not worry about these structures. Interested users
are referred to .

You must CREATE a database before you can USE it (see section [\[USE
DATABASE\]](/mql/schema/databases/usedatabase/)). Alternatively, if
you have a database that is already created but not initialized, you
can use the INITIALIZE DATABASE statememt (see Section
[\[INITIALIZE_DATABASE\]](/mql/schema/databases/initializedatabase/)).

If a transaction was in progress (see BEGIN TRANSACTION statement,
section [\[BEGIN TRANSACTION\]](/mql/meta/begintransaction/)), the
transaction is automatically committed before the CREATE DATABASE
statement is executed. Thus the user need not, cannot, and should not
commit it or abort it afterwards.

The database name can be either a T\_IDENTIFIER or a T\_STRING. For
MySQL and PostgreSQL, it must be a T\_IDENTIFIER. For SQLite3, it can
be a T\_STRING giving the filename (optionally including the full
path) of the file in which the database is to be created. If no path
is given, the file is created in the current working directory.

The optional “WITH KEY” syntax can be used on SQLite3 to send a key to
SQLite3’s sqlite3\_open\_encrypted API when opening the database. Note
that this won't actually perform any encryption at all, unless you
obtain an encryption-enabled SQLite3 from somewhere, e.g., Dr. Hipp
himself, the author of SQLite3.

The optional “WITH ENCODING” syntax can be used to specify the default
encoding to be used for the database when creating it in the backend
database. Currently, the following values are supported:

  - utf-8

  - iso-8859-1

If the WITH ENCODING clause is not supplied, then the default encoding
is used. The default encoding for each database is given in the
following list:

  - PostgreSQL: utf-8

  - MySQL: iso-8859-1

  - SQLite 3: utf-8

For SQLite 3, the only encoding available is utf-8. To specify any other
encoding would be an error.

Note that the encoding specified only has a bearing on how the database
backend interprets the data, not on how Emdros interprets the data. In
fact, Emdros most likely will not interpret the data at all, but rather
will pass whatever is stored in the database on to the application using
Emdros, which must the interpret the data according to domain-specific
knowledge of which encoding has been used.

## Return type

There is no return value, and hence no return type.

