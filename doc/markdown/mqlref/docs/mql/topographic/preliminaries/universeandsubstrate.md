# Universe and substrate<span id="sec:Universe-and-substrate" label="sec:Universe-and-substrate">\[sec:Universe-and-substrate\]

## Introduction

Two concepts which we shall need when explaining the blocks in MQL are
“Universe” and “Substrate.” In this section, we define and explain
them.

## Universe and substrate

A Universe is a contiguous set of monads. It always starts at a
particular monad \(a\) and ends at another monad \(b\), where
\(a\leq b\). In more everyday language, a Universe is a stretch of
monads that starts at one monad and ends at another monad later in the
database. The ending monad may be the same as the starting monad.

A Substrate, on the other hand, is an arbitrary set of monads. It may
have gaps (see section [\[gaps\]](#gaps) on page ). That is, while a
Substrate always begins at a certain monad \(a\) and always ends at
another monad \(b\), where \(a\leq b\), it need not contain all of the
monads in between.

A Universe always has an accompanying Substrate, and a Substrate always
has an accompanying Universe. Their starting- and ending-monads are the
same. That is, the first monad of the Universe is always the same as the
first monad of the accompanying Substrate. And the last monad of the
Universe is always the same as the last monad of the Substrate. So a
Universe is a Substrate with all the gaps (if any) filled in.

See section [\[SELECT OBJECTS:
Explanation\]](#SELECT%20OBJECTS:%20Explanation) for an explanation of
how the initial substrate and universe are calculated for the query.

With that definition out of the way, let us proceed to describing,
exemplifying, and explaining
*blocks*.

