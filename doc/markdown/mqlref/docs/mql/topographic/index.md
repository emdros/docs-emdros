# Introduction to the topographic part of MQL

Crist-Jan Doedens invented the term "topographic" in his 1994 PhD
thesis.  For a language to be "topograpic" means that there exists an
isomorphism (loosely: analogy) between the structure of the language
strings and the reality to which they refer.

MQL is a topographic query language, meaning there is an isomorphism
(or analogy) between the structure of an MQL query and the objects
which it finds.

For example, the following query finds Phrase objects which are
*inside* Clause objects.  Here, "inside" means that the "monads"
features of the Phrase objects which are sets of monads which are
"part\_of" (i.e., subsets of) the "monads" features of the Clause
objects.  That is, the relationship between the sets of monads of the
Phrase objects found and the sets of monads of the Clause objects
found is a "subset" relation.

```
SELECT ALL OBJECTS
WHERE
[Clause
   [Phrase]
]
```

Since the `[Phrase]` object block is syntactically "inside" the
surrounding `[Clause ...]` object block, there is a direct analogy
(isomorphism) between the structure of the query and the structure of
the objects it finds.

Similarly, the following query finds two Phrases inside a Clause.
Both Phrases must be "inside" the clause (i.e., their "monads"
features must be subsets of the surrounding "Clause" objects' "monads"
features).

```
SELECT ALL OBJECTS
WHERE
[Clause
   [Phrase]
   [Phrase]
]
```

In addition, the two Phrases must be adjacent in the database, since
they are adjacent in the query.  Here, "adjacent" means "adjacent with
respect to the surrounding context's monads.  If there are no gaps in
the Clause (i.e., the set of monads "monads" of the Clause object is a
contiguous stretch of monads), then the first phrase's last monad must
be 1 monad less than the second phrase's first monad.  If, on the
other hand, the Clause has gaps (i.e., its monad set "monads" is not
contiguous), then the two phrases could also be found just by virtue
of being separated by a gap in the clause.


We shall now explore in detail how this works.

