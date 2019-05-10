# BEGIN TRANSACTION

## Purpose

To begin or start a transaction on the connection to the current
database.

## Grammar

```
begin_transaction_statement = "BEGIN" "TRANSACTION"; 

```

## Examples

```
BEGIN TRANSACTION
GO
```

## Explanation

On PostgreSQL, this statement begins a transaction if no transaction is
in progress already. The return value is a boolean saying whether the
transaction was started (true) or not (false). If this value is false,
the user should not subsequently issue a COMMIT TRANSACTION or ABORT
TRANSACTION statement. If this value is true, the user should issue
either a COMMIT TRANSACTION or an ABORT TRANSACTION later.

On MySQL, this has no effect, and always returns false.

On SQLite3, the behavior is the same as on PostgreSQL.

The transaction, if started, is automatically committed if a CREATE
DATABASE, USE DATABASE, DROP DATABASE or QUIT statement is issued before
a COMMIT TRANSACTION or ABORT TRANSACTION statement has been issued.

Also, the transaction is automatically committed if the connection to
the database is lost, e.g., if the mql(1) program reaches the end of
the MQL stream (e.g., an MQL script) and thus has to close down.
Transactions are not maintained across invocations of the mql(1)
program. The transaction is also committed if the EMdFDB, MQLExecEnv,
or EmdrosEnv object is destroyed.


## Return type

A table with the following schema:

| transaction\_started : boolean |
| :----------------------------: |

This table is empty if and only if there was a compiler error, i.e., if
the syntax was not obeyed. The statement cannot fail with a database
error. If no transaction was started, false is returned. If a
transaction was started, true is
returned.


