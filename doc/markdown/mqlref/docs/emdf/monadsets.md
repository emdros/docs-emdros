# What are named monad sets?

Each database has a central repository of monad sets which are not
associated with any objects. That is, they are not objects, have no
object type, and no features. They are just plain monad sets.

# Why do they exist?

These monad sets can be used as the basis for searches. That is, when
doing a SELECT ALL OBJECTS query (or SELECT FOCUS OBJECTS), one can
specify within which arbitrary monad set the search should be conducted.

# What statements can be used?

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




