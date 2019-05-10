# CREATE OBJECT TYPE

## Purpose

To create an object type in a given database.  This sets up all
aspects of the object type, including a name, its implicit features,
and its explicit features.  This is necessary before you can put
objects into the object type.

## Grammar

```
create_object_type_statement = "CREATE" ["OBJECT"] "TYPE"
                               [if_not_exists]
                               [range_type]
                               [monad_uniqueness_type]
                               "[" object_type_name
                                  [feature_declaration_list]
                               "]"; 

if_not_exists = "IF"  "NOT"  "EXISTS" ;

range_type = "WITH"  "MULTIPLE"  "RANGE"  "OBJECTS"
           | "WITH"  "SINGLE"    "RANGE"  "OBJECTS"
           | "WITH"  "SINGLE"    "MONAD"  "OBJECTS" ;

monad_uniqueness_type = "HAVING"  "UNIQUE"  "FIRST"  "MONADS"
                      | "HAVING"  "UNIQUE"
                        "FIRST"   "AND"     "LAST"   "MONADS"
                      | "WITHOUT" "UNIQUE"  "MONADS" ;

object_type_name = IDENTIFIER ;  

feature_declaration_list = feature_declaration { feature_declaration } ;

feature_declaration = feature_name ":" feature_type 
                      default_specification ["COMPUTED"] ";"
                    | feature_name ":" "LIST" "OF" 
                      list_feature_type ";" ; 

feature_name = IDENTIFIER | "MONADS" ;

feature_type = "INTEGER" [with_index]
             | "STRING" [string_length] [from_set] [with_index]
             | "ASCII" [string_length] [from_set] [with_index]
             | "ID_D" [with_index]
             | IDENTIFIER [with_index] /* For enumerations */
             | "SET" "OF" "MONADS" /* Same as MULTIPLE RANGE SET OF MONADS */
             | "SINGLE"   "MONAD"  "SET"  "OF"  "MONADS"
             | "SINGLE"   "RANGE"  "SET"  "OF"  "MONADS"
             | "MULTIPLE" "RANGE"  "SET"  "OF"  "MONADS" ;

with_index = "WITH"    "INDEX"
           | "WITHOUT" "INDEX"; 

string_length = "(" unsigned_integer ")" ;

unsigned_integer = digit { digit } ;

digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;

from_set = "FROM"  "SET";

default_specification = ["DEFAULT" expression ];

expression = signed_integer /* integer and id_d */
           | STRING
           | IDENTIFIER /* enumeration constant */
           | monad_set  /* set of monads */
           | "(" ")"    /* empty list */
           | "(" list_of_integer ")" 
           | "(" list_of_identifier ")" ;

signed_integer = unsigned_integer | "-" unsigned_integer | "NIL" ; 

monad_set = "{" monad_set_element_list "}" ;

monad_set_element_list = monad_set_element { "," monad_set_element } ;

monad_set_element = unsigned_integer
                  | unsigned_integer "-" unsigned_integer
                  | unsigned_integer "-" ;

list_of_integer = signed_integer { "," signed_integer } ;

list_of_identifier = IDENTIFIER { "," IDENTIFIER } ;

list_feature_type = "INTEGER" 
                  | "ID_D" ;

```

## Examples

Basic example, creating an object type called `Word`.

```
CREATE OBJECT WITH
WITH SINGLE MONAD OBJECTS
[Word
  surface: STRING WITHOUT INDEX;
  lemma : STRING WITH INDEX;
  parsing_tag : STRING FROM SET WITH INDEX;
  psp : part_of_speech_t;
  parents : LIST OF id_d;
]
GO
```

The following example creates an object type called `Clause` with four
features:

- `parent`, whose type is id\_d, pointing to the object which is the
  parent of this clause in a tree.

- `clause_type`, which has the enumeration-type `clause_type_t` and
  the default value `NC` (which must be an enumeration constant in the
  `clause_type_t` enumeration).

- `functions`, which is a list of enumeration constants drawn from the
  enumeration `clause_function_t`

- `descendants`, which is a list of id\_ds, which should then point to
  the descendants in the tree.

In addition, if the object type “Clause” exists already, no error is
thrown, and the object type is left untouched.


```
CREATE OBJECT TYPE
IF NOT EXISTS
[Clause
   parent : id_d;
   // An enumeration, previously CREATEd, with a specific default
   clause_type : clause_type_t default NC;
   // LIST OF an enumeration, previously CREATEd   
   functions : LIST OF clause_function_t;
   descendants : LIST OF ID_D;
   parallel_monads : SET OF MONADS;
]
GO
```


## Explanation

### Overview

This statement *creates an object type* in the meta-data repository of
the current database. It starts out with the keywords “CREATE OBJECT
TYPE”, followed by an optional clause which states whether the objects
will be single-range or multiple-range (see below). After that comes a
specification of the object type name and its features enclosed in
square brackets. The `feature_declaration_list` is optional, so it is
possible for an object type to have no features, except for the
default ones, `monads` and `self`, which are always created
implicitly.

### Feature declarations

Each feature\_declaration consists of a feature name, followed by a
colon, followed by a feature type, followed by an optional
specification of the default value.

### Indexes

An INTEGER, ID\_D, STRING, or ASCII feature can be declared “WITH
INDEX”. This will put an index on the feature’s column. The default is
not to add an index. This index will be dropped if a DROP INDEXES
statement is issued for the object type (see Section [\[DROP
INDEXES\]](/mql/schema/indexes/dropindexes/)), but it will be
recreated if a CREATE INDEXES statement is issued for the object type
(see Section [\[CREATE
INDEXES\]](/mql/schema/indexes/createindexes/)). If a feature is an
enumeration, it is usually not a good idea to create an index on the
feature. This is because enumeration constants are usually few in
number, and it is generally not a good idea to index columns that draw
their values from a small pool of values, since this can lead to speed
decreases (O(NlogN) instead of O(N)). Therefore, the MQL language does
not allow creating indexes on enumeration features. You can add them
yourself, of course, if you like, with the backend’s corresponding SQL
interface.

### Strings

A STRING or ASCII feature can be declared “FROM SET”. The default is for
it not to be from a set. This does *not* mean that the value of the
feature *is* a set, but rather that the values are drawn FROM a set.
Whenever an object is created or updated, and a feature is assigned
which is declared “FROM SET”, the string value is first looked up in a
special table that maps strings to unique integers. Then this unique
integer is used in lieu of the string in the feature column. If the
string does not exist in the separate table, it is added, with a unique
integer to go with it, and that integer is used. If the string is there,
then the integer already associated with the string is used. This gives
a space savings (on MySQL and PostgreSQL), and sometimes also a speed
advantage, especially if used on the string features of a Word object
type which do no have high cardinality (number of unique instances), and
the words number many millions. SQLite and SQLite 3 may not see any
speed or space savings advantage. Note that using FROM SET on a string
may actually impede performance (especially database loading times),
especially on MySQL, if the cardinality of the string data is high. This
will likely be the case for strings like “surface” and “lemma”, which
generally should not be declared FROM SET. However, features like
“part\_of\_speech”, “case”, “number”, “gender”, which all most likely
have low cardinality, might be good candidates for using a STRING FROM
SET. Thus STRING FROM SET is a performance-enhanced way of using general
strings instead of enumerations, and should be just as fast as
enumerations for most queries, provided it is not used with
high-cardinality data.

The difference between “ASCII” and “STRING” is that the user promises
only to store 7-bit data in an ASCII string, whereas a STRING string may
contain 8-bit data.

In previous versions, you could specify a string length in parentheses
after the STRING or ASCII keyword. As of Emdros version 1.2.0, all
strings can have arbitrary length, with no maximum. The old
syntax is still available, but is ignored.


### The implicif feature "self"

The feature “self” is implicitly created. It is an error if it is
declared. The “self” feature is a computed feature which holds the
unique object id\_d of the object.


### The implicif feature "monads"

The feature “monads” is implicitly created. It is an error if it is
declared. The “monads” feature is the privileged set of monads which
defines the placement of an object in the sequence of monads.  That it
is privileged simply means that it is the default monad set feature
used if no other monad set feature is specified.

The feature “monads” is always of type SET OF MONADS.  Any object MUST
give a non-empty value to this set when it is created.

### LIST OF

If a feature is declared as a LIST OF *something*, that something has
to be either INTEGER, ID\_D, or an enumeration constant. Lists of
strings are currently not supported. Also, you cannot declare a
default value for a list – the default value is always the empty list.

### DEFAULT

The specification of the default value (`default_specification`)
consists of the keyword “DEFAULT”, followed by an expression. An
expression is either a `signed_integer`, a string, or an identifier. The
identifier must be an enumeration constant belonging to the enumeration
which is also the type of the feature. The `signed_integer` is either a
signed integer (positive or negative), or the keyword “NIL”, meaning the
id\_d that points to no object.


### IF NOT EXISTS

This statement can be “hedged” with the “IF NOT EXISTS” clause. If this
clause is included, the statement does not throw an error if the object
type exists already. Instead, the object type is left as it is (no
changes are made to what is in the database already), and the statement
returns success. If the “IF NOT EXISTS” clause is omitted, the statement
throws an error if the object type exists already.

### Range type

An object type can be declared “WITH SINGLE MONAD OBJECTS”, “WITH SINGLE
RANGE OBJECTS” or “WITH MULTIPLE RANGE OBJECTS”. The difference is that:

- An object type which has been declared “WITH SINGLE MONAD OBJECTS”
  can only hold objects which consist of a single monad (i.e., the
  first monad is the same as the last monad).

- An object type which has been declared “WITH SINGLE RANGE OBJECTS”
  can only hold objects which consist of a *single monad range*, i.e.,
  there are no gaps in the monad set, but it consists of a single
  contiguous stretch of monads (possibly only 1 monad long).

- An object type which has been declared “WITH MULTIPLE RANGE OBJECTS”
    (the default) can hold objects which have arbitrary monad sets.

A single-monad object must consist of only 1 monad, e.g., {1}, {2},
{3}.

A single-range object can consist of a single monad (e.g., { 1 }, { 2
}, { 3 }, etc.), or it can consist of a single interval (e.g., { 6-7 }, { 9-13 }, { 100-121 }, etc.).

However, as soon as an object type needs to hold objects which can
consist of more than one range (e.g., { 6-7, 9-13 }), then it must be
declared WITH MULTIPLE RANGE OBJECTS.

If no object range type is specified, then WITH MULTIPLE RANGE OBJECTS
is assumed.

There is a speed advantage of using WITH SINGLE MONAD OBJECTS over WITH
SINGLE RANGE OBJECTS, and again a speed advantage of using WITH SINGLE
RANGE OBJECTS over WITH MULTIPLE RANGE OBJECTS. The latter is the
slowest, but is also the most flexible in terms of monad sets.


### Monad uniqueness

In addition, and orthogonally to the range type, an object type can be
declared “HAVING UNIQUE FIRST MONADS”, “HAVING UNIQUE FIRST AND LAST
MONADS”, or “WITHOUT UNIQUE MONADS”. The difference is:

- An object type which has been declared “HAVING UNIQUE FIRST MONADS”
  can only hold objects which are unique in their first monad within
  the object type. That is, within this object type, no two objects
  may start at the same monad.

- An object type which has been declared “HAVING UNIQUE FIRST AND LAST
  MONADS” can only hold objects which are unique in their first monad
  and in their last monad (as a pair: You are allowed to have two
  objects with the same starting monad but different ending monads, or
  vice versa). That is, no two objects within this object type start
  at the same monad while also ending at the same monad. Note that for
  object types declared WITH SINGLE MONAD OBJECTS, a “HAVING UNIQUE
  FIRST AND LAST MONADS” restriction is upgraded to a “HAVING UNIQUE
  FIRST MONADS” restriction, since they are equivalent for this range
  type.

- An object type which has been declared “WITHOUT UNIQUE MONADS” (or
  which omits any of the “monad uniqueness constraints”) has no
  restrictions on the monads, other than those implied by the range
  type.

## Return type

There is no return value.

