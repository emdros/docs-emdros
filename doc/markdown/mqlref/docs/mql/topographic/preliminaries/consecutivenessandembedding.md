# Consecutiveness and embedding

Two important notions in the MQL query-subset are embedding and
consecutiveness. If two blocks (be they object blocks or gap blocks) are
consecutive in a query, it means that they will only match two objects
or gaps which are consecutive with respect to the substrate. Likewise, a
string of blocks (i.e., a `blocks`) which is embedded inside of a block
of some sort will only match within the confines of the monads of the
surrounding block.

For example, the following topograph:

```

\[Word psp=article\]

\[Word psp=noun\]

```

will match two adjacent (or consecutive) words where the first is an
article and the second is a noun. The consecutiveness is calculated with
respect to the current substrate (see section
[\[consecutive\]](#consecutive)).

Likewise, the following topograph:

```

\[Clause

  \[Phrase phrase\_type = NP\]

  \[Phrase phrase\_type = VP\]

\]

```

will match only if the two (adjacent) phrases are found *within the
confines of* the monads of the surrounding Clause. In fact the monads of
the surrounding clause serve as the substrate when matching the inner
`blocks`.

You can specify the kind of containment you want: Either part\_of or
overlap. Part\_of means that the inner object must be a subset (proper
or not) of the outer object.

You can also specify whether the containment should be relative to the
substrate or the universe. The universe is always the universe coming
out the of the substrate that is the surrounding object or gap.

This is done as
follows:

```

\[Clause

  // Phrase is part\_of the monads of the clause

  \[Phrase part\_of(substrate) phrase\_type=NP\]

  // Phrase is part\_of the monads of the clause, including any gaps

  // in the clause

  \[Phrase part\_of(universe) phrase\_type=VP\]

  

  // Phrase has non-empty intersection with the monads of the clause

  \[Phrase overlaps(substrate) phrase\_type=AdvP\]

  // Phrase is non-empty intersection with the monads of the clause, 

  // including any gaps in the clause

  \[Phrase overlaps(universe) phrase\_type=PP\]

\]

```

The default is to use `part_of(substrate)`.
