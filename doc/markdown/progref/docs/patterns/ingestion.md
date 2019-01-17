# Data ingestion

The term "Data ingestion" refers to populating a database with a
database schema and data conforming to that schema.

## Basic patterns

There are three basic patterns for ingesting data:

1. Use the [xml2emdrosmql tool](#xml2emdrosmql).
2. Use one of the provided [import tools](#importers)
3. Do it [by MQL](#by-mql).

## xml2emdrosmql

The [Python-based XML to MQL
tool](https://github.com/emdros/python-xml2emdrosmql) is able to take
XML documents with inline content (as opposed to standoff markup) and
generate MQL statements that create a database from the XML documents.

See the help output from the tool in order to see how to use it.

## Importers

Importers for various formats are provided with Emdros.

They take input in the given formats and generate MQL statements which
can be used to create the database.

The importers provided include:

1. **plaintextimport**: Plain text import

2. **slashedtextimport**: Slashed text in the style of `word1/POSTAG1
word2/POSTAG2`.

3. **negraimport**: Import of the NEGRA corpus format.

4. **tigerxmlimport**: Import of the TIGERXML corpus format.

5. **pennimport**: Import of the Penn Treebank corpus format.

6. **ubimport**: Import of the the "Unbound Bible" format for Bibles
from Biola University Unbound Bible project.


## By MQL

If none of the above ways work for you, you need to either:

1. Develop the importer yourself, or

2. Contract with someone to do it for you, such as [the company
employing Emdros's creator](https://scripturesys.com/).

Both ways will involve writing one or more programs which perform the
following basic stages.

### Basic stages

The following are the basic stages in data ingestion:

1. Create the schema.
2. Drop indexes.
3. Create the data.
4. Recreate indexes.
5. Post-processing.

Stages 1 and 2 can be intertwined.

This is described in more detail in the [Database designer's
guide](https://dbdg.emdros.com/).


### Schema creation

The schema is created with the following MQL statements:

1. `CREATE ENUMERATION` (creates an enumeration with enumeration constants).

2. `CREATE OBJECT TYPE` (creates an object type with features,
constraints, and other characteristics).

3. `CREATE MONAD SET` (create a named monad set, which is not a
feature on any object, but rather can be used to query given parts of
the database).


### Drop indexes

In order to speed up the data creation, it might be beneficial to drop
all indexes on all object types. This can be done with the
`manage_indices` command-line tool, or with the following MQL
statement:

1. `DROP INDEXES ON OBJECT TYPES [ALL] GO`.


### Data creation

The data is then created with the following kinds of statements:

1. `CREATE OBJECTS WITH OBJECT TYPE`, which creates one or more
objects in one go.  This is usually faster than creating the objects
one by one.

2. `CREATE OBJECT`, which creates a single object, giving values to
its features.

### Recreate indexes

After the data has been added, you can choose to re-create indexes on
one, more, or all object types.  This can be done with the
`manage_indices` command-line tool, or it can be done with one of the
following MQL statements:

1. `CREATE INDEXES ON OBJECT TYPES [ALL] GO`, which creates indexes on
all object types.

2. `CREATE INDEXES ON OBJECT TYPE [Token] GO`, which creates indexes
on the "Token" object type (given that this object type has been
created as part of the schema creation stage).

### Post-processing

The post-processing steps usually include vacuuming the database,
and/or adding any final metadata to the database in some object type
suited for the purpose.

The database can be "VACUUMED" with one of the following MQL
statements:

1. `VACUUM DATABASE`, which cleans up the database structures (works
on SQLite 3, PostgreSQL, and MySQL/MariaDB).

2. `VACUUM DATABASE ANALYZE`, which cleans up and provides statistical
hints to the backend's query processor (works on SQLite3, PostgreSQL,
and MySQL/MariaDB).

## Conclusion

You can consult both the [MQL Reference
Guide](https://mqlref.emdros.com/) and the [Database Designer's
Guide](https://dbdg.emdros.com/) for more information on how to ingest
data.

