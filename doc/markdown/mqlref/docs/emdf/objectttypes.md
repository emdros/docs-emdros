# Objects are grouped in types

In any populated EMdF database, there will be at least one object type.
Otherwise, no objects can be created, and thus the database cannot store
textual information.

Objects are grouped in types, such as “word”, “phrase”, “clause”,
“sentence”, but also “chapter”, “part”, “page”, etc. Each of these are
potential object types that the user can create. Once an object type has
been created, objects of that type can also be created.

Any object is of exactly one object type. Object types are what gives
objects their interpretation. For example, an object of type “phrase”
is, by itself, just a set of monads, such as
{1,2,4}. But seen in conjunction with its
object type, it becomes possible to interpret those monads as a number
of words that make up a phrase.

An object type is also what determines what *features* an object has.
And thus we turn to the last major concept in the EMdF model, namely
features.
