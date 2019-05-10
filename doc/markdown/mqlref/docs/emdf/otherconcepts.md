# Introduction

Having learned the basic concepts of the EMdF model, we now turn to the
additional concepts which we use to talk about EMdF databases. These
concepts are:

1. The special object types:
    1. pow\_m,
    2. any\_m, and
    3. all\_m
2. object ids (id\_d, id\_m)
3. self
4. part\_of
5. gaps
6. borders, first, and last
7. min\_m and max\_m
8. arbitrary monad sets


## pow\_m

In each EMdF database, we assume an abstract object type, pow\_m. This
object type has one object for every possible set of monads. Thus the
pow\_m object type has objects consisting of the sets
{1}, {2}, {3}, …, {1,2}, {1,3}, {1,4}, …, {2,3}, {2,4}, {2,5},…, {1,2,3}, {1,2,4}, …, etc. Every possible set of monads is represented in the pow\_m object
type.

The pow\_m object type is an *abstract* object type. That is, no objects
of type pow\_m actually exist in the EMdF database. However, it is
useful to be able to talk about a particular pow\_m object. In effect, a
pow\_m object is simply a set of monads, and sometimes, it is convenient
to be able to talk about a particular pow\_m object. This is especially
true with gaps (see below).

The pow\_m object type has no features.

## any\_m

The any\_m object type is an abstract object type like pow\_m. Each of
its objects consist of a single monad. So the any\_m objects are:
{1}, {2}, {3}, … etc. The any\_m object type has no
features.

## all\_m

The all\_m object type has only one object, and it consists of all the
monads in the database. That is, it consists of the monads from min\_m
to max\_m (see sections [\[SELECT MIN\_M\]](/mql/data/globaldata/selectminm/) and
[\[SELECT MAX\_M\]](/mql/data/globaldata/selectmaxm/)), the smallest and the largest
monads in use in the database at any given time. This one object is
called all\_m-1.

## object ids (id\_d, id\_m)

Each object in the database (apart from pow\_m objects) has an *object
id\_d*. An object id\_d is a unique ID assigned to the object when the
object is created. The id\_d is used only for that particular object, and the id\_d is never used again when the object is deleted.

A feature can have the type “id\_d”, meaning that the values of the
feature are taken from the id\_ds in the database.

Each object in the database (including pow\_m, any\_m, and all\_m
objects) also has an id\_m. The id\_m is simply the set of monads which
makes up the object. This is not strictly an ID, since objects of the
same object type may have exactly the same monads. However, for
historical reasons, this is called an id\_m. See  or  for details.

## self

Each object type in the database (apart from the pow\_m, any\_m, and
all\_m object types) has a feature called “self”. This is used to get
the object id\_d of the object in question.

The “self” feature is a read-only feature, which means that you cannot
update an object’s self feature, or write to it when creating the
object. The value of the “self” feature is assigned automatically when
the object is created.

The type of the “self” feature is “id\_d”.

## part\_of

If all of the monads of one object, O<sub>1</sub>, are contained
within the set of monads making up another object, O<sub>2</sub>, we
say that O<sub>1</sub> is part\_of O<sub>2</sub>.

For example, an object with the monads
{1,2} would be part\_of another object
with the monads {1,2,4}.

In mathematical terms, O<sub>1</sub> is part\_of O<sub>2</sub> if and
only if O<sub>1</sub> is a subset of (possibly equal to)
O<sub>2</sub>. That is, O<sub>1</sub> ⊆ O<sub>2</sub>.

## gaps

Objects may have gaps. A gap in an object is a maximal stretch of
monads which are not part of the object, but which are nevertheless
within the boundaries of the endpoints of the object. For example, an
object consisting of the monads {1,3,4,7,8,13} has three gaps: {2},
{5,6}, and {9,10,11,12}.

Note that gaps are always maximal, i.e., extend across the whole of
the gap in the object. For example, {6} is not a gap in the above
object: instead, {5,6} is.

## borders, first, last

Each non-empty object, being a set of monads, has a left border and a
right border. The left border is the lowest monad in the set, while the
right border is the highest monad in the set. These are also called the
first monad and the last monad in the object. If we have an object O, the notation for these monads is O.first and O.last.

For example, if we have an object O consisting of the monads
{2,3,4,5}, then O.first = 2 and O.last =
5.

## consecutive with respect to a set of monads

The basic idea is that two sets of monads are consecutive if they follow
each other without any gaps in between. However, this idea is extended
so that the “no gaps in between” is interpreted with respect to a
reference set of monads called Su. For example, if Su =
{1,2,5,6}, then the sets
{2} and {5}
are consecutive with respect to Su. However, the sets
{2} and {6}
are not consecutive with respect to Su, since there is a “gap”
consisting of the monad 5 in between the two sets. Likewise, the sets
{1} and {5}
are not consecutive with respect to Su, because Su has a monad, 2, which
is a “gap” between the two sets.

## min\_m, max\_m

An EMdF database has a knowledge of which is the smallest monad in use
(min\_m) and which is the largest monad in use (max\_m). Normally, you
don’t need to worry about these; the database maintains its knowledge of
these monads without your intervention. You can, however, query the
database for the minimum and maximum monads (see sections
[\[SELECT MIN\_M\]](/mql/data/globaldata/selectminm/) and
[\[SELECT MAX\_M\]](/mql/data/globaldata/selectmaxm/)), and when you query the database
for objects, this is done within the confines of the minimum and maximum
monads. Thus it is useful to know of their existence, but you needn’t
worry too much about them.

The associated statements are SELECT MIN\_M (section [\[SELECT MIN\_M\]](/mql/data/globaldata/selectminm/)) and SELECT MAX\_M (section
[\[SELECT MAX\_M\]](/mql/data/globaldata/selectmaxm/)).

## Arbitrary monad sets

Each database has a central repository of monad sets which are not
associated with any objects. That is, they are not objects, have no
object type, and no features. They are just plain monad sets.

These monad sets can be used as the basis for searches. That is, when
doing a SELECT ALL OBJECTS query (or SELECT FOCUS OBJECTS), one can
specify within which arbitrary monad set the search should be conducted.

The associated statements are:

- CREATE MONAD SET (section [\[CREATE MONAD
  SET\]](/mql/data/monadsets/createmonadset/)),

- UPDATE MONAD SET (section [\[UPDATE MONAD
  SET\]](mql/data/monadsets/updatemonadset/)),

- DROP MONAD SET (section [\[DROP MONAD
  SET\]](/mql/data/monadsets/dropmonadset/)), 

- MONAD SET CALCULATION (section [\[MONAD SET CALCULATION\]](/mql/data/monadsets/monadsetcalculation/),

- SELECT MONAD SETS (section [\[SELECT MONAD
  SETS\]](/mql/data/monadsets/selectmonadsets/)), and

- GET MONAD SETS (section [\[GET MONAD
  SETS\]](/mql/data/monadsets/getmonadsets/)).




