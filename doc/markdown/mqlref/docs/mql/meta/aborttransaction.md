# ABORT TRANSACTION

## Purpose

To abort a transaction before it is committed, i.e., to lose all
changes made to the database since the last `BEGIN TRANSACTION`.

## Grammar

```
abort_transaction_statement = "ABORT" "TRANSACTION"; 

```

## Examples

```
ABORT TRANSACTION
GO
```

## Explanation


Aborts the current transaction, if one is in progress. Has no effect if
a transaction was not in progress. In such cases, false is returned.

If the abort failed, false is returned. If the abort succeeded, true is
returned.

NOTE that this is slightly different from other statements which flag a
DB error if unsuccessful. Here, no DB error is flagged, but false is
returned in the table.


## Return type


A table with the following schema:

| transaction\_aborted : boolean |
| :----------------------------: |

This table is empty if and only if there was a compiler error, i.e., if
the syntax was not obeyed. The statement cannot fail with a database
error. If no transaction was started when the ABORT TRANSACTION
statement was invocated, false is returned. If a transaction was
started, and it was aborted successfully, true is returned. If a
transaction was started, but it was not aborted successfully, false is
returned.


