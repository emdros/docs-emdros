# What is an object?

An object is a collection of data.  One of the kinds of data which is
always present in an object is a "feature" of type "SET OF MONADS",
called `monads`.

Thus, for example, an object might be of the object type "Clause" (if
such an object type has been created), and its "monads" feature might
be the set of monads `{1,2,4}`.

The EMdF model does not impose any restrictions on the set of monads
making up an object, except that it must be non-empty. For example,
objects can be discontiguous, as in the above example. In addition,
objects can have exactly the same monads as other objects, and objects
may share monads.

We need the last two concepts, object types and features, before we can
understand exactly how an object can encode, say, a word or a phrase.
