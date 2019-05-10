# Return types

## Three kinds of return values: Nothing, Table, or Sheaf.

MQL is made up of statements, each of which either returns something or
doesn’t.

1. If an MQL statement doesn't return anything, there is no return value,
and hence there is no return type.

2.  If it returns something, there are two possibilities for what
the return-type can be. It can be:

    1.  A table, or

    2.  A sheaf

## Output-formats

The MQL engine gives you four options for using the results of an MQL
query:

1. You can specify that you want XML output.  This, in turn, is
either compact XML or indented XML.

2. You can specify that you want JSON output.  This, in turn, can be
either pretty-printed JSON or compact JSON.

3. You can specify that you want output for displaying on a console.

4. You can use the datatype provided if your program is linked to Emdros.

If you use the mql(1) program for output, please see the manual page
for how to choose the output kind.

## No return value, no return type

Some MQL statements do not return a value. In this case, there will be
no result, not even an empty table.

## Tables

The tables will look differently, depending on whether you choose
XML-output, JSON-output, or console-output.  The underlying idea is
the same: A list of rows, each consisting of a list of columns, with
values drawn from a particular type for each column in the overall
table.  The first row is the header, detailing the names and types of
the columns.

### Example of a table

In the descriptions below, we will give abstract schemas for the
tables, such as the following:

| object\_type\_name : string | monad : monad\_m | id\_d : id\_d |
| :-------------------------: | :--------------: | :-----------: |

This means that, in each row in the table, the first piece of data will
be a string (called object\_type\_name), the second piece of data will
be a monad\_m (called monad), and the last piece of data will be an
id\_d (called id\_d). And then the row stops. There will always be the
same number of columns in each row.

### Empty tables

A table of values may be empty, meaning it has no rows. In this case,
there will still be a table header with names and type-specifications.

### Atomic output-types in tables

The following types can get into a table and will be announced in the
header of the table:

1. string
2. integer
3. boolean (true or false)
4. id\_d
5. enumeration
6. list of integer
7. list of id_d
8. list of enumeration constant
9. set of monads

## Sheaf

The sheaf is a recursively defined data structure, designed to hold
detailed information about the results of a query on an EMdF database.  It is described in detail in [the section on the Sheaf](/mql/topographic/preliminaries/sheaf/)

## Other return values

Besides the value returned by an MQL query (if it returns any value),
there is also a number of metadata items which are returned from each
query:

1.  A boolean indicating whether there were any compiler-errors.
2.  A boolean indicating whether there were any database-errors.
3.  A string carrying any error messages.
4.  An integer showing which stage of the compilation/interpretation
    we had come to when we exited the function. In XML, this is a
    string as shown in the table, of the attribute “stage” attribute
    of the “error\_stage” element.

| Stage           | Value | XML string |
| :-------------- | :---: | :--------- |
| None            |   0   | none       |
| Parsing         |   1   | parse      |
| Weeding         |   2   | weed       |
| Symbol-checking |   3   | symbol     |
| Type-checking   |   4   | type       |
| Monads-checking |   5   | monads     |
| Execution       |   6   | exec       |

