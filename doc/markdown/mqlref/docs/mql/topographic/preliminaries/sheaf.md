# Sheaf

## Introduction

The sheaf is the data structure that is returned from an MQL
query-query. The structure of the sheaf closely reflects the structure
of the query on which it is based. This section is meant as reading for
implementors of Emdros-systems, not for end-users.

The sheaf has a specific structure, which we will look at next. After
that, we will take a look at the meaning of the structures of the sheaf.

## Structure of the sheaf

A sheaf consists of the following element types:

1.  Sheaf

2.  Straw

3.  Matched\_object

### What is a sheaf?

A sheaf *is* a list of straws.

### What is a straw?

A straw *is* a list of matched\_objects.

### What is a matched\_object?

A matched\_object *is* one of the following:

1.  (object id\_d, focus boolean, marks, sheaf, object type, set of
    monads, list of feature-values)

2.  (object id\_m, focus boolean, marks, sheaf)

That is, a matched\_object is an object id (either id\_d or id\_m),
coupled with a boolean indicating whether the block that gave rise to
the matched\_object had the “FOCUS” modifier, coupled with a “marks”
string, coupled with a sheaf. If the matched\_object is of the first
kind, then additionally, the object type and the object’s set of monads
are also available, and there is a (possibly empty) list of
feature-values.

## MQL is topographic

There is a correspondence between the way an MQL query is structured and
the structure of the resulting sheaf. In fact, the two are isomorphic to
some extent. Doedens, in , called this property “topographicity.” Thus a
`blocks` gives rise to a sheaf, a `block_str` gives rise to a straw, and
a `block` gives rise to a matched\_object. Inside a `block`, there is an
optional inner `blocks`, which again gives rise to an inner sheaf. Hence
a matched\_object contains a sheaf. The origin of this sheaf is the
optional inner `blocks` in the `block` which gave rise to the
matched\_object.

Note that this description applies to “full sheaves.” Flat sheaves are a
different matter. See section
[\[Flat-sheaf\]](#Flat-sheaf) for a description of flat
sheaves.

## Meaning of matched\_object

A matched\_object is the result of one of the following matches:

1.  An `object_block` against an object in the database.

2.  An `opt_gap_block` against a gap.

3.  A `gap_block` against a gap.

A matched\_object’s first component is either an id\_d or an id\_m. If
the matched\_object is the result of a match against an object\_block or
an object\_block\_first, then the id will be an id\_d. If the
matched\_object is the result of a match against a `gap_block` or an
`opt_gap_block`, the id is an id\_m.

The second component is a boolean indicating whether the “FOCUS” keyword
was present on the block.

The third component is a sheaf.

As we will see later, a sheaf is the result of matching against a
`blocks`. It so happens that there is an optional `blocks` inside each
of the four kinds of block (in the list above). The sheaf inside the
matched\_object is the result of a match against this `blocks`, if
present. If the `blocks` is not present, then the sheaf is simply an
empty sheaf.

For example, the following topograph:

```

\[word FOCUS\]

```

will contain one matched\_object for each word-object within the
substrate of the topograph. The sheaf of each of these matched\_objects
will be empty, and the FOCUS boolean will be “true” because we specified
the FOCUS keyword.

## Meaning of straw

A straw is the result of one complete match of a `block_str`. That is, a
straw is a “string” of matched\_objects corresponding to the blocks in
the `block_str` which we should retrieve (which we can specify with the
(“FOCUS”|”RETRIEVE”|”NORETRIEVE”) keyword triad).

For example, consider the following topograph:

```

\[word

   surface = the;

\]

\[word

   part\_of\_speech = noun;

\]

```

This will return a sheaf with as many straws as there are pairs of
adjacent words where the first is the word “the” and the second is a
noun. Each straw will contain two matched\_objects, one for each word.

## Meaning of the sheaf

A sheaf is the result of gathering all the matchings of a `blocks`
non-terminal. There are four places in the MQL grammar where a `blocks`
non-terminal shows up:

1.  In the `topograph`,

2.  In the `object_block`,

3.  In the `opt_gap_block`, and

4.  In the `gap_block`.

The first is the top-level non-terminal of the MQL query-query grammar.
Thus the result of an MQL query-query is a sheaf.

Each of the last three is some kind of block. Inside each of these,
there is an optional `blocks`. The result of matching this `blocks` is a
sheaf.

But a sheaf is a list of straws. What does that mean?

It means that a sheaf contains as many matches of the strings of blocks
(technically, block\_string2) making up the `blocks` as are available
within the substrate and universe that governed the matching of the
`blocks`.

A straw constitutes one matching of the `block_str`ing2. A sheaf, on the
other hand, constitutes all the
matchings.

## Flat sheaf<span id="Flat-sheaf" label="Flat-sheaf">\[Flat-sheaf\]

Most of the above description has applied to “full sheaves.” We now
describe flat sheaves.

A “flat sheaf,” like a “full sheaf,” consists of the datatypes “sheaf,”
“straw,” and “matched\_object.” The difference is that a
“matched\_object” in a flat sheaf cannot have an embedded sheaf. This
makes a flat sheaf a non-recursive datastructure.

A flat sheaf arises from a full sheaf by means of the “flatten”
operator.

If “FullSheaf” is a full sheaf, then “flatten(FullSheaf)” returns a flat
sheaf that corresponds to the full sheaf.

A flat sheaf contains the same matched\_objects as its originating full
sheaf. However, they are structured such that each straw in the flat
sheaf contains only matched\_objects of one object type. Each object
type that is represented in the full sheaf results in one straw in the
flat sheaf.

Thus a straw in a flat sheaf does not correspond to the matching of a
block\_string. Instead, it is a list of all the matched\_objects of one
particular object type in the originating full sheaf. All of the
matched\_objects in the full sheaf are represented in the flat sheaf,
regardless of whether they represent the same object in the database.

The “flatten” operator is only applied to the output of an MQL query if
the “RETURNING FLAT SHEAF” clause is given (see section
[\[SELECT\_OBJECTS\]](#SELECT_OBJECTS)). The programmer of an Emdros
application can also apply it programmatically.

There is a variant of the flatten operator which also takes a list of
object type names, in addition to the full sheaf. Then only those object
types which are in the list are put into the flat sheaf. If L is a list
of object type names, and FullSheaf is a full sheaf, then
flatten(FullSheaf, L) returns a flat sheaf with straws for only those
object types which are in L. If L is empty, then this is interpreted as
meaning that all object types in FullSheaf must go into the flat sheaf.
In the this light, the single-argument flatten operator may be seen as
being a special case of the two-argument flatten operator, with L being
empty. That is, flatten(FullSheaf) is the same as flatten(FullSheaf,
\[\]).


