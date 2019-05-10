# COMMIT TRANSACTION

## Purpose

To commit a transaction, i.e., to make sure that all of the data
changes made since the last BEGIN TRANSACTION come into effect in the
database.

## Grammar

```
commit_transaction_statement = "COMMIT" "TRANSACTION"; 

```

## Examples

```
COMMIT TRANSACTION
GO
```

## Explanation

Commits the current transaction, if one is in progress. Has no effect if
a transaction was not in progress. In such cases, false is returned.

If the commit failed, false is returned. If the commit succeeded, true
is returned.

NOTE that this is slightly different from other statements which flag
a DB error if unsuccessful. Here, no DB error is flagged, but false is
returned in the table.


## Return type

A table with the following schema:

| transaction\_committed : boolean |
| :------------------------------: |

This table is empty if and only if there was a compiler error, i.e., if
the syntax was not obeyed. The statement cannot fail with a database
error. If no transaction was started when the COMMIT TRANSACTION
statement was invocated, false is returned. If a transaction was
started, and it was committed successfully, true is returned. If a
transaction was started, but it was not committed successfully, false is
returned.
