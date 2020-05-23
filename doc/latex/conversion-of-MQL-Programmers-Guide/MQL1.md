
# Segment manipulation

## Introduction

Segments were present in Emdros up to and including version 1.1.12.
After that, support for segments was removed.

A segment used to be an arbitrary, contiguous stretch of monads which
was given a name. Objects could not be created which crossed the
boundaries of a segment. You could restrict your search to within a
single segment with SELECT ALL OBJECTS.

However, segments were found to be ugly baggage, cumbersome and not
useful. Therefore, they were removed.

The CREATE SEGMENT statement is retained for backward
compatibility.

## CREATE SEGMENT<span id="CREATE_SEGMENT" label="CREATE_SEGMENT">\[CREATE\_SEGMENT\]

# Syntax

```

create\_segment\_statement : “CREATE”   “SEGMENT”

    segment\_name

    “RANGE”   “=”   segment\_range

;

segment\_name : T\_IDENTIFIER

;

segment\_range : T\_INTEGER “-” T\_INTEGER

;

```

# Example

```

CREATE SEGMENT Old\_Testament

RANGE = 1 - 500000

GO

```

This example used to create a segment named “Old\_Testament” starting at
monad 1 and ending at monad 500000.

Now it does nothing.

# Explanation

This statement currently does nothing. It will fail with a database
error.

# Return type

There is no return value.

# Querying the data

This section describes statements which can be used to query the *data*
in an Emdros database, as opposed to querying the
*schema*.




## GET OBJECTS HAVING MONADS IN

# Example

```

```

# Explanation


# Return type


## GET AGGREGATE FEATURES

# Syntax

```

get\_aggregate\_features\_statement : “GET” “AGGREGATE” (“FEATURE” | “FEATURES”)

    aggregate\_feature\_list

    “FROM” “OBJECTS” opt\_in\_clause

    “WHERE” 

    “\[“ object\_type\_name 

       feature\_constraints

    “\]”

;

aggregate\_feature\_list : aggregate\_feature 

                       | aggregate\_feature\_list “,” aggregate\_feature

;

aggregate\_feature : aggregate\_function “(“ feature\_name “)”

                  | “COUNT” “(“ “\*” “)”

                  | “COUNT” “(“ feature\_name “=” feature\_value “)”

;

aggregate\_function : “MIN” | “MAX” | “SUM”

;

feature\_name : T\_IDENTIFIER

;

object\_type\_name : T\_IDENTIFIER

;

```

# Examples

```

/\*

 \* Create the enumerations and object types of an 

 \* example database.

 \*

 \*/

CREATE ENUMERATION boolean\_t = {

    false = 0,

    true

}

GO

CREATE ENUMERATION part\_of\_speech\_t = {

    Verb,

    Noun,

    ProperNoun,

    Pronoun,

    Adjective,

    Adverb,

    Preposition,

    Conjunction,

    Particle

}

GO

CREATE OBJECT TYPE

WITH SINGLE MONAD OBJECTS

\[Token

    has\_space\_before : boolean\_t;  // Any space before the surface?

    surface : STRING;              // The surface itself

    has\_space\_after : boolean\_t;   // Any space after the surface?

    part\_of\_speech : part\_of\_speech\_t;

    is\_punctuation : boolean\_t;     // true iff the surface is punctuation.

\]

GO

CREATE OBJECT TYPE

WITH SINGLE RANGE OBJECTS

\[Line

    actant\_name : STRING FROM SET;

    gender : gender\_t;

    words\_spoken : INTEGER; 

    line\_number\_in\_act : INTEGER;

\]

GO

/\*

 \* Example 1:

 \*

 \* Founds all Token objects in the entire database whose 

 \* is\_punctuation feature equals false.

 \*

 \* Then retrieve one aggregate function, namely a count of 

 \* all Token objects whose part\_of\_speech is equal to Verb.

 \*/

GET AGGREGATE FEATURES

COUNT(part\_of\_speech=Verb)

FROM OBJECTS

WHERE

\[Token is\_punctuation=false\]

GO

/\* 

 \* Example 2:

 \*

 \* Finds all Line objects in the database (no monad restriction), and

 \* does three aggregate functions:

 \* - Find the sum of all words spoken by all actants.

 \* - Find a count of all Line objects. (Note that this, together with the

 \*   sum of all words spoken, can be used to calculate the average

 \*   number of words spoken by any actant. This has to be done outside of 

 \*   Emdros, as Emdros does not yet support floating point return values.)

 \* - Find a count of all Line objects whose gender feature is Man, i.e., the

 \*   number of Line spoken by a Man.

 \*/

GET AGGREGATE FEATURES

SUM(words\_spoken), COUNT(\*), COUNT(gender=Man)

FROM OBJECTS

WHERE

\[Line\]

GO

/\*

 \* Example 3:

 \*

 \* Finds all Line objects where actant\_name is equal to Hamlet in

 \* the monad set { 1-12478 } (an arbitrarily chosen example).

 \* Does three aggregate functions:

 \* - Finds the maximum number of words spoken in any of Hamlet’s 

 \*   lines.

 \* - Finds the minimum line number in any act (i.e., the first line

 \*   in which Hamlet speaks.

 \* - Finds the total count of Lines spoken by Hamlet.

 \*/

GET AGGREGATE FEATURES

MAX(words\_spoken), MIN(line\_number\_in\_act), COUNT(\*)

FROM OBJECTS

IN { 1-12478 }

WHERE

\[Line actant\_name=Hamlet

GO

/\*

 \* Example 4:

 \*

 \* Finds all Line objects in all monads,

 \* where actant\_name is equal to Hamlet 

 \* OR is equal to “Ophelia”.

 \* Does three aggregate functions:

 \* - Finds the total sum of words spoken by either Hamlet or Ophelia.

 \* - Finds the count of all Lines in which the actant\_name is “Hamlet”.

 \* - Finds the count of all Lines in which the actant\_name is “Ophelia”.

 \*/

GET AGGREGATE FEATURES

SUM(words\_spoken), COUNT(actant\_name=Hamlet), COUNT(actant\_name=Ophelia)

FROM OBJECTS

IN ALL

WHERE

\[Line actant\_name=Hamlet OR actant\_name=Ophelia

GO

```

# Explanation

This statement returns a table giving the desired aggregate functions
over the objects specified in the WHERE clause.

In essence, five aggregate functions are available:

  - MIN(feature\_name):  
    Retrieves the minimum value of the given feature. The feature must
    be of type integer. The result is also an integer.

  - MAX(feature\_name):  
    Retrieves the maximum value of the given feature. The feature must
    be of type integer. The result is also an integer.

  - SUM(feature\_name):  
    Retrieves the sum of all values of the given feature. The feature
    must be of type integer. The result is also an integer.

  - COUNT(\*):  
    Retrieves a count of all objects retrieved by the WHERE clause. The
    result is an integer.

  - COUNT(feature\_name=feature\_value):  
    Retrieves a count of all objects retrieves, with the added
    restriction that the given feature name must have the given feature
    value. The result is an integer.

The standard SQL aggregate function “AVG” is missing. This is because
Emdros does not (yet) support return values with type “floating point”.
Note that the same result as AVG can be achieved by retrieving two
aggregate functions: SUM(feature\_name) and COUNT(\*), and
then doing the appropriate division outside of Emdros.

The `opt_in_clause` can be used to limit the monad set within which to
retrieve the objects. If omitted, it means that the entire database is
searched, without monad restriction.

The object type name given after the “WHERE” and “\[“
tokens is also the object type on which any features in the aggregate
feature list are found. Hence, the features mentioned in the aggregate
feature list must exist on the object type.

It is possible to use an arbitrary Boolean expression after the object
type name, just as in the topographic MQL queries explained in Chapter .

# Return type

Upon failure, an empty table.

Upon success, a table with one row, and as many columns as there are
aggregate functions in the query. The column types are all “integer”,
and the column names are given as “Column1”, “Column2”, ...,
“Column*N*”, where the number given is the index (1-based) of the
aggregate functions in the input
query.

## GET MONADS<span id="Section:GET MONADS" label="Section:GET MONADS">\[Section:GET MONADS\]

# Syntax

```

get\_monads\_statement : “GET” “MONADS” 

    “FROM”   (“OBJECT” | “OBJECTS”)

    “WITH” id\_ds\_specification

    “\[” object\_type\_name “\]”

;

object\_type\_name : T\_IDENTIFIER

;

```

# Example

```

GET MONADS 

FROM OBJECTS

WITH ID\_DS = 10342, 10344, 10383

\[Clause\]

GO

```

# Explanation<span id="GET_MONADS:Explanation" label="GET_MONADS:Explanation">\[GET\_MONADS:Explanation\]

This statement returns, for each object in the list of id\_ds, a
representation of its set of monads. The set is represented by maximal
stretches of monads. For example, if an object consists of the monads
{ 1, 2, 4, 5, 6, 9, 11, 12 }, and its
id\_d is 10342, then the following will be in the results of the above
example:

| object\_id\_d : id\_d | mse\_first : monad\_m | mse\_last : monad\_m |
| :-------------------: | :-------------------: | :------------------: |
|         10342         |           1           |          2           |
|         10342         |           4           |          6           |
|         10342         |           9           |          9           |
|         10342         |          11           |          12          |

The “mse” in “mse\_first” and “mse\_last” stands for “Monad Set
Element.” A monad set element consists of a starting monad and an
ending monad (always greater than or equal to the starting monad). It
represents all of the monads between the two borders, including the
borders. An mse’s last monad is always greater than or equal to its
first monad.

The mses in the list are always maximal. That is, there is a gap of at
least one monad in between each of the MSEs.

In mathematical terms, suppose we have an MSE A. Then for all other MSEs
B for the same object, it is the case that either A.last + 1 \< B.first
or B.last \< A.first - 1

The MSEs will come in no particular order.

See  for more information on monad sets and the way Emdros treats them.

It does not matter whether you write “OBJECT” or “OBJECTS”: The choice
is merely syntactic sugar.

There is no limit on how many id\_ds can be specified. The algorithm
will not balk at even many thousand id\_ds, but it will, of course, take
more time to get the monads of more objects.

This statement was typically used in a series of SELECT OBJECTS HAVING
MONADS IN, GET MONADS, and GET FEATURES statements, in order to obtain
all information necessary for display of data. This sequence has been
wrapped neatly into the GET OBJECTS HAVING MONADS IN statement, which is
now the preferred method of doing this sequence.

# Return type

A table with the following schema:

| object\_id\_d : id\_d | mse\_first : monad\_m | mse\_last : monad\_m |
| :-------------------: | :-------------------: | :------------------: |

## GET FEATURES<span id="GET-FEATURES" label="GET-FEATURES">\[GET-FEATURES\]

# Syntax

```

get\_features\_statement : “GET”   

    (“FEATURE” | “FEATURES”)

    feature\_list

    “FROM”   (“OBJECT” | “OBJECTS”)

    “WITH” id\_ds\_specification

    “\[”  object\_type\_name   “\]”

;

/\*

 \* feature\_list

 \*/

feature\_list : feature\_name   { “,”  feature\_name }

;

feature\_name : T\_IDENTIFIER

;

object\_type\_name : T\_IDENTIFIER

;

```

# Example

```

GET FEATURES surface, psp

FROM OBJECTS WITH ID\_DS = 12513,12514

\[Word\]

GO

```

# Explanation

This statement returns a table containing feature-values of certain
objects in the database.

Note how this is different from the “SELECT FEATURES” command. The
“SELECT FEATURES” command queries an *object type* for a list of its
*features*. The “GET FEATURES” command queries *objects* for the
*values* of some of their features.

This statement was typically used in a series of SELECT OBJECTS HAVING
MONADS IN, GET MONADS, and GET FEATURES statements, in order to obtain
all information necessary for display of data. This sequence has been
wrapped neatly into the GET OBJECTS HAVING MONADS IN statement, which is
now the preferred method of doing this sequence.

# Return type

The return type is a table with a schema containing one string for each
feature in the list of features. The order of the columns is that in the
list of features. The first column in the table contains the object
id\_d involved in the row. Thus for \(n\) features, the number of
columns will be \(n+1\).

The return type of each feature is the same as the type of the feature.
The exact representation depends on whether the output is console output
or XML output. For XML, see the DTD. For console output, see the
examples below. Enumeration constants are shown as the enumeration
constant label, not the integer value.

For list features, the value is a space-surrounded, space-delimited list
of values. Integers and ID\_Ds are given as integers; enumeration
constant values as their constant names (e.g.,
“first\_person”).

| object\_id\_d: id\_d | surface: string | psp: enum(psp\_t) | number\_in\_corpus : integer | parent: id\_d | parents: list\_of\_id\_d | functions : list\_of\_enum(function\_t) |
| :------------------: | :-------------: | :---------------: | :--------------------------: | :-----------: | :----------------------: | :-------------------------------------: |

The table contains the objects in no particular order.

## GET SET FROM FEATURE

# Syntax

```

get\_set\_from\_feature\_statement : “GET”   “SET”

    “FROM”   “FEATURE”

    feature\_name

    “\[”  object\_type\_name   “\]”

;

feature\_name : T\_IDENTIFIER

;

object\_type\_name : T\_IDENTIFIER

;

```

# Example

```

GET SET 

FROM FEATURE lexeme

\[Word\]

GO

```

# Explanation

This statement returns a table containing the set of existing
feature-values for a feature declared FROM SET. See the CREATE OBJECT
TYPE and UPDATE OBJECT TYPE statements on page and respectively for the
syntax of the FROM SET declaration.

Note how this is different from GET FEATURES: The “GET FEATURES” command
queries *objects* for the *values* of some of their features. The GET
SET FROM FEATURE queries the *set* of existing values for a given
feature, regardless of which objects have these values for this feature.

# Return type

The return type is a table with a schema containing one string for each
value in the set.

| value: string |
| :-----------: |

The order of the strings in the table is
undefined.

## SELECT MIN\_M<span id="SELECT_MIN_M" label="SELECT_MIN_M">\[SELECT\_MIN\_M\]

# Syntax

```

select\_min\_m\_statement : “SELECT”   “MIN\_M”

;

```

# Example

```

SELECT MIN\_M

GO

```

# Explanation

Returns the minimum monad in use in the database. The table returned has
only one data row, namely the minimum monad. See section
[\[min\_m,max\_m\]](#min_m,max_m) for more information.

# Return type

A table with the following schema:

| min\_m : monad\_m |
| :---------------: |

On failure, this table is
empty.

## SELECT MAX\_M<span id="SELECT_MAX_M" label="SELECT_MAX_M">\[SELECT\_MAX\_M\]

# Syntax

```

select\_max\_m\_statement : “SELECT”   “MAX\_M”

;

```

# Example

```

SELECT MAX\_M

GO

```

# Explanation

Returns the maximum monad in use in the database. The table returned has
only one data row, namely the maximum monad. See section
[\[min\_m,max\_m\]](#min_m,max_m) for more information.

# Return type

A table with the following schema:

| max\_m : monad\_m |
| :---------------: |

On failure, this table is
empty.

## SELECT MONAD SETS<span id="SELECT-MONAD-SETS" label="SELECT-MONAD-SETS">\[SELECT-MONAD-SETS\]

# Syntax

```

select\_monad\_sets\_statement : “SELECT” “MONAD” “SETS”

;

```

# Example

```

SELECT MONAD SETS GO

```

# Explanation

This statement returns a table listing the names of the monad sets
stored in the database. These are the monad sets referred to in section
[\[Arbitrary-monad-sets\]](#Arbitrary-monad-sets).

The monad set names come in no particular order.

# Return type

| monad\_set\_name : string |
| :-----------------------: |

## GET MONAD SETS<span id="GET-MONAD-SETS" label="GET-MONAD-SETS">\[GET-MONAD-SETS\]

# Syntax

```

get\_monad\_sets\_statement : “GET” “MONAD” (“SET” | “SETS”)

                          monad\_sets\_specification

;

monad\_sets\_specification : “ALL”

  | monad\_set\_list

;

monad\_set\_list : monad\_set\_name { “,” monad\_set\_name }

;

monad\_set\_name : T\_IDENTIFIER

;

```

# Example

```

GET MONAD SET My\_research\_collection

GO

GET MONAD SETS Historical\_books, Former\_prophets

GO

GET MONAD SETS ALL

GO

```

# Explanation

This statement returns a table listing the monads of each of the monad
sets named in the query. These monad sets are the arbitrary monad sets
described in section
[\[Arbitrary-monad-sets\]](#Arbitrary-monad-sets).

It doesn’t matter whether you say “SET” or “SETS”. This is purely
syntactic sugar.

If “ALL” is given as the monad\_sets\_specification, then all monad sets
are listed, in no particular order.

In the output, each monad set is represented in the same way as
described in section
[\[GET\_MONADS:Explanation\]](#GET_MONADS:Explanation). Each monad set
is guaranteed to appear in the table in one contiguous stretch, that is,
monad sets are not interleaved. Moreover, the monad set elements of each
monad set is sorted on mse\_first, in ascending
order.

# Return type

| monad\_set\_name : string | mse\_first : monad\_m | mse\_last : monad\_m |
| :-----------------------: | :-------------------: | :------------------: |

# Schema reflection

This section describes those query statements which can be used to
retrieve information about the schema.

## SELECT OBJECT TYPES

# Syntax

```

select\_object\_types\_statement : “SELECT”

    \[ “OBJECT” \]    “TYPES”

;

```

# Example

```

SELECT OBJECT TYPES

GO

```

# Explanation

This statement returns a list of the names of all the object types
available in the database.

# Return type

A table with the following schema:

| object\_type\_name: string |
| :------------------------: |

On failure, this table is
empty.

## SELECT FEATURES

# Syntax

```

select\_features\_statement : “SELECT”   “FEATURES”

    “FROM”   \[ \[ “OBJECT” \]   “TYPE” \]

    “\[”   object\_type\_name   “\]”

;

object\_type\_name : T\_IDENTIFIER

;

```

# Example

```

SELECT FEATURES

FROM OBJECT TYPE

\[Phrase\]

GO

```

# Explanation

This statement returns a table with the features belonging to the given
object type.

The type\_name string in the result gives the type of the feature. It
has the values as in table
[\[cap:Possible-type-names\]](#cap:Possible-type-names).

The default\_value string in the result is a string representation of
the default value. It must be interpreted according to the feature type.

The computed boolean in the result shows whether the feature is computed
or not. Currently, the only computed features are: “self”,
“first\_monad”, “last\_monad”, “monad\_count”, and
“monad\_set\_length”.

For lists, what is shown in the “default value” field is always “()”
meaning “the empty list”.

For sets of monads, a string giving the canonical form of an empty set
of monads is used: “ {  }
”.

| Type name                | Meaning                                                  |
| :----------------------- | :------------------------------------------------------- |
| integer                  | integer                                                  |
| id\_d                    | id\_d                                                    |
| list of integer          | list of integer                                          |
| list of id\_d            | list of id\_d                                            |
| list of *something else* | list of enumeration constants from the enumeration given |
| string                   | 8-bit string of arbitrary length                         |
| ascii                    | 7-bit (ASCII) string of arbitrary length                 |
| set of monads            | set of monads                                            |
| *everything else*        | enumeration by the name given                            |

Possible type names in SELECT
FEATURES<span id="cap:Possible-type-names" label="cap:Possible-type-names">\[cap:Possible-type-names\]

# Return type

A table with the following
schema:

| feature\_name: string | type\_name: string | default\_value: string | computed: boolean |
| :-------------------: | :----------------: | :--------------------: | :---------------: |

On failure, this table is empty. On success, the table cannot be empty,
since every object type has the feature “self”.

## SELECT ENUMERATIONS

# Syntax

```

select\_enumerations\_statement : “SELECT”

    “ENUMERATIONS”

;

```

# Example

```

SELECT ENUMERATIONS

GO

```

# Explanation

This statement returns a table with the names of all the enumerations
available in the database.

# Return type

A table with the following schema:

| enumeration\_name: string |
| :-----------------------: |

On failure, this table is empty. Note, however, that it can also be
empty because there are no enumerations in the database yet.

## SELECT ENUMERATION CONSTANTS

# Syntax

```

select\_enumeration\_constants\_statement : “SELECT”

    (“ENUM” | “ENUMERATION”)   “CONSTANTS”

    “FROM”    \[ (“ENUM” | “ENUMERATION” ) \]

    enumeration\_name

;

enumeration\_name : T\_IDENTIFIER

;

```

# Example

```

SELECT ENUMERATION CONSTANTS

FROM ENUMERATION phrase\_types

GO

```

# Explanation

This statement returns a table with the enumeration constants in a given
enumeration.

Note that the syntax is made so that the query need not be as verbose as
in the example just given. There is quite a lot of syntactic sugar\[5\]
in this statement.

# Return type

A table with the following
schema:

| enum\_constant\_name: string | value : integer | is\_default : boolean |
| :--------------------------: | :-------------: | :-------------------: |

On failure, this table is empty.

## SELECT OBJECT TYPES USING ENUMERATION 

# Syntax

```

select\_object\_types\_which\_use\_enum\_statement : “SELECT” 

    \[ “OBJECT” \]    “TYPES”

    “USING”

    (“ENUM” | “ENUMERATION”) enumeration\_name

;

enumeration\_name : T\_IDENTIFIER

;

```

# Example

```

SELECT OBJECT TYPES

USING ENUMERATION phrase\_types\_t

GO

```

# Explanation

This statement returns a table with the names of the object types which
use a given enumeration. The rows of the table are not ordered. An
object type uses an enumeration if at least one of its features is of
the enumeration type.

# Return type

A table with the following schema:

| object\_type\_name: string |
| :------------------------: |

On failure, this table is empty. Note, however, that it can also be
empty because there are no object types using the
enumeration.

# Object manipulation

## CREATE OBJECT FROM MONADS<span id="CREATE_OBJECT_FROM_MONADS" label="CREATE_OBJECT_FROM_MONADS">\[CREATE\_OBJECT\_FROM\_MONADS\]

# Syntax

```

create\_object\_from\_monads\_statement : “CREATE”   “OBJECT”

    “FROM”   monad\_specification

    \[ with\_id\_d\_specification \]

    object\_creation\_specification

;

/\*

 \* monad-specification

 \*/

monad\_specification : “MONADS”   “=”   monad\_set

;

/\*

 \* with-id\_d-specification

 \*/

with\_id\_d\_specification : “WITH”   “ID\_D” 

    “=”  id\_d\_const

;

id\_d\_const : T\_INTEGER

  | “NIL”

;

/\*

 \* object-creation-specification

 \*/

object\_creation\_specification : “\[”

    object\_type\_name

    \[ list\_of\_feature\_assignments \]

    “\]”

;

object\_type\_name : T\_IDENTIFIER

;

list\_of\_feature\_assignments : feature\_assignment    
                              { feature\_assignment }

;

feature\_assignment : feature\_name  “:=”  expression  “;”

    | feature\_name  “:=”  list\_expression  “;”

;

feature\_name : T\_IDENTIFIER

;

expression : signed\_integer /\* integer and id\_d \*/

  | T\_STRING

  | T\_IDENTIFIER /\* enumeration constant \*/

  | monad\_set

;

list\_expression : “(“ \[list\_values\] “)”

;

list\_values : list\_value { “,” list\_value }

;

list\_value : signed\_integer

  | T\_IDENTIFIER /\* enumeration constant \*/

;

```

# Example

```

CREATE OBJECT FROM MONADS = { 1-2, 4-7 }

\[Clause

   clause\_type := NC;

   parent := 10033;

   descendants := (104546, 104547, 104549);

\]

GO   
   
CREATE OBJECTS FROM MONADS = { 35-37 }

WITH ID\_D = 104546

\[Phrase

   phrase\_type := NP;

   parents := (104212, 104215, 104219);

\]

GO

```

# Explanation

This statement creates a new object from a specified set of monads.

In creating an object, four items of information are necessary:

1.  The new id\_d,

2.  The object type,

3.  The set of monads,

4.  Any features that need non-default values.

This statement creates an object of type “`object_type_name`” using the
monads and features, and optional id\_d, given. All features not
specified will be given default values.

If you specify an id\_d with the “WITH ID\_D” specification, the system
first checks whether that object id\_d is already in use. If it is, the
creation fails. If it is not, that id\_d is used. If you do not specify
an id\_d, a unique id\_d is auto-generated.

Note that when using WITH ID\_D, it is not recommended to run several
concurrent processes against the same database which issue CREATE OBJECT
or CREATE OBJECTS statements. Doing so may cause the auto-generated
object id\_d sequence to become invalid. However, several concurrent
processes may safely issue CREATE OBJECT(S) statements if none of them
use WITH ID\_D.

Note that objects of the special object types all\_m, any\_m, and pow\_m
cannot be created.

# Return type

A table with the following schema:

| object\_id\_d: id\_d |
| :------------------: |

On success, there is always only one row in the table, namely the row
containing the object id\_d of the newly created object.

On failure, the table is
empty.

## CREATE OBJECT FROM ID\_DS<span id="CREATE_OBEJCT_FROM_ID_DS" label="CREATE_OBEJCT_FROM_ID_DS">\[CREATE\_OBEJCT\_FROM\_ID\_DS\]

# Syntax

```

create\_object\_from\_id\_ds\_statement : “CREATE”   “OBJECT”

    “FROM”   id\_ds\_specification

    \[ with\_id\_d\_specification \]

    object\_creation\_specification

;

/\*

 \* id\_ds-specification

 \*/

id\_ds\_specification : (“ID\_D” | “ID\_DS”) 

    “=”   id\_d\_list

;

id\_d\_list : id\_d   { “,”  id\_d }

;

id\_d : id\_d\_const

;

id\_d\_const : T\_INTEGER

  | “NIL”

;

```

# Example

```

CREATE OBJECT FROM ID\_DS = 10028, 10029

\[Clause

   clause\_type := NC;

   parent := 10033;

\]

GO

```

# Explanation

This statement creates a new object with the monads contained in the
objects specified by their id\_ds.

The id\_ds specified are used only to calculate the set of monads to be
used. This is calculated as the union of the set of monads of the
objects with the id\_ds specified. These id\_ds can point to objects of
any type, and it need not be the same type for all id\_ds.

Note that there is a syntactic sugar-choice of whether to say “ID\_DS”
or “ID\_D”.

Note that objects of the special object types all\_m, any\_m, and pow\_m
cannot be created.

See the “CREATE OBJECT FROM MONADS” (section
[\[CREATE\_OBJECT\_FROM\_MONADS\]](#CREATE_OBJECT_FROM_MONADS) on page )
for further explanation and warnings. Especially about concurrent use of
WITH ID\_D.

# Return type

The return type is the same as for CREATE OBJECT FROM MONADS (section
[\[CREATE\_OBJECT\_FROM\_MONADS\]](#CREATE_OBJECT_FROM_MONADS)).

## CREATE OBJECTS WITH OBJECT TYPE

# Syntax

```

create\_objects\_statement : “CREATE”  “OBJECTS”

                           “WITH”  “OBJECT” “TYPE”

                           “\[”  object\_type\_name  “\]”

                           object\_creation\_list 

;   
   
object\_creation\_list : object\_creation { object\_creation }

;   
   
object\_creation : “CREATE”  “OBJECT”

                  “FROM”  monad\_specification

                  \[ with\_id\_d\_specification \]

                  “\[” 

                  \[ list\_of\_feature\_assignments \] 

                  “\]” 

; 

```

# Example

```

CREATE OBJECTS

WITH OBJECT TYPE \[Phrase\]

CREATE OBJECT

FROM MONADS = { 1-2 }

\[ 

  phrase\_type := NP; 

  function := Subj;

\]

CREATE OBJECT

FROM MONADS = { 3-7 }

\[

  // Use default values for phrase\_type and function

  // (probably VP/Pred in this fictive example)

\] 

CREATE OBJECT

FROM MONADS = { 4-7 }

WITH ID\_D = 1000000 // Assign specific ID\_D

\[

  phrase\_type := NP;

  function := Objc;

\]

GO

```

# Explanation

This statement is for batch importing of objects. It is useful when
populating databases, either from scratch or by adding large numbers of
objects to an existing database. This statement is much faster than
individual CREATE OBJECT statements.

The object type is specified only once, at the top. Note that no
features can be assigned where the object type is specified: That comes
later in the query, when each object is created.

Each object to be created must be given a monad set. The monad set
follows the syntax specified in section
[\[SELECT\_OBJECTS\]](#SELECT_OBJECTS).

Optionally, an id\_d can be specified. If an id\_d is specified, it is
the user’s responsibility to ensure that the id\_d assigned does not
clash with another id\_d in the database. This is mainly useful when
dumping/restoring databases.

If no id\_d is specified, a unique id\_d is generated. This id\_d is
only guaranteed to be unique if no other objects are created with
specific id\_ds.

Note that when using WITH ID\_D, it is not recommended to run several
concurrent processes against the same database which issue CREATE OBJECT
or CREATE OBJECTS statements. Doing so may cause the auto-generated
object id\_d sequence to become invalid. However, several concurrent
processes may safely issue CREATE OBJECT(S) statements if none of them
use WITH ID\_D.

The feature-value assignments follow the same rules as for CREATE OBJECT
FROM MONADS (see section
[\[CREATE\_OBJECT\_FROM\_MONADS\]](#CREATE_OBJECT_FROM_MONADS)). If an
object has a feature which is not assigned a value, the default value is
used. The default value of a given feature can be specified when
creating the object type, or when updating the object type (see section
[\[CREATE\_OBJECT\_TYPE\]](#CREATE_OBJECT_TYPE) and section
[\[UPDATE\_OBJECT\_TYPE\]](#UPDATE_OBJECT_TYPE)).

A table is returned showing the number of objects created successfully.
This number is valid even if the process failed half way through. In
other words, if the process did not run to completion due to a DB error,
the value in the return type will show how many objects, if any, were
created successfully. This means that there is no way of knowing which
object got which object id\_d, a difference from the regular CREATE
OBJECT statement.

# Return type

A table with the following schema:

| object\_count: integer |
| :--------------------: |

On both success and failure, the table contains one row showing the
number of objects created
successfully.

## UPDATE OBJECTS BY MONADS<span id="UPDATE_OBJECTS_BY_MONADS" label="UPDATE_OBJECTS_BY_MONADS">\[UPDATE\_OBJECTS\_BY\_MONADS\]

# Syntax

```

update\_objects\_by\_monads\_statement : “UPDATE” 

    (“OBJECT” | “OBJECTS”)

    “BY”   monad\_specification 

    object\_update\_specification

;

/\*

 \* object-update-specification

 \*/

object\_update\_specification : “\[“   object\_type\_name 

    list\_of\_feature\_assignments

    “\]”

;

object\_type\_name : T\_IDENTIFIER

;

```

# Example

```

UPDATE OBJECTS BY MONADS = { 1-2, 4-7, 8-20 }

\[Clause

    clause\_type := VC;

\]

GO

```

# Explanation

This statement finds all the objects of type `object_type_name` which
are part\_of the monads specified (i.e., they must be wholly contained
within the monads specified), and updates their features according to
the list of feature assignments.

Note that there is a syntactic sugar-choice of whether to say “OBJECTS”
or “OBJECT”. This is because the user may know that only one object is
to be found within the monads, in which case having to write “OBJECTS”
would be intellectually irritating.

Note that objects of the special object types all\_m, any\_m, and pow\_m
cannot be updated.

The feature “self” cannot be updated.

# Return type

A table with the following schema:

| object\_id\_d: id\_d |
| :------------------: |

On success, the table contains one row for each updated object.

On failure, the table is empty.

## UPDATE OBJECTS BY ID\_DS

# Syntax

```

update\_objects\_by\_id\_ds\_statement : “UPDATE” 

    (“OBJECT” | “OBJECTS”)

    “BY”   id\_ds\_specification 

    object\_update\_specification

;

```

# Example

```

UPDATE OBJECTS BY ID\_DS = 10028, 10029

\[Phrase

    parent := 10034;

\]

GO

```

# Explanation

This statement updates all the objects of the given type with the given
id\_ds.

The id\_ds should point to objects which are really of the given type.
Otherwise, an error is issued.

Note that there is a syntactic sugar-choice between “OBJECTS” and
“OBJECT.”

Note that objects of the special object types all\_m, any\_m, and pow\_m
cannot be updated.

The feature “self” cannot be updated.

# Return type

The return type is the same as for UPDATE OBJECTS BY MONADS (section
[\[UPDATE\_OBJECTS\_BY\_MONADS\]](#UPDATE_OBJECTS_BY_MONADS)).

## DELETE OBJECTS BY MONADS<span id="DELETE_OBJECTS_WITH_MONADS" label="DELETE_OBJECTS_WITH_MONADS">\[DELETE\_OBJECTS\_WITH\_MONADS\]

# Syntax

```

delete\_objects\_by\_monads\_statement : “DELETE”

    (“OBJECT” | “OBJECTS”)

    “BY”   monad\_specification

    object\_deletion\_specification

;

/\*

 \* object-deletion-specification

 \*/

object\_deletion\_specification : “\[”

    object\_type\_name\_to\_delete

    “\]”

;

object\_type\_name\_to\_delete : object\_type\_name 

  | “ALL”

;

object\_type\_name : T\_IDENTIFIER

;

```

# Example

```

DELETE OBJECTS BY MONADS = { 1-20 }

\[Clause\]

GO

```

If “`object_name_to_delete`” is “ALL”, then all objects of all types
which are at these monads are deleted:

```

DELETE OBJECTS BY MONADS = { 28901-52650 }

\[ALL\]

GO

```

# Explanation

This command deletes all the objects of type `object_type_name` which
are part\_of the set of monads specified.

# Return type

A table with the following schema:

| object\_id\_d: id\_d |
| :------------------: |

On success, the table contains one row for each deleted object.

On failure, the table is empty.

## DELETE OBJECTS BY ID\_DS

# Syntax

```

delete\_objects\_by\_id\_ds\_statement : “DELETE”

    (“OBJECT” | “OBJECTS”)

    “BY”   id\_ds\_specification

    object\_deletion\_specification

;

```

# Example

```

DELETE OBJECTS BY ID\_DS 10028, 10029

\[Phrase\]

GO

```

# Explanation

This statement deletes objects by their id\_ds. Note that you cannot
write “ALL” for `object_deletion_specification`. The id\_ds given should
point to objects of the type given.

# Return type

The return type is the same as for DELETE OBJECTS BY MONADS (section
[\[DELETE\_OBJECTS\_WITH\_MONADS\]](#DELETE_OBJECTS_WITH_MONADS)).

# Monad manipulation

## MONAD SET CALCULATION<span id="MONAD-SET-CALCULATION" label="MONAD-SET-CALCULATION">\[MONAD-SET-CALCULATION\]

# Syntax

```

monad\_set\_calculation\_statement : “MONAD”  “SET”

    “CALCULATION”

    monad\_set\_chain

;

monad\_set\_chain : monad\_set    
                  { monad\_set\_operator  monad\_set }

;

monad\_set\_operator : “UNION”

  | “DIFFERENCE”

  | “INTERSECT”

;

```

# Example

```

// Produces { 1-10 }

MONAD SET CALCULATION

{ 1-5, 7-8 }

UNION

{ 5-10 }

GO   
   
// Produces { 2-5, 22-24 }

MONAD SET CALCULATION

{ 1-10, 20-30, 50-60 }

INTERSECT

{ 2-5, 22-24 }

GO   
   
// Produces { 1-4, 8-10 }

MONAD SET CALCULATION

{ 1-10 }

DIFFERENCE

{ 5-7 }

GO   
   
// Produces { 2-3, 5-6, 10-12 }

MONAD SET CALCULATION

{ 1-3, 5-9 }

INTERSECT

{ 2-6 }

UNION

{ 10-12 }

GO

```

# Explanation

This statement is for performing set-operations on sets of monads. The
three standard set operations “union,” “intersect,” and “difference” are
provided.

The return value is a representation of the resulting set of monads
along the same lines as for the GET MONADS statement (see section
[\[Section:GET MONADS\]](#Section:GET%20MONADS)).

The MSEs (see section [\[Section:GET MONADS\]](#Section:GET%20MONADS))
are listed in ascending order.

You can specify as many sets of monads as you want. The operations are
done in succession from the first to the last set of monads. For
example, in the last example above, the intersection is done first, and
the union is done on the result of the intersection.

You can also specify only one set of monads, with no set operator. This
is useful for creating a sorted, normalized set of monads from a number
of different MSEs.

Note that this statement does not manipulate the stored arbitrary monad
sets described in section
[\[Arbitrary-monad-sets\]](#Arbitrary-monad-sets).

# Return type

A table with the following schema:

| mse\_first : monad\_m | mse\_last : monad\_m |
| :-------------------: | :------------------: |

## CREATE MONAD SET<span id="CREATE-MONAD-SET" label="CREATE-MONAD-SET">\[CREATE-MONAD-SET\]

# Syntax

```

create\_monad\_set\_statement : “CREATE” “MONAD” “SET”

            monad\_set\_name

            “WITH” “MONADS” “=” monad\_set

;

monad\_set\_name : T\_IDENTIFIER

;

```

# Example

```

CREATE MONAD SET

My\_research\_collection

WITH MONADS = { 1-10394, 14524-29342, 309240-311925 }

GO

```

# Explanation

This statement creates an arbitrary monad set in the database. These
monad sets are the ones described in section
[\[Arbitrary-monad-sets\]](#Arbitrary-monad-sets).

# Return type

There is no return value.

## UPDATE MONAD SET<span id="UPDATE-MONAD-SET" label="UPDATE-MONAD-SET">\[UPDATE-MONAD-SET\]

# Syntax

```

update\_monad\_set\_statement : “UPDATE” “MONAD” “SET”

     monad\_set\_name

     (“UNION” | “INTERSECT” | “DIFFERENCE” | “REPLACE”)

     (monad\_set | monad\_set\_name)

;

monad\_set\_name : T\_IDENTIFIER

;

```

# Examples

```

// Adds the specified monad set to “Historical\_books”

UPDATE MONAD SET

Historical\_books

UNION

{ 310320-329457 }

GO

// Remove the specified monad set from “Historical\_books”

UPDATE MONAD SET

Historical\_books

DIFFERENCE

{ 310320-329457 }

GO

// Intersects the monad set “My\_research\_collection”

// with the monad set “My\_experimental\_collection”

UPDATE MONAD SET

My\_research\_collection

INTERSECT

My\_experimental\_collection

GO

// Replaces the monad set “Lamentations” with 

// the specified monad set

UPDATE MONAD SET

Lamentations

REPLACE

{ 380300-383840 }

GO

```

# Explanation

This statement is used to update an already-existing arbitrary monad set
(see section
[\[Arbitrary-monad-sets\]](#Arbitrary-monad-sets)). Four
operations are provided: set union, set intersection, set difference,
and replacement. In all cases, the operation is done using two monad
sets. The first set is the named set that is updated. The second set is
either a set described in terms of monads, or the name of another
arbitrary monad set.

The replacement operator effectively deletes the old set, replacing it
with the new. Note, however, that this does not imply that the new is
deleted – if you update one named monad set, replacing it with another
named monad set, that other monad set is not deleted, but simply copied
into the old monad set.

The other three operators are standard set-theoretic operators.

# Return type

There is no return value.

## DROP MONAD SET<span id="DROP-MONAD-SET" label="DROP-MONAD-SET">\[DROP-MONAD-SET\]

# Syntax

```

drop\_monad\_set\_statement : “DROP” “MONAD” “SET”

                           monad\_set\_name

;

monad\_set\_name : T\_IDENTIFIER

;

```

# Example

```

DROP MONAD SET Historical\_books

GO

```

# Explanation

This statement drops an arbitrary monad set (i.e., deletes it) from the
database. These are the arbitrary monad sets described in section
[\[Arbitrary-monad-sets\]](#Arbitrary-monad-sets).

# Return type

There is no return value.

# Meta-statements

## QUIT

# Syntax

```

quit\_statement : “QUIT”

;

```

# Example

```

QUIT

```

# Explanation

This causes the rest of the MQL stream not to be interpreted. It also
causes the mql(1) program to quit after having executed this statement.

The QUIT statement can be used, e.g., if running the mql(1) program as a
daemon through xinetd(8) or inetd(8), to end the connection.

The QUIT statement is special in that it does not need a “GO” keyword
after it. You may supply the “GO” keyword if you wish, but it is not
required.

If a transaction was in progress (see BEGIN TRANSACTION statement,
section [\[BEGIN TRANSACTION\]](/mql/meta/begintransaction/)), the
transaction is automatically committed before the QUIT statement is
executed.

# Return type

There is no return value.

# MQL Query subset<span id="chapter:MQL Query Subset" label="chapter:MQL Query Subset">\[chapter:MQL Query Subset\]

# Introduction

This chapter is an introduction to the query-subset of MQL for
programmers. That is, it introduces the important subset of MQL in which
you can express queries that find objects and gaps in interesting
environments, with specified interrelations, and with specified
feature-values.

An easier-to-read MQL Query Guide is available from the Emdros website,
or with the Emdros sourcecode in the doc/ directory (see ).

First, we give an informal introduction to MQL by means of some examples
([\[sec:Informal-introduction-to\]](#sec:Informal-introduction-to)).
Then we give a complete overview of the syntax of the MQL query-subset
([3](#mql_query:Syntax)). Then we explain the sheaf, which is the
data-structure that an MQL query-query returns ([\[sheaf\]](/mql/topographic/preliminaries/sheaf/)).
Then we explain what a Universe and a Substrate are, since they are
important in understanding how a query works
([\[sec:Universe-and-substrate\]](#sec:Universe-and-substrate)). After
that, we explain two important properties of mql queries, namely
consecutiveness and embedding
([\[mql-query:Consecutiveness-and-embedding\]](#mql-query:Consecutiveness-and-embedding)).
After that, we give detailed explanations of the blocks of the MQL
query-subset, which are the “building blocks” out of which a query is
made ([\[Blocks\]](#Blocks)). Finally, we explain how strings of blocks
are written, and what they mean
([\[sec:Strings-of-blocks\]](#sec:Strings-of-blocks)).

# Informal introduction to MQL by means of some examples<span id="sec:Informal-introduction-to" label="sec:Informal-introduction-to">\[sec:Informal-introduction-to\]

## Introduction

This section informally introduces the query-part of MQL by way of a
number of examples. The example database which we will use is the same
as in Doedens’ book, namely part of Melville’s “Moby Dick”:

> “CALL me Ishmael. Some years ago - never mind how long precisely -
> having little or no money in my purse, and nothing particular to
> interest me on shore, I thought I would sail about a little and see
> the watery part of the world. It is a way I have of driving off the
> spleen, and regulating the circulation. Whenever I find myself growing
> grim about the mouth; whenever it is damp, drizzly November in my
> soul; whenever I find myself involuntarily pausing before coffin
> warehouses, and bringing up the rear of every funeral I meet; and
> especially whenever my hypos get such an upper hand of me, that it
> requires a strong moral principle to prevent me from deliberately
> stepping into the street, and methodically knocking people’s hats off
> - then, I account it high time to get to sea as soon as I can.
> \[...\]
> 
> “\[...\] By reason of these things, then,
> the whaling voyage was welcome; the great flood-gates of the
> wonder-world swung open, and in the wild conceits that swayed me to my
> purpose, two and two there floated into my inmost soul, endless
> processions of the whale, and, mid most of them all, one grand hoofed
> phantom, like a snow hill in the air.”

Suppose that we have in this EMdF database the domain-dependent object
types “paragraph”, “sentence”, and “word”, which correspond to
paragraphs, sentences, and words of the text. And suppose that we add to
the object type “sentence” the feature “mood,” which draws its values
from the enumeration type { imperative, declarative
}. And suppose that we add to the object type “word” the
features “surface” (which gives the surface text of the word) and
“part\_of\_speech” (which gives the part of speech of the word). The
codomain of the feature “part\_of\_speech” on the object type “word”
draws its values from the enumeration type { adjective,
adverb, conjunction, determiner, noun, numeral, particle, preposition,
pronoun, verb }. This hypothetical database will give the
background for most of the examples in our informal introduction to MQL.

In the following, when we refer to an “MQL query”, we will mean the
query-subset of MQL. That is, we abstract away from the
database-manipulation-part of MQL and concentrate on the query-queries.
In addition, we will abstract away from the required “SELECT (FOCUS|ALL)
OBJECTS” syntax that must precede an MQL query-query.

## topograph

An MQL query is called a topograph. Consider the following topograph:

```

\[sentence\]

```

This topograph retrieves a list of all sentence objects in the database.

## features

A query can specify which features an object must have for it to be
retrieved. For example, consider the following topograph:

```

\[word

   surface = Ishmael or part\_of\_speech = verb;

\]

```

This topograph retrieves a list of all words which either have the
surface “Ishmael”, or whose part of speech is “verb.”

## object\_block, object\_block\_first

There are several types of blocks. They are meant to come in a string of
blocks, where each block in the string must match some part of the
database in order for the whole string to match. Two such blocks are the
`object_block` and the `object_block_first`.

Object blocks are the heart and soul of MQL queries. They are used to
match objects and objects nested in other objects. An object block (be
it an `object_block` or an `object_block_first`) consists of the
following parts:

1.  The opening square bracket, ‘`[`’.

2.  An identifier indicating the object type of the objects which we
    wish to match (e.g., “phrase”).

3.  An optional T\_MARKS (e.g., “‘yellow’’ or “‘red‘context’’). This
    will be put into the result set (i.e., sheaf) unchanged, and can be
    used to pass information back into the application from the user.
    The meaning of the T\_MARKS is wholly application-dependent, since
    Emdros does nothing special with it — it just passes the T\_MARKS on
    into the sheaf. See page for the formal definition of T\_MARKS.

4.  An optional “object reference declaration.” A reference to this
    object can be declared with the “`as`” keyword, like “`[word as w`
    \(\ldots\)”. Subsequent blocks can then refer to features of this
    object as “`w`.*featurename*” (see section [\[Object
    references\]](#Object%20references)).

5.  An optional keyword which can be either of “`noretrieve`”,
    “`retrieve`” or “`focus`”. The default, when it is not specified,
    is “`retrieve`”. The keyword “`noretrieve`” says as much as “I do
    not wish to retrieve this object, even if matched”. It is useful for
    specifying the context of what we really wish to retrieve. The
    keyword “`focus`” specifies that this object is to be retrieved (it
    implies “`retrieve`”), and also that, when sifting the sheaf for
    focus objects, this object must go into the result (see section
    [\[Retrieval\]](#Retrieval)).

6.  An optional keyword, “`first`” or “`last`”, which says as much as
    “this object must be first/last in the universe against which we
    are matching (see section [\[First and
    last\]](#First%20and%20last)).

7.  An optional Boolean expression giving what features need to hold
    true for this object for it to be retrieved (see section [\[Feature
    specifications\]](#Feature%20specifications)). This boolean
    expression must be prefixed by one of the words “`feature`” or
    “`features`”. It makes no difference which is used – it is merely
    syntactic sugar.

8.  An optional inner `blocks` which matches objects inside the object
    (see section [\[Block strings:
    blocks\]](#Block%20strings:%20blocks)).

9.  The closing square bracket, ‘`]`’.

Note that only the first object block in a string of blocks can have the
“`first`” keyword, and only the last `object_block` in a string of
`block`s can have the “`last`” keyword.

Consider the following `topograph`:

```

\[sentence‘yellow

    mood = imperative;

    \[word noretrieve first

         surface = CALL;

    \]

    \[word‘red\]

\]

```

This `topograph` retrieves the set of sentences which are imperative,
and whose first word is “CALL”. Within each sentence in that set, we
retrieve the second word, but not the first. The only sentence in our
example database which qualifies is the first sentence.

## power

The power construct is used to indicate that we allow some distance in
between two blocks. A power construct must always stand between two
other blocks, and can thus never be first or last in a query. It comes
in three varieties:

  - A “plain vanilla” power construct, syntactically denoted by two
    dots, “`..`”, and

  - A power construct with a single, upper limit. The limit specifies
    the maximum monads that can intervene between the two surrounding
    blocks. It is denoted as e.g., “`.. < 5`”, or “`.. <= 5`”.

  - A power construct with a compound min/max limit. The limit specifies
    the minimum and maximum monads that can intervene. It is denoted as,
    e.g., “`.. BETWEEN 1 AND 5`”.

Consider the following topograph:

```

\[sentence

    \[word

        part\_of\_speech = preposition\]

    .. \< 4

    \[word

        part\_of\_speech = noun\]

    ..

    \[word last

        surface = world

\]

```

This topograph retrieves a list of sentences which have a word that has
part of speech preposition, followed by a word which has part of speech
noun, and which is within 4 monads of the preposition, followed by the
last word of the sentence, which must be “world”. Within that sentence,
retrieve all the three words. The only sentence which qualifies is the
second.

## opt\_gap\_block

An `opt_gap_block` is used to match an optional gap in the text. It
consists of:

1.  The opening square bracket, ‘`[`’.

2.  The keyword “`gap?`”.

3.  An optional T\_MARKS (e.g., “‘yellow’’ or “‘red‘context’’). This
    will be put into the result set (i.e., sheaf) unchanged, and can be
    used to pass information back into the application from the user.
    The meaning of the T\_MARKS is wholly application-dependent, since
    Emdros does nothing special with it — it just passes the T\_MARKS on
    into the sheaf. See page for the formal definition of T\_MARKS.

4.  An optional “`noretrieve`,” “`retrieve`” or “`focus`.” The default
    is “`noretrieve`”. (See section [\[Retrieval\]](#Retrieval))

5.  An optional `blocks` (see section [\[Block strings:
    blocks\]](#Block%20strings:%20blocks)).

6.  The closing square bracket, ‘`]`’.

The `opt_gap_block` matches gaps in the *substrate* against which we are
matching. Thus if we look at the example in figure
[\[TheDoor\]](#TheDoor), we can construct the following topograph:

```

\[clause

    \[clause\_atom

        \[word

             surface = door,

        \]

    \]

    \[gap? noretrieve\]

    \[clause\_atom noretrieve\]

\]

```

This retrieves all clauses which happen to have inside them a
clause\_atom which contains the word “door,”, followed by a gap,
followed by a clause\_atom. The gap and the second clause\_atom are not
retrieved. This would retrieve clause-1. The gap need not be there.

The default is for the result of an `opt_gap_block` not to be retrieved.
Thus one needs to explicitly write “`retrieve`” if one wishes to
retrieve the gap.

## gap\_block

A `gap_block` is used to match a gap in the text. It consists of:

1.  The opening square bracket, ‘`[`’.

2.  The keyword “`gap`”.

3.  An optional T\_MARKS (e.g., “‘yellow’’ or “‘red‘context’’). This
    will be put into the result set (i.e., sheaf) unchanged, and can be
    used to pass information back into the application from the user.
    The meaning of the T\_MARKS is wholly application-dependent, since
    Emdros does nothing special with it — it just passes the T\_MARKS on
    into the sheaf. See page for the formal definition of T\_MARKS.

4.  An optional “`noretrieve`,” “`retrieve`” or “`focus`.” The default
    is “`noretrieve`”. (See section [\[Retrieval\]](#Retrieval)).

5.  An optional `blocks`. (See section [\[Block strings:
    blocks\]](#Block%20strings:%20blocks)).

6.  The closing square bracket, ‘`]`’.

The `gap_block` is analogous to the `opt_gap_block` in all respects
except that there *must* be a gap in order for the query to match.

## object references

An object reference is a name given to a previously retrieved object
with the “`as` *identifier*” declaration. An object reference can then
be used in subsequent comparisons with features of other objects. This
is done by selecting the desired feature from the object reference by
using dot-notation, as in the example below:

```

\[word as w

    part\_of\_speech = article;

\]

\[word‘myhit

   (part\_of\_speech = noun 

    or part\_of\_speech = adjective)

    and case = w.case 

    and number = w.number 

    and gender = w.gender;

\]

```

Assuming that the `word` object type has features part\_of\_speech,
case, number, and gender, this topograph retrieves all pairs of words
which satisfy the following conditions:

  - The first word has part of speech “article”,

  - The second word has part of speech “noun” or “adjective”, and

  - Both words have the same case, number, and gender.

This concludes our gentle, informal introduction to MQL.

# Syntax of mql\_query 

## Introduction

The `mql_query` non-terminal is the entry-point for the MQL
query-subset. It is used in the WHERE clause of the SELECT (FOCUS|ALL)
OBJECTS statement (section [\[SELECT\_OBJECTS\]](#SELECT_OBJECTS) on
page ). In this section, we give the full grammar of the MQL
query-subset. It is important that you take some time to read through
the grammar. Subsequent sections will build on the bird’s-eye view given
in this
section.

## Syntax

```

mql\_query : topograph

; 

topograph : blocks 

;

blocks : block\_string

;

block\_string : block\_string2 

             | block\_string2 “OR” block\_string

;

block\_string2 : block\_string1

              | block\_string1 block\_string2

              | block\_string1 “\!” block\_string2

;

block\_string1 : block\_string0

              | block\_string0 “\*” \[monad\_set\]

;

block\_string0 : block

              | “\[“ block\_string “\]”

;

block : opt\_gap\_block 

      | gap\_block 

      | power\_block

      | object\_block

      | (“NOTEXIST” | “NOTEXISTS” ) object\_block

;

opt\_gap\_block : “\[”   “GAP?”   

                      \[ marks\_declaration \]

                      \[ gap\_retrieval \]   

                      \[ blocks \]  

                “\]” 

;

marks\_declaration : T\_MARKS

;

gap\_retrieval : “NORETRIEVE”

              | “RETRIEVE”

              | “FOCUS”

;

gap\_block : “\[”   “GAP”   

                  \[ marks\_declaration \]

                  \[ gap\_retrieval \]   

                  \[ blocks \]   

            “\]”

;

object\_block :  “\[”   object\_type\_name

                     \[ marks\_declaration \]

                     \[ object\_reference\_declaration \]

                     \[ retrieval \]  

                     \[ firstlast \]

                     \[ monad\_set\_relation\_clause \]

                     \[ feature\_constraints \]

                     \[ feature\_retrieval \]

                     \[ blocks \]   

               “\]”

;

object\_reference\_declaration : “AS” object\_reference 

;

object\_reference : T\_IDENTIFIER 

;

retrieval : “NORETRIEVE”

          | “RETRIEVE”

          | “FOCUS”

;

firstlast : “FIRST”

          | “LAST”

          | “FIRST”   “AND”   “LAST”

;

feature\_constraints  : ffeatures 

;

ffeatures : fterm 

          |  ffeatures   “OR”   fterm 

;

fterm : ffactor

      | ffactor   “AND”   fterm 

;

ffactor : “NOT”   ffactor

        | “(”   ffeatures   “)”

        | feature\_comparison 

;

feature\_comparison : 

    comparison\_feature\_name  comparison\_operator   value

  | comparison\_feature\_name  “=”   ()

  | comparison\_feature\_name  “=”   enum\_const\_set

  | comparison\_feature\_name  “=”   “(“ list\_of\_integer “)”

  | comparison\_feature\_name  “IN”   enum\_const\_set

  | comparison\_feature\_name  “IN”   “(“ list\_of\_integer “)”

  | comparison\_feature\_name  “IN”   object\_reference\_usage

;

comparison\_operator : “=”

                    | “\<”

                    | “\>”

                    | “\<\>”  /\* not equal \*/

                    | “\<=”  /\* less than or equal \*/

                    | “=\<”  /\* less than or equal \*/

                    | “\>=”  /\* greater than or equal \*/

                    | “=\>”  /\* greater than or equal \*/

                    | “~”   /\* regular expression \*/

                    | “\!~”  /\* inverted regular expression \*/

                    | “HAS” /\* lhs: list; rhs: atomic value.

                                 signifies list membership. \*/

;

list\_of\_integer : T\_INTEGER { “,” T\_INTEGER }\*

;

value : enum\_const

      | signed\_integer

      | T\_STRING

      | object\_reference\_usage

;

enum\_const : T\_IDENTIFIER

;

object\_reference\_usage : object\_reference   

                         “.”   feature\_name 

;

enum\_const\_set : “(“ enum\_const\_list “)”

;

enum\_const\_list : enum\_const { “,” enum\_const\_list }

;

power : “..”   \[ restrictor \]

;

restrictor : “\<” limit 

           | “\<=” limit

           | “BETWEEN” limit “AND” limit

;

limit : T\_INTEGER /\* non-negative integer, may be 0. \*/

; 

feature\_retrieval : “GET” feature\_list

  | /\* empty: Don’t retrieve any features \*/

;

monad\_set\_relation\_clause : /\* empty; which means: part\_of(substrate) \*/

           | monad\_set\_relation\_operation “(“ universe\_or\_substrate “)”

           | monad\_set\_relation\_operation “(“ monad\_set\_or\_monads “,” universe\_or\_substrate “)”

;

monad\_set\_relation\_operation : “part\_of” | “overlap”

;

universe\_or\_substrate : “universe” | “substrate”

;

monad\_set\_or\_monads : “monads” | T\_IDENTIFIER 

;

comparison\_feature\_name : feature\_name

           | computed\_feature\_name

;

computed\_feature\_name : 

             “first\_monad” computed\_feature\_monad\_set\_name

           | “last\_monad” computed\_feature\_monad\_set\_name

           | “monad\_count” computed\_feature\_monad\_set\_name

           | “monad\_set\_length” computed\_feature\_monad\_set\_name

;

computed\_feature\_monad\_set\_name : /\* empty: Means “(monads)”. \*/

           | “(“ “monads” “)” /\* Means: “(monads)”

           | “(“ monad\_set\_name “)”

;

```

# The sheaf<span id="sheaf" label="sheaf">\[sheaf\]

# Blocks<span id="Blocks" label="Blocks">\[Blocks\]

## Introduction

Blocks are the heart and soul of MQL query-queries. They specify which
objects and which gaps in those objects should be matched and/or
retrieved. With object blocks, you specify which objects should be
matched. With gap blocks, you specify whether a gap should be looked
for.

In this section, we treat the four kinds of blocks in MQL in some
detail. First, we describe and explain the two kinds of object block
(Object blocks, [\[Object blocks\]](#Object%20blocks)). Then we treat
the two kinds of gap blocks (Gap blocks, [\[Gap
blocks\]](#Gap%20blocks)). Then we describe how to specify whether to
retrieve a block’s contents (Retrieval, [\[Retrieval\]](#Retrieval)).
After that we describe how to specify that an object block should be
either first or last in its enclosing `blocks` (First and last, [\[First
and last\]](#First%20and%20last)). Then we describe and explain how to
specify constraints on features (Feature constraints, [\[Feature
specifications\]](#Feature%20specifications)). Then we describe object
references, which are a way of referring to other objects in a query
(Object references, [\[Object references\]](#Object%20references)).
Finally, we wrap up the syntactic non-terminals dealing with blocks by
describing the `block` (Block, [\[Blocks:
block\]](#Blocks:%20block))

## Object blocks<span id="Object blocks" label="Object blocks">\[Object blocks\]

### Introduction

Object blocks specify which objects should be matched. Therefore, they
are quite important in MQL. With object blocks, it is also possible to
specify whether or not matched objects should be retrieved. You can also
specify constraints on the features of the objects which should be
matched; You can specify whether you want objects matched against a
certain object block to be first or last in the string of blocks we are
looking for at the moment; And finally, you can label objects matched in
a query with object reference labels, so that those objects can be
referred to later in the query (i.e., further down in the MQL query, and
thus further on in the string of monads). In this subsection, we deal
with the object blocks themselves, deferring the treatment of
feature-constraints, first/last-specifications, and object references to
later subsections.

First, we describe the syntax of object blocks, then we give some
examples, and finally we give some explanatory
information.

# Syntax

```

object\_block :  “\[”   object\_type\_name

                     \[ marks\_declaration \]

                     \[ object\_reference\_declaration \]

                     \[ retrieval \]  

                     \[ firstlast \]

                     \[ monad\_set\_relation\_clause \]

                     \[ feature\_constraints \]

                     \[ feature\_retrieval \]

                     \[ blocks \]   

               “\]”

;

object\_type\_name : T\_IDENTIFIER

;

marks\_declaration : T\_MARKS

;

retrieval : “NORETRIEVE”

          | “RETRIEVE”

          | “FOCUS”

;

firstlast : “FIRST”

          |  “LAST”

          |  “FIRST”   “AND”   “LAST”

;

last : “LAST”

;

feature\_retrieval : “GET” feature\_list

  | /\* empty: Don’t retrieve any features \*/

;

monad\_set\_relation\_clause : /\* empty; which means: part\_of(substrate) \*/

           | monad\_set\_relation\_operation “(“ universe\_or\_substrate “)”

           | monad\_set\_relation\_operation “(“ monad\_set\_or\_monads “,” universe\_or\_substrate “)”

;

monad\_set\_relation\_operation : “part\_of” | “overlap”

;

universe\_or\_substrate : “universe” | “substrate”

;

monad\_set\_or\_monads : “monads” | T\_IDENTIFIER 

;

```

# Examples

```

1. \[Clause\]   
   
2. \[Phrase noretrieve first

      phrase\_type = NP

   \]   
   
3. \[Clause first and last\]   
   
4. \[Word as w focus last 

      psp = noun and number = pl

      GET surface, lexeme

   \]   
   
5. \[Clause‘context

     \[Phrase‘red first

       phrase\_type = NP and phrase\_function = Subj

     \]

     \[Phrase‘green

       phrase\_type = VP

       \[Word

         psp = V

       \]

       \[Phrase‘blue

         phrase\_type = NP and phrase\_function = Obj

       \]

     \]

   \]   
    
6. \[Sentence

      NOTEXIST \[Word surface = saw

   \]

```

# Explanation

Firstly, it will be noticed that the first item after the opening
bracket must always be an object type name. This is in keeping with all
other parts of MQL where object type names are used.

Secondly, it will be noticed that all of the other syntactic
non-terminals in the definition of the object blocks are optional.

The marks declaration comes after the object type name. The query-writer
can use it to pass information back into the application that sits on
top of Emdros. Emdros does nothing special with the T\_MARKS, other than
passing it on into the sheaf, that is, into the matched\_object that
arises because of the object\_block. In particular, there is no
semantics associated with the marks\_declaration. See page for the
formal definition of T\_MARKS.

The object reference declaration comes after the marks declaration, and
will be dealt with below ([\[Object references\]](#Object%20references)
on page ).

The specification of the retrieval comes after the object reference
declaration and will be dealt with in another section
([\[Retrieval\]](#Retrieval) on page ).

The specification of the monad set relation clause has an impact on how
the containment is calculated, and was dealt with above
([\[mql-query:Consecutiveness-and-embedding\]](#mql-query:Consecutiveness-and-embedding)
on page ).

The specification of first/last-constraints comes after the
specification of retrieval, and will also be dealt with in another
section ([\[First and last\]](#First%20and%20last) on page ).

The specification of the monad set relation determines four things:

1.  It determines which monad set will be used to match against the
    Substrate or Universe that accompanies the surrounding `blocks`. If
    the “`monad_set_or_monads`” specification is left out, the
    constituting monad set is used (i.e., the monad set which makes up
    the object). The same is true if the monad\_set\_or\_monads
    specification is “`monads`”. If the `monad_set_or_monads`
    specification is not left out, it must be a feature which must exist
    on the object type and be of the type “set of monads”.

2.  It determines which monad set to use as the Substrate of the inner
    `blocks`. The monad set used for the Substrate of the inner `blocks`
    is currently the same as the monad set used to match against the
    Universe or Substrate of the outer `blocks`. This may change in
    future releases of Emdros.

3.  It determines whether to match against the Universe or Substrate of
    the outer bl`ocks`. This is done by the mention of “`universe`” or
    “`substrate`”.

4.  It determines which operation to use when matching against the
    Universe or Substrate of the surrounding `blocks`. This can be
    either “`part_of`” (the monad set of the object must be a subset of
    the Universe or Substrate) or “`overlap`” (non-empty set
    intersection). See section [\[part\_of\]](#part_of) on page for
    details of the part\_of relation.

It is possible to specify constraints on the features of objects. This
is done in the `feature_constraints` non-terminal, which comes after the
first/last-constraints. These constraints will be dealt with in a
section below ([\[Feature specifications\]](#Feature%20specifications)
on page ).

A list of features can be given in the `feature_retrieval` clause. Their
values for a given object are placed on the list of features in the
matched\_object in the sheaf.

The inner `blocks` syntactic non-terminal allows the writer of MQL
queries the possibility of matching objects nested inside objects.
Example 5 above shows several examples of this. Example 5 finds those
clauses which have inside them first a phrase which is a Subject NP,
then followed by a Phrase which is a VP, the first word inside of which
is a verb, followed by an Object NP. Thus we have an object block
(“Clause”) with an inner `blocks` (“NP followed by VP”), where inside
the VP we have another `blocks` (V followed by NP).

The inner blocks, if present, must match if the object block is to
match. When entering the inner `blocks`, the Substrate for that `blocks`
becomes the monads of the enclosing object. Let us call that object O.
The Universe for the inner `blocks` becomes the set of monads between
and including the borders of the enclosing object (see section
[\[borders, first, last\]](#borders,%20first,%20last) on page ), i.e.,
the stretch of monads between (and including) O.first and O.last. This
is the same as the substrate, except with any gaps filled in.

If you want any objects or gaps inside the object block to be retrieved,
then the retrieval of the enclosing object block must be either retrieve
or focus. Since the default retrieval for object blocks is to retrieve
them, this condition is satisfied if you write nothing for the
retrieval.

An object, if it is to match against a given object block, must meet all
of the following criteria:

1.  The first/last constraints must be met.

2.  The operation (“part\_of” or “overlap”) of the
    monad\_set\_relation\_clause must be true on the given monad set and
    the Substrate or Universe.

3.  The feature constraints must hold. See section [\[Feature
    specifications\]](#Feature%20specifications) on page for details.

4.  The inner blocks must not return a failed sheaf.

You can optionally place the keyword “NOTEXIST” before the object block.
This will result in matching those cases where the object block does not
occur, and will result in a failed match where the object block does
occur. This is most useful if you have some context, i.e., a surrounding
context (e.g., a sentence which does not contain such and such a word,
see example 6 above). You are allowed to have blocks before and after a
NOTEXIST block. Let us say that there is a block before the NOTEXIST
block. Then the Substrate within which the NOTEXIST block will be
matched is the Substrate of the context, minus the monads from the
beginning of the Substrate to the end of the MatchedObject matching the
previous block. The Universe of the NOTEXIST block will be defined
analogously on the Universe of the context.

The NOTEXIST block will have “zero width” with respect to
consecutiveness: If it matches anything, the entire block\_string fails.
If it does not match, it is as though the NOTEXIST block had not been
there, and any block after the NOTEXIST block will be attempted matched
starting at the previous block’s last monad plus 1.

The NOTEXIST keyword acts as an “upwards export barrier” of object
reference declarations. That is, you cannot “see” an object reference
declaration outside of the NOTEXIST, only inside of
it.

## Gap blocks<span id="Gap blocks" label="Gap blocks">\[Gap blocks\]

### Introduction

Gap blocks are used to match gaps in the substrate we are currently
matching against. There are two kinds of blocks: plain gap blocks and
optional gap blocks.

We start by defining the syntax related to gap blocks. We then give some
examples of gap blocks. And finally, we provide some explanation.

# Syntax

```

gap\_block : “\[”   “GAP”   

                  \[ marks\_declaration \]

                  \[ gap\_retrieval \]   

                  \[ blocks \]   

            “\]”

;

opt\_gap\_block : “\[”   “GAP?”   

                      \[ marks\_declaration \]

                      \[ gap\_retrieval \]   

                      \[ blocks \]  

                “\]” 

;

marks\_declaration : T\_MARKS

;

gap\_retrieval : “NORETRIEVE”

              | “RETRIEVE”

              | “FOCUS”

;

```

# Examples

```

1. \[gap\]   
   
2. \[gap?\]   
   
3. \[gap noretrieve\]   
   
4. \[gap?‘yellow focus\]   
   
5. \[gap‘context‘red retrieve

     \[Word retrieve

       psp = particle

     \]

   \]   
   
6. \[gap‘yellow

   \]

```

# Explanation

There are two differences between the two types of gap block: One is
that the `gap_block` *must* match a gap in the substrate for the whole
query to match, while the `opt_gap_block` *may* (but need not) match a
gap in the substrate. The other is that the default retrieval of an
opt\_gap\_block is NORETRIEVE, whereas the default retrieval of a
gap\_block is RETRIEVE. Otherwise, they are identical in semantics.

The retrieval will be dealt with more fully in the next section.

The inner `blocks`, if present, must match if the gap block is to match.
When trying to match the inner `blocks`, both the Universe and the
Substrate are set to the monads of the gap. So if the gap matches the
monad-stretch \([a..b]\), then both the Universe and the Substrate for
the inner `blocks` will be this stretch of monads.

The last point is important in example 5. Here the Word which we are
looking for inside the gap will be looked for within the monads which
made up the gap.

If you want any objects or gaps to be retrieved inside the gap (as in
example 5 above, where we want to retrieve the Word), then the retrieval
of the gap block must be either “retrieve” or “focus”.

You can optionally specify a T\_MARKS after the `gap` or `gap?` keyword.
If you do, the MatchedObjects that arise because of this
(opt\_)gap\_block will contain the same T\_MARKS as you specified here.
The query-writer can use it to pass information back into the
application that sits on top of Emdros. Emdros does nothing special with
the T\_MARKS, other than passing it on into the sheaf, that is, into the
matched\_object that arises because of the (opt\_)gap\_block. In
particular, there is no semantics associated with the
marks\_declaration. See page for the formal definition of T\_MARKS.

## Power block

# Syntax

```

power : “..”   \[ restrictor \]

;

restrictor : “\<” limit 

           | “\<=” limit

           | “BETWEEN” limit “AND” limit

;

limit : T\_INTEGER /\* non-negative integer, may be 0. \*/

; 

```

# Examples

```

1. \[Word\]   
   
2. \[Word psp=article\]

   \[Word psp=noun\]

   .. \<= 5

   \[Word psp=verb\]   
   
3. \[Phrase phrase\_type = NP\]

   ..

   \[Phrase phrase\_type = AdvP\]

   .. BETWEEN 1 AND 5

   \[Phrase phrase\_type = VP\]   
   
4. \[Chapter

     topic = Noun classes in Bantu

   \]

   \[Chapter 

     topic = Causatives in Setswana

   \]

   ..

   \[Chapter

     topic = Verb-forms in Sesotho

   \]

```

### power

The power block means “before the start of the next block, there must
come a stretch of monads of arbitrary length, which can also be no
monads (0 length)”. In its basic form, it is simply two dots, “`..`”.

The stretch of monads is calculated from the monad after the last monad
of the previous block. If the previous block ended at monad 7, then the
power block starts counting monads from monad 8.

One can optionally place a `restrictor` after the two dots, thus making
the power block look like this, e.g., “`.. < 5`”, “`.. <= 5`”, or “`..
BETWEEN 1 AND 5`”.

The first two kinds of restrictor mean “although the stretch of monads
is of arbitrary length, the length must be less than (or equal to) the
number of monads given in the restrictor”. Thus “`.. < 5`” means “from 0
to 4 monads after the end of the previous block”, and “`.. <= 5`” means
“from 0 to 5 monads after the end of the previous block”. That is, if
the previous block ended at monad 7, then “`.. < 5`” means “the next
block must start within the monads 8 to 12”, while “`.. <= 5`” means
“the next block must start within the monads 8 to 13”.

Similarly, the third kind, “`.. BETWEEN` `min` `AND` `max`” means “there
must be at least `min` monads in between, and at most `max` monads. This
is construed as “`>=` `min` `AND <=` `max`”.

## Retrieval<span id="Retrieval" label="Retrieval">\[Retrieval\]

### Introduction

Retrieval is used in four places in the MQL grammar. Once for each of
the two object blocks and once for each of the two gap blocks. In this
section we describe the three kinds of retrieval, specify the default
behavior, and provide a bit of explanation.

# Syntax

```

retrieval : “NORETRIEVE”

          | “RETRIEVE”

          | “FOCUS”

;

gap\_retrieval : “NORETRIEVE”

              | “RETRIEVE”

              | “FOCUS”

;

```

# Examples

```

1. \[Word focus

     psp = verb

   \]   
   
2. \[gap? retrieve\]   
   
3. \[Phrase noretrieve\]   
   
4. \[gap focus\]   
   
5. \[Phrase retrieve

     \[Word focus

       psp = article

     \]

     \[gap retrieve

       \[Word focus

         psp=conjunction

       \]

     \]

     \[Word focus

       psp = noun

     \]

   \]

```

# Explanation

Retrieval has to do with two domains pertaining to objects and gaps:

1.  Whether to retrieve the objects or gaps, and

2.  Whether those objects or gaps should be in *focus*.

Whether to retrieve is straightforward to understand. If we don’t
retrieve, then the object or gap doesn’t get into the sheaf. The sheaf
is the data-structure returned by an MQL query. The object or gap (if
the gap is not optional) must still match for the overall match to be
successful, but the object or gap won’t get into the sheaf if we don’t
retrieve.

When an object is in focus, that means your application has the
opportunity to filter this object out specifically from among all the
objects retrieved. Exactly how this feature is used (or not used) will
depend on your application. When is this useful?

Recall that, for objects in an inner `blocks` to be retrieved (in an
object block or a gap block), the enclosing object or gap must also be
retrieved. Thus you might end up with objects in the sheaf which you
don’t really care about. The focus-modifier is a way of signaling
special interest in certain objects or gaps. Thus you can specify
exactly which objects should be of special interest to the application.
In example 5 above,\[6\] the outer Phrase must be retrieved, because we
wish to retrieve the inner objects and gaps. The inner gap must also be
retrieved because we wish to retrieve the inner Word. The three Words
are what we are really interested in, however, so we mark their
retrieval as “focus”.

If we specify “focus” as the retrieval, then that implies “retrieve”.
Thus we can’t not retrieve an object which is in “focus”. This makes
sense. If you have registered a special interest in an object, that
means you want to retrieve it as well.

The default for object blocks of both kinds, when no retrieval is
specified, is to assume “retrieve”. The default for gap blocks of both
kinds, on the other hand, is
“noretrieve”.

## First and last<span id="First and last" label="First and last">\[First and last\]

### Introduction

The object blocks have the option of specifying whether they should be
first and/or last in their enclosing `blocks`.

# Syntax

```

firstlast : “FIRST”

          | “LAST”

          | “FIRST”   “AND”   “LAST”

;

```

# Examples

```

1. \[Clause first and last\]   
   
2. \[Phrase first\]   
   
3. \[Clause

     \[Phrase first\]

     \[Word last

       psp = verb

     \]

   \]

```

# Explanation

In example 1, the clause must be both first and last in its surrounding
`blocks`. In the second example, the phrase must merely be the first. In
the third example, the Phrase must be first in the clause, followed by a
word, which must be a verb, and which must be last. This can be
realized, e.g., in verb-final languages.

What does it mean to be “first” and “last” in the enclosing `blocks`?

Again we must appeal to the notion of Universe and Substrate. Each
`blocks` carries with it a Universe and a Substrate. Let us say that an
object block must be first, and let us say that we are trying to match
an object O against this object block. Let us call the substrate of the
enclosing blocks “Su”. Then, for the object O to be first in the blocks
means that O.first = Su.first. That is, the first monad of the object
must be the same as the first monad of the Substrate.

Conversely, for an object O to be last in a blocks, means that O.last =
Su.last. That is, the last monad of the object must be the same as the
last monad of the
Substrate.

## Feature constraints<span id="Feature specifications" label="Feature specifications">\[Feature specifications\]

### Introduction

Object blocks can optionally have feature constraints. The feature
constraints are boolean (i.e., logical) expressions whose basic boolean
building-blocks are “and”, “or”, and “not”. The things that are related
logically are comparisons of features and values, i.e., a feature
followed by a comparison-symbol (e.g., “=”), followed by a value.
Parentheses are allowed to make groupings explicit.

In the following, we first define the syntax of feature constraints. We
then make refer to other parts of this manual for details of certain
non-terminals. We then give some examples, followed by explanations of
those examples. We then give some explanation and elucidation on
feature-constraints. We then describe the constraints on
type-compatibility between the feature and the value. Finally we
elaborate on
comparison-operators.

# Syntax

```

feature\_constraints  : ffeatures 

;

ffeatures : fterm 

          |  ffeatures   “OR”   fterm 

;

fterm : ffactor

      | ffactor   “AND”   fterm 

;

ffactor : “NOT”   ffactor

        | “(”   ffeatures   “)”

        | feature\_comparison 

;

feature\_comparison : 

    feature\_name  comparison\_operator   value

  | feature\_name  “IN”   enum\_const\_set

  | feature\_name  “IN”   “(“  list\_of\_integer  “)”

  | feature\_name  “IN”   object\_reference\_usage

;

comparison\_operator : “=”

                    | “\<”

                    | “\>”

                    | “\<\>”  /\* not equal \*/

                    | “\<=”  /\* less than or equal \*/

                    | “\>=”  /\* greater than or equal \*/

                    | “~”   /\* regular expression \*/

                    | “\!~”  /\* inverted regular expression \*/

                    | “HAS” /\* lhs: list; rhs: atomic value.

                                 signifies list membership. \*/

;

list\_of\_integer : T\_INTEGER  { “,” T\_INTEGER }\*

;

value : enum\_const

      | signed\_integer

      | T\_STRING

      | object\_reference\_usage

;

enum\_const : T\_IDENTIFIER

;

object\_reference\_usage : object\_reference   

                         “.”   feature\_name 

;

enum\_const\_set : “(“ enum\_const\_list “)”

;

enum\_const\_list : enum\_const { “,” enum\_const\_list }

;

```

# Examples

```

1. \[Word psp = noun\]   
   
2. \[Word gender = neut or gender = fem\]   
   
3. \[Word psp = adjective and not case = nominative\]   
   
4. \[Phrase (phrase\_type = NP

            and phrase\_determination = indetermined)

           or phrase\_type = AP

   \]   
   
5. \[Word as w

     psp = article

   \]

   \[Word

     psp = noun 

     and case = w.case

     and gender = w.gender

     and number = w.number

   \]   
   
6. \[Word

     surface \> Aa and surface ~ A-D\]orkin

   \]   
   
7. \[Word psp IN (verb, participle, infinitive)\]   
   
8. \[Word psp = verb OR psp = participle OR psp = infinitive\]

```

# Explanation of Examples

Example 1 above is the simple case where a feature (“psp”) is being
tested for equality with a value (“noun”). Example 2 is more of the
same, except the gender can either be neuter or feminine, and the
feature constraint would match in both cases. Example 3 finds those
words which are adjectives *and* whose case is *not* nominative. Example
4 finds either adjectival phrases or NPs which are indetermined.

Example 5 is an example of usage of object references. The first Word is
given the “label” (or “object reference”) “w”. Then the second Word’s
feature-constraints refer to the values of the features of the first
Word, in this case making sure that case, number, and gender are the
same.

Example 6 is an example of two different comparison-operators,
“greater-than” and “regular expression-match”.

Example 7 shows the comparison IN. It takes a comma-separated list of
enumeration constant names in parentheses as its right-hand-side. The
effect is the same as an OR-separated list of “=” feature-comparisons.
So 7. and 8. are equilalent.

# Explanation

While the syntax may look daunting to the uninitiated, the system is
quite straightforward. At the bottom, we have feature comparisons. These
consist of a feature, followed by a comparison-operator (such as “=”),
followed by a value. These feature-comparisons can be joined by the
three standard boolean operators “and”, “or”, and “not”.

The precedence of the operators follows standard practice, i.e., “not”
has highest precedence, followed by “and”, followed by “or”. Parentheses
are allowed to make groupings explicit. That is, “and” “binds” more
closely than “or” so that the interpretation of this expression:

\smallskip{}

f\_1 = val\_1 “and” f\_2 = val\_2 “or” f\_3 = val\_3

\smallskip{}

is the following:

\smallskip{}

(f\_1 = val\_1 “and” f\_2 = val\_2) “or” f\_3 = val\_3

\smallskip{}

Note that if you use “not” on a feature comparison, and if you have
another feature comparison before it, then you must explicitly state
whether the relationship between the two is “and” or “or”. Thus the
following is illegal:

\smallskip{}

f\_1 = val\_1 “not” f\_2 = val\_2

\smallskip{}

The following, however, would be legal:

\smallskip{}

f\_1 = val\_1 “and” “not” f\_2 = val\_2

\smallskip{}

The “in” comparison-operator can only be used with a comma-separated
list of enumeration constant names on the right-hand-side. The effect is
the same as if all of the enumeration constants had been compared “=” to
the feature, with “OR” between them.

### Type-compatibility

The feature and the value with which we compare both have a *type*. The
type is, one of “integer”, “7-bit (ASCII) string”, “8-bit string”,
“enumeration constant”, “id\_d”. Thus a type tells us how to interpret
a value.

The types of the two values being compared must be *compatible*. Table
[\[Table:
Type-compatibility-constraints\]](#Table:%20Type-compatibility-constraints)
summarizes the
type-compatibility-constraints.

| If value’s type is...       | Then feature’s type must be...              |
| :-------------------------- | :------------------------------------------ |
| enumeration constant        | The same enumeration as the value           |
| (enumeration constant-list) | The same enumeration as all the values      |
| signed\_integer             | integer or id\_d                            |
| 7-bit or 8-bit string       | 7-bit or 8-bit string                       |
| object reference usage      | The same type as the feature in the object  |
|                             | reference usage, or a list of the same type |

Type-compatibility-constraints<span id="Table: Type-compatibility-constraints" label="Table: Type-compatibility-constraints">\[Table:
Type-compatibility-constraints\]

The 8-bit strings need not be of the same encoding.

### Comparison-operators

Table [\[Table: Comparison-operators\]](#Table:%20Comparison-operators)
summarizes the
comparison-operators.

| op.  | meaning                                                                             |
| :--: | :---------------------------------------------------------------------------------- |
|  \=  | Equality                                                                            |
|  \<  | Less-than                                                                           |
|  \>  | Greater-than                                                                        |
| \<\> | Inequality (different from)                                                         |
| \<=  | Less-than-or-equal-to                                                               |
| \>=  | Greater-than-or-equal-to                                                            |
|  ~   | Regular expression-match                                                            |
| \!~  | Negated regular-expression-match                                                    |
|  IN  | Member of a list of enum constants                                                  |
| HAS  | List on left-hand-side, atomic value on right-hand-side. Signifies list membership. |

Comparison-operators<span id="Table: Comparison-operators" label="Table: Comparison-operators">\[Table:
Comparison-operators\]

#### Inequality

The inequality-operator “\<\>” is logically equivalent to “not ... =
...”. The negated regular-expression-match “\!~” is logically
equivalent to “not ... ~ ...”.

#### Equality

Equality is defined as follows: If the type is id\_d, then both must be
the same id\_d. If the type is integer, then both must be the same
number. If the type is string, then both must be byte-for-byte
identical, and of the same length. If the type is enumeration, then both
must have the same numerical value. That is, the enumeration constants
must be the same, since an enumeration is a one-to-one correspondence
between a set of labels and a set of values. If the type is a list, the
two lists must be identical, i.e., consist of the same sequence of
values.

#### Less-than/greater-than

The four less-than/greater-than-operators use 8-bit scalar values for
the comparison of strings. That is, it is the numerical value of the
bytes in the strings that determine the comparison. In particular, the
locale is not taken into consideration. For comparison of id\_ds, the
id\_ds are treated as ordinary numbers, with nil being lower than
everything else. For comparison of integers, the usual rules apply. For
comparison of enumeration constants, it is the values of the enumeration
constants that are compared, as
integers.

#### Regular expressions<span id="par:Regular-expressions" label="par:Regular-expressions">\[par:Regular-expressions\]

There are two regular expression-comparison-operators (“~” and “\!~”).
They operate on 8-bit strings. That is, both the feature-type and the
value against which the match is made must be 8-bit strings. The negated
match matches everything that does not match the regular expression
provided as the value.

The value that they are matched against must be a string.

The regular expressions are the same as in Perl 5. See section
[\[PCRE\]](#PCRE) on page for details of where regular
expression-support comes from. See `http://www.perl.com/` for details of
Perl regular expressions.

Before version 1.2.0.pre46, regular expressions were anchored, meaning
that they always started matching at the start of the string. As of
1.2.0.pre46, regular expressions are not anchored, meaning that they can
start their match anywhere in the string.

#### IN

The IN comparison operator must have:

1.  either an enumeration feature on the left hand side and a
    comma-separated list of enumeration constants in parentheses on the
    right-hand-side (or an object refence usage resolving to a
    list-of-enum-constants of the same type),

2.  or an INTEGER feature on the left hand side, and a list of integers
    on the right-hand-side (or an object reference usage resolving to
    this),

3.  or an ID\_D feature on the left hand side, and a list of integers on
    the right-hand-side (or an object reference usage resolving to a
    list of ID\_Ds).

For the first case, all of the enumeration constants must belong to the
enumeration of the feature. The meaning is “feature must be in this
list”, and is equivalent to a string of “=” comparisons with “OR” in
between, and with parentheses around the string of OR-separated
comparisons.

For the second and third cases, the meaning is the same, but applied to
integers and id\_ds respectively.

#### HAS

The HAS comparison operator must have:

1.  Either a list-of-enumeration constant on the left hand side and an
    enumeration constant belonging to the same enumeration on the left
    hand side (or an object reference usage resolving to this),

2.  or a list-of-INTEGER feature on the left hand side, and an atomic
    integer value the right-hand-side (or an object reference usage
    resolving to this),

3.  or a list-of-ID\_D feature on the left hand side, and an atomic
    id\_d value on the right-hand-side (or an object reference usage
    resolving to this).

This signifies list-membership of the right-hand-side in the list on the
left-hand-side.

## Object references<span id="Object references" label="Object references">\[Object references\]

### Introduction

Object references are a way of referring to objects in a query outside
of the object block which they matched. This provides the possibility of
matching objects on the basis of the features of other objects earlier
in the query.

In this subsection, we first give the syntax of object references, their
declaration and their usage. We then provide some examples, followed by
an explanation of those examples. We then give some explanation of
object references. Finally, we document some constraints that exist on
object references.

# Syntax

```

object\_reference\_declaration : “AS” object\_reference 

;

object\_reference : T\_IDENTIFIER 

;

object\_reference\_usage : object\_reference   

                         “.”   feature\_name 

;

feature\_name : T\_IDENTIFIER

;

```

# Examples

```

1. \[Clause

     \[Phrase as p

       phrase = NP

     \]

     ..

     \[Phrase

       phrase = AP 

       and case = p.case 

       and number = p.number

       and gender = p.gender

     \]

   \]   
   
2. \[Clause as C

     \[Phrase

       phrase\_type = NP

       parent = C.self

     \]

   \]   
   
3. \[Sentence as S\]

   ..

   \[Sentence 

     head = S.self

   \]

```

# Explanation of examples

Example 1 finds, within a clause, first an NP, followed by an arbitrary
stretch of text, followed by an AP. The AP’s case, number, and
gender-features must be the same as the NP’s case, number, and
gender-features respectively.

Example 2 finds a clause, and within the clause an NP which is a direct
constituent of the clause. That is, its parent feature is an id\_d which
points to its parent in the tree. This id\_d must be the same as the
clause’s “self” feature. See section [\[self\]](#self) on page for more
information about the “self” feature.

Example 3 finds a sentence and calls it S. Then follows an arbitrary
stretch of text. Then follows another sentence whose head feature is an
id\_d which points to the first sentence. That is, the second sentence
is dependent upon the first sentence.

# Explanation

The `object_reference_declaration` non-terminal is invoked from the
object blocks, right after the object type name. That is, the
`object_reference_declaration` must be the first item after the object
type name, if it is to be there at all, as in all of the examples above.
The object reference declaration says that the object that matched this
object block must be called whatever the `object_reference` is (e.g.,
“p”, “C”, and “S” in the examples above). Then object blocks later
in the query can refer to this object’s features on the right-hand-side
of feature comparisons. See section [\[Feature
specifications\]](#Feature%20specifications) on page for details of
feature-comparisons.

The `object_reference_usage` non-terminal shows up on the
right-hand-side of feature comparisons, as in the examples above. It
consists of an object reference followed by a dot followed by a feature
name.

### Constraints on object references

The following are the constraints on object references:

  - Object references must be declared before they can be used. That is,
    they must appear in an `object_reference_declaration` earlier in the
    query (i.e., further towards the top).

  - The feature name on an object reference usage must be a feature of
    the object type of the object that had the corresponding object
    reference declaration.

  - The feature type of the object reference usage must be the same as
    the feature type of the feature with which it is compared (not just
    compatible with).

  - An object reference must only be declared once in a query. That is,
    no two object references must have the same name.

  - A “Kleene Star” construct (see Section
    [\[Block:KleeneStar(\*)\]](#Block:KleeneStar\(*\)))
    acts as an “export barrier” upwards in the tree for object reference
    declarations. Thus any object reference usages which are separated
    from the object reference declaration by a Kleene Star cannot be
    “seen”. For example, this is not
allowed:

```

\[Clause

   \[Phrase

      \[Word as w1\]

   \]\* // Kleene Star acts as an export barrier\!

   \[Word surface=w1.surface\] // So we can’t see the declaration here...

\]

```

  - You also cannot have an object reference declaration on an object
    block that itself bears the Kleene Star. Thus this is not
allowed:

```

\[Clause

   \[Phrase as p1\]\* // This is NOT allowed\!

   \[Phrase function=p1.function\]

\]

```

  - It is not allowed to have an object reference declaration that is
    used “above” an OR. That is, all object reference declarations and
    usages should be within the same block\_string2 (see Section
    [\[block\_string\]](#block_string) and Section
    [\[Block strings: block\_str's\]](#Block%20strings:%20block_str's)).
    “OR” acts as an “export barrier” on object reference declarations,
    not allowing them to be “seen” beyond the “OR”. Thus this is *not*
    allowed:

```

\[Phrase as p1\]

OR

\[Phrase function=p1.function\] // Oops\! Can’t see declaration from here\!

 

<span class="roman">Whereas this <span class="roman">*is*
<span class="roman">allowed:

\[Phrase as p1 

   \[Phrase function=p1.function\] // This is OK

   OR

   \[Phrase function\<\>p1.function\] // This is also OK

\]

 

<span class="roman">The reason the second is allowed but the first is
not is that it is the object reference
<span class="roman">*declaration* <span class="roman">which is
under embargo above (not below) an OR, whereas the object
reference <span class="roman">*usage*
<span class="roman">is free to see an object reference
<span class="roman">*declaration* <span class="roman">that has
been declared above an
OR.

```

## Block<span id="Blocks: block" label="Blocks: block">\[Blocks: block\]

### Introduction

The non-terminal `block` is a choice between three kinds of block:
`opt_gap_block`s, `gap_block`s, and `object_block`s. It is used in the
grammar of MQL queries in the definition of `block_string`s, that is, in
when defining strings of blocks. See section [\[Block strings:
block\_str's\]](#Block%20strings:%20block_str's) on page for more
information on
`block_string`s.

# Syntax

```

block : opt\_gap\_block 

      | gap\_block 

      | power

      | object\_block

      | (“NOTEXIST” | “NOTEXISTS”) object\_block

;

```

# Strings of blocks<span id="sec:Strings-of-blocks" label="sec:Strings-of-blocks">\[sec:Strings-of-blocks\]

## Introduction

Having now described all the syntax and semantics of individual blocks,
we now go on to giving the bigger picture of MQL queries. This section
describes strings of blocks, as well as the higher-level non-terminals
in the MQL query-query subset.

We first describe the `topograph`, the top-level entry-point into the
MQL query-query grammar ([\[topograph\]](#topograph)). We then describe
the `blocks` non-terminal, which shows up inside each of the three kinds
of blocks as an inner `blocks` ([\[Block strings:
blocks\]](#Block%20strings:%20blocks)). We then describe the `block_str`
non-terminal, which provides for strings of blocks optionally connected
by power blocks (the “`..`” blocks which have been exemplified
previously, and which mean “an arbitrary stretch of space”) ([\[Block
strings: block\_str's\]](#Block%20strings:%20block_str's)).

## topograph<span id="topograph" label="topograph">\[topograph\]

### Introduction

The `topograph` non-terminal is the entry-point for the MQL query-query
subset.\[7\] It simply consists of a `blocks` non-terminal. The
topograph passes on a Universe and a Substrate to the `blocks`
non-terminal, and these will be described below.

# Syntax

```

topograph : blocks 

;

```

# Examples

```

1. \[Word\]   
   
2. \[Word psp=article\]

   \[Word psp=noun\]   
   
3. \[Clause

     \[Phrase phrase\_type = NP\]

     ..

     \[Phrase phrase\_type = VP\]

   \]   
   
4. \[Book

     title = Moby Dick

     \[Chapter chapter\_no = 3

       \[Paragraph

         \[Word surface = Ishmael

       \]

       ..

       \[Paragraph

         \[Word surface = whaling

       \]

     \]

   \]

```

# Explanation of examples

Example 1 simply finds all words within the topograph’s Universe and
Substrate.

Example 2 finds all pairs of adjacent words in which the first word is
an article and the second word is a noun, within the topograph’s
Universe and Substrate.

Example 3 finds all clauses within which there are pairs of first an NP,
followed by an arbitrary stretch of monads, then a VP. Within the
topograph’s Universe and Substrate, of course.

Example 4 finds a book whose title is “Moby Dick”, and within the book
it finds chapter 3, and within this chapter it finds a Paragraph within
which there is a word whose surface is “Ishmael”. Then, still within the
chapter, after an arbitrary stretch of monads, it finds a Paragraph
within which there is a word whose surface is “whaling”.

### Universe and Substrate

In order to understand how the Universe and Substrate are calculated, it
is necessary to refer back to the definition of the SELECT OBJECTS
query. Please consult section [\[SELECT OBJECTS:
Explanation\]](#SELECT%20OBJECTS:%20Explanation) on page for
details.

## blocks<span id="Block strings: blocks" label="Block strings: blocks">\[Block strings: blocks\]

### Introduction

The `blocks` non-terminal is central in the MQL query-query subset. It
shows up in five places:

  - In the `topograph`,

  - Inside the `object_block` as the inner `blocks`,

  - Inside the `gap_block` and the `opt_gap_block` as the inner
    `blocks`.

# Syntax

```

blocks : block\_string

;

```

## block\_string<span id="block_string" label="block_string">\[block\_string\]

### Introduction

A “block\_string” is basically either a “block\_string2” or it is a
block\_string2 followed by the keyword “OR” followed by another
block\_string. Or, put another way, a block\_string is a string
(possibly 1 long) or block\_string2’s, separated by
“OR”.

# Syntax

```

block\_string : block\_string2 

             | block\_string2 “OR” block\_string

;

block\_string2 : block\_string1

              | block\_string1 block\_string2

              | block\_string1 “\!” block\_string2

;

block\_string1 : block\_string0

              | block\_string0 “\*” \[monad\_set\]

;

block\_string0 : block

              | “\[“ block\_string “\]”

;

```

# Examples

```

1. \[Clause

      \[Phrase function = Predicate\]  // This...

      \[Phrase function = Objc\]       // ... is a block\_string2

      OR

      \[Phrase function = Predicate\]  // And this...

      \[Phrase function = Complement\] // is another block\_string2

   \]

2. \[Sentence

      \[gap \[Clause function = relative\] // This is a block\_string2

      OR

      \[Clause AS c1 function = Subject\] // And this...

      ..                                // ... is also ...

      \[Clause daughter = c1.self\]       // ... a block\_string2

   \]

```

# Explanation

Block\_strings are recursive in that the lowest level (Block\_string0)
can be either a Block, or a full BlockString in \[square
brackets\].

Notice that Kleene Star (\*) binds more tightly than
concatenation. Thus if you wish to use Kleene Star with more than one
block, you must wrap those blocks in a \[square bracket
group\].

Notice also that OR binds less tightly than concatenation. Thus OR works
between strings of blocks.

The first example finds all clauses in which it is either the case that
there exist two phrases inside the clause where the first is a predicate
and right next to it is an object, or the first is a predicate and right
next to it is a complement (or both might be true, in which case you’ll
get two straws inside the inner sheaf of the clause).

The second example finds all clauses in which it is the case that there
either is a gap with a relative clause inside it, or there are two
clauses (possibly separated) where the first clause is a subject in the
second. (This assumes a data model where mother clauses do not include
the monads of their daughter clauses).

See Section [\[Object references\]](#Object%20references) for some
restrictions on object references regarding
OR.

### The “\*” construct<span id="Block:KleeneStar(*)" label="Block:KleeneStar(*)">\[Block:KleeneStar(\*)\]

The “\*” construct is a so-called “Kleene Star”. It allows
searching for object blocks or groups that are repeated. It has two
forms: One with and one without a trailing set of integers (with the
same syntax as a set of monads). For
example:

```

SELECT ALL OBJECTS 

WHERE

\[Sentence 

  \[Phrase FIRST phrase\_type = NP\] 

  \[Phrase phrase\_type IN (VP, NP, AP)\]\* 

  \[Phrase function = adjunct\]\* {1-3} 

\] 

GO

```

This finds sentences whose first phrase is an NP, followed by
arbitrarily many phrases which can either be VPs, NPs, or APs (or any
combination of those), followed by between 1 and 3 phrases whose
function is adjunct.

A less contrived
example:

```

SELECT ALL OBJECTS

WHERE 

\[Sentence 

  \[Word psp=verb\] 

  \[Word psp=article or psp=noun 

        or psp=adjective or psp=conjunction\]\*{1-5} 

\] 

GO

```

This finds sentences where there exists a word whose part of speech is
verb, followed by 1 to 5 words whose parts of speech may be article,
noun, adjective, or conjunction (or any combination of those).
Presumably this would (in English) be a VP with (parts of) the object NP
after the verb.

The Kleene-Star without a trailing set of integers means from 0 to
MAX\_MONADS. Note, however, that there is no performance penalty
involved in such a large end: The algorithm stops looking when getting
getting one more fails.

If 0 is in the set of integers, then this means that the object need not
be there. This means that the
following:

```

SELECT ALL OBJECTS 

WHERE 

\[Sentence 

  \[Word psp=verb\] 

  \[Word psp=article\]\*{0-1} 

  \[Word psp=noun\] 

\] 

GO

```

would find sentences where there exists a verb followed by 0 or 1
articles followed by a noun. Thus the case of verb immediately followed
by noun would also be found by this query. Thus the
{0-1} is equivalent to ? in regular
expressions.

The set of integers has the same syntax as monad sets. Therefore, to
obtain a “no upper bound” star-construct, use
{\<lower-bound\>-}, e.g.,
{10-} to mean “from 10 times to
(practically) infinitely many times.”

The following restrictions apply:

  - You cannot have a Kleene Star on an object block which also has the
    `NOTEXIST` keyword in front.

  - You cannot have a Kleene Star on an object block which has the
    `“noretrieve`” keyword.

```

```

### The bang (“\!”)

You can optionally place a bang (“`!`”) between any of the `block`s in a
`block_string2`. The bang indicates that there must be no gaps between
the two blocks. It is an implicit rule of MQL that there is a hidden
`opt_gap_block` between each pair of `block`s in a `block_string` which
are not mediated by a bang.

The reason for having the `opt_gap_block` is the following: It protects
you from what you do not know. In some languages, there can be gaps in
clauses because of post-positive conjunctions “sticking out” at a higher
level. One would not wish to have to specify all the time that one
wanted to look for gaps, for one would invariably forget it sometimes,
thus not getting all the results available. Thus MQL inserts an
`opt_gap_block` between each pair of blocks that are not mediated by a
bang. The bang is a way of specifying that one does not wish the hidden
`opt_gap_block` to be inserted.

The `opt_gap_block` that is inserted is not retrieved.

\appendix

# Copying

# Introduction

Emdros is covered by two different licenses, both of which allow you
freely to copy, use, and modify the sourcecode. The parts which were
written by Ulrik Sandborg-Petersen are covered by the MIT License. The
pcre library, which provides regular expressions-capabilities, is
covered by a different license. Some parts were contributed by Kirk E.
Lowery, Martin Korshøj Petersen, or Claus Tøndering; they are Copyright
Sandborg-Petersen Holding ApS and are also under the MIT.

SQLite is in the Public Domain. See `www.sqlite.org` for details.

All Emdros documentation (including this document) is covered under the
Creative Commons Attribution-Sharealike license version 4.0. Please see
the Creative Commons website for the details.

# MIT License

MIT
License

```

Copyright (C) 1999-2018 Ulrik Sandborg-Petersen

Copyright (C) 2018-present Sandborg-Petersen Holding ApS

Permission is hereby granted, free of charge, to any person obtaining

a copy of this software and associated documentation files (the

Software), to deal in the Software without restriction, including

without limitation the rights to use, copy, modify, merge, publish,

distribute, sublicense, and/or sell copies of the Software, and to

permit persons to whom the Software is furnished to do so, subject to

the following conditions:

The above copyright notice and this permission notice shall be

included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED AS IS, WITHOUT WARRANTY OF ANY KIND,

EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF

MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND

NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE

LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION

OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION

WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

```

# PCRE license<span id="sec:PCRE-license" label="sec:PCRE-license">\[sec:PCRE-license\]

PCRE is a library of functions to support regular expressions whose
syntax and semantics are as close as possible to those of the Perl 5
language.

Release 6 of PCRE is distributed under the terms of the BSD licence, as
specified below. The documentation for PCRE, supplied in the doc
directory, is distributed under the same terms as the software itself.

The basic library functions are written in C and are freestanding. Also
included in the distribution is a set of C++ wrapper functions.

## THE BASIC LIBRARY FUNCTIONS

Written by: Philip Hazel

Email local part: ph10

Email domain: cam.ac.uk

University of Cambridge Computing Service,

Cambridge, England. Phone: +44 1223 334714.

Copyright (c) 1997-2006 University of Cambridge

All rights reserved.

## THE C++ WRAPPER FUNCTIONS

Contributed by: Google Inc.

Copyright (c) 2006, Google Inc. All rights reserved.

## The “BSD” license

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

  - Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer.

  - Redistributions in binary form must reproduce the above copyright
    notice, this list of conditions and the following disclaimer in the
    documentation and/or other materials provided with the distribution.

  - Neither the name of the University of Cambridge nor the name of
    Google Inc. nor the names of their contributors may be used to
    endorse or promote products derived from this software without
    specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS AS
IS AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH
DAMAGE.

```

```

# Console sheaf grammar<span id="Appendix:Console-sheaf-grammar" label="Appendix:Console-sheaf-grammar">\[Appendix:Console-sheaf-grammar\]

# Introduction

The sheaf’s contents were explained in section [\[sheaf\]](/mql/topographic/preliminaries/sheaf/). In
this appendix, we give the grammar for the sheaf as it is output with
console output (as opposed to XML
output).

# Sheaf grammar

```

/\* Sheaf \*/

sheaf : failed\_sheaf | successful\_sheaf

;   
failed\_sheaf : “//”  /\* A failed sheaf means 

                          that the query failed

                          in some way. \*/

;   
successful\_sheaf : “//” straws /\* A successful sheaf

                                    means that the query

                                    did not fail. It may

                                    however, be empty,

                                    in which case the

                                    list\_of\_straws will

                                    not be there, and the

                                    sheaf will look like

                                    this: “// \< \>”.

                                 \*/

;   
straws : “\<” list\_of\_straws “\>”

;   
list\_of\_straws : { straw }

;   
   
/\* Straw \*/

straw : “\<” list\_of\_matched\_objects “\>”

;   
list\_of\_matched\_objects : { matched\_object }

;   
/\* Matched object \*/

matched\_object : mo\_id\_d | mo\_id\_m

;   
   
/\* Matched object with id\_d \*/

mo\_id\_d : “\[” object\_type\_name

          id\_d\_of\_object

          monad\_set

          is\_focus

          \[marks\]

          inner\_sheaf

          “\]”

;   
object\_type\_name : T\_IDENTIFIER

;   
id\_d\_of\_object : T\_INTEGER

;   
is\_focus : “true” | “false” /\* Was the block against 

                                   which this matched\_object

                                   was matched a “focus”

                                   block or not? I.e., was

                                   they keyword “focus” 

                                   present in the block?

                                \*/

;   
   
marks : T\_MARKS   
;   
inner\_sheaf : sheaf

;   
   
/\* Matched object with id\_m (see ) \*/

mo\_id\_d : “\[” “pow\_m”

          monad\_set

          is\_focus

          \[marks\]

          inner\_sheaf

          “\]”

;

```

Bibliography

Doedens, Crist-Jan. 1994: *Text Databases, One Database Model and
Several Retrieval Languages.* ‘Language and Computers,’ Volume
14. Editions Rodopi Amsterdam, Atlanta, GA. ISBN 90-5183-729-1.

Sandborg-Petersen, Ulrik. 2008. *Annotated text databases in the context
of the Kaj Munk archive: One database model, one query language, and
several applications*. PhD dissertation, Department of Communication and
Psychology, Aalborg University, Denmark. Obtainable from URL:
`http://ulrikp.org/`

Petersen, Ulrik. 2002: *The Standard MdF Model*. Unpublished article.
Obtainable from URL: `http://emdros.org/`

Petersen, Ulrik. 2002: *Monad Sets – Implementation and Mathematical
Foundations*. Unpublished article. Obtainable from URL:
`http://emdros.org/`

Petersen, Ulrik. 2004. *Emdros -- a text database engine for analyzed or
annotated text*. In ICCL, Proceedings of COLING 2004, held August 23-27
in Geneva. International Commitee on Computational Linguistics, pp.
1190--1193. `http://emdros.org/`

Petersen, Ulrik. 2007: *Relational Implementation of EMdF and MQL.*
Unpublished working-paper. Obtainable from URL: `http://emdros.org/`

Petersen, Ulrik. 2007: *MQL Query Guide*. Obtainable from URL:
`http://emdros.org/`

\printindex

1.  Strictly, this is not true, since all object types (except pow\_m,
    any\_m, and all\_m) have at least one feature, namely the one called
    “self”. Please see section [\[self\]](#self) for more information.

2.  ASCII strings are stored exactly the same way as 8-bit STRINGs. This
    distinction is mostly obsolete.

3.  This is true for PostgreSQL (it is a TEXT). For MySQL, the maximum
    is 4294967295 (2^32 - 1) characters (it is a LONGTEXT). On SQLite,
    it is a TEXT, but it is unknown how much this can hold.

4.  For part\_of, see section [\[part\_of\]](#part_of).

5.  “Syntactic sugar” is a term used by computer-scientists for niceties
    in the grammar of a language which help the user in some way,
    usually so that they do not have to type as much as would otherwise
    be required. Here, it simply means that some of the keywords are
    optional, or have shorthand forms.

6.  This construction actually does occur in at least one language,
    namely ancient Greek. It is due to post-positive particles and
    conjunctions such as “de”, “gar”, “men”, and the like.

7.  Even though `mql_query` is really the proper entry-point for an MQL
    query-query, we may consider the topograph to be the top-level
    syntactic non-terminal in the MQL query-subset. The topograph has
    historical primacy, since it was defined first in Doedens’ QL (see
    ). The `mql_query` non-terminal simply acts as a proxy, passing
    control to the topograph immediately.
