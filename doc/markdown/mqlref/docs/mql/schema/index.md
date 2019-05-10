# MQL schema manipulation

The term "schema" of a database refers to the "data model" embodied in
a particular database.  That is, the schema of a database defines the
*categories* that exist in that particular database, in terms of:

- enumerations in the database
- object types in the database
- features of those object types

The following are also treated under the heading of "schema":

- databases
- indexes

# Data vs. Data Model vs. Database Model

## Three levels of data

There are three levels of data in any database:

1. The data
2. The data model
3. The database model.

Briefly, the data model is chosen by designer of a given database, and
determines the categories of data available.  The database model,
however, is chosen by the designer of the database engine, and
determines the categories available to the database designer to design
data categories.

Let us unpack this.

## Data

The *data* in a database is the information that is stored in the
database.  In Emdros, it is the objects and their feature-values,
along with named monad sets, that make up the data in an Emdros
database.

## Data model

The *data model* of a database defines the possible *categories of
data* in the database.  For example, the existence of a particular
object type "Word" with particular features with particular types is
part of the *data model* of a particular database.  The database
designer is free to create any data model, with any object types and
any features on those object types.

## Database model

By contrast, the *database model* of a database engine defines the
*possible categories* of *categories of data*.  Thus Emdros's EMdF
database model states that the *category* "object type" is available
to the database designer to create *particular* instances of the
category of "object type".

Similarly, the EMdF database model states that all object types have
"features", which in turn can be of several possible, well-defined
"feature types".  A database designer is thhen free to create object
types with particular features with particular feature types.

# Comparison of EMdF and the relational model

In the EMdF database model, the following comparisons can be made:

- An EMdF object type is similar to an SQL table.

- The features of an EMdF object type is similar to the columns of an
  SQL table.

- An EMdF object is similar to a row in an SQL table.

# Comparison of MQL and SQL

The central feature of the SQL language is arguably "joins between
tables".  In an SQL database engine, the tables contain relations
between different kinds of data, and the SQL `JOIN` clause makes new,
dynamic relations between tables possible.

In MQL, the fundamental way of "joining" objects is by means of the
sets of monads.  That is, if you want two objects to be related, you
compare their features which are of type "SET OF MONADS".  This can
either be "before", after", "before and adjacent to", "after and
adjacent to", "inside", "overlaps", "starts inside", and other
relationships that can exist between sets of monads.

In MQL, the topographic part of the language has direct, first-class
support for querying objects based on these relations between the sets
of monads.

That is one of the fundamental reasons for the power of the Emdros
database engine.  It is a new way of modeling data, with a powerful
query language to go with it.  The query language makes it possible to
state these "before", "after", "inside", and other relationships
declaratively as part of the syntax of the query.  

In essence, the concepts inhering in the EMdF model are mirrored in
the query language.  Just as the SQL query language closely mirrors
the concepts of the accompanying relational database model, so the MQL
language fits the EMdF model like a hand in a glove.





